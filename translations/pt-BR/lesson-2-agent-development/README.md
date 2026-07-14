# Lição 2 Desenvolvimento de Agentes

Bem-vindo à segunda lição do curso "Construindo Agentes de IA do Zero à Produção"!

Nesta lição, abordaremos:

- As ferramentas para criar nossos Agentes de IA
  
- Instruções de configuração para nossos recursos de desenvolvimento

- Melhores práticas para desenvolvimento de Agentes de IA
  
- Passo a passo do código para criar nossos Agentes de IA
  
Vamos começar olhando as ferramentas que usaremos para criar nossos Agentes de IA.

## Ferramentas e Instruções de Configuração

### Microsoft Foundry

Para acessar Modelos de Linguagem de Grande Escala (LLMs), usaremos [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Há custos associados ao uso do Foundry, portanto certifique-se de seguir as instruções de configuração de conta se você ainda não tiver acesso.

### OpenAI Models

Os exemplos de código dos agentes neste curso estão configurados para usar modelos OpenAI através do [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Use este guia para aprender como implantar um modelo usando o Foundry: [Implantar modelos do Microsoft Foundry no portal Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Escolha um modelo da série GPT-5 (por exemplo `gpt-5.1`) para este curso. Evite modelos aposentados como GPT-4o e GPT-4.1, que atingem o fim de vida em 2026.

### Microsoft Agent Framework

Como mencionado anteriormente, usaremos o [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) tanto para criar quanto para orquestrar nossos Agentes de IA.

Você precisará de **Python 3.12 ou superior**. Para instalar o Microsoft Agent Framework e outros pacotes necessários, execute o seguinte comando estando no diretório raiz deste projeto:

```bash
pip install -r requirements.txt
```

### Autenticar com o Azure

Os agentes se autenticam no Microsoft Foundry usando suas credenciais do Azure CLI
(`AzureCliCredential`), portanto você deve fazer login antes de executar qualquer exemplo:

```bash
az login
# Se você tiver mais de uma assinatura, selecione a que contém seu projeto Foundry:
az account set --subscription "<your-subscription-id>"
```

Certifique-se de que sua conta tenha a **Azure AI User** função (ou equivalente) no Foundry
projeto para que ela possa chamar as APIs de modelo e agente.

### Setup .env Variables

Para executar os exemplos de código deste curso, você precisará criar um arquivo `.env` no diretório raiz deste projeto. 

Para facilitar, você pode copiar o arquivo `.env.example` fornecido:

```bash
cp .env.example .env
``` 

Em seguida, preencha as duas variáveis que os agentes leem (o `FoundryChatClient` as detecta
automaticamente):

| Variável | O que é | Onde encontrá-la |
|----------|------------|------------------|
| `FOUNDRY_PROJECT_ENDPOINT` | Seu endpoint do projeto Foundry, terminando em `/api/projects/<project>` | Portal Foundry → seu projeto → **Overview** → *Endpoints* |
| `FOUNDRY_MODEL` | O nome da implantação do modelo em que seus agentes são executados (por exemplo `gpt-5.1`) | Portal Foundry → **Models + endpoints** |

### Create the employee vector store

One sample — the **Employee Search Agent** — searches an employee directory held in a
Microsoft Foundry **vector store**. Crie-o uma vez e copie o ID que ele imprimir para o seu `.env`
como `VECTOR_STORE_ID` (execute a partir da raiz do repositório para que ele leia seu `.env`):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### Run a sample

Cada agente executa sua própria DevUI local. Por exemplo:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

Em seguida, abra a URL impressa `http://localhost:<port>` no seu navegador para conversar com o agente.

## Os agentes nesta lição

Cada exemplo é um agente independente construído com o Microsoft Agent Framework. Juntos, eles
implementam os cenários que você projetou na [Lição 1](../lesson-1-agent-design/README.md):

| Exemplo | Cenário da Lição 1 | Ferramenta usada | Porta |
|--------|-------------------|-----------|------|
| `employee-search-agent.py` | Cenário 1 — Pesquisa de Funcionários | Pesquisa de **arquivos** hospedada no Foundry sobre um vector store | 8090 |
| `task-recommendation-agent.py` | Cenário 2 — Recomendação de Tarefas | servidor **GitHub MCP** (ferramenta MCP hospedada) | 8095 |
| `azure-learning-agent.py` | Cenário 3 — Assistente de Código (pesquisa) | servidor **Microsoft Learn MCP** (ferramenta MCP hospedada) | 8092 |
| `coding-agent.py` | Cenário 3 — Assistente de Código (código) | **Code Interpreter** | 8093 |
| `learning-recommendation-agent.py` | Agente de suporte | Learn MCP + raciocínio | 8091 |
| `agent-orchestration.py` | Integra os cenários | Orquestração multi-agente de **handoff** | 8094 |

> **Nota sobre o Agente de Recomendação de Tarefas.** `task-recommendation-agent.py` precisa de um
> `GITHUB_PERSONAL_ACCESS_TOKEN` no seu `.env` (crie um em
> <https://github.com/settings/personal-access-tokens/new>). Ele lê as atividades recentes no GitHub de um desenvolvedor e
> recomenda 1–3 issues abertas que correspondam — exatamente ao design do Cenário 2.
> Este é o único exemplo que chama o GitHub; os demais precisam apenas do seu projeto Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->