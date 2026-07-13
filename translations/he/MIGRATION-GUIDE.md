# מדריך הגירה — Microsoft Foundry Agent Framework (יולי 2026)

מדריך זה ממפה את ממשק ה-SDK שלמדגמי הקורס נכתבו במקור מולו
אל חבילות **Microsoft Agent Framework המעודכנות והמפוברקות**. כל המיפוי וה
החתימה שלהלן אומתו באמצעות התבוננות פנימית בחבילות המותקנות
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **מדוע זה חשוב:** עם השם החדש **Microsoft Foundry**, ממשק הלקוח הועבר
> מ-`agent_framework.azure` (מחלקות ה-`AzureAI*` הישנות) אל **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). מחלקות הכלים המארחים הישנות
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) הוסרו; כלים
> שהיו מארחים כיום נוצרים **מהלקוח** באמצעות פונקציות מפעל `get_*_tool(...)`.

---

## 1. מיפוי ייבוא ולקוח

| ישן (דגימות קורס) | חדש (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → מחזיר `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (לקוח צד MCP) | ללא שינוי — עדיין `from agent_framework import MCPStreamableHTTPTool` |

**פרמטר האימות שונה:** הלקוחות הישנים קיבלו `async_credential=...`;
`FoundryChatClient` מקבל `credential=...`.

---

## 2. חתימות מאומתות

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # או קבע את AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # או קבע את משתנה הסביבה של הדגם
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
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # יכולת תצפית
```

---

## 3. לפני / אחרי — סוכן יחיד עם כלי MCP מארח

**לפני** (`azure-learning-agent.py`):

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

**אחרי** (Microsoft Foundry):

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

## 4. לפני / אחרי — חיפוש קבצים מארח (מאגר וקטורים)

**לפני** (`employee-search-agent.py`):

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

**אחרי**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. דפוס אסינכרוני מיושן

**לפני** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` מיושן. עדיף להשתמש בלקוח המארח `client.get_mcp_tool(...)`
(ללא התחברות ידנית), או אם חייבים להשתמש בלקוח צד `MCPStreamableHTTPTool`, לעטוף אותו
ב-`asyncio.run(...)` או הקשר `async with`.

---

## 6. ממשקים מתקדמים שהקורס הזה משתמש בהם כעת

| יכולת | ייבוא |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observability / eval** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Hosted-agent runtime** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **הערה.** קטעי הקוד האלה אומתו בנוגע לייבוא וחתימה מול החבילות הנוכחיות.
> הפעלה מקצה לקצה דורשת בנוסף פרויקט Microsoft Foundry, מודל שיחה פרוס,
> ו(לצורך חיפוש קבצים) מאגר וקטורים מאוכלס.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->