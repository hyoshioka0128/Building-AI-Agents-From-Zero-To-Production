# Migratiehandleiding — Microsoft Foundry Agent Framework (juli 2026)

Deze handleiding brengt de SDK-oppervlakte waartegen de cursusvoorbeelden oorspronkelijk waren geschreven
in kaart naar de **huidige, gepubliceerde** Microsoft Agent Framework-pakketten. Elke mapping en
handtekening hieronder is geverifieerd door de geïnstalleerde pakketten te inspecteren
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Waarom dit belangrijk is:** met de rebranding naar **Microsoft Foundry** is de client-oppervlakte verplaatst
> van `agent_framework.azure` (de oude `AzureAI*` klassen) naar **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). De oude top-level hosted-tool klassen
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) zijn verwijderd; hosted
> tools worden nu gemaakt **vanuit de client** via `get_*_tool(...)` fabrieksmethoden.

---

## 1. Import & client mapping

| Oud (cursusvoorbeelden) | Nieuw (Microsoft Foundry) |
|------------------------|---------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → retourneert `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (client-side MCP) | ongewijzigd — nog steeds `from agent_framework import MCPStreamableHTTPTool` |

**Naam van credential-parameter gewijzigd:** de oude clients gebruikten `async_credential=...`;
`FoundryChatClient` gebruikt `credential=...`.

---

## 2. Geverifieerde handtekeningen

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # of stel AZURE_AI_PROJECT_ENDPOINT in
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # of stel de model omgevingsvariabele in
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
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Observeerbaarheid
```

---

## 3. Voor / na — een enkele agent met een hosted MCP tool

**Voor** (`azure-learning-agent.py`):

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

**Na** (Microsoft Foundry):

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

## 4. Voor / na — hosted bestandszoekopdracht (vector store)

**Voor** (`employee-search-agent.py`):

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

**Na**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Verouderd async-patroon

**Voor** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` is verouderd. Gebruik bij voorkeur de hosted `client.get_mcp_tool(...)`
(geen handmatige connectie), of als je de client-side `MCPStreamableHTTPTool` moet gebruiken, gebruik het dan
in een `asyncio.run(...)` of een `async with` context.

---

## 6. Geavanceerde oppervlakken die deze cursus nu gebruikt

| Mogelijkheid | Import |
|-------------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observability / evaluatie** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Hosted-agent runtime** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Notitie.** Deze fragmenten zijn geïmporteerd en handtekening-geverifieerd tegen de huidige pakketten.
> End-to-end uitvoering vereist bovendien een Microsoft Foundry-project, een gedeployed chat
> model, en (voor bestandszoek) een gevulde vector store.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->