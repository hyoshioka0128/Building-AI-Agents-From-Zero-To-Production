# Migrationshandbuch — Microsoft Foundry Agent Framework (Juli 2026)

Dieses Handbuch ordnet die SDK-Oberfläche, gegen die die Kursbeispiele ursprünglich geschrieben wurden,
auf die **aktuell veröffentlichten** Microsoft Agent Framework-Pakete ab. Jede untenstehende Zuordnung und
Signatur wurde durch die Inspektion der installierten Pakete
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`) verifiziert.

> **Warum das wichtig ist:** Mit der Umbenennung zu **Microsoft Foundry** wurde die Client-Oberfläche
> von `agent_framework.azure` (den alten `AzureAI*`-Klassen) zu **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`) verschoben. Die alten Top-Level Hosted-Tool-Klassen
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) wurden entfernt; Hosted
> Tools werden nun **vom Client aus** über die Fabrikmethoden `get_*_tool(...)` erstellt.

---

## 1. Import & Client-Zuordnung

| Alt (Kursbeispiele) | Neu (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → gibt `Agent` zurück |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (Client-seitiges MCP) | unverändert — weiterhin `from agent_framework import MCPStreamableHTTPTool` |

**Credential-Parameter umbenannt:** Die alten Clients verwendeten `async_credential=...`;
`FoundryChatClient` verwendet `credential=...`.

---

## 2. Verifizierte Signaturen

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # oder setzen Sie AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # oder setzen Sie die Modell-Umgebungsvariable
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Microsoft Werkzeugkasten
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Beobachtbarkeit
```

---

## 3. Vorher / Nachher — ein einzelner Agent mit einem gehosteten MCP-Tool

**Vorher** (`azure-learning-agent.py`):

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

**Nachher** (Microsoft Foundry):

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

## 4. Vorher / Nachher — gehostete Dateisuche (Vektor-Speicher)

**Vorher** (`employee-search-agent.py`):

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

**Nachher**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Veraltetes Async-Muster

**Vorher** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` ist veraltet. Bevorzuge das gehostete `client.get_mcp_tool(...)`
(kein manuelles Verbinden), oder falls du das clientseitige `MCPStreamableHTTPTool` verwenden musst,
wickle es in `asyncio.run(...)` oder einen `async with` Kontext ein.

---

## 6. Erweiterte Oberflächen, die dieser Kurs jetzt nutzt

| Fähigkeit | Import |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observability / Eval** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Hosted-Agent Runtime** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Hinweis:** Diese Ausschnitte sind import- und signaturüberprüft gegen die aktuellen Pakete.
> Für eine Ende-zu-Ende-Ausführung wird zusätzlich ein Microsoft Foundry-Projekt, ein bereitgestelltes Chat-
> Modell und (für die Dateisuche) ein befüllter Vektor-Speicher benötigt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->