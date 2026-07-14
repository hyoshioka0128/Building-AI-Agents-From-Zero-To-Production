# Migrointiohje — Microsoft Foundry Agent Framework (heinäkuu 2026)

Tämä ohje kartoittaa SDK-pinnan, jota kurssinäytteet alun perin käyttivät,
nykyisiin, julkaistuihin Microsoft Agent Framework -paketteihin. Jokainen alla oleva kartoitus ja
allekirjoitus on varmistettu tarkastelemalla asennettuja paketteja
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Miksi tämä on tärkeää:** Microsoft Foundry -brändäyksen myötä asiakaspinta siirtyi
> `agent_framework.azure` -moduulista (vanhat `AzureAI*`-luokat) kohti **`agent_framework.foundry`** -moduulia
> (`FoundryChatClient`, `FoundryAgent`). Vanhoja ylimmän tason hosted-työkalu-luokkia
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) ei enää ole; hosted-
> työkaluja luodaan nyt **asiakkaan kautta** `get_*_tool(...)` -tehtaan metodeilla.

---

## 1. Tuonti ja asiakaspinta

| Vanha (kurssinäytteet) | Uusi (Microsoft Foundry) |
|------------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → palauttaa `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (client-puolen MCP) | muuttumaton — edelleen `from agent_framework import MCPStreamableHTTPTool` |

**Todistusparametrin nimi muutettu:** vanhat asiakkaat käyttivät `async_credential=...`;
`FoundryChatClient` käyttää `credential=...`.

---

## 2. Varmistetut allekirjoitukset

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # tai aseta AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # tai aseta mallin ympäristömuuttuja
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Microsoft Työkalupakki
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Havainnointi
```

---

## 3. Ennen / jälkeen — yksi agentti ja hosted MCP-työkalu

**Ennen** (`azure-learning-agent.py`):

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

**Jälkeen** (Microsoft Foundry):

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

## 4. Ennen / jälkeen — hosted-tiedostohaku (vektorivarasto)

**Ennen** (`employee-search-agent.py`):

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

**Jälkeen**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Vanhentunut async-tyyli

**Ennen** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` on vanhentunut. Suositeltavaa on käyttää hosted-työkalua `client.get_mcp_tool(...)`
(ei manuaalista yhdistämistä), tai jos on pakko käyttää client-puolen `MCPStreamableHTTPTool`ia,
kääri se `asyncio.run(...)`-kutsuun tai `async with` -kontekstiin.

---

## 6. Tämän kurssin edistyneet pinnat

| Ominaisuus | Tuonti |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Havainnointi / arviointi** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Hosted-agent runtime** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Huom.** Nämä koodikatkelmat on varmistettu tuonnin ja allekirjoitusten osalta nykyisillä paketeilla.
> Kokonaisvaltainen suoritus vaatii lisäksi Microsoft Foundry -projektin, käytössä olevan chat-
> mallin ja (tiedostohakuun) täytetyn vektorivaraston.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->