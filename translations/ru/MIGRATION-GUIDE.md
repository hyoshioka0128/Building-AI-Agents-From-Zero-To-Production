# Руководство по миграции — Microsoft Foundry Agent Framework (июль 2026)

Это руководство сопоставляет поверхность SDK, с которой изначально были написаны примеры курса,
с **текущими, опубликованными** пакетами Microsoft Agent Framework. Каждое сопоставление и
сигнатура ниже были проверены путем изучения установленных пакетов
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Почему это важно:** с ребрендингом в **Microsoft Foundry** клиентская поверхность переместилась
> из `agent_framework.azure` (старые классы `AzureAI*`) в **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Старые топ-уровневые классы размещенных инструментов
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) были удалены; размещенные
> инструменты теперь создаются **с клиента** через фабричные методы `get_*_tool(...)`.

---

## 1. Сопоставление импортов и клиента

| Старое (примеры курса) | Новое (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → возвращает `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (клиентская сторона MCP) | без изменений — все еще `from agent_framework import MCPStreamableHTTPTool` |

**Параметр учетных данных переименован:** старые клиенты принимали `async_credential=...`;
`FoundryChatClient` принимает `credential=...`.

---

## 2. Проверенные сигнатуры

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # или установите AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # или установите переменную окружения модели
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Инструментарий Microsoft
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Наблюдаемость
```

---

## 3. До / после — один агент с размещенным MCP инструментом

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

**После** (Microsoft Foundry):

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

## 4. До / после — размещенный поиск по файлам (vector store)

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

**После**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Устаревший асинхронный паттерн

**До** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` устарел. Предпочтительно использовать размещенный `client.get_mcp_tool(...)`
(без ручного подключения), либо если необходимо использовать клиентскую `MCPStreamableHTTPTool`, оберните её
в `asyncio.run(...)` или в асинхронный контекст `async with`.

---

## 6. Расширенные возможности, используемые этим курсом

| Возможность | Импорт |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observability / оценка** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Время выполнения размещенного агента** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Примечание.** Эти фрагменты проверены по импортам и сигнатурам на соответствие текущим пакетам.
> Для полного выполнения дополнительно требуется проект Microsoft Foundry, развернутая модель чата
> и (для поиска по файлам) заполненный vector store.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->