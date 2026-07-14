# Migrasjonsveiledning — Microsoft Foundry Agent Framework (juli 2026)

Denne veiledningen kartlegger SDK-flaten som kursprøvene opprinnelig ble skrevet mot
til de **nåværende, publiserte** Microsoft Agent Framework-pakkene. Hver kartlegging og
signatur nedenfor ble verifisert ved å inspisere de installerte pakkene
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Hvorfor dette er viktig:** med rebrandingen til **Microsoft Foundry** flyttet klientflaten
> fra `agent_framework.azure` (de gamle `AzureAI*`-klassene) til **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). De gamle toppnivå klassene for hosted-verktøy
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) ble fjernet; hosted
> verktøy opprettes nå **fra klienten** via fabrikkmetoder `get_*_tool(...)`.

---

## 1. Import & klientkartlegging

| Gammel (kursprøver) | Ny (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → returnerer `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (klient-side MCP) | uendret — fortsatt `from agent_framework import MCPStreamableHTTPTool` |

**Legitimasjonsparameter omdøpt:** de gamle klientene brukte `async_credential=...`;
`FoundryChatClient` bruker `credential=...`.

---

## 2. Verifiserte signaturer

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # eller sett AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # eller sett modellens miljøvariabel
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Microsoft verktøykasse
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Observabilitet
```

---

## 3. Før / etter — en enkelt agent med hosted MCP-verktøy

**Før** (`azure-learning-agent.py`):

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

**Etter** (Microsoft Foundry):

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

## 4. Før / etter — hosted fil-søk (vektorlager)

**Før** (`employee-search-agent.py`):

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

**Etter**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Utdødd asynkron mønster

**Før** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` er utdatert. Foretrekk det hostede `client.get_mcp_tool(...)`
(ingen manuell tilkobling), eller hvis du må bruke klient-side `MCPStreamableHTTPTool`, pakk det
inn i `asyncio.run(...)` eller en `async with`-kontekst.

---

## 6. Avanserte flater kurset nå bruker

| Mulighet | Import |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observabilitet / eval** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Hosted-agent runtime** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Merk.** Disse utsnittene er import- og signaturverifisert mot de nåværende pakkene.
> End-to-end kjøring krever i tillegg et Microsoft Foundry-prosjekt, en distribuert chat
> modell, og (for filsøk) et fylt vektorlager.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->