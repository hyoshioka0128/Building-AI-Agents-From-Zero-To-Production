# Guida alla migrazione — Microsoft Foundry Agent Framework (luglio 2026)

Questa guida mappa la superficie SDK contro cui sono stati originariamente scritti i campioni del corso
sulle **attuali, pubblicate** package di Microsoft Agent Framework. Ogni mappatura e
firma sottostante è stata verificata ispezionando i pacchetti installati
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Perché è importante:** con il rebrand in **Microsoft Foundry**, la superficie client si è spostata
> da `agent_framework.azure` (le vecchie classi `AzureAI*`) a **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Le vecchie classi di livello superiore per gli strumenti ospitati
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) sono state rimosse; gli strumenti ospitati
> ora vengono creati **dal client** tramite metodi factory `get_*_tool(...)`.

---

## 1. Importazione e mappatura client

| Vecchio (campioni del corso) | Nuovo (Microsoft Foundry) |
|-----------------------------|----------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → restituisce `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (MCP lato client) | invariato — ancora `from agent_framework import MCPStreamableHTTPTool` |

**Parametro delle credenziali rinominato:** i vecchi client prendevano `async_credential=...`;
`FoundryChatClient` prende `credential=...`.

---

## 2. Firme verificate

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # o imposta AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # o imposta la variabile di ambiente del modello
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
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Osservabilità
```

---

## 3. Prima / dopo — un singolo agente con uno strumento MCP ospitato

**Prima** (`azure-learning-agent.py`):

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

**Dopo** (Microsoft Foundry):

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

## 4. Prima / dopo — ricerca file ospitata (archivio vettoriale)

**Prima** (`employee-search-agent.py`):

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

**Dopo**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Pattern async deprecato

**Prima** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` è deprecato. Preferire lo strumento ospitato `client.get_mcp_tool(...)`
(nessuna connessione manuale), oppure se si deve usare `MCPStreamableHTTPTool` lato client, incapsularlo
in `asyncio.run(...)` o in un contesto `async with`.

---

## 6. Superfici avanzate che questo corso utilizza ora

| Capacità | Importazione |
|---------|------------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observability / valutazione** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Runtime hostato agente** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Nota.** Questi frammenti sono importati e verificati nelle firme rispetto ai pacchetti correnti.
> L'esecuzione end-to-end richiede inoltre un progetto Microsoft Foundry, un modello chat distribuito
> e (per la ricerca file) un archivio vettoriale popolato.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->