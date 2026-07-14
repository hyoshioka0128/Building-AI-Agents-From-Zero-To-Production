# माइग्रेशन मार्गदर्शक — मायक्रोसॉफ्ट फायंड्री एजंट फ्रेमवर्क (जुलै 2026)

हा मार्गदर्शक SDK पृष्ठभाग मॅप करतो ज्यावर कोर्स सॅम्पल्स मूळतः लिहिले गेले होते
ते **सध्याच्या, प्रकाशित** मायक्रोसॉफ्ट एजंट फ्रेमवर्क पॅकेजेसवर. खालील प्रत्येक मॅपिंग आणि
स्वाक्षरी स्थापीत पॅकेजेस तपासून पडताळली गेली आहे
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **हे महत्त्वाचे का आहे:** **Microsoft Foundry** मध्ये रीब्रँडिंगमुळे क्लायंट पृष्ठभाग
> `agent_framework.azure` (जुने `AzureAI*` वर्ग) पासून **`agent_framework.foundry`** कडे हलवले गेले आहे
> (`FoundryChatClient`, `FoundryAgent`). जुने टॉप-लेवल होस्टेड-टूल वर्ग
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) काढून टाकले गेले आहेत; होस्टेड
> टूल आता **क्लायंटमधून** `get_*_tool(...)` फॅक्टरी पद्धतींनी तयार केले जातात.

---

## 1. इंपोर्ट आणि क्लायंट मॅपिंग

| जुने (कोर्स नमुने) | नवीन (मायक्रोसॉफ्ट फायंड्री) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → `Agent` परत मिळतो |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (क्लायंट-साइड MCP) | अपरिवर्तित — अजूनही `from agent_framework import MCPStreamableHTTPTool` |

**प्रमाणपत्र पॅरामीटरचे नाव बदलले:** जुने क्लायंट `async_credential=...` घेत होते;
`FoundryChatClient` `credential=...` घेतो.

---

## 2. पडताळलेल्या स्वाक्षऱ्या

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # किंवा AZURE_AI_PROJECT_ENDPOINT सेट करा
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # किंवा मॉडेल एनव्हायर्नमेंट व्हरिएबल सेट करा
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Microsoft टूलबॉक्स
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # निरीक्षणीयता
```

---

## 3. आधी / नंतर — एकाच एजंटसह होस्टेड MCP टूल

**पूर्वी** (`azure-learning-agent.py`):

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

**नंतर** (मायक्रोसॉफ्ट फायंड्री):

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

## 4. आधी / नंतर — होस्टेड फाइल शोध (वेक्टर स्टोअर)

**पूर्वी** (`employee-search-agent.py`):

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

**नंतर**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. बंद झालेले async पॅटर्न

**पूर्वी** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` बंद झाले आहे. होस्टेड `client.get_mcp_tool(...)`
(कोणतेही मॅन्युअल कनेक्ट न करता) प्राधान्य द्या, किंवा तुम्हाला क्लायंट-साइड `MCPStreamableHTTPTool` वापरायचे असल्यास,
त्याला `asyncio.run(...)` किंवा `async with` संदर्भात रॅप करा.

---

## 6. या कोर्समध्ये आता वापरल्या जाणाऱ्या उन्नत पृष्ठभाग

| क्षमता | इंपोर्ट |
|-----------|--------|
| **मायक्रोसॉफ्ट टूलबॉक्स** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **फायंड्री मेमरी** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **ऑब्झर्वेबिलिटी / मूल्यमापन** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **फायंड्री लोकल** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **होस्टेड-एजंट रनटाइम** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **नोट:** हे स्निपेट्स सध्याच्या पॅकेजेसच्या विरुद्ध इंपोर्ट- आणि स्वाक्षरी-पडताळणीसाठी आहेत.
> एंड-टू-एंड अंमलबजावणीसाठी मायक्रोसॉफ्ट फायंड्री प्रोजेक्ट, एक तैनात चॅट
> मॉडेल आणि (फाइल शोधासाठी) एक भरलेला वेक्टर स्टोर आवश्यक आहे.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->