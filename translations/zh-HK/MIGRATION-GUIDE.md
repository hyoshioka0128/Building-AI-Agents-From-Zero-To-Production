# 遷移指南 — Microsoft Foundry Agent Framework (2026年7月)

本指南將課程範例原先使用的 SDK 介面對應到
<strong>目前發佈的</strong> Microsoft Agent Framework 套件。以下每個映射及
簽名均透過檢查已安裝的套件
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`) 確認。

> **為何這很重要：** 隨著品牌改名為 **Microsoft Foundry**，用戶端介面從
> `agent_framework.azure`（舊有的 `AzureAI*` 類別）移轉至 **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`)。舊有頂層托管工具類別
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) 被移除；托管
> 工具現於 <strong>由用戶端透過工廠方法</strong> `get_*_tool(...)` 建立。

---

## 1. 匯入與用戶端對應

| 舊版（課程範例） | 新版（Microsoft Foundry） |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → 回傳 `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool`（用戶端 MCP） | 無改動 — 仍為 `from agent_framework import MCPStreamableHTTPTool` |

**認證參數改名：** 舊用戶端使用 `async_credential=...`；
`FoundryChatClient` 改為 `credential=...`。

---

## 2. 簽名已驗證

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # 或設定 AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # 或設定模型環境變數
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Microsoft 工具箱
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # 可觀察性
```

---

## 3. 之前／之後 — 擁有托管 MCP 工具的單一代理

<strong>之前</strong> (`azure-learning-agent.py`)：

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

## 4. 之前／之後 — 托管檔案搜尋（向量庫）

<strong>之前</strong> (`employee-search-agent.py`)：

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

## 5. 已棄用的 async 模式

<strong>之前</strong> (`learning-recommendation-agent.py`)：

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` 已被棄用。建議使用托管的 `client.get_mcp_tool(...)`
（無需手動連接），若必須使用用戶端的 `MCPStreamableHTTPTool`，請用
`asyncio.run(...)` 或 `async with` 區塊封裝。

---

## 6. 本課程目前使用的進階介面

| 功能 | 匯入 |
|-----------|--------|
| **Microsoft 工具箱** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry 記憶體** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **可觀察性 / 評估** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| <strong>托管代理運行時</strong> | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **注意。** 此代碼片段均已針對目前套件之匯入與簽名做驗證。
> 完整執行流程則另需 Microsoft Foundry 專案、已部署的聊天模型，及（檔案搜尋用）
> 已填充的向量庫。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->