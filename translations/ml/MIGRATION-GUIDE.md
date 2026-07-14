# മൈഗ്രേഷൻ ഗൈഡ് — Microsoft Foundry ഏജന്റ് ഫ്രെയിംവർക്ക് (ജൂലൈ 2026)

ഈ ഗൈഡ് കോഴ്സ് സാമ്പിളുകൾ ആദ്യം എഴുതിയ SDK സർഫേസിനെ
**നിലവിലുള്ള, പ്രസിദ്ധീകരിച്ച** Microsoft ഏജന്റ് ഫ്രെയിംവർക്ക് പാക്കേജുകളിൽ മാപ്പ് ചെയ്യുന്നു. താഴെ എല്ലാ മാപ്പുകളും
സെൻചറുകളും ഇൻസ്റ്റാൾ ചെയ്ത പാക്കേജുകൾ
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`) പരിശോധന വഴി വിശേഷിപ്പിച്ചു.

> **ഇത് എന്തുകൊണ്ട് പ്രധാനമാണ്:** **Microsoft Foundry** എന്ന പുനര്‍നാമകരണത്തോടെ, ക്ലയന്റ് സർഫസ്
> `agent_framework.azure` (പഴയ `AzureAI*` ക്ലാസുകൾ) വഴി **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`) ൽ മാറി. പഴയ ടോപ്-ലേവൽ ഹോസ്റ്റഡ്-ടൂൾ ക്ലാസുകൾ
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) നീക്കം ചെയ്തു; ഹോസ്റ്റഡ്
> ടൂളുകൾ ഇപ്പോൾ **ക്ലയന്റ്** വഴി `get_*_tool(...)` ഫാക്ടറി രീതികൾ ഉപയോഗിച്ച് സൃഷ്ടിക്കുന്നു.

---

## 1. ഇറക്കുമതി & ക്ലയന്റ് മാപ്പിംഗ്

| പഴയ (കോഴ്സ് സാമ്പിളുകൾ) | പുതിയ (Microsoft Foundry) |
|----------------------------|-----------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → `Agent` 반환ക്കായി |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (ക്ലയന്റ്-സൈഡ് MCP) | മാറ്റമില്ല — ഇപ്പോഴും `from agent_framework import MCPStreamableHTTPTool` |

**അംഗീകൃതപരമായ പാരാമീറ്റർ പേരിൽ മാറ്റം:** പഴയ ക്ലയന്റുകൾ `async_credential=...` സ്വീകരിച്ചപ്പോൾ;
`FoundryChatClient` `credential=...` സ്വീകരിക്കുന്നു.

---

## 2. സ്ഥിരീകരിച്ച സീഗ്നേച്ചറുകൾ

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # അല്ലെങ്കിൽ AZURE_AI_PROJECT_ENDPOINT സജ്ജമാക്കുക
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # അല്ലെങ്കിൽ മോഡൽ എൻവ് വാരിയബിൾ സജ്ജമാക്കുക
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # മൈക്രോസോഫ്റ്റ് ടൂൾബോക്സ്
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # നിരീക്ഷണക്ഷമത
```

---

## 3. മുകളിൽ / അടിയിൽ — ഒരൊറ്റ ഏജന്റ് ഒരു ഹോസ്റ്റഡ് MCP ടൂൾ ഉപയോഗിച്ചു

**മുന്‍പ്** (`azure-learning-agent.py`):

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

**പിന്നീട്** (Microsoft Foundry):

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

## 4. മുകളിൽ / അടിയിൽ — ഹോസ്റ്റഡ് ഫയൽ തിരയൽ (വെക്ടർ സ്റ്റോർ)

**മുന്‍പ്** (`employee-search-agent.py`):

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

**പിന്നീട്**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. പഴയ async മാതൃക

**മുന്‍പ്** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` പഴകരിക്കുന്നു. ഹോസ്റ്റഡ് `client.get_mcp_tool(...)`
(മാനുവൽ കണക്റ്റ് ഇല്ല) മുൻഗണന നൽകുക, അല്ലെങ്കിൽ നിങ്ങൾക്കു ക്ലയന്റ്-സൈഡ് `MCPStreamableHTTPTool` ഉപയോഗിക്കേണ്ടി വന്നെങ്കിൽ,
അതിനെ `asyncio.run(...)` അല്ലെങ്കിൽ `async with` കണ്ടക്സ്റ്റിൽ വെട്ടിച്ചെറിഞ്ഞ് ഉപയോഗിക്കുക.

---

## 6. ഈ കോഴ്‌സ് ഇപ്പോൾ ഉപയോഗിക്കുന്ന പുരോഗതിയുള്ള സർഫേസുകൾ

| കഴിവ് | ഇറക്കുമതി |
|-------|---------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **നിരീക്ഷണശക്തി / മൂല്യനിർണയം** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **ഹോസ്റ്റഡ്-ഏജന്റ് റൺടൈം** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **കുറിപ്പ്.** ഈ സ്നിപ്പറ്റുകൾ നിലവിലുള്ള പാക്കേജുകളെ അടിസ്ഥാനമാക്കി ഇറക്കുമതി-യും സീഗ്നേച്ചർ-ഉം സ്ഥിരീകരിച്ചു.
> എഞ്ചിനീയർ ചെയ്ത് പ്രവർത്തിപ്പാക്കുന്നതിന് കൂടാതെ Microsoft Foundry പ്രോജക്റ്റ്, വിന്യസിച്ച ഒരു ചാറ്റ്
> മോഡൽ, (ഫയൽ തിരയലിനായി) ഒരു പൂരിപ്പിച്ച വെക്ടർ സ്റ്റോർ ആവശ്യമുണ്ട്.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->