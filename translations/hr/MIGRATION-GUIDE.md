# Vodič za migraciju — Microsoft Foundry Agent Framework (srpanj 2026.)

Ovaj vodič preslikava SDK sučelje na kojem su izvornici tečaja prvotno napisani
na **trenutne, objavljene** Microsoft Agent Framework pakete. Svako preslikavanje i
potpis u nastavku potvrđen je pregledavanjem instaliranih paketa
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Zašto je ovo važno:** s rebrendingom u **Microsoft Foundry**, klijentsko sučelje se premjestilo
> s `agent_framework.azure` (stare klase `AzureAI*`) na **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Stare glavne klase hostiranih alata
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) uklonjene su; hostirani
> alati se sada stvaraju **iz klijenta** pomoću tvorničkih metoda `get_*_tool(...)`.

---

## 1. Uvoz i preslikavanje klijenta

| Staro (primjeri tečaja) | Novo (Microsoft Foundry) |
|------------------------|--------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → vraća `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (MCP na strani klijenta) | nepromijenjeno — još uvijek `from agent_framework import MCPStreamableHTTPTool` |

**Parametar vjerodajnica preimenovan:** stari klijenti su koristili `async_credential=...`;
`FoundryChatClient` koristi `credential=...`.

---

## 2. Potvrđeni potpisi

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # ili postavite AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # ili postavite varijablu okoline modela
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Microsoftova alatna traka
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Promatranje
```

---

## 3. Prije / poslije — jedan agent s hostiranim MCP alatom

**Prije** (`azure-learning-agent.py`):

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

**Poslije** (Microsoft Foundry):

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

## 4. Prije / poslije — hostirano pretraživanje datoteka (vektorska pohrana)

**Prije** (`employee-search-agent.py`):

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

**Poslije**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Zastarjeli async obrazac

**Prije** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` je zastarjelo. Preporučajte hostirani `client.get_mcp_tool(...)`
(bez ručnog povezivanja), ili ako morate koristiti `MCPStreamableHTTPTool` na strani klijenta,
omotajte ga u `asyncio.run(...)` ili unutar `async with` konteksta.

---

## 6. Napredna sučelja koja ovaj tečaj sada koristi

| Mogućnost | Uvoz |
|----------|-------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memorija** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Promatranje / evaluacija** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Lokalni** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Pokretanje hostiranog agenta** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Napomena.** Ovi isječci su provjereni uvozi i potpisima u skladu s trenutnim paketima.
> End-to-end izvršavanje dodatno zahtijeva Microsoft Foundry projekt, raspoređeni chat
> model i (za pretraživanje datoteka) popunjenu vektorsku pohranu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->