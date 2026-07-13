# Ghid de migrare — Microsoft Foundry Agent Framework (iulie 2026)

Acest ghid mapează suprafața SDK împotriva căreia au fost inițial scrise exemplele cursului
pe pachetele **curente, publicate** Microsoft Agent Framework. Fiecare mapare și
semnătură de mai jos a fost verificată prin introspectarea pachetelor instalate
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **De ce contează:** odată cu schimbarea brandului în **Microsoft Foundry**, suprafața clientului s-a mutat
> de la `agent_framework.azure` (vechile clase `AzureAI*`) la **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Vechile clase la nivel înalt pentru unelte găzduite
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) au fost eliminate; uneltele găzduite
> sunt acum create **din client** prin metodele de fabrică `get_*_tool(...)`.

---

## 1. Import și mapare client

| Vechi (exemple curs) | Nou (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → returnează `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (client-side MCP) | neschimbat — încă `from agent_framework import MCPStreamableHTTPTool` |

**Parametrul credential redenumit:** vechii clienți foloseau `async_credential=...`;
`FoundryChatClient` folosește `credential=...`.

---

## 2. Semnături verificate

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # sau setează AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # sau setează variabila de mediu a modelului
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Trusă de unelte Microsoft
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Observabilitate
```

---

## 3. Înainte / după — un singur agent cu unelte MCP găzduite

**Înainte** (`azure-learning-agent.py`):

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

**După** (Microsoft Foundry):

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

## 4. Înainte / după — căutare de fișiere găzduită (vector store)

**Înainte** (`employee-search-agent.py`):

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

**După**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Model asincron învechit

**Înainte** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` este învechit. Preferă uneltele găzduite `client.get_mcp_tool(...)`
(fără conectare manuală), sau dacă trebuie să folosești `MCPStreamableHTTPTool` pe client,
înfășoară-l în `asyncio.run(...)` sau într-un context `async with`.

---

## 6. Suprafețe avansate folosite acum de acest curs

| Capacitate | Import |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observabilitate / evaluare** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Runtime pentru agent găzduit** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Notă.** Aceste fragmente sunt verificate la import și semnături față de pachetele curente.
> Executarea end-to-end necesită suplimentar un proiect Microsoft Foundry, un model de chat implementat
> și (pentru căutarea de fișiere) un vector store populat.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->