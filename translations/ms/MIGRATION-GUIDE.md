# Panduan Migrasi — Microsoft Foundry Agent Framework (Julai 2026)

Panduan ini memetakan permukaan SDK yang asalnya digunakan untuk contoh kursus
kepada pakej **semasa, diterbitkan** Microsoft Agent Framework. Setiap pemetaan dan
tandatangan di bawah telah disahkan dengan memeriksa pakej yang dipasang
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Mengapa ini penting:** dengan penjenamaan semula kepada **Microsoft Foundry**, permukaan klien
> beralih daripada `agent_framework.azure` (kelas `AzureAI*` lama) kepada **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Kelas alat hos tahap atas yang lama
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) telah dialih keluar; alat hos
> kini dibuat **dari klien** melalui kaedah kilang `get_*_tool(...)`.

---

## 1. Pemetaan Import & Klien

| Lama (contoh kursus) | Baru (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → mengembalikan `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (MCP sisi klien) | tidak berubah — masih `from agent_framework import MCPStreamableHTTPTool` |

**Parameter kelayakan ditukar nama:** klien lama menerima `async_credential=...`;
`FoundryChatClient` mengambil `credential=...`.

---

## 2. Tandatangan disahkan

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # atau tetapkan AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # atau tetapkan pemboleh ubah persekitaran model
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Kotak Alat Microsoft
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Kebolehamatan
```

---

## 3. Sebelum / selepas — satu agen dengan alat MCP hos

**Sebelum** (`azure-learning-agent.py`):

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

**Selepas** (Microsoft Foundry):

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

## 4. Sebelum / selepas — carian fail hos (penyimpanan vektor)

**Sebelum** (`employee-search-agent.py`):

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

**Selepas**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Corak async usang

**Sebelum** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` sudah tidak digunakan. Lebih baik gunakan `client.get_mcp_tool(...)`
hos (tiada sambungan manual), atau jika perlu gunakan `MCPStreamableHTTPTool` sisi klien,
bungkus dalam `asyncio.run(...)` atau konteks `async with`.

---

## 6. Permukaan lanjutan yang kini digunakan oleh kursus ini

| Keupayaan | Import |
|-----------|--------|
| **Kotak Alat Microsoft** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Memori Foundry** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Pemantauan / penilaian** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Tempatan** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Runtime agen hos** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Nota.** Petikan ini telah disahkan import dan tandatangan terhadap pakej semasa.
> Pelaksanaan dari hujung ke hujung juga memerlukan projek Microsoft Foundry, model sembang
> yang diterapkan, dan (untuk carian fail) penyimpanan vektor yang diisi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->