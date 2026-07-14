# 遷移指南 — Microsoft Foundry Agent Framework（2026年7月）

本指南將課程範例最初所使用的 SDK 表面映射到
<strong>目前已發佈的</strong> Microsoft Agent Framework 套件。下面的每個映射和
函式簽名均透過檢視已安裝的套件
（`agent-framework 1.2.0`、`agent-framework-foundry 1.2.0`）進行驗證。

> **為何這很重要：** 隨著重新命名為 **Microsoft Foundry**，用戶端界面從
> `agent_framework.azure`（舊的 `AzureAI*` 類別）遷移到了 **`agent_framework.foundry`**
> （`FoundryChatClient`、`FoundryAgent`）。舊的頂層託管工具類別
> （`HostedMCPTool`、`HostedFileSearchTool`、`HostedVectorStoreContent`）已被移除；
> 現在託管工具是從 <strong>用戶端</strong> 透過 `get_*_tool(...)` 工廠方法建立。

---

## 1. 匯入和用戶端映射

| 舊版（課程範例） | 新版（Microsoft Foundry） |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → 回傳 `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool`（用戶端 MCP） | 不變 — 仍是 `from agent_framework import MCPStreamableHTTPTool` |

**認證參數名稱變更：** 舊用戶端接受 `async_credential=...`；
`FoundryChatClient` 則接受 `credential=...`。

---

## 2. 已驗證的函式簽名

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # 或設置 AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # 或設置模型環境變數
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # 微軟工具箱
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # 可觀察性
```

---

## 3. 前／後 — 單一代理與託管 MCP 工具

<strong>之前</strong>（`azure-learning-agent.py`）：

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

<strong>之後</strong>（Microsoft Foundry）：

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

## 4. 前／後 — 託管檔案搜尋（向量庫）

<strong>之前</strong>（`employee-search-agent.py`）：

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

<strong>之後</strong>：

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. 棄用的非同步模式

<strong>之前</strong>（`learning-recommendation-agent.py`）：

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` 已被棄用。建議使用託管的 `client.get_mcp_tool(...)`
（不需手動連接），或者若必須使用用戶端的 `MCPStreamableHTTPTool`，請用
`asyncio.run(...)` 或 `async with` 區塊包裝它。

---

## 6. 本課程現在使用的進階功能

| 功能 | 匯入 |
|-----------|--------|
| **Microsoft 工具箱** | `client.get_toolbox("<name>")`，`from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry 記憶體** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **可觀察性／評估** | `client.configure_azure_monitor()`，`from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry 本地端** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a`（`import agent_framework.a2a`） |
| <strong>託管代理執行時</strong> | `agent-framework-foundry-hosting`，`azure.ai.agentserver` |

> **注意。** 這些程式片段的匯入和函式簽名均已根據目前套件驗證。
> 端對端執行還需要 Microsoft Foundry 專案、一個已部署的聊天模型，
> 以及（針對檔案搜尋）一個已填充的向量庫。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->