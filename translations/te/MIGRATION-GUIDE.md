# మైగ్రేషన్ గైడ్ — Microsoft Foundry Agent Framework (జూలై 2026)

ఈ గైడ్ SDK సర్ఫెస్‌ను మ్యాప్ చేస్తుంది, కోర్స్ సాంపిల్స్ ప్రారంభంలో వ్రాయబడినవి
**ప్రస్తుతం, ప్రచురించబడిన** Microsoft Agent Framework ప్యాకేజీలపై. ప్రతి మ్యాపింగ్ మరియు
సంతకం దిగువలో సంస్థాపిత ప్యాకేజీలను పరిశీలించడం ద్వారా ధృవీకరించబడింది
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **ఇది ఎందుకు ముఖ్యం:** **Microsoft Foundry** కు రీబ్యాండ్ తో, క్లయింట్ సర్ఫెస్ మార్చబడింది
> `agent_framework.azure` నుండి (పాత `AzureAI*` క్లాసులు) **`agent_framework.foundry`** కు
> (`FoundryChatClient`, `FoundryAgent`). పాత టాప్-లెవల్ హోస్టెడ్-టూల్ క్లాసులు
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) తొలగించబడ్డాయి; హోస్టెడ్
> టూల్స్ ఇప్పుడు **క్లయింట్ నుండి** `get_*_tool(...)` ఫాక్టరీ విధానాల ద్వారా సృష్టించబడతాయి.

---

## 1. దిగుమతి & క్లయింట్ మ్యాపింగ్

| పాతది (కోర్స్ సాంపిల్స్) | కొత్తది (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → `Agent` ని తిరిగి ఇస్తుంది |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (క్లయింట్-సైడ్ MCP) | మారలేదు — ఇప్పటికీ `from agent_framework import MCPStreamableHTTPTool` |

**ప్రామాణిక పరామితి పేరు మార్చబడింది:** పాత క్లయింట్లు `async_credential=...` తీసుకున్నారు;
`FoundryChatClient` `credential=...` తీసుకుంటుంది.

---

## 2. ధృవీకరించబడిన సంతకాలు

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # లేదా AZURE_AI_PROJECT_ENDPOINT ను సెట్ చేయండి
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # లేదా మోడల్ env var ను సెట్ చేయండి
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # మైక్రోసాఫ్ట్ టూల్‌బాక్స్
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # పరిశీలనీయత
```

---

## 3. ముందు / తర్వాత — ఒకే ఏజెంట్ ఒక హోస్టెడ్ MCP టూల్తో

**ముందు** (`azure-learning-agent.py`):

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

**తర్వాత** (Microsoft Foundry):

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

## 4. ముందు / తర్వాత — హోస్టెడ్ ఫైల్ సెర్చ్ (వెక్టార్ స్టోర్)

**ముందు** (`employee-search-agent.py`):

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

**తర్వాత**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. పాత async నమూనా

**ముందు** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` పాతది. హోస్టెడ్ `client.get_mcp_tool(...)`
(యొక్క మాన్యువల్ కనెక్ట్ అవసరం లేదు) ను ప్రాధాన్యం ఇవ్వండి, లేదా మీరు తప్పనిసరిగా క్లయింట్-సైడ్ `MCPStreamableHTTPTool` ను ఉపయోగించాల్సి వచ్చినప్పుడు,
దానిని `asyncio.run(...)` లేదా `async with` సందర్భంలో చుట్టండి.

---

## 6. ఈ కోర్సు ఇప్పుడు వాడే సమృద్ధి సర్ఫేసులు

| సామర్థ్యం | దిగుమతి |
|-----------|--------|
| **Microsoft టూల్‌బాక్స్** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry మెమరీ** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **గమనించదగిన / మూల్యాంకనం** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry లోకల్** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Hosted-agent runtime** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **గమనిక.** ఈ ఉదాహరణలు దిగుమతి మరియు సంతకం అక్రమాలను ప్రస్తుత ప్యాకేజీలతో ధృవీకరించబడ్డాయి.
> మొత్తం అమలుకు అదనంగా Microsoft Foundry ప్రాజెక్టు, ప్రైయోగీకరించిన చాట్
> మోడల్, మరియు (ఫైల్ సెర్చ్ కొరకు) ఒక నింపబడిన వెక్టర్ స్టోర్ అవసరం.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->