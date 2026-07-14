# Migreringsguide — Microsoft Foundry Agent Framework (juli 2026)

Denna guide kartlägger SDK-gränssnittet som kursens exempel ursprungligen skrevs mot
till de **nuvarande, publicerade** Microsoft Agent Framework-paketen. Varje mappning och
signatur nedan har verifierats genom att inspektera de installerade paketen
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Varför detta är viktigt:** med omprofileringen till **Microsoft Foundry** flyttades klientgränssnittet
> från `agent_framework.azure` (de gamla `AzureAI*`-klasserna) till **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). De gamla toppnivå-klasserna för värdverktyg
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) togs bort; värdverktyg
> skapas nu **från klienten** via `get_*_tool(...)` fabriksmetoder.

---

## 1. Import & klientmappning

| Gammalt (kursens exempel) | Nytt (Microsoft Foundry) |
|--------------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → returnerar `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (klientsidan MCP) | oförändrad — fortfarande `from agent_framework import MCPStreamableHTTPTool` |

**Referensparametern bytt namn:** de gamla klienterna använde `async_credential=...`;
`FoundryChatClient` använder `credential=...`.

---

## 2. Verifierade signaturer

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # eller ange AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # eller ange modellens miljövariabel
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Microsoft-verktygslåda
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Observabilitet
```

---

## 3. Före / efter — en enda agent med ett värd-MCP-verktyg

**Före** (`azure-learning-agent.py`):

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

## 4. Före / efter — värd för filsökning (vektorlagring)

**Före** (`employee-search-agent.py`):

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

## 5. Föråldrat asynkront mönster

**Före** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` är föråldrat. Föredra det värdade `client.get_mcp_tool(...)`
(ingen manuell anslutning), eller om du måste använda klientsidans `MCPStreamableHTTPTool`, lägg in det
i `asyncio.run(...)` eller en `async with`-kontext.

---

## 6. Avancerade ytor som denna kurs nu använder

| Funktionalitet | Import |
|-------------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observability / evaluering** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Hosted-agent runtime** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Notera.** Dessa kodsnuttar är import- och signaturverifierade mot de aktuella paketen.
> Slut-till-slut-exekvering kräver dessutom ett Microsoft Foundry-projekt, en distribuerad chatt-
> modell och (för filsök) en ifylld vektorlagring.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->