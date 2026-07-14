# माइग्रेसन गाइड — माइक्रोसफ्ट फाउन्ड्री एजेन्ट फ्रेमवर्क (जुलाई २०२६)

यस गाइडले SDK सतहको नक्सा बनाउँछ जसमा कोर्सका नमूनाहरू मूल रूपमा लेखिएका थिए
**हालको, प्रकाशित** माइक्रोसफ्ट एजेन्ट फ्रेमवर्क प्याकेजहरूमा। तलको प्रत्येक नक्सा र 
हस्ताक्षर स्थापना गरिएको प्याकेजहरूद्वारा प्रमाणीकरण गरिएको छ
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`)।

> **किन यो महत्वपूर्ण छ:** माइक्रोसफ्ट फाउन्ड्रीमा पुनः ब्रान्ड गर्दा, क्लाइन्ट सतह 
>  `agent_framework.azure` (पुराना `AzureAI*` वर्गहरू) बाट **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`) मा सरेको छ। पुराना शीर्ष स्तरको होस्ट गरिएको टूल
> वर्गहरू (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) हटाइएका छन्; होस्ट गरिएको
> उपकरणहरू अब **क्लाइन्टबाट** `get_*_tool(...)` फैक्ट्री विधिहरू मार्फत सिर्जना गरिन्छ।

---

## 1. इम्पोर्ट र क्लाइन्ट नक्सा

| पुरानो (कोर्स नमूनाहरू) | नयाँ (माइक्रोसफ्ट फाउन्ड्री) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → `Agent` फर्काउँछ |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (क्लाइन्ट-साइड MCP) | अपरिवर्तित — अझै `from agent_framework import MCPStreamableHTTPTool` |

**क्रेडेन्शियल प्यारामिटर नाम परिवर्तन:** पुराना क्लाइन्टहरूले `async_credential=...` लिने गर्थे;
`FoundryChatClient` ले `credential=...` लिन्छ।

---

## 2. प्रमाणीकरण गरिएको हस्ताक्षरहरू

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # वा AZURE_AI_PROJECT_ENDPOINT सेट गर्नुहोस्
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # वा मोडेल वातावरण परिवर्तनशील सेट गर्नुहोस्
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # माइक्रोसफ्ट टुलबक्स
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # अवलोकनीयता
```

---

## 3. पहिले / पछि — होस्ट गरिएको MCP उपकरण सहित एक एकल एजेन्ट

**पहिले** (`azure-learning-agent.py`):

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

**पछि** (माइक्रोसफ्ट फाउन्ड्री):

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

## 4. पहिले / पछि — होस्ट गरिएको फाइल खोज (भेक्टर स्टोर)

**पहिले** (`employee-search-agent.py`):

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

**पछि**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. अप्रचलित async ढाँचा

**पहिले** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` अप्रचलित छ। होस्ट गरिएको `client.get_mcp_tool(...)`
(म्यानुअल कनेक्ट बिना) लाई प्राथमिकता दिनुहोस्, वा यदि क्लाइन्ट-साइड `MCPStreamableHTTPTool`
प्रयोग गर्नै पर्छ भने, यसलाई `asyncio.run(...)` वा `async with` सन्दर्भमा राख्नुहोस्।

---

## 6. यस कोर्सले अब प्रयोग गर्ने उन्नत सतहहरू

| सुविधा | इम्पोर्ट |
|-----------|--------|
| **माइक्रोसफ्ट टूलबक्स** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **फाउन्ड्री मेमोरी** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **अवलोकन / मूल्याङ्कन** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **फाउन्ड्री लोकल** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **होस्ट गरिएको एजेन्ट रनटाइम** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **नोट।** यी टुक्राहरू हालको प्याकेजहरू विरुद्ध इम्पोर्ट र हस्ताक्षर प्रमाणित छन्।
> अन्ततः पूर्ण कार्यान्वयनको लागि माइक्रोसफ्ट फाउन्ड्री परियोजना, परिनियोजित च्याट
> मोडेल, र (फाइल खोजको लागि) पूरक गरिएको भेक्टर स्टोर आवश्यक छ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->