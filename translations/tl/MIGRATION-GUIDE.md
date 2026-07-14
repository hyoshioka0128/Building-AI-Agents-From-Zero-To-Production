# Gabay sa Migrasyon — Microsoft Foundry Agent Framework (Hulyo 2026)

Ang gabay na ito ay nagtutugma ng SDK surface na orihinal na isinulat para sa mga halimbawa ng kurso
sa **kasalukuyang inilathalang** Microsoft Agent Framework packages. Ang bawat pagtutugma at
signature sa ibaba ay na-verify sa pamamagitan ng pagsusuri sa mga naka-install na package
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Bakit ito mahalaga:** dahil sa pagbabago ng pangalan sa **Microsoft Foundry**, lumipat ang client surface
> mula sa `agent_framework.azure` (ang mga lumang `AzureAI*` na klase) papunta sa **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Ang mga lumang top-level na hosted-tool na klase
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) ay tinanggal; ang mga hosted
> na tools ay ngayon nililikha **mula sa client** gamit ang `get_*_tool(...)` factory methods.

---

## 1. Pag-import at pagtutugma ng client

| Lumang (mga halimbawa sa kurso) | Bago (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → nagpapabalik ng `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (client-side MCP) | hindi nagbago — nananatili bilang `from agent_framework import MCPStreamableHTTPTool` |

**Pinalitang pangalan ng parameter ng Credential:** ang mga lumang client ay gumagamit ng `async_credential=...`;
ang `FoundryChatClient` ay gumagamit ng `credential=...`.

---

## 2. Na-verify na mga signature

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # o itakda ang AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # o itakda ang model env var
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
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Observability
```

---

## 3. Bago / pagkatapos — isang solong agent na may hosted MCP tool

**Bago** (`azure-learning-agent.py`):

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

**Pagkatapos** (Microsoft Foundry):

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

## 4. Bago / pagkatapos — hosted file search (vector store)

**Bago** (`employee-search-agent.py`):

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

**Pagkatapos**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Hindi na ginagamit na async na pattern

**Bago** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` ay deprecated na. Mas mainam gamitin ang hosted na `client.get_mcp_tool(...)`
(walang manual na connect), o kung kailangang gumamit ng client-side na `MCPStreamableHTTPTool`, balutin ito
sa `asyncio.run(...)` o sa isang `async with` na konteksto.

---

## 6. Mga advanced na surface na ginagamit ngayon ng kursong ito

| Kakayahan | Pag-import |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observability / eval** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Hosted-agent runtime** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Tandaan.** Ang mga snippet na ito ay na-verify sa import at signature laban sa kasalukuyang mga package.
> Ang end-to-end na pagpapatupad ay nangangailangan din ng isang Microsoft Foundry project, isang na-deploy na chat
> model, at (para sa file search) isang napunan na vector store.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->