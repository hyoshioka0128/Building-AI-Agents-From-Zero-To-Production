# माइग्रेशन गाइड — Microsoft Foundry एजेंट फ्रेमवर्क (जुलाई 2026)

यह गाइड SDK सतह को मैप करता है जिस पर पाठ्यक्रम उदाहरण मूल रूप से लिखे गए थे
**वर्तमान, प्रकाशित** Microsoft एजेंट फ्रेमवर्क पैकेजों पर। नीचे हर मैपिंग और
हस्ताक्षर स्थापित पैकेजों का निरीक्षण करके सत्यापित किया गया था
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **यह महत्वपूर्ण क्यों है:** Microsoft Foundry के रूपांतरण के साथ, क्लाइंट सतह
> `agent_framework.azure` (पुराने `AzureAI*` क्लासेस) से **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`) पर स्थानांतरित हो गई है। पुराने टॉप-लेवल होस्टेड-टूल क्लासेस
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) को हटा दिया गया है; होस्टेड
> टूल अब **क्लाइंट से** `get_*_tool(...)` फैक्ट्री मेथड्स के माध्यम से बनाए जाते हैं।

---

## 1. इम्पोर्ट और क्लाइंट मैपिंग

| पुराना (पाठ्यक्रम उदाहरण) | नया (Microsoft Foundry) |
|---------------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → `Agent` वापस करता है |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (क्लाइंट-साइड MCP) | अपरिवर्तित — अभी भी `from agent_framework import MCPStreamableHTTPTool` |

**क्रेडेंशियल पैरामीटर का नाम बदला गया:** पुराने क्लाइंट `async_credential=...` लेते थे;
`FoundryChatClient` `credential=...` लेता है।

---

## 2. सत्यापित हस्ताक्षर

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # या AZURE_AI_PROJECT_ENDPOINT सेट करें
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # या मॉडल पर्यावरण चर सेट करें
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # माइक्रोसॉफ्ट टूलबॉक्स
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # प्रेक्षणीयता
```

---

## 3. पहले / बाद — एक एकल एजेंट एक होस्टेड MCP टूल के साथ

**पहले** (`azure-learning-agent.py`):

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

**बाद में** (Microsoft Foundry):

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

## 4. पहले / बाद — होस्टेड फ़ाइल खोज (वेक्टर स्टोर)

**पहले** (`employee-search-agent.py`):

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

**बाद में**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. अप्रचलित async पैटर्न

**पहले** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` अप्रचलित है। होस्टेड `client.get_mcp_tool(...)` (कोई मैन्युअल कनेक्ट नहीं)
का उपयोग करना बेहतर है, या यदि आपको क्लाइंट-साइड `MCPStreamableHTTPTool` का उपयोग करना है, तो इसे
`asyncio.run(...)` या `async with` संदर्भ में रैप करें।

---

## 6. उन्नत सतहें जो यह पाठ्यक्रम अब उपयोग करता है

| क्षमता | इम्पोर्ट |
|---------|---------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **ऑब्ज़र्वेबिलिटी / इवैल्यूएशन** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **होस्टेड-एजेंट रनटाइम** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **ध्यान दें।** ये स्निपेट वर्तमान पैकेजों के खिलाफ इम्पोर्ट और हस्ताक्षर सत्यापन के साथ हैं।
> पूर्ण निष्पादन के लिए Microsoft Foundry प्रोजेक्ट, तैनात चैट मॉडल,
> और (फ़ाइल खोज के लिए) भरा हुआ वेक्टर स्टोर आवश्यक है।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->