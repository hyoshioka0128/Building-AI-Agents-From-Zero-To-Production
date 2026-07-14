# Mwongozo wa Uhamiaji — Mfumo wa Wakala wa Microsoft Foundry (Julai 2026)

Mwongozo huu unaonesha meza ya uso wa SDK ambapo mifano ya kozi iliolewa awali
juu ya vifurushi vya **Microsoft Agent Framework** vilivyotolewa hivi karibuni. Kila picha na
saini zilithibitishwa kwa kuchunguza vifurushi vilivyowekwa
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Kwa nini hii ni muhimu:** kwa mabadiliko ya jina kuwa **Microsoft Foundry**, uso wa mteja ulisogezwa
> kutoka `agent_framework.azure` (darasa za zamani `AzureAI*`) hadi **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Madarasa ya zana zilizokuwa juu kabisa ya zamani
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) yalifutwa; zana zilizohudumiwa sasa
> hutengenezwa **kutoka kwa mteja** kupitia njia za kiwanda `get_*_tool(...)`.

---

## 1. Uingizaji & meza ya mteja

| Zamani (mifano ya kozi) | Mpya (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → hurudisha `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (MCP upande wa mteja) | haijabadilika — bado `from agent_framework import MCPStreamableHTTPTool` |

**Kigezo cha usahihi kimebadilika:** wateja wa zamani walichukua `async_credential=...`;
`FoundryChatClient` huchukua `credential=...`.

---

## 2. Sahihi zilizo thibitishwa

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # au weka AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # au weka variable ya mazingira ya mfano
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Sanduku la Zana la Microsoft
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Ufuatiliaji
```

---

## 3. Kabla / baada — wakala mmoja na zana ya MCP iliyohudumiwa

**Kablica** (`azure-learning-agent.py`):

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

**Baada** (Microsoft Foundry):

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

## 4. Kabla / baada — utafutaji wa faili uliohudumiwa (hifadhi ya vector)

**Kablica** (`employee-search-agent.py`):

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

**Baada**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Msururu wa async uliodhoofishwa

**Kablica** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` imedhoofishwa. Tumia zana iliyohudumiwa `client.get_mcp_tool(...)`
(hamna connect ya mkono), au kama lazima utumie upande wa mteja `MCPStreamableHTTPTool`, izungushe
ndani ya `asyncio.run(...)` au muktadha wa `async with`.

---

## 6. Uso wa juu ambao kozi hii sasa inatumia

| Uwezo | Ingiza |
|-----------|--------|
| **Sanduku la Zana la Microsoft** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Kumbukumbu ya Foundry** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Uangalizi / tathmini** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Uendeshaji wa wakala uliohudumiwa** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Kumbuka.** Vidokezo hivi vimeangaliwa usahihi wa uingizaji na saini dhidi ya vifurushi vya sasa.
> Kutekeleza kutoka mwanzo hadi mwisho pia kunahitaji mradi wa Microsoft Foundry, mfano wa mazungumzo uliowekwa,
> na (kwa utafutaji wa faili) hifadhi ya vector iliyojaa.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->