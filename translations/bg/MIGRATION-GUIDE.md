# Ръководство за миграция — Microsoft Foundry Agent Framework (юли 2026)

Това ръководство свързва SDK интерфейса, за който първоначално са написани примерите от курса,
с **текущите, публикувани** пакети на Microsoft Agent Framework. Всяко съвпадение и
подпис по-долу е проверен чрез инспектиране на инсталираните пакети
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Защо е важно:** с ребрандиране към **Microsoft Foundry**, клиентският предпаз е преместен
> от `agent_framework.azure` (старите класове `AzureAI*`) към **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Старите върхови класове за хоствани инструменти
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) бяха премахнати; хостваните
> инструменти сега се създават **от клиента** чрез фабричните методи `get_*_tool(...)`.

---

## 1. Импортиране и карта на клиента

| Стар (примери от курса) | Нов (Microsoft Foundry) |
|------------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → връща `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (клиентска страна MCP) | без промяна — все още `from agent_framework import MCPStreamableHTTPTool` |

**Параметърът за удостоверяване е преименуван:** старите клиенти използваха `async_credential=...`;
`FoundryChatClient` използва `credential=...`.

---

## 2. Проверени подписи

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # или задайте AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # или задайте променливата на средата за модела
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
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Наблюдаемост
```

---

## 3. Преди / след — един агент с хостван MCP инструмент

**Преди** (`azure-learning-agent.py`):

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

**След** (Microsoft Foundry):

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

## 4. Преди / след — хоствано търсене във файлове (векторен стор)

**Преди** (`employee-search-agent.py`):

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

**След**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Отхвърлен асинхронен модел

**Преди** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` е отхвърлено. Предпочитайте хоствания `client.get_mcp_tool(...)`
(без ръчно свързване), или ако трябва да използвате клиентската страна `MCPStreamableHTTPTool`, обвийте го
в `asyncio.run(...)` или в асинхронен контекст `async with`.

---

## 6. Разширени интерфейси, които този курс вече използва

| Възможност | Импорт |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Наблюдаемост / оценка** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Хостван агент runtime** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Забележка.** Тези фрагменти са импортирани и проверени за съвпадение на подписите спрямо текущите пакети.
> За пълна работа е необходим проект Microsoft Foundry, внедрен чат модел,
> и (за търсене във файлове) запълнен векторен стор.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->