# Lição 6: Microsoft Toolbox — Ferramentas Governadas para Agentes

Após a [Lição 5](../lesson-5-hosted-agents-production/README.md) seu agente hospedado é executado em
produção com a postura de armazenamento e governança que sua organização precisa. Mas volte a olhar para o
agente da Lição 4: cada ferramenta foi **codificada diretamente** em `main.py` — a URL MCP do Microsoft Learn, o
repositório de vetores de pesquisa de arquivos, e assim por diante. Isso funciona para um agente. Não **escala** para uma
organização com dezenas de agentes e equipes.

Esta lição apresenta o **Microsoft Toolbox**: a forma como o Foundry permite que você defina um conjunto selecionado de
ferramentas **uma vez**, gerencie-as **centralmente**, e exponha-as a qualquer agente por meio de um **único,
endpoint governado**.

## Objetivos de Aprendizagem

Ao final desta lição você será capaz de:

- Explicar o problema de proliferação de ferramentas que o Toolbox resolve.
- Descrever os pilares **Build** e **Consume** e os tipos de ferramentas que um toolbox pode conter.
- **Build** uma versão de toolbox com o Foundry SDK.
- **Consume** um toolbox a partir de um agente hospedado do Microsoft Agent Framework via um único endpoint MCP.
- Usar **versionamento** para entregar mudanças de ferramentas sem alterações no código do agente ou reimplantação.
- Aplicar **governança**: RBAC, injeção de credenciais, e políticas de guardrail (RAI).

---

## Pré-requisitos

1. Ter concluído a [Lição 4](../lesson-4-agentdeployment/README.md) e, idealmente,
   [Lição 5](../lesson-5-hosted-agents-production/README.md).
2. Um projeto **Microsoft Foundry** com permissão para criar e gerenciar recursos de toolbox.
3. **Azure CLI** autenticado: `az login`. As APIs do toolbox do Foundry requerem o
   escopo de token `https://ai.azure.com/.default` (mostrado no código abaixo).
4. **Python 3.12+** com as dependências do curso instaladas (`pip install -r ../requirements.txt`).
5. Uma implantação de modelo atual e não descontinuada (por exemplo `gpt-5.1`). Evite GPT-4o / GPT-4.1 descontinuados.

---

## 1. O problema: proliferação de ferramentas

Um único agente pode depender de muitas ferramentas — APIs REST, servidores MCP, conectores e fluxos — cada
com seu próprio modelo de autenticação e equipe responsável. À medida que você escala por uma organização:

- Equipes **re-implementam as mesmas ferramentas** de forma independente.
- **As credenciais ficam duplicadas** entre agentes e repositórios.
- **A governança se torna inconsistente** — cada agente aplica (ou esquece) a política por conta própria.
- Há **pouca visibilidade** sobre quais ferramentas existem ou quem as está usando.

Os desenvolvedores travam — não porque os modelos não sejam capazes, mas porque a **integração de ferramentas se torna
o gargalo**.

```mermaid
flowchart LR
    subgraph BEFORE["❌ Sem Caixa de Ferramentas"]
        A1[Agente A] --> W1[API web + credenciais]
        A1 --> M1[Servidor MCP + credenciais]
        A2[Agente B] --> W2[API web + credenciais novamente]
        A2 --> S1[Pesquisa de IA + credenciais]
        A3[Agente C] --> M2[Servidor MCP + credenciais novamente]
    end

    subgraph AFTER["✅ Com Caixa de Ferramentas"]
        B1[Agente A] --> TB
        B2[Agente B] --> TB
        B3[Agente C] --> TB
        TB["Caixa de Ferramentas<br/>(endpoint MCP único)"] --> T1[Pesquisa na Web]
        TB --> T2[Servidor MCP]
        TB --> T3[Azure AI Search]
        TB -.governed by default.-> G[(Credenciais · Política · Observabilidade)]
    end
```

As empresas já possuem a infraestrutura — gateways, cofres de credenciais, políticas, observabilidade.
O que faltava era uma experiência de desenvolvedor que empacotasse isso em algo **reutilizável,
descobrável e governado por padrão**. Isso é o Toolbox.

