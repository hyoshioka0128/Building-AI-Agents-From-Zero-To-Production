# Migration Guide — Microsoft Foundry Agent Framework (July 2026)

Dis guide show how di SDK surface wey di course samples bin originally write for
take relate to di **current, published** Microsoft Agent Framework packages. Every mapping and
signature below e don check by looking inside di installed packages
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Why dis matter:** as dem don rebrand am to **Microsoft Foundry**, di client surface don shift
> from `agent_framework.azure` (di old `AzureAI*` classes) to **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Di old top-level hosted-tool classes
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) dem don remove; hosted
> tools now na **from di client** via `get_*_tool(...)` factory methods wey dem dey create am.

---

## 1. Import & client mapping

| Old (course samples) | New (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → e go return `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (client-side MCP) | no change — still `from agent_framework import MCPStreamableHTTPTool` |

**Credential parameter rename:** di old clients dey use `async_credential=...`;
`FoundryChatClient` dey use `credential=...`.

---

## 2. Verified signatures

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # or set AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # or set di model env var
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Microsoft Toolbox
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Observability
```

---

## 3. Before / after — one single agent wey get hosted MCP tool

**Before** (`azure-learning-agent.py`):

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

**After** (Microsoft Foundry):

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

## 4. Before / after — hosted file search (vector store)

**Before** (`employee-search-agent.py`):

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

**After**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Deprecated async pattern

**Before** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` don old. E good make you prefer di hosted `client.get_mcp_tool(...)`
(no need connect manually), or if you need use di client-side `MCPStreamableHTTPTool`, make you wrap am
inside `asyncio.run(...)` or use am with `async with` context.

---

## 6. Advanced surfaces wey dis course de use now

| Capability | Import |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observability / eval** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Hosted-agent runtime** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Note.** Dis snippets na import- and signature-verified with di current packages.
> To run am end-to-end, you need Microsoft Foundry project, deployed chat
> model, and (for file search) vector store wey don fill.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->