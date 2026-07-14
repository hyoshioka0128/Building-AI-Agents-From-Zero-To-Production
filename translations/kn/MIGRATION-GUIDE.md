# міಗ್ರೇಷನ್ ಗೈಡ್ — ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವಾರ್ಕ್ (ಜುಲೈ 2026)

ಈ ಗೈಡ್ SDK ಮೇಲ್ಮೈ ಎಲ್ಲದನ್ನು ಕೋರ್ಸ್ ಮಾದರಿಗಳು ಮೂಲತಃ ಬರಹ ಮಾಡಿದ್ದವು ಅನ್ವಯವಾಗಿದಂತೆ ನಕ್ಷೆ ಹಾಕುತ್ತದೆ
**ಪ್ರಸ್ತುತ, ಪ್ರಕಟಿತ** ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವಾರ್ಕ್ ಪ್ಯಾಕೇಜುಗಳಿಗೆ. ಪ್ರತಿಯೊಂದು ನಕ್ಷೆ ಮತ್ತು
ಕೆಳಗಿನ ಸಹಿ ಸ್ಥಿತಿಯನ್ನು ಸ್ಥಾಪಿಸಲಾಗಿದೆ ಸ್ಥಾಪಿಸಲಾಗಿರುವ ಪ್ಯಾಕೇಜುಗಳನ್ನು ಪರಿಶೀಲಿಸಿ
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **ಏಕೆ ಇದು ಪ್ರಮುಖ:** ಮರುಬ್ರ್ಯಾಂಡ್ ಆಗಿ **Microsoft Foundry** ಗೆ, ಕ್ಲೈಂಟ್ ಮೇಲ್ಮೈ
> `agent_framework.azure` (ಹಳೆಯ `AzureAI*` ವರ್ಗಗಳು) ನಿಂದ **`agent_framework.foundry`** ಗೆ ಸೇರಿದೆ
> (`FoundryChatClient`, `FoundryAgent`). ಹಳೆಯ top-level ಹೋಸ್ಟ್ ಮಾಡಿದ ಟೂಲ್ ವರ್ಗಗಳು
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) ತೆಗೆದಿವೆ; 
> ಟೂಲ್ ಗಳು ಈಗ **ಕ್ಲೈಂಟ್ ಮೂಲಕ** `get_*_tool(...)` ಫ್ಯಾಕ್ಟರಿ ವಿಧಾನಗಳ ಮೂಲಕ ರಚಿಸಲಾಗಿದೆ.

---

## 1. ಆಮದು ಮತ್ತು ಕ್ಲೈಂಟ್ ನಕ್ಷೆ

| ಹಳೆಯದು (ಕೋರ್ಸ್ ಮಾದರಿಗಳು) | ಹೊಸದು (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → `Agent` ಅನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (ಕ್ಲೈಂಟ್-ಮಾಧ್ಯಮ MCP) | ಬದಲಾಗಿಲ್ಲ — ಇನ್ನೂ `from agent_framework import MCPStreamableHTTPTool` |

**ಪ್ರಮಾಣಪತ್ರ ಪರಾಮಿತಿ ಹೆಸರು ಬದಲಾಗಿದೆ:** ಹಳೆಯ ಕ್ಲೈಂಟ್ ಗಳು `async_credential=...` ಬಳಸಿ;
`FoundryChatClient` `credential=...` ಅನ್ನು ತೆಗೆದುಕೊಳ್ಳುತ್ತದೆ.

---

## 2. ಪರಿಶೀಲಿತ ಸಹಿಗಳು

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # ಅಥವಾ AZURE_AI_PROJECT_ENDPOINT ಅನ್ನು ಹೊಂದಿಸಿ
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # ಅಥವಾ ಮಾದರಿ ಪರಿಸರ ಚರವನ್ನು ಹೊಂದಿಸಿ
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # ಮೈಕ್ರೋಸಾಫ್ಟ್ ಟೂಲ್ಬಾಕ್ಸ್
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # ವೀಕ್ಷಣೀಯತೆ
```

---

## 3. ಮುಂಚೆ / ನಂತರ — ಹೋಸ್ಟ್ ಮಾಡಿದ ಒಬ್ಬ ಏಜೆಂಟ್ ಮತ್ತು MCP ಟೂಲ್

**ಮುಂಚೆ** (`azure-learning-agent.py`):

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

**ನಂತರ** (Microsoft Foundry):

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

## 4. ಮುಂಚೆ / ನಂತರ — ಹೋಸ್ಟ್ ಮಾಡಿದ ಫೈಲ್ ಶೋಧ (ವೆಕ್ಟರ್ ಸ್ಟೋರ್)

**ಮುಂಚೆ** (`employee-search-agent.py`):

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

**ನಂತರ**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. ಹಳೆಯ async ಮಾದರಿ

**ಮುಂಚೆ** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` ನಿಷೇಧಿಸಲಾಗಿದೆ. ಹೋಸ್ಟ್ ಮಾಡಿದ `client.get_mcp_tool(...)`
(ಯಾವುದೇ ಕೈಯಿಂದ ಸಂಪರ್ಕವಿಲ್ಲ), ಅಥವಾ ನೀವು ಕ್ಲೈಂಟ್-ಮಾಧ್ಯಮ `MCPStreamableHTTPTool` ಅನ್ನು ಬಳಸಬೇಕಾದರೆ,
ಅದನ್ನು `asyncio.run(...)` ಅಥವಾ `async with` ಪ್ರ_CONTEXT ನಲ್ಲಿ ಮುಚ್ಚಿ.

---

## 6. ಈ ಕೋರ್ಸ್ ಈಗ ಬಳಸುವ ಪ್ರगत ಮೇಲ್ಮೈಗಳು

| ಸಾಮರ್ಥ್ಯ | ಆಮದು |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **ಪರೀಕ್ಷಣೆ / ಮೌಲ್ಯಾಂಕನ** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **ಹೋಸ್ಟ್ ಮಾಡಿದ ಏಜೆಂಟ್ ರನ್‌ಟೈಮ್** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **ಗುರುತಿಸಿ.** ಈ ಉದಾಹರಣೆಗಳು ಆಮದು ಮತ್ತು ಸಹಿ ಪರಿಶೀಲನೆಯನ್ನು ಪ್ರಸ್ತುತ ಪ್ಯಾಕೇಜುಗಳಿಗೇ ಮಾಡಲಾಗಿದೆ.
> ಪೂರ್ಣ ಅಂತಿಮ ಕಾರ್ಯಕ್ಕೆ Microsoft Foundry ಪ್ರಾಜೆಕ್ಟ್, ನಿಯೋಜಿತ ಚಾಟ್
> ಮಾದರಿ ಮತ್ತು (ಫೈಲ್ ಶೋಧಕ್ಕಾಗಿ) ತುಂಬಿದ ವೆಕ್ಟರ್ ಸ್ಟೋರ್ ಅಗತ್ಯವಿದೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->