# Migration Guide — Microsoft Foundry Agent Framework (July 2026)

This guide maps the SDK surface the course samples were originally written against
onto the **current, published** Microsoft Agent Framework packages. Every mapping and
signature below was verified by introspecting the installed packages
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Why this matters:** with the rebrand to **Microsoft Foundry**, the client surface moved
> from `agent_framework.azure` (the old `AzureAI*` classes) to **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). The old top-level hosted-tool classes
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) were removed; hosted
> tools are now created **from the client** via `get_*_tool(...)` factory methods.

---

## 1. Import & client mapping

| Old (course samples) | New (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → returns `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (client-side MCP) | unchanged — still `from agent_framework import MCPStreamableHTTPTool` |

**Credential parameter renamed:** the old clients took `async_credential=...`;
`FoundryChatClient` takes `credential=...`.

---

## 2. Verified signatures

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # or set AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # or set the model env var
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

## 3. Before / after — a single agent with a hosted MCP tool

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

`asyncio.get_event_loop()` is deprecated. Prefer the hosted `client.get_mcp_tool(...)`
(no manual connect), or if you must use the client-side `MCPStreamableHTTPTool`, wrap it
in `asyncio.run(...)` or an `async with` context.

---

## 6. Advanced surfaces this course now uses

| Capability | Import |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observability / eval** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Hosted-agent runtime** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Note.** These snippets are import- and signature-verified against the current packages.
> End-to-end execution additionally requires a Microsoft Foundry project, a deployed chat
> model, and (for file search) a populated vector store.
