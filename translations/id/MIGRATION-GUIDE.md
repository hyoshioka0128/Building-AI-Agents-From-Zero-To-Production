# Panduan Migrasi — Microsoft Foundry Agent Framework (Juli 2026)

Panduan ini memetakan permukaan SDK yang digunakan oleh contoh kursus awalnya
ke paket **Microsoft Agent Framework** yang **saat ini diterbitkan**. Setiap pemetaan dan
tanda tangan di bawah ini telah diverifikasi dengan mengintrospeksi paket yang terinstal
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Mengapa ini penting:** dengan perubahan merek menjadi **Microsoft Foundry**, permukaan klien pindah
> dari `agent_framework.azure` (kelas `AzureAI*` lama) ke **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Kelas alat-host tingkat atas lama
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) telah dihapus; alat Host
> sekarang dibuat **dari klien** melalui metode pabrik `get_*_tool(...)`.

---

## 1. Pemetaan impor & klien

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

**Parameter kredensial berganti nama:** klien lama menggunakan `async_credential=...`;
`FoundryChatClient` menggunakan `credential=...`.

---

## 2. Tanda tangan yang terverifikasi

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # atau atur AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # atau atur variabel lingkungan model
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
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Observabilitas
```

---

## 3. Sebelum / sesudah — satu agen dengan alat MCP host

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

**Sesudah** (Microsoft Foundry):

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

## 4. Sebelum / sesudah — pencarian file host (penyimpanan vektor)

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

**Sesudah**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Pola async yang sudah usang

**Sebelum** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` sudah usang. Gunakan yang dihosting `client.get_mcp_tool(...)`
(tanpa koneksi manual), atau jika Anda harus menggunakan `MCPStreamableHTTPTool` sisi klien, bungkus
dengan `asyncio.run(...)` atau konteks `async with`.

---

## 6. Permukaan canggih yang kini digunakan kursus ini

| Kemampuan | Impor |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observabilitas / eval** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Runtime agen-hosted** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Catatan.** Cuplikan ini diverifikasi impor dan tandatangan terhadap paket saat ini.
> Eksekusi ujung-ke-ujung juga memerlukan proyek Microsoft Foundry, model obrolan yang telah diterapkan,
> dan (untuk pencarian file) penyimpanan vektor yang sudah diisi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->