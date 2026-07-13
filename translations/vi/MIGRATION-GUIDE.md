# Hướng dẫn chuyển đổi — Microsoft Foundry Agent Framework (Tháng 7 năm 2026)

Hướng dẫn này trình bày bản đồ bề mặt SDK mà các ví dụ khóa học ban đầu được viết dựa trên
sang các gói **hiện tại, được phát hành** của Microsoft Agent Framework. Mỗi bản đồ và
chữ ký dưới đây đều được xác minh bằng cách kiểm tra các gói đã cài đặt
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Tại sao điều này quan trọng:** với việc đổi tên thành **Microsoft Foundry**, bề mặt client đã chuyển
> từ `agent_framework.azure` (các lớp cũ `AzureAI*`) sang **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Các lớp công cụ cấp cao cũ
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) đã bị loại bỏ; các công cụ được lưu trữ
> hiện được tạo **từ phía client** thông qua các phương thức nhà máy `get_*_tool(...)`.

---

## 1. Nhập khẩu & ánh xạ client

| Cũ (ví dụ khóa học) | Mới (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → trả về `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (MCP phía client) | không thay đổi — vẫn `from agent_framework import MCPStreamableHTTPTool` |

**Tham số credential được đổi tên:** các client cũ sử dụng `async_credential=...`;
`FoundryChatClient` sử dụng `credential=...`.

---

## 2. Chữ ký đã xác minh

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # hoặc đặt AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # hoặc đặt biến môi trường mô hình
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Hộp công cụ Microsoft
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Khả năng quan sát
```

---

## 3. Trước / sau — một agent đơn với công cụ MCP được lưu trữ

**Trước** (`azure-learning-agent.py`):

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

**Sau** (Microsoft Foundry):

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

## 4. Trước / sau — tìm kiếm tập tin được lưu trữ (vector store)

**Trước** (`employee-search-agent.py`):

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

**Sau**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Mẫu bất đồng bộ đã bị loại bỏ

**Trước** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` đã bị loại bỏ. Ưu tiên công cụ được lưu trữ `client.get_mcp_tool(...)`
(không kết nối thủ công), hoặc nếu bạn phải sử dụng `MCPStreamableHTTPTool` phía client, hãy bao bọc nó
trong `asyncio.run(...)` hoặc một ngữ cảnh `async with`.

---

## 6. Các bề mặt nâng cao khóa học này hiện sử dụng

| Khả năng | Nhập khẩu |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Quan sát / đánh giá** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Thời gian chạy hosted-agent** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Lưu ý.** Những đoạn mã này đã được xác minh nhập khẩu và chữ ký với các gói hiện tại.
> Thực thi từ đầu đến cuối còn yêu cầu một dự án Microsoft Foundry, một mô hình chat đã triển khai,
> và (cho tìm kiếm tập tin) một vector store đã được lấp đầy.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->