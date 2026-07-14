# دليل الهجرة — إطار عميل مايكروسوفت فاوندري (يوليو 2026)

يطابق هذا الدليل واجهة SDK التي كتبت عينات الدورة التدريبية الأصلية بناءً عليها
مع حزم **مايكروسوفت فاوندري** المنشورة **الحالية**. تم التحقق من كل تعيين
وتوقيع أدناه من خلال فحص الحزم المثبتة
(`agent-framework 1.2.0`، `agent-framework-foundry 1.2.0`).

> **لماذا هذا مهم:** مع إعادة العلامة إلى **مايكروسوفت فاوندري**، انتقلت واجهة العميل
> من `agent_framework.azure` (فئات `AzureAI*` القديمة) إلى **`agent_framework.foundry`**
> (`FoundryChatClient`، `FoundryAgent`). تم إزالة فئات الأدوات المستضافة العلوية القديمة
> (`HostedMCPTool`، `HostedFileSearchTool`، `HostedVectorStoreContent`); الأدوات المستضافة الآن
> تُنشأ **من العميل** عبر طرق المصنع `get_*_tool(...)`.

---

## 1. استيراد وتعيين العميل

| القديم (عينات الدورة) | الجديد (مايكروسوفت فاوندري) |
|-----------------------|----------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → يعيد `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (MCP على جانب العميل) | بدون تغيير — لا يزال `from agent_framework import MCPStreamableHTTPTool` |

**تم إعادة تسمية معامل الاعتماد:** كان العملاء القديمون يأخذون `async_credential=...`;
يأخذ `FoundryChatClient` `credential=...`.

---

## 2. التوقيعات التي تم التحقق منها

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # أو تعيين AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # أو تعيين متغير بيئة النموذج
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # صندوق أدوات مايكروسوفت
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # القابلية للمراقبة
```

---

## 3. قبل / بعد — وكيل واحد مع أداة MCP مستضافة

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

**بعد** (مايكروسوفت فاوندري):

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

## 4. قبل / بعد — بحث مستضاف عن الملفات (مخزن متجهات)

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

## 5. نمط غير متزامن مهجور

**قبل** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

تم إهمال `asyncio.get_event_loop()`. يفضل استخدام `client.get_mcp_tool(...)` المستضافة
(لا اتصال يدوي)، أو إذا كان لا بد من استخدام `MCPStreamableHTTPTool` على جانب العميل،
غلفه في `asyncio.run(...)` أو في سياق `async with`.

---

## 6. الواجهات المتقدمة التي يستخدمها هذا الدورة الآن

| القدرة | الاستيراد |
|---------|----------|
| **صندوق أدوات مايكروسوفت** | `client.get_toolbox("<name>")`، `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **ذاكرة فاوندري** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **المراقبة / التقييم** | `client.configure_azure_monitor()`، `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **فاوندري محلي** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **بيئة تشغيل العميل المستضاف** | `agent-framework-foundry-hosting`، `azure.ai.agentserver` |

> **ملاحظة.** تم التحقق من هذه القصاصات من حيث الاستيراد والتوقيعات مقابل الحزم الحالية.
> يتطلب التنفيذ الشامل بالإضافة إلى ذلك مشروع مايكروسوفت فاوندري، ونموذج دردشة منشور،
> و(لبحث الملفات) مخزن متجهات مملوء.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->