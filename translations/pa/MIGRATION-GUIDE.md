# ਮਾਈਗ੍ਰੇਸ਼ਨ ਗਾਈਡ — Microsoft Foundry Agent Framework (ਜੁਲਾਈ 2026)

ਇਹ ਗਾਈਡ SDK ਸਤਹ ਦਾ ਨਕਸ਼ਾ ਦਿਖਾਉਂਦੀ ਹੈ ਜਿਸਦੇ ਖਿਲਾਫ ਕੋਰਸ ਨਮੂਨੇ ਮੁਲ਼ ਰੂਪ ਵਿੱਚ ਲਿਖੇ ਗਏ ਸਨ
onto the **ਮੌਜੂਦਾ, ਪ੍ਰਕਾਸ਼ਿਤ** Microsoft Agent Framework ਪੈਕੇਜਾਂ. Every mapping and
signature below was verified by introspecting the installed packages
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **ਇਹ ਮਹੱਤਵਪੂਰਨ ਕਿਉਂ ਹੈ:** Microsoft Foundry ਵੱਲ ਰੀਬ੍ਰੈਂਡ ਹੋਣ ਨਾਲ, ਕਲਾਇੰਟ ਸਤਹ moved
> from `agent_framework.azure` (ਪੁਰਾਣੇ `AzureAI*` ਕਲਾਸਾਂ) to **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). ਪੁਰਾਣੀਆਂ ਟੌਪ-ਲੇਵਲ hosted-tool ਕਲਾਸਾਂ
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) ਹਟਾ ਦਿੱਤੀਆਂ ਗਈਆਂ; hosted
> tools are now created **from the client** via `get_*_tool(...)` factory methods.

---

## 1. ਇੰਪੋਰਟ ਅਤੇ ਕਲਾਇੰਟ ਮੈਪਿੰਗ

| ਪੁਰਾਣਾ (ਕੋਰਸ ਨਮੂਨੇ) | ਨਵਾਂ (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → ਵਾਪਸ ਕਰਦਾ ਹੈ `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (ਕਲਾਇੰਟ-ਸਾਈਡ MCP) | ਬਦਲਿਆ ਨਹੀਂ — ਹਾਲੇ ਵੀ `from agent_framework import MCPStreamableHTTPTool` |

**ਕ੍ਰੈਡੈਂਸ਼ੀਅਲ ਪੈਰਾਮੀਟਰ ਦਾ ਨਾਮ ਬਦਲਿਆ ਗਿਆ:** the old clients took `async_credential=...`;
`FoundryChatClient` takes `credential=...`.

---

## 2. ਪ੍ਰਮਾਣਿਤ ਸਿਗਨੇਚਰ

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # ਜਾਂ AZURE_AI_PROJECT_ENDPOINT ਸੈੱਟ ਕਰੋ
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # ਜਾਂ ਮਾਡਲ ਐਨਵਾਇਰਨਮੈਂਟ ਵੈਰੀਏਬਲ ਸੈੱਟ ਕਰੋ
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Microsoft ਟੂਲਬਾਕਸ
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # ਨਿਰੀਖਣ ਯੋਗਤਾ
```

---

## 3. ਪਹਿਲਾਂ / ਬਾਅਦ — ਇੱਕ ਇੱਕਲਾ ਏਜੰਟ ਹੋਸਟਡ MCP ਟੂਲ ਨਾਲ

**ਪਹਿਲਾਂ** (`azure-learning-agent.py`):

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

**ਬਾਅਦ** (Microsoft Foundry):

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

## 4. ਪਹਿਲਾਂ / ਬਾਅਦ — ਹੋਸਟਡ ਫਾਈਲ ਖੋਜ (ਵੈਕਟਰ ਸਟੋਰ)

**ਪਹਿਲਾਂ** (`employee-search-agent.py`):

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

**ਬਾਅਦ**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. ਡੀਪ੍ਰੀਕੇਟਿਡ async ਪੈਟਰਨ

**ਪਹਿਲਾਂ** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` ਨਿਰਸਤ ਹੈ। ਹੋਸਟਡ `client.get_mcp_tool(...)` ਨੂੰ ਤਰਜੀਹ ਦਿਓ
(ਕੋਈ ਮੈਨੂਅਲ ਕਨੈਕਟ ਨਹੀਂ), ਜਾਂ ਜੇ ਤੁਹਾਨੂੰ ਕਲਾਇੰਟ-ਸਾਈਡ `MCPStreamableHTTPTool` ਵਰਤਣੀ ਪਏ, ਤਾਂ ਇਸ ਨੂੰ
`asyncio.run(...)` ਜਾਂ `async with` ਸੰਦਰਭ ਵਿੱਚ ਲਪੇਟੋ.

---

## 6. ਉन्नਤ ਸਤਹ ਜੋ ਇਹ ਕੋਰਸ ਹੁਣ ਵਰਤਦਾ ਹੈ

| ਸਮਰੱਥਾ | ਇੰਪੋਰਟ |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **ਨਿਰੀਖਣ / ਮੁਲਾਂਕਣ** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **ਹੋਸਟਡ-ਏਜੰਟ ਰਨਟਾਈਮ** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **ਨੋਟ.** ਇਹ ਸ્નਿਪੇਟਸ ਇੰਪੋਰਟ ਅਤੇ ਸਿਗਨੇਚਰ ਦੇ ਸੰਦਰਭ ਵਿੱਚ ਮੌਜੂਦਾ ਪੈਕੇਜਾਂ ਨਾਲ ਪ੍ਰਮਾਣਿਤ ਕੀਤੇ ਗਏ ਹਨ।
> ਆਖਰੀ ਤੱਕ ਕਾਰਜਨਿਰਵਾਹ ਲਈ ਵਧੇਰੇ ਤੌਰ 'ਤੇ ਇੱਕ Microsoft Foundry ਪ੍ਰੋਜੈਕਟ, ਇੱਕ ਡਿਪਲੌਏਡ ਚੈਟ
> ਮਾਡਲ, ਅਤੇ (ਫਾਈਲ ਖੋਜ ਲਈ) ਇੱਕ ਭਰਿਆ ਹੋਇਆ ਵੈਕਟਰ ਸਟੋਰ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->