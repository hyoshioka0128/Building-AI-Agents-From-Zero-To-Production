# مائیگریشن گائیڈ — مائیکروسافٹ فاؤنڈری ایجنٹ فریم ورک (جولائی 2026)

یہ گائیڈ SDK کی سطح کو جو پہلے کورس کے نمونوں کے لیے لکھی گئی تھی
کو **موجودہ، اشاعت شدہ** مائیکروسافٹ ایجنٹ فریم ورک پیکجز پر نقشہ کرتا ہے۔ ہر نقشہ اور
دستخط نیچے نصب شدہ پیکجز کی جانچ کر کے تصدیق کیے گئے ہیں
(`agent-framework 1.2.0`، `agent-framework-foundry 1.2.0`)۔

> **یہ کیوں اہم ہے:** مائیکروسافٹ فاؤنڈری کے دوبارہ برانڈ ہونے کے ساتھ، کلائنٹ سطح منتقل ہوگئی ہے
> `agent_framework.azure` (پرانی `AzureAI*` کلاسز) سے **`agent_framework.foundry`**
> (`FoundryChatClient`، `FoundryAgent`) کی طرف۔ پرانی بہترین سطح کی ہوسٹڈ-ٹول کلاسز
> (`HostedMCPTool`، `HostedFileSearchTool`، `HostedVectorStoreContent`) کو ہٹا دیا گیا ہے؛ ہوسٹڈ
> ٹولز اب **کلائنٹ سے** `get_*_tool(...)` فیکٹری میتھڈز کے ذریعے بنائے جاتے ہیں۔

---

## 1. درآمد اور کلائنٹ نقشہ

| پرانا (کورس نمونے) | نیا (مائیکروسافٹ فاؤنڈری) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → واپسی `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (کلائنٹ-سائیڈ MCP) | بدون تبدیلی — اب بھی `from agent_framework import MCPStreamableHTTPTool` |

**اسناد کے پیرامیٹر کا نام تبدیل ہوا:** پرانے کلائنٹس `async_credential=...` لیتے تھے؛
`FoundryChatClient` `credential=...` لیتا ہے۔

---

## 2. تصدیق شدہ دستخط

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # یا AZURE_AI_PROJECT_ENDPOINT سیٹ کریں
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # یا ماڈل کا env var سیٹ کریں
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # مائیکروسافٹ ٹول باکس
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # نگرانیت
```

---

## 3. قبل / بعد — ایک واحد ایجنٹ جو ایک ہوسٹڈ MCP ٹول کے ساتھ

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

**بعد** (مائیکروسافٹ فاؤنڈری):

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

## 4. قبل / بعد — ہوسٹڈ فائل تلاش (ویکٹر اسٹور)

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

## 5. متروک async پیٹرن

**قبل** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` متروک ہو چکا ہے۔ ہوسٹڈ `client.get_mcp_tool(...)`
کو ترجیح دیں (کوئی دستی رابطہ نہیں)، یا اگر آپ کو کلائنٹ-سائیڈ `MCPStreamableHTTPTool` استعمال کرنا ہے، تو اسے
`asyncio.run(...)` یا `async with` کانٹیکسٹ میں لپیٹیں۔

---

## 6. اس کورس میں اب استعمال ہونے والے جدید سطحیں

| قابلیت | درآمد |
|-----------|--------|
| **مائیکروسافٹ ٹولباکس** | `client.get_toolbox("<name>")`، `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **فاؤنڈری میموری** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **مشاہدہ پذیری / جائزہ** | `client.configure_azure_monitor()`، `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **فاؤنڈری لوکل** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **ہوسٹڈ ایجنٹ رن ٹائم** | `agent-framework-foundry-hosting`، `azure.ai.agentserver` |

> **نوٹ:** یہ کوڈ کے نمونے موجودہ پیکجز کے خلاف درآمد اور دستخط کی تصدیق شدہ ہیں۔
> مکمل طور پر عمل درآمد کے لیے اضافی طور پر ایک مائیکروسافٹ فاؤنڈری پروجیکٹ، ایک تعین شدہ چیٹ
> ماڈل، اور (فائل تلاش کے لیے) ایک بھرپور ویکٹر اسٹور ضروری ہے۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->