---

## 2. O que é um Toolbox

Um **Toolbox** é um **recurso gerenciado do Foundry**. Você define um conjunto selecionado de ferramentas uma vez, gerencia
elas centralmente no Foundry e as expõe por meio de **um único endpoint compatível com MCP** que qualquer
agente pode consumir. Em tempo de execução a plataforma cuida da **injeção de credenciais, renovação de token e
aplicação de políticas empresariais**.

Como um toolbox é um recurso gerenciado, você pode adicionar, remover ou reconfigurar ferramentas **sem
alterar o código do seu agente** — o agente sempre se conecta ao mesmo endpoint.

O Toolbox cobre o ciclo de vida das ferramentas por meio de quatro pilares; **Build** e **Consume** estão disponíveis
hoje:

| Pilar | Status | O que possibilita |
|--------|--------|-----------------|
| **Build** | Disponível hoje | Selecionar ferramentas, configurar autenticação centralmente, publicar um toolbox reutilizável que qualquer equipe possa consumir. |
| **Consume** | Disponível hoje | Conectar qualquer agente a um endpoint compatível com MCP para descobrir e invocar dinamicamente todas as ferramentas no toolbox. |

A superfície de consumo é **aberta**: qualquer runtime ou cliente compatível com MCP pode usar um toolbox —
Microsoft Agent Framework, LangGraph, GitHub Copilot, Claude Code, Microsoft Copilot Studio, ou
código personalizado.

### Tipos de ferramentas que um toolbox pode conter

Web Search · MCP · Azure AI Search · Code Interpreter · File Search · OpenAPI · **Agent-to-Agent
(A2A)** · Fabric IQ · Tool Search · Work IQ · Browser Automation · referências de skill, além de uma
**política Guardrail (RAI)** aplicada no nível do toolbox.

> **Dica:** Adicione um `description` a **cada** ferramenta para que o modelo possa escolher a correta. Um toolbox
> permite no máximo **uma ferramenta sem nome por tipo** — dê a cada instância adicional do mesmo tipo um
> único `name`, ou você receberá um erro `invalid_payload`.

---

## 3. Construir um toolbox

Toolboxes são gerenciados com os SDKs do Foundry (Python/.NET/JavaScript), a REST API, `azd`, e o
**Microsoft Foundry Toolkit for VS Code**. Aqui está o padrão em Python (`azure-ai-projects`):

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import MCPTool, ToolboxSearchPreviewTool, WebSearchTool

endpoint = "https://<your-foundry-account>.services.ai.azure.com/api/projects/<your-project>"
project = AIProjectClient(endpoint=endpoint, credential=DefaultAzureCredential())

toolbox_version = project.toolboxes.create_toolbox_version(
    name="agent-tools",
    description="Web search + an MCP server + tool search",
    tools=[
        WebSearchTool(),
        MCPTool(
            server_label="myserver",
            server_url="https://your-mcp-server.example.com",
            require_approval="never",
            project_connection_id="my-key-auth-connection",  # as credenciais ficam no Foundry
        ),
        ToolboxSearchPreviewTool(),
    ],
)
print(f"Created toolbox: {toolbox_version.name}, version: {toolbox_version.version}")
```

Observe o que você **não** faz: nenhum segredo fica no agente. As credenciais são mantidas por uma Foundry
**connection** (`project_connection_id`) e injetadas pela plataforma no momento da chamada.

> **Nota de visualização.** O **gerenciamento** do Toolbox (criação/atualização de versões) é uma capacidade em visualização.
> As operações `project.toolboxes.*` mostradas acima são entregues em builds de SDK em preview, na REST API, `azd`,
> e no **Foundry Toolkit for VS Code** — elas **não** estão no `azure-ai-projects` fixado usado
> em outro lugar neste curso. Trate o trecho acima como o formato da etapa Build; para um
> caminho de clique, crie o toolbox no **Foundry portal** ou no **Foundry Toolkit**. O
> passo **Consume** abaixo funciona com o SDK fixado do curso hoje.

---

## 4. Consumir um toolbox a partir do seu agente

Um toolbox expõe um **endpoint MCP**. Existem dois padrões:

| Papel | Endpoint | Quando usar |
|------|----------|-------------|
| **Consumidor de toolbox** | `{project_endpoint}/toolboxes/{name}/mcp?api-version=v1` | Conectar agentes. Sempre serve a **versão padrão**. |
| **Desenvolvedor de toolbox** | `{project_endpoint}/toolboxes/{name}/versions/{version}/mcp?api-version=v1` | Testar uma versão específica antes de promovê-la. |

> **Conecte os agentes ao endpoint *consumer*.** Como ele sempre serve a versão padrão, você
> pode promover novas versões **sem alterar o código do agente ou reimplantar**.

### Integração com um agente hospedado do Microsoft Agent Framework

Lembre-se que o agente da Lição 4 adicionou uma única ferramenta MCP codificada diretamente com `client.get_mcp_tool(...)`. Com
o Toolbox você em vez disso aponta **um** `MCPStreamableHTTPTool` para o endpoint do toolbox — e o agente
recebe **todas** as ferramentas do toolbox, governadas centralmente:

```python
import httpx
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from agent_framework import MCPStreamableHTTPTool

