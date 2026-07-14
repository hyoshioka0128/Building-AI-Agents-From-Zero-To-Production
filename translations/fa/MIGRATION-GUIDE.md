# راهنمای مهاجرت — چارچوب عامل مایکروسافت فاندری (ژوئیه ۲۰۲۶)

این راهنما سطح SDK را که نمونه‌های دوره اصلی بر اساس آن نوشته شده بودند
به بسته‌های چارچوب عامل **جاری و منتشر شده** مایکروسافت نگاشت می‌کند. هر نگاشت و
امضا در زیر با بررسی بسته‌های نصب شده تأیید شده است
(`agent-framework 1.2.0`، `agent-framework-foundry 1.2.0`).

> **چرا این مهم است:** با تغییر برند به **Microsoft Foundry**، سطح مشتری از
> `agent_framework.azure` (کلاس‌های قدیمی `AzureAI*`) به **`agent_framework.foundry`**
> (`FoundryChatClient`، `FoundryAgent`) منتقل شده است. کلاس‌های قدیمی ابزارهای میزبان در سطح بالا
> (`HostedMCPTool`، `HostedFileSearchTool`، `HostedVectorStoreContent`) حذف شده‌اند؛ ابزارهای میزبان
> اکنون **از کلاینت** از طریق متدهای کارخانه‌ای `get_*_tool(...)` ایجاد می‌شوند.

---

## ۱. نگاشت واردات و کلاینت

| قدیم (نمونه‌های دوره) | جدید (مایکروسافت فاندری) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → بازمی‌گرداند `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (MCP سمت کلاینت) | بدون تغییر — هنوز `from agent_framework import MCPStreamableHTTPTool` |

**پارامتر اعتبارنامه تغییر نام داد:** کلاینت‌های قدیمی از `async_credential=...` استفاده می‌کردند؛
`FoundryChatClient` از `credential=...` استفاده می‌کند.

---

## ۲. امضاهای تأیید شده

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # یا تنظیم AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # یا تنظیم متغیر محیطی مدل
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # جعبه ابزار مایکروسافت
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # قابلیت مشاهده‌پذیری
```

---

## ۳. قبل / بعد — یک عامل واحد با یک ابزار MCP میزبان

**قبل** (`azure-learning-agent.py`):

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

**بعد** (مایکروسافت فاندری):

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

## ۴. قبل / بعد — جستجوی فایل میزبان (مخزن برداری)

**قبل** (`employee-search-agent.py`):

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

**بعد**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## ۵. الگوی غیرهمزمان منسوخ شده

**قبل** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` منسوخ شده است. بهتر است از `client.get_mcp_tool(...)`
میزبان استفاده کنید (بدون اتصال دستی)، یا اگر باید از `MCPStreamableHTTPTool` سمت کلاینت استفاده کنید،
آن را در `asyncio.run(...)` یا یک بستر `async with` بپیچید.

---

## ۶. سطوح پیشرفته‌ای که این دوره اکنون استفاده می‌کند

| قابلیت | واردات |
|-----------|--------|
| **جعبه‌ابزار مایکروسافت** | `client.get_toolbox("<name>")`، `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **حافظه فاندری** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **مشاهده‌پذیری / ارزیابی** | `client.configure_azure_monitor()`، `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **محلی فاندری** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **زمان اجرا برای عامل میزبان** | `agent-framework-foundry-hosting`، `azure.ai.agentserver` |

> **نکته.** این قطعات کد واردات و امضاهایشان مطابق بسته‌های جاری تأیید شده است.
> اجرای انتها به انتها همچنین نیازمند یک پروژه Microsoft Foundry، مدلی چت مستقر شده،
> و (برای جستجوی فایل) یک مخزن برداری پر شده است.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->