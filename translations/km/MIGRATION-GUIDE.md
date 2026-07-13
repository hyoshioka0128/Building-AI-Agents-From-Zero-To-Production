# មគ្គុទេសក៍បម្លែង — ស៊ុមគ្រប់គ្រង Microsoft Foundry Agent Framework (កក្កដា 2026)

មគ្គុទេសក៍នេះបង្ហាញផែនទីផ្ទៃ SDK ដែលគំរូមេរៀនបានសរសេរដើមនឹង
ទៅកាន់កញ្ចប់ Microsoft Agent Framework **បច្ចុប្បន្នដែលបានបោះពុម្ពផ្សាយ**។ រាល់ផែនទី និង
ហត្ថលេខាខាងក្រោមត្រូវបានផ្ទៀងផ្ទាត់ដោយត្រួតពិនិត្យកញ្ចប់ដែលបានដំឡើង
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`)។

> **ហេតុអ្វីបានជា​រឿងនេះ​សំខាន់៖** ជាមួយនឹងការប្តូរឈ្មោះទៅជា **Microsoft Foundry** ផ្ទៃមុខ
> អតិថិជនបានផ្លាស់ប្តូរ​ពី `agent_framework.azure` (ថ្នាក់ `AzureAI*` ចាស់ៗ) ទៅជា **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`)។ ថ្នាក់ hosted-tool កំពូលចាស់ៗ
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) ត្រូវបានលុបចោល; ឧបករណ៍ hosted
> ឥឡូវនេះត្រូវបានបង្កើត **ពីអតិថិជន** តាមរយៈវិធីសាស្រ្តរោងចក្រ `get_*_tool(...)`។

---

## 1. ការនាំចូល និងផែនទីអតិថិជន

| ចាស់ (គំរូមេរៀន) | ថ្មី (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → បញ្ចេញ `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (MCP ភាគអតិថិជន) | មិនផ្លាស់ប្តូរ — នៅតែ `from agent_framework import MCPStreamableHTTPTool` |

**បម្លែងឈ្មោះប៉ារ៉ាម៉ែត្រcredential:** អតិថិជនចាស់ប្រើ `async_credential=...`;
`FoundryChatClient` ប្រើ `credential=...`។

---

## 2. ហត្ថលេខាដែលបានផ្ទៀងផ្ទាត់

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # ឬកំណត់ AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # ឬកំណត់អថេរព្រឹត្តិបរិស្ថាននៃម៉ូដែល
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # ប្រអប់ឧបករណ៍ Microsoft
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # ការត្រួតពិនិត្យមើល
```

---

## 3. មុន / បន្ទាប់ — ប្រតិបត្តិករ ម្នាក់ជាមួយឧបករណ៍ MCP hosted

**មុន** (`azure-learning-agent.py`):

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

**បន្ទាប់** (Microsoft Foundry):

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

## 4. មុន / បន្ទាប់ — ស្វែងរកឯកសារ hosted (ជំពូកវ៉ិចទ័រ)

**មុន** (`employee-search-agent.py`):

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

**បន្ទាប់**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. លំនាំ async ដែលត្រូវបានលុបចោល

**មុន** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` ត្រូវបានលុបចោល។ ជ្រើសរើស `client.get_mcp_tool(...)` hosted
(មិនត្រូវភ្ជាប់ដោយដៃ), ឬបើត្រូវប្រើ `MCPStreamableHTTPTool` ភាគអតិថិជន សូមបង្កប់វា
ក្នុង `asyncio.run(...)` ឬ context `async with`។

---

## 6. ផ្ទៃខាងក្រោយកម្រិតខ្ពស់ដែលមេរៀននេះប្រើឥឡូវនេះ

| សមត្ថភាព | ការនាំចូល |
|-----------|--------|
| **ប្រអប់ឧបករណ៍ Microsoft** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **អង្គចងចាំ Foundry** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **ការដំណើរការ / ពិនិត្យ** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry តំបន់កម្មវិធី** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **រត់កម្មវិធី hosted-agent** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **សម្គាល់។** ខាន់ស្លាយទាំងនេះត្រូវបានបញ្ជាក់ការនាំចូល និងហត្ថលេខារួមគ្នាជាមួយកញ្ចប់បច្ចុប្បន្ន។
> ការប្រតិបត្តិការពេញលេញតម្រូវឲ្យមានគម្រោង Microsoft Foundry, ម៉ូដែលសន្ទនា​ដែលបានដាក់ឲ្យដំណើរការ,
> និង (សម្រាប់ស្វែងរកឯកសារ) ជំពូកវ៉ិចទ័រដែលបានបំពេញ។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->