# Autenticação: Foundry toolbox requer o escopo https://ai.azure.com/.default
credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(credential, "https://ai.azure.com/.default")
http_client = httpx.AsyncClient(auth=_ToolboxAuth(token_provider), timeout=120.0)

TOOLBOX_ENDPOINT = os.environ["TOOLBOX_ENDPOINT"]  # injetado pela plataforma em tempo de execução

mcp_tool = MCPStreamableHTTPTool(
    name="toolbox",
    url=TOOLBOX_ENDPOINT,
    http_client=http_client,
    load_prompts=False,
)

agent = chat_client.as_agent(
    name="my-toolbox-agent",
    instructions="You are a helpful assistant with access to Foundry toolbox tools.",
    tools=[mcp_tool],
)
```

`.env` correspondente (observação: use um modelo **atual** como `gpt-5.1`, **não** o aposentado
`gpt-4o`):

```env
FOUNDRY_PROJECT_ENDPOINT=https://<account>.services.ai.azure.com/api/projects/<project>
TOOLBOX_ENDPOINT=https://<account>.services.ai.azure.com/api/projects/<project>/toolboxes/agent-tools/mcp?api-version=v1
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5.1
```

> **Verifique primeiro.** Antes de ligar o agente completo, conecte um SDK cliente MCP (`pip install mcp`) ao
> endpoint **específico da versão** e liste as ferramentas para confirmar que elas carregam como esperado.

### Execute o exemplo de consumo

Esta lição fornece um exemplo executável do lado consumidor, [`toolbox_agent.py`](../../../lesson-6-toolbox/toolbox_agent.py). Ele usa
o mesmo padrão `FoundryChatClient.get_mcp_tool(...)` que você aprendeu na Lição 2, mas aponta a única
ferramenta MCP para o seu endpoint **toolbox** — assim o agente obtém todas as ferramentas governadas no toolbox:

```bash
# No seu arquivo .env, defina TOOLBOX_ENDPOINT para o endpoint do consumidor da toolbox, então:
python lesson-6-toolbox/toolbox_agent.py
```

Abra a URL impressa `http://localhost:8096` e faça uma pergunta que exercite uma das
ferramentas do toolbox. Adicione ou atualize uma ferramenta no toolbox e pergunte novamente — **sem alterar este
código** — para ver a governança central e o versionamento em ação.

---

## 5. Versionamento: implantar alterações de ferramentas com segurança

O versionamento do toolbox dá a você controle explícito sobre quando as mudanças entram em vigor:

1. **Criar** uma nova versão do toolbox com o conjunto de ferramentas atualizado.
2. **Testar** ela contra o endpoint específico da versão (developer).
3. **Promover** ela para `default_version` quando estiver pronto.

Todo agente apontado para o endpoint **consumer** pega a versão promovida automaticamente — **sem
alterações de código, sem reimplantação**. (A primeira versão que você criar é promovida automaticamente para a padrão.)

Isto é o equivalente em governança de ferramentas a um deploy blue/green: você valida uma mudança isoladamente,
então alterna o padrão para todos os consumidores de uma vez.

---

## 6. Governança: como o Toolbox melhora o controle

O Toolbox é **governado por padrão**. As alavancas de governança que você deve conhecer:

- **RBAC.** Conceda o papel **Foundry User** no projeto para cada identidade: o **desenvolvedor** que
  gerencia versões do toolbox, a **managed identity do agente** (para agentes hospedados chamando ferramentas em
  tempo de execução), e, para fluxos OAuth, o **usuário final** cuja identidade é proxyada.
- **Credenciais centralizadas.** As credenciais das ferramentas vivem em Foundry **connections**, não no código do agente
  ou em arquivos `.env`. A plataforma as injeta e renova os tokens em tempo de execução.
- **Guardrails (política RAI).** Anexe uma política responsável por IA nomeada a uma versão do toolbox via
  `policies.rai_config.rai_policy_name`. Ela é executada no **nível do toolbox**, independentemente de qualquer
  filtro de conteúdo a nível de modelo, filtrando entradas e saídas das ferramentas.
- **Aprovação MCP.** O `require_approval` por ferramenta controla se uma chamada de ferramenta MCP precisa de aprovação —
  o mesmo conceito de fluxo de aprovação que você viu na [Lição 5 §7](../lesson-5-hosted-agents-production/README.md#7-hosted-mcp-tools--approval-workflows).
- **Rede privada.** O Toolbox suporta configurações de rede virtual para empresas que
  mantêm o tráfego dentro de sua rede.
- **Visibilidade.** Como as ferramentas são catalogadas centralmente, você finalmente obtém um inventário do que
  existe e quem as consome.

---

## Exercícios práticos

1. **Refatorar a Lição 4.** O agente da Lição 4 codifica de forma fixa a ferramenta Microsoft Learn MCP. Esboce como você
   moveria essa ferramenta para um toolbox `agent-tools` e redirecionaria `main.py` para o endpoint consumidor do toolbox.
   O que muda em `main.py`? O que deixaria de estar lá?
2. **Planeje um aumento de versão.** Você precisa adicionar uma ferramenta Web Search a um toolbox em produção usado por cinco
   agentes. Descreva a sequência criar → testar → promover e explique por que nenhum dos cinco agentes
   precisa ser reimplantado.
3. **Escolha as identidades de autenticação.** Para um agente hospedado que chama uma ferramenta MCP baseada em OAuth através de um
   toolbox, liste quais identidades precisam do papel **Foundry User** e por quê.
4. **Posicionamento do guardrail.** Explique a diferença entre um filtro de conteúdo a nível de modelo e um
   guardrail do toolbox, e dê um cenário em que você precisa especificamente do guardrail no toolbox.

---

## Recursos

- [Criar, testar e implantar um toolbox no Foundry](https://learn.microsoft.com/azure/foundry/agents/how-to/tools/toolbox)
- [Catálogo de ferramentas — Foundry Agent Service](https://learn.microsoft.com/azure/foundry/agents/concepts/tool-catalog)
- [Microsoft Agent Framework — provedor Microsoft Foundry (ferramentas)](https://learn.microsoft.com/agent-framework/agents/providers/microsoft-foundry)
- [Visão geral do Guardrails](https://learn.microsoft.com/azure/foundry/guardrails/guardrails-overview)
- [Comece com Foundry no VS Code (Foundry Toolkit)](https://learn.microsoft.com/azure/ai-foundry/how-to/develop/get-started-projects-vs-code)
- [Model Context Protocol](https://modelcontextprotocol.io/)

---

**Anterior:** [Lição 5 — Agentes Hospedados em Produção](../lesson-5-hosted-agents-production/README.md)
&nbsp;·&nbsp; **Próximo:** [Lição 7 — Multi-Agente & A2A](../lesson-7-multi-agent-a2a/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->