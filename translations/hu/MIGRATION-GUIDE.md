# Migrációs Útmutató — Microsoft Foundry Agent Framework (2026 július)

Ez az útmutató leképezi az SDK felületet, amely ellen a tanfolyami minták eredetileg íródtak,
a **jelenlegi, kiadott** Microsoft Agent Framework csomagokra. Az alábbi összes leképzés és
aláírás ellenőrzött az telepített csomagok bejárásával
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Miért fontos ez:** a **Microsoft Foundry** átnevezéssel az ügyfél felület
> átköltözött az `agent_framework.azure` -ról (a korábbi `AzureAI*` osztályok)
> a **`agent_framework.foundry`**-ra (`FoundryChatClient`, `FoundryAgent`). A régi felső szintű hosztolt eszközosztályok
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) eltávolításra kerültek;
> a hosztolt eszközök most már **az ügyféltől** jönnek létre `get_*_tool(...)` gyári metódusokkal.

---

## 1. Importálás és ügyfél leképzés

| Régi (tanfolyami minták) | Új (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → visszatér `Agent` objektummal |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (ügyfél-oldali MCP) | változatlan — még mindig `from agent_framework import MCPStreamableHTTPTool` |

**Hitelesítési paraméter átnevezve:** a régi kliensek `async_credential=...` paramétert használtak;
a `FoundryChatClient` `credential=...` paramétert vár.

---

## 2. Ellenőrzött aláírások

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # vagy állítsa be az AZURE_AI_PROJECT_ENDPOINT értékét
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # vagy állítsa be a modell környezeti változót
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Microsoft Eszköztár
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Megfigyelhetőség
```

---

## 3. Előtte / utána — egyetlen ügynök hosztolt MCP eszközzel

**Előtte** (`azure-learning-agent.py`):

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

**Utána** (Microsoft Foundry):

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

## 4. Előtte / utána — hosztolt fájlkeresés (vektor tároló)

**Előtte** (`employee-search-agent.py`):

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

**Utána**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Elavult aszinkron minta

**Előtte** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

Az `asyncio.get_event_loop()` elavult. Előnyben részesítendő a hosztolt `client.get_mcp_tool(...)`
(kézi csatlakozás nélkül), vagy ha feltétlenül az ügyfél-oldali `MCPStreamableHTTPTool` -t kell használni, fogja be
`asyncio.run(...)`-ba vagy egy `async with` kontextusba.

---

## 6. Haladó felületek, amelyeket ez a tanfolyam most használ

| Képesség | Importálás |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observability / értékelés** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Hosztolt ügynök futtatás** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Megjegyzés.** Ezek a kódrészletek import- és aláírás-ellenőrzöttek a jelenlegi csomagokra.
> A teljes körű futtatáshoz ezen felül szükséges egy Microsoft Foundry projekt, egy telepített chat
> modell, és (fájlkereséshez) egy feltöltött vektor tároló.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->