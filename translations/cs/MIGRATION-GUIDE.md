# Průvodce migrací — Microsoft Foundry Agent Framework (červenec 2026)

Tento průvodce mapuje plochu SDK, proti které byly původně napsány ukázky kurzu,
na **aktuální, publikované** balíčky Microsoft Agent Framework. Každé mapování a
signatura níže byla ověřena introspektováním nainstalovaných balíčků
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Proč je to důležité:** s přejmenováním na **Microsoft Foundry** se klientská plocha přesunula
> z `agent_framework.azure` (staré třídy `AzureAI*`) na **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Staré top-level třídy hostovaných nástrojů
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) byly odstraněny; hostované
> nástroje se nyní vytvářejí **přímo z klienta** pomocí továrních metod `get_*_tool(...)`.

---

## 1. Mapování importů a klienta

| Staré (příklad kurzu) | Nové (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → vrací `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (MCP na straně klienta) | beze změny — stále `from agent_framework import MCPStreamableHTTPTool` |

**Přejmenovaný parametr pověření:** staré klienty braly `async_credential=...`;
`FoundryChatClient` používá `credential=...`.

---

## 2. Ověřené signatury

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # nebo nastavte AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # nebo nastavte proměnnou prostředí modelu
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
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Pozorovatelnost
```

---

## 3. Před / po — jeden agent s hostovaným MCP nástrojem

**Před** (`azure-learning-agent.py`):

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

## 4. Před / po — hostované hledání souborů (vektorové úložiště)

**Před** (`employee-search-agent.py`):

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

## 5. Zastaralý asynchronní vzor

**Před** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` je zastaralé. Doporučuje se použití hostovaného `client.get_mcp_tool(...)`
(žádné manuální připojování), nebo pokud musíte použít klientskou stranu `MCPStreamableHTTPTool`, zabalte ji
do `asyncio.run(...)` nebo použijte `async with` kontext.

---

## 6. Pokročilé plochy, které tento kurz nyní používá

| Funkčnost | Import |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Monitorování / vyhodnocování** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Runtime hostovaného agenta** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Poznámka.** Tyto úryvky importů a signatur byly ověřeny vůči aktuálním balíčkům.
> Pro kompletní běh je navíc potřeba projekt Microsoft Foundry, nasazený chat
> model a (pro hledání souborů) naplněné vektorové úložiště.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->