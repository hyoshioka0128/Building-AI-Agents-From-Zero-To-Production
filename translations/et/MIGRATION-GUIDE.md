# Migratsioonijuhend — Microsoft Foundry Agent Framework (juuli 2026)

See juhend kaardistab SDK pinna, mille vastu kursusenäited algselt kirjutati,
vastavusse **praeguste, avaldatud** Microsoft Agent Frameworki pakettidega. Kõik alljärgnevad
vastavused ja signatuurid on kinnitatud paigaldatud pakettide
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`) introspektiivsel kontrollimisel.

> **Miks see oluline on:** Microsoft Foundry kaubamärgi alla minekuga liikus kliendi pind
> `agent_framework.azure` juurest (vanad `AzureAI*` klassid) üle **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Vanad tipptasemel hostitud tööriistaklassid
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) eemaldati; hostitud
> tööriistad luuakse nüüd **kliendi kaudu** `get_*_tool(...)` tehase meetoditega.

---

## 1. Impordi- ja kliendikaardistus

| Vana (kursuse näited) | Uus (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → tagastab `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (kliendi MCP) | muutmata — ikka `from agent_framework import MCPStreamableHTTPTool` |

**Tunnuse parameetri ümbernimetamine:** vanad kliendid kasutasid `async_credential=...`;
`FoundryChatClient` kasutab `credential=...`.

---

## 2. Kinnitatud signatuurid

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # või määra AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # või määra mudeli keskkonnamuutuja
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Microsofti tööriistakomplekt
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Jälgitavus
```

---

## 3. Enne / pärast — üks agent hostitud MCP tööriistaga

**Enne** (`azure-learning-agent.py`):

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

**Pärast** (Microsoft Foundry):

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

## 4. Enne / pärast — hostitud failide otsing (vektori pood)

**Enne** (`employee-search-agent.py`):

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

**Pärast**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Aegunud asünkroonne muster

**Enne** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` on aegunud. Eelistada tuleks hostitud `client.get_mcp_tool(...)`
(manuaalne ühendamine puudub), või kui peab kasutama kliendipoolset `MCPStreamableHTTPTool`i, katta see
`asyncio.run(...)` või `async with` kontekstiga.

---

## 6. Selle kursuse täiendavad kasutatavad pinnad

| Võimekus | Import |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Jälgitavus / hindamine** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Hosted-agent runtime** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Märkus.** Need lõigud on impordi- ja signatuurikinnitusega vastavuses praeguste pakettidega.
> Täiskohaliku täitmise jaoks on lisaks vajalik Microsoft Foundry projekt, juurutatud vestlusmudel,
> ja (failiotsingu puhul) täidetud vektori pood.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->