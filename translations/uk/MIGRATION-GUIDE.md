# Посібник із міграції — Microsoft Foundry Agent Framework (липень 2026)

Цей посібник зіставляє поверхню SDK, проти якої спочатку були написані приклади курсу,
із **поточними, опублікованими** пакетами Microsoft Agent Framework. Кожне зіставлення і
підпис нижче було перевірено шляхом інспектування встановлених пакетів
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Чому це важливо:** із ребрендингом на **Microsoft Foundry** клієнтська поверхня перейшла
> від `agent_framework.azure` (старі класи `AzureAI*`) до **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Старі основні класи розміщених інструментів
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) були вилучені; розміщені
> інструменти тепер створюються **з клієнта** через фабричні методи `get_*_tool(...)`.

---

## 1. Імпорт і відображення клієнта

| Старе (приклади курсу) | Нове (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → повертає `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (MCP на стороні клієнта) | без змін — досі `from agent_framework import MCPStreamableHTTPTool` |

**Параметр для облікових даних перейменовано:** старі клієнти приймали `async_credential=...`;
`FoundryChatClient` приймає `credential=...`.

---

## 2. Перевірені підписи

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # або встановіть AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # або встановіть змінну оточення моделі
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
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Спостережливість
```

---

## 3. До / після — один агент із розміщеним MCP-інструментом

**До** (`azure-learning-agent.py`):

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

**Після** (Microsoft Foundry):

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

## 4. До / після — розміщений пошук файлів (векторне сховище)

**До** (`employee-search-agent.py`):

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

**Після**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Застарілий асинхронний патерн

**До** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` застарілий. Краще використовувати розміщений `client.get_mcp_tool(...)`
(без ручного підключення), або, якщо потрібно використовувати клієнтський `MCPStreamableHTTPTool`, обгорніть його
в `asyncio.run(...)` або контекст `async with`.

---

## 6. Розширені поверхні, використовувані в цьому курсі

| Можливість | Імпорт |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Спостережуваність / оцінка** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Запуск хостинг-агентів** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Примітка.** Ці фрагменти перевірені за імпортом і підписами у відповідності з поточними пакетами.
> Для повного виконання крізь весь процес потрібно також мати проект Microsoft Foundry,
> розгорнуту модель чату та (для пошуку файлів) заповнене векторне сховище.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->