# Guia de Migração — Microsoft Foundry Agent Framework (julho de 2026)

Este guia mapeia a superfície do SDK contra a qual os exemplos do curso foram originalmente escritos
para os pacotes **atuais e publicados** do Microsoft Agent Framework. Cada mapeamento e
assinatura abaixo foi verificada inspecionando os pacotes instalados
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Porque isto importa:** com a mudança de marca para **Microsoft Foundry**, a superfície do cliente mudou
> de `agent_framework.azure` (as antigas classes `AzureAI*`) para **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). As antigas classes de ferramentas hospedadas de nível superior
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) foram removidas; as ferramentas hospedadas
> são agora criadas **pelo cliente** através dos métodos de fábrica `get_*_tool(...)`.

---

## 1. Importação e mapeamento do cliente

| Antigo (exemplos do curso) | Novo (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → retorna `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (MCP do lado do cliente) | inalterado — ainda `from agent_framework import MCPStreamableHTTPTool` |

**Parâmetro credential renomeado:** os clientes antigos usavam `async_credential=...`;
`FoundryChatClient` usa `credential=...`.

---

## 2. Assinaturas verificadas

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # ou defina a variável AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # ou defina a variável de ambiente do modelo
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Caixa de ferramentas Microsoft
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Observabilidade
```

---

## 3. Antes / depois — um único agente com uma ferramenta MCP alojada

**Antes** (`azure-learning-agent.py`):

```python
from azure.identity.aio import AzureCliCredential
from agent_framework import HostedMCPTool
from agent_framework.azure import AzureAIClient

client = AzureAIClient(async_credential=AzureCliCredential())
agent = client.create_agent(
    name="LearningPathAgent",
    instructions=AGENT_INSTRUCTIONS,
    tools=HostedMCPTool(
        name="Microsoft Learn MCP",
        url="https://learn.microsoft.com/api/mcp",
        approval_mode="never_require",
    ),
)
```

**Depois** (Microsoft Foundry):

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    name="LearningPathAgent",
    instructions=AGENT_INSTRUCTIONS,
    tools=client.get_mcp_tool(
        name="Microsoft Learn MCP",
        url="https://learn.microsoft.com/api/mcp",
        approval_mode="never_require",
    ),
)
```

---

## 4. Antes / depois — pesquisa de ficheiros alojada (armazenamento vetorial)

**Antes** (`employee-search-agent.py`):

```python
from agent_framework import ChatAgent, HostedFileSearchTool, HostedVectorStoreContent
from agent_framework.azure import AzureAIAgentClient

file_search_tool = HostedFileSearchTool(
    inputs=[HostedVectorStoreContent(vector_store_id=os.environ["VECTOR_STORE_ID"])]
)
agent = ChatAgent(
    chat_client=AzureAIAgentClient(async_credential=AzureCliCredential()),
    instructions="...",
    tools=[file_search_tool],
)
```

**Depois**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Padrão assíncrono obsoleto

**Antes** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` está obsoleto. Prefira a `client.get_mcp_tool(...)` hospedada
(sem ligação manual), ou se tiver de usar o `MCPStreamableHTTPTool` do lado do cliente, envolva-o
em `asyncio.run(...)` ou num contexto `async with`.

---

## 6. Interfaces avançadas que este curso agora utiliza

| Funcionalidade | Importação |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observabilidade / avaliação** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Runtime do agente hospedado** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Nota.** Estes excertos foram verificados quanto às importações e assinaturas contra os pacotes atuais.
> A execução de ponta a ponta requer adicionalmente um projeto Microsoft Foundry, um modelo de chat implantado
> modelo, e (para pesquisa de ficheiros) um armazenamento vetorial populado.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->