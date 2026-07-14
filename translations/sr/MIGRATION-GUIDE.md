# Водич за миграцију — Microsoft Foundry Agent Framework (јул 2026)

Овај водич пресликава SDK површину на коју су примерци из курса оригинално написани
на **тренутне, објављене** Microsoft Agent Framework пакете. Свака пресликавања и
потписи испод су проверени инспекцијом инсталираних пакета
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Зашто је ово важно:** са променом имена у **Microsoft Foundry**, клијентска површина се померала
> са `agent_framework.azure` (стари `AzureAI*` класе) на **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Стари топ-летел нивои класа за хостоване алате
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) су уклоњени; хостовани
> алати се сада праве **из клијента** путем фабричких метода `get_*_tool(...)`.

---

## 1. Мапирање увоза и клијента

| Стари (примерци из курса) | Нови (Microsoft Foundry) |
|--------------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → враћа `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (MCP на страни клијента) | непромењено — и даље `from agent_framework import MCPStreamableHTTPTool` |

**Преименован параметар Credential:** стари клијенти су користили `async_credential=...`;
`FoundryChatClient` користи `credential=...`.

---

## 2. Верификовани потписи

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # или подесите AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # или подесите модел као променљиву окружења
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Microsoft алатка
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Посматрање
```

---

## 3. Пре / после — један агент са хостованим MCP алатом

**Пре** (`azure-learning-agent.py`):

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

## 4. Пре / после — хостована претрага фајлова (vector store)

**Пре** (`employee-search-agent.py`):

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

## 5. Застарели асинхрони образац

**Пре** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` је застарео. Преферирајте хостовани `client.get_mcp_tool(...)`
(без ручног повезивања), или ако морате да користите MCP на страни клијента `MCPStreamableHTTPTool`, умотајте га
у `asyncio.run(...)` или у контекст `async with`.

---

## 6. Напредне површине које овај курс сада користи

| Капабилити | Увоз |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Обзервабилити / евалуација** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Hosted-agent runtime** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Напомена.** Ови исечци су увозно и потписно проверени у односу на тренутне пакете.
> За крај-главно извршење додатно је потребан Microsoft Foundry пројекат, распоређени модели за ћаскање,
> и (за претрагу фајлова) попуњени vector store.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->