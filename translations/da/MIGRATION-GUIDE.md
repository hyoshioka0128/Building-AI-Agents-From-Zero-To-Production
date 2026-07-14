# Migreringsvejledning — Microsoft Foundry Agent Framework (juli 2026)

Denne vejledning kortlægger SDK-fladen, som kursuseksemplerne oprindeligt blev skrevet til,
til de **nuværende, offentligt udgivne** Microsoft Agent Framework-pakker. Hver kortlægning og
signatur nedenfor blev verificeret ved at introspektere de installerede pakker
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Hvorfor det betyder noget:** med ommærkningen til **Microsoft Foundry** flyttede klientfladen
> sig fra `agent_framework.azure` (de gamle `AzureAI*` klasser) til **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). De gamle topniveau hosted-tool klasser
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) blev fjernet; hosted
> tools oprettes nu **fra klienten** via fabriksmetoderne `get_*_tool(...)`.

---

## 1. Import og klientkortlægning

| Gammel (kursuseksempler) | Ny (Microsoft Foundry) |
|--------------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → returnerer `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (client-side MCP) | uændret — stadig `from agent_framework import MCPStreamableHTTPTool` |

**Legitimationsparameter omdøbt:** de gamle klienter tog `async_credential=...`;
`FoundryChatClient` tager `credential=...`.

---

## 2. Verificerede signaturer

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # eller sæt AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # eller sæt modelens miljøvariabel
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Microsoft Værktøjskasse
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Observabilitet
```

---

## 3. Før / efter — en enkelt agent med et hosted MCP-værktøj

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

**Efter** (Microsoft Foundry):

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

## 4. Før / efter — hosted fil-søgning (vector store)

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

**Efter**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Forældet asynkront mønster

**Før** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` er forældet. Foretræk det hosted `client.get_mcp_tool(...)`
(ingen manuel tilslutning), eller hvis du skal bruge client-side `MCPStreamableHTTPTool`, indpak det
i `asyncio.run(...)` eller en `async with` kontekst.

---

## 6. Avancerede flader, som dette kursus nu benytter

| Funktionalitet | Import |
|---------------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observability / eval** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Hosted-agent runtime** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Bemærk.** Disse uddrag er import- og signaturverificerede mod de nuværende pakker.
> Fuldt gennemløb kræver derudover et Microsoft Foundry-projekt, en udrullet chat
> model og (for fil-søgning) en befolket vector store.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->