# இடமாற்ற வழிகாட்டி — Microsoft Foundry அழைப்பு அமைப்புக் கட்டமைப்பு (ஜூலை 2026)

இந்த வழிகாட்டி SDK மேற்பரப்பை வரைபடமாக்குகிறது, பாடநெறித் உதாரணங்கள் முதலில் எழுதப்பட்டவை
**தற்போதைய, வெளியிடப்பட்ட** Microsoft Agent Framework தொகுப்புகளுடன். கீழே உள்ள ஒவ்வொரு வரைபாடும் மற்றும்
கையொப்பமும் நிறுவப்பட்ட தொகுப்புக்களை ஊடறிதல் மூலம் சரிபார்க்கப்பட்டது
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **இதன் முக்கியத்துவம்:** **Microsoft Foundry** என மீண்டும் பெயரிடலுடன், கிளையண்ட் மேற்பரப்பு நகர்ந்தது
> `agent_framework.azure` (பழைய `AzureAI*` வகுப்புகள்) இலிருந்து **`agent_framework.foundry`** க்கு
> (`FoundryChatClient`, `FoundryAgent`). பழைய முதன்மை உள்ளமைவுச் சாதன வகுப்புகள்
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) நீக்கப்பட்டன; கொண்டுசெல்வது
> சாதனங்கள் இப்போது **கிளையண்டிலிருந்து** `get_*_tool(...)` தொழிற்சாலை முறைகள் மூலம் உருவாக்கப்படுகின்றன.

---

## 1. இறக்குமதி & கிளையண்ட் வரைபாடு

| பழைய (பாடநெறி உதாரணங்கள்) | புதிய (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → `Agent` ஐ மீள்கொடுக்கிறது |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (கிளையண்ட் தோராயமாக MCP) | மாற்றமின்றி — இன்னும் `from agent_framework import MCPStreamableHTTPTool` |

**சான்று அளிக்கும் அளவுரு மீண்டும் பெயரிடப்பட்டது:** பழைய கிளையண்ட்கள் `async_credential=...` எடுத்துக் கொண்டன;
`FoundryChatClient` `credential=...` எடுத்துக் கொள்கிறது.

---

## 2. சரிபார்க்கப்பட்ட கையெழுத்துக்கள்

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # அல்லது AZURE_AI_PROJECT_ENDPOINT ஐ அமைக்கவும்
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # அல்லது மாதிரி சுற்றுச்சூழல் மாறியை அமைக்கவும்
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # மைக்ரோசாஃப்ட் டூல்பாக்ஸ்
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # கண்காணிப்பு
```

---

## 3. முன் / பின் — ஒரு ஒரே முகவர் கொண்ட ஒரு கொண்டுச்செல்வது MCP சாதனம்

**முன்** (`azure-learning-agent.py`):

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

**பின்** (Microsoft Foundry):

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

## 4. முன் / பின் — கொண்டுச்செல்வது கோப்பு தேடல் (வேக்டர் ஸ்டோர்)

**முன்** (`employee-search-agent.py`):

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

**பின்**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. பழமையான அசிங்க் மாதிரி

**முன்** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` பழமையானது. கொண்டுச்செல்வது `client.get_mcp_tool(...)`
(கையேடு இணைப்பில்லாமல்), அல்லது கிளையண்ட் பக்கம் `MCPStreamableHTTPTool` பயன்படுத்த வேண்டுமானால், அதை
`asyncio.run(...)` அல்லது `async with` சூழலில் மூடுங்கள்.

---

## 6. இந்தக் பாடநெறி இப்போது பயன்படுத்தும் முன்னேறிய மேற்பரப்புகள்

| திறன் | இறக்குமதி |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry நினைவகம்** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **பரிசோதனையாக்கம் / மதிப்பீடு** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry உள்ளூர்** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **கொண்டுச்செல்வது-முகவர் இயக்க சூழல்** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **குறிப்பு.** இந்தக் குறியீடுகள் இறக்குமதி மற்றும் கையெழுத்துக்கள் இப்போது உள்ள தொகுப்புகளுக்கு சரிபார்க்கப்பட்டவை.
> முழுமையான செயலாக்கத்திற்கு கூடுதலாக Microsoft Foundry திட்டம், அமைக்கப்பட்ட உரையாடல்
> மாதிரி, மற்றும் (கோப்பு தேடலுக்கு) நிரப்பப்பட்ட வேக்டர் ஸ்டோர் தேவை.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->