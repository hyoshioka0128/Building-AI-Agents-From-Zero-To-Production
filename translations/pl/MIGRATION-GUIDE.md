# Przewodnik migracji — Microsoft Foundry Agent Framework (lipiec 2026)

Ten przewodnik przedstawia odwzorowanie powierzchni SDK, na której pierwotnie opierały się przykłady z kursu,
na **aktualne, opublikowane** pakiety Microsoft Agent Framework. Każde odwzorowanie i
podpis poniżej został zweryfikowany przez introspekcję zainstalowanych pakietów
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Dlaczego to jest ważne:** wraz z rebrandingiem do **Microsoft Foundry**, powierzchnia klienta została przeniesiona
> z `agent_framework.azure` (stare klasy `AzureAI*`) do **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Stare klasy narzędzi hostowanych na najwyższym poziomie
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) zostały usunięte; narzędzia hostowane
> są obecnie tworzone **z poziomu klienta** za pomocą metod fabrykujących `get_*_tool(...)`.

---

## 1. Mapowanie importów i klienta

| Stare (przykłady z kursu) | Nowe (Microsoft Foundry) |
|--------------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → zwraca `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (MCP po stronie klienta) | bez zmian — nadal `from agent_framework import MCPStreamableHTTPTool` |

**Parametr poświadczeń przemianowany:** stare klienty używały `async_credential=...`;
`FoundryChatClient` używa `credential=...`.

---

## 2. Zweryfikowane podpisy

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # lub ustaw AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # lub ustaw zmienną środowiskową modelu
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
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Obserwowalność
```

---

## 3. Przed / po — pojedynczy agent z narzędziem MCP hostowanym

**Przed** (`azure-learning-agent.py`):

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

**Po** (Microsoft Foundry):

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

## 4. Przed / po — hostowane wyszukiwanie plików (wektorowy magazyn)

**Przed** (`employee-search-agent.py`):

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

**Po**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Przestarzały wzorzec async

**Przed** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` jest przestarzałe. Zalecane jest użycie hostowanego `client.get_mcp_tool(...)`
(bez ręcznego łączenia), lub jeśli musisz użyć klienta `MCPStreamableHTTPTool`, opakuj go
w `asyncio.run(...)` lub kontekst `async with`.

---

## 6. Zaawansowane powierzchnie, które ten kurs teraz wykorzystuje

| Możliwość | Import |
|----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Obserwowalność / ewaluacja** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Środowisko runtime agenta hostowanego** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Uwaga.** Te fragmenty zostały zweryfikowane pod względem importów i podpisów względem aktualnych pakietów.
> Do pełnego wykonania end-to-end wymagany jest projekt Microsoft Foundry, wdrożony model rozmowy
> oraz (dla wyszukiwania plików) zapełniony wektorowy magazyn.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->