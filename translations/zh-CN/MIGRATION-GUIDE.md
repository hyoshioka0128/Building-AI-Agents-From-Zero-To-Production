# 迁移指南 — Microsoft Foundry 代理框架（2026年7月）

本指南将课程示例最初编写时使用的 SDK 接口映射
到<strong>当前发布的</strong> Microsoft 代理框架包。下面的每个映射和
签名均通过检查已安装的包
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`) 验证。

> **为何重要：** 随着更名为 **Microsoft Foundry**，客户端接口
> 从 `agent_framework.azure`（旧的 `AzureAI*` 类）迁移到 **`agent_framework.foundry`**
> （`FoundryChatClient`，`FoundryAgent`）。旧的顶级托管工具类
> （`HostedMCPTool`，`HostedFileSearchTool`，`HostedVectorStoreContent`）被移除；托管
> 工具现在通过客户端的 `get_*_tool(...)` 工厂方法创建。

---

## 1. 导入和客户端映射

| 旧版（课程示例） | 新版（Microsoft Foundry） |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → 返回 `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool`（客户端 MCP） | 不变 — 仍然是 `from agent_framework import MCPStreamableHTTPTool` |

**凭据参数重命名：** 旧客户端使用 `async_credential=...`；
`FoundryChatClient` 使用 `credential=...`。

---

## 2. 已验证的签名

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # 或设置 AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # 或设置模型环境变量
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # 微软工具箱
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # 可观测性
```

---

## 3. 前后对比 — 带有托管 MCP 工具的单一代理

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

<strong>之后</strong>（Microsoft Foundry）：

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

## 4. 前后对比 — 托管文件搜索（向量存储）

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

<strong>之后</strong>：

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. 弃用的异步模式

<strong>之前</strong>（`learning-recommendation-agent.py`）：

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` 已弃用。推荐使用托管的 `client.get_mcp_tool(...)`
（无手动连接），或者如果必须使用客户端的 `MCPStreamableHTTPTool`，则用 `asyncio.run(...)` 
或 `async with` 上下文包裹。

---

## 6. 本课程当前使用的高级接口

| 功能 | 导入 |
|-----------|--------|
| **Microsoft 工具箱** | `client.get_toolbox("<name>")`，`from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry 记忆** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **可观测性 / 评估** | `client.configure_azure_monitor()`，`from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry 本地** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a`（`import agent_framework.a2a`） |
| <strong>托管代理运行时</strong> | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **注意：** 这些代码片段已经根据当前包进行了导入和签名验证。
> 端到端执行还需要一个 Microsoft Foundry 项目、已部署的聊天
> 模型，以及（文件搜索所需的）已填充的向量存储。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->