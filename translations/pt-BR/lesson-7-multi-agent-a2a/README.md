# Lição 7: Orquestração Multi-Agente & Agente-para-Agente (A2A)

Com a [Lição 6](../lesson-6-toolbox/README.md) você pode construir ferramentas governadas e agentes hospedados.
Mas sistemas reais raramente usam **um** agente. À medida que você escala, você compõe **muitos** agentes — alguns que você
possui, alguns pertencentes a outras equipes, alguns executando em outras organizações completamente. Esta lição é sobre
como os agentes trabalham **juntos**.

Você já conheceu uma forma de design multi-agente em
[o `agent-orchestration.py` da Lição 2](../lesson-2-agent-development/README.md): o padrão **handoff**
padrão, onde um agente de triagem direciona para especialistas **dentro de um único processo**. Esta lição avança
um nível acima — para **Agente-para-Agente (A2A)**, o protocolo aberto para agentes que rodam como
**serviços em rede** e se chamam uns aos outros através de processos, equipes e limites organizacionais.

## Objetivos de Aprendizagem

Ao final desta lição, você será capaz de:

- Explicar a diferença entre **orquestração em processo** (handoff/workflows) e
  comunicação **Agente-para-Agente (A2A)**, e escolher a apropriada.
- Descrever os blocos de construção do A2A: **Agent Card**, **skills**, **tasks**, e **discovery**.
- **Expor** um agente do Microsoft Agent Framework como um serviço A2A com `A2AExecutor`.
- **Consumir** um agente remoto como um par em rede com `A2AAgent`.
- Aplicar preocupações empresariais ao A2A: **segurança, identidade, governança, observabilidade e custo**.

---

## Pré-requisitos

1. Ter concluído a [Lição 2](../lesson-2-agent-development/README.md) (desenvolvimento de agentes e orquestração).
2. Um projeto **Microsoft Foundry** com uma implantação de modelo atual (por exemplo `gpt-5.1`, e
   `gpt-5-codex` para o exemplo de codificação). Evite GPT-4o / GPT-4.1 descontinuados.
3. **Azure CLI** autenticado: `az login`.
4. **Python 3.12+** com as dependências do curso instaladas (`pip install -r ../requirements.txt`).
   A Lição 7 adiciona os pacotes de pré-visualização `agent-framework-a2a`, `a2a-sdk`, e `uvicorn`.
5. `FOUNDRY_PROJECT_ENDPOINT` e `FOUNDRY_MODEL` configurados no seu `.env` (veja o README do curso).

---

## 1. Duas maneiras de os agentes trabalharem juntos

Não existe um único padrão "multi-agente". Escolha aquele que corresponde ao seu **limite**:

| Padrão | Onde os agentes rodam | Como eles se conectam | Usar quando |
|---------|------------------|------------------|----------|
| **Handoff / Workflow** (Lição 2) | Um processo, uma base de código | Grafo em memória (`HandoffBuilder`, `WorkflowBuilder`) | Você possui todos os agentes e os implanta juntos. |
| **Agente-para-Agente (A2A)** (esta lição) | Serviços separados, ciclos de vida separados | Protocolo **A2A** aberto sobre HTTP, descoberto via **Agent Cards** | Agentes são propriedade de diferentes equipes/organizações, escalam de forma independente, ou são escritos em frameworks diferentes. |

Handoff é sobre **roteamento dentro de uma aplicação**. A2A é sobre **compor agentes como
serviços independentes** — o equivalente, para agentes, de passar de chamadas de função para microsserviços.

```mermaid
flowchart LR
    subgraph INPROC["Orquestração em processo (Lição 2)"]
        T[Triagem] --> E[Busca de Funcionários]
        T --> L[Aprendizado]
        L --> C[Programação]
    end

    subgraph A2A["Agente-para-Agente (esta lição)"]
        O[Agente Orquestrador] -->|Protocolo A2A| S1[Assistente de Programação<br/>Equipe A · URL própria]
        O -->|Protocolo A2A| S2[Agente de RH<br/>Equipe B · URL própria]
        O -->|Protocolo A2A| S3[Agente Parceiro<br/>outra organização]
        S1 -.publishes.-> AC[(Cartão do Agente)]
    end
```

> **Eles se compõem.** Um orquestrador que você constrói com `HandoffBuilder` pode ter **agentes A2A remotos**
> como participantes — roteamento em processo para serviços que por sua vez rodam em qualquer lugar.

---

## 2. Os blocos de construção do A2A

A2A é um **protocolo aberto** (não específico da Microsoft), então um agente A2A pode ser consumido pelo Microsoft
Agent Framework, LangGraph, código customizado, ou pela pilha de outra empresa. Quatro conceitos importam:

- **Agent Card** — um pequeno documento JSON, publicado em
  `/.well-known/agent-card.json`, que divulga o **nome, descrição, URL, versão,**
  skills e capacidades**. É assim que um cliente **descobre** o que um agente remoto pode fazer.
- **Skills** — as coisas declaradas que o agente pode fazer (`id`, `name`, `description`, `tags`,
  `examples`). Clientes (e modelos) usam isso para decidir se devem chamá-lo.
- **Tasks** — uma chamada para um agente A2A é uma **task** com um ciclo de vida (submitted → working →
  completed/failed). O servidor rastreia tasks em um **task store**; atualizações em streaming são suportadas.
- **Discovery** — um cliente que recebe apenas uma URL busca o Agent Card e sabe como chamar o agente.

---

## 3. Expor um agente como um serviço A2A — `a2a_server.py`

O lado **Build/serve** envolve qualquer agente do Microsoft Agent Framework com `A2AExecutor` e o monta
em uma aplicação HTTP A2A. Veja [`a2a_server.py`](../../../lesson-7-multi-agent-a2a/a2a_server.py). A configuração principal:

```python
from agent_framework.a2a import A2AExecutor
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill

agent = client.as_agent(name="coding-assistant", instructions="...")

agent_card = AgentCard(
    name="Coding Assistant",
    description="Generates runnable code samples...",
    url="http://localhost:9000/",
    version="1.0.0",
    capabilities=AgentCapabilities(streaming=True),
    default_input_modes=["text"],
    default_output_modes=["text"],
    skills=[AgentSkill(id="generate-code", name="Generate code",
                       description="Write a runnable code snippet.", tags=["code"])],
)

request_handler = DefaultRequestHandler(
    agent_executor=A2AExecutor(agent),
    task_store=InMemoryTaskStore(),
)
app = A2AStarletteApplication(agent_card=agent_card, http_handler=request_handler).build()
# servido com uvicorn na porta 9000
```

Observe que o código do agente permanece **inalterado** — `A2AExecutor` adapta seu agente existente ao protocolo.
O Agent Card é o que o torna **descobrível** para qualquer cliente A2A.

---

## 4. Consumir um agente remoto — `a2a_client.py`

O lado **Consume** conecta-se a um agente remoto **pela URL**, busca seu Agent Card e o chama
exatamente como um agente local. Veja [`a2a_client.py`](../../../lesson-7-multi-agent-a2a/a2a_client.py):

```python
from agent_framework.a2a import A2AAgent

remote_agent = A2AAgent(name="remote-coding-assistant", url="http://localhost:9000")
result = await remote_agent.run("Write a Python function that reverses a string.")
print(result.text)
```

Esse é o objetivo do A2A: do lado do chamador, um agente remoto se comporta como qualquer outro
`agent_framework` agent, então você pode inseri-lo em um workflow ou delegar para ele — mesmo que ele rode
em um processo diferente, em uma máquina diferente, e seja propriedade de uma equipe diferente.

### Execute-o de ponta a ponta

```bash
# Terminal 1 — iniciar o serviço A2A
python a2a_server.py

# Terminal 2 — chamá-lo
python a2a_client.py "Write a Python function that reverses a string."
```

Você verá a resposta do assistente de codificação chegar via protocolo A2A. Abra
`http://localhost:9000/.well-known/agent-card.json` em um navegador para ver o Agent Card publicado.

---

## 5. Preocupações empresariais

Transformar agentes em serviços em rede introduz as mesmas preocupações de qualquer sistema distribuído —
além de algumas específicas de IA:

- **Identidade e autenticação.** Nunca exponha um agente A2A sem autenticação. O Agent Card carrega
  `security` / `security_schemes`, e `A2AAgent` aceita um `auth_interceptor` para que os chamadores anexem
  credenciais (tokens bearer OAuth, chaves de API). Use Entra ID / managed identities para
  autenticação serviço-a-serviço em produção; coloque o serviço atrás de um gateway.
- **Governança.** Combine A2A com a [Toolbox da Lição 6](../lesson-6-toolbox/README.md): um agente remoto
  pode ser publicado como uma **ferramenta A2A** dentro de uma toolbox governada para que RBAC, injeção de credenciais,
  e políticas de governança sejam aplicadas centralmente.
- **Observabilidade.** Uma requisição agora cruza limites de processo, então propague o rastreamento através da chamada.
  Habilite [Foundry Observability / OpenTelemetry](../lesson-3-agent-evals/README.md) em **ambos** os
  orquestrador e cada agente remoto para obter um rastreamento de ponta a ponta.
- **Versionamento.** O Agent Card tem um `version`. Trate-o como uma API: mudanças aditivas são seguras;
  quebrar o contrato de uma skill exige uma nova versão e uma janela de migração para os consumidores.
- **Confiabilidade.** Agentes remotos falham de forma independente. Defina timeouts (`A2AAgent(timeout=...)`), trate
  falhas parciais, e não deixe que um par lento bloqueie toda a orquestração.
- **Custo.** Cada chamada a um agente remoto é sua própria invocação de modelo. Fan-out multiplica o gasto de tokens —
  reserve orçamento para isso, e prefira rotear para **um** agente melhor ao invés de transmitir para muitos.

---

## Exercícios práticos

1. **Adicione um segundo serviço.** Copie `a2a_server.py` para expor o agente **employee-search** na porta
   9001 com seu próprio Agent Card e skills. Execute ambos, e faça um cliente chamar cada um.
2. **Orquestre pares remotos.** Construa um pequeno `HandoffBuilder` (ou um roteador simples) cujos participantes
   incluam dois `A2AAgent`s apontando para seus dois serviços. Roteie uma consulta para o correto.
3. **Proteja-o.** Adicione um `auth_interceptor` ao cliente e exija um token bearer no servidor.
   O que quebra se o token estiver ausente? Onde você armazenaria o token em produção?
4. **Handoff vs A2A.** Escreva dois parágrafos curtos: quando você manteria o handoff em processo
   e quando a complexidade extra do A2A é justificada? Dê um exemplo concreto de cada.

---

## Recursos

- [Agente-para-Agente (A2A) — Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/user-guide/agent-orchestration/a2a)
- [Orquestração multi-agente — Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/user-guide/agent-orchestration/)
- [Especificação do protocolo A2A](https://a2a-protocol.org/)
- [A2A Python SDK (`a2a-sdk`)](https://github.com/a2aproject/a2a-python)
- [Foundry Agent Service — padrões multi-agente](https://learn.microsoft.com/azure/ai-foundry/agents/concepts/connected-agents)

---

**Anterior:** [Lição 6 — Microsoft Toolbox](../lesson-6-toolbox/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->