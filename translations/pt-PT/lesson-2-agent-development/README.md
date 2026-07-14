# Lição 2 Desenvolvimento de Agentes

Bem-vindo à segunda lição do  "Building AI Agent from Zero to Production Course"!

Nesta lição vamos abordar:

- As Ferramentas para Criar os nossos Agentes de IA
  
- Instruções de Configuração para os nossos Recursos de Desenvolvimento

- Boas Práticas de Desenvolvimento de Agentes de IA
  
- Revisão do Código para Criar os nossos Agentes de IA
  
Comecemos por olhar para as ferramentas que iremos usar para criar os nossos Agentes de IA.

## Ferramentas e Instruções de Configuração

### Microsoft Foundry

Para aceder a Large Langauge Models (LLMs) iremos utilizar o [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Existem custos associados ao uso do Foundry, por isso certifique-se de seguir as instruções para configurar a conta se ainda não tiver acesso.

### Modelos OpenAI

Os exemplos de código dos agentes neste curso estão configurados para usar modelos OpenAI através do [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Use este guia para aprender como implantar um modelo usando o Foundry: [Implantar modelos Microsoft Foundry no portal Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Escolha um modelo da série GPT-5 (por exemplo `gpt-5.1`) para este curso. Evite modelos descontinuados como GPT-4o e GPT-4.1, que atingem o fim de vida em 2026.

### Microsoft Agent Framework

Como mencionado anteriormente, iremos usar o [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) para criar e orquestrar os nossos Agentes de IA.

Vai precisar de **Python 3.12 ou posterior**. Para instalar o Microsoft Agent Framework e outros pacotes necessários, execute o seguinte comando enquanto estiver no diretório raiz deste projeto:

```bash
pip install -r requirements.txt
```

### Autenticar com o Azure

Os agentes autenticam-se no Microsoft Foundry usando as suas credenciais do Azure CLI
(`AzureCliCredential`), portanto deve iniciar sessão antes de executar qualquer exemplo:

```bash
az login
# Se tiver mais do que uma subscrição, selecione aquela que contém o seu projeto Foundry:
az account set --subscription "<your-subscription-id>"
```

Certifique-se de que a sua conta tem a função **Azure AI User** (ou equivalente) no Foundry
projeto para que possa chamar as APIs de modelos e agentes.

### Setup .env Variables

Para executar os exemplos de código deste curso, será necessário criar um ficheiro `.env` no diretório raiz deste projeto. 

Para facilitar, pode copiar o ficheiro `.env.example` fornecido:

```bash
cp .env.example .env
``` 

Depois preencha as duas variáveis que os agentes lêem (o `FoundryChatClient` capta-as
automaticamente):

| Variável | O que é | Onde encontrá-la |
|----------|------------|------------------|
| `FOUNDRY_PROJECT_ENDPOINT` | O endpoint do **projeto** Foundry, terminando em `/api/projects/<project>` | Foundry portal → o seu projeto → **Overview** → *Endpoints* |
| `FOUNDRY_MODEL` | O nome da implantação do modelo onde os seus agentes são executados (por exemplo `gpt-5.1`) | Foundry portal → **Models + endpoints** |

### Create the employee vector store

One sample — the **Employee Search Agent** — searches an employee directory held in a
Microsoft Foundry **vector store**. Create it once and copy the ID it prints into your `.env`
as `VECTOR_STORE_ID` (run from the repository root so it picks up your `.env`):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### Run a sample

Each agent runs its own local DevUI. For example:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

Then open the printed `http://localhost:<port>` URL in your browser to chat with the agent.

## The agents in this lesson

Each sample is a standalone agent built with the Microsoft Agent Framework. Together they
implement the scenarios you designed in [Lição 1](../lesson-1-agent-design/README.md):

| Exemplo | Cenário da Lição 1 | Ferramenta utilizada | Porta |
|--------|-------------------|-----------|------|
| `employee-search-agent.py` | Cenário 1 — Pesquisa de Funcionários | Foundry hosted **file search** over a vector store | 8090 |
| `task-recommendation-agent.py` | Cenário 2 — Recomendação de Tarefas | **GitHub MCP** server (hosted MCP tool) | 8095 |
| `azure-learning-agent.py` | Cenário 3 — Assistente de Código (pesquisa) | **Microsoft Learn MCP** server (hosted MCP tool) | 8092 |
| `coding-agent.py` | Cenário 3 — Assistente de Código (código) | **Code Interpreter** | 8093 |
| `learning-recommendation-agent.py` | Agente de suporte | Learn MCP + reasoning | 8091 |
| `agent-orchestration.py` | Integra os cenários | Multi-agent **handoff** orchestration | 8094 |

> **Nota sobre o Agente de Recomendação de Tarefas.** `task-recommendation-agent.py` needs a
> `GITHUB_PERSONAL_ACCESS_TOKEN` in your `.env` (create one at
> <https://github.com/settings/personal-access-tokens/new>). It reads a developer's recent
> GitHub activity and recommends 1–3 open issues that match — exactly the Scenario 2 design.
> This is the only sample that calls GitHub; the others need only your Foundry project.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->