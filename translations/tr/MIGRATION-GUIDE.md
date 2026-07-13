# Geçiş Rehberi — Microsoft Foundry Agent Framework (Temmuz 2026)

Bu rehber, SDK yüzeyini kurs örneklerinin orijinal olarak yazıldığı
**güncel, yayımlanmış** Microsoft Agent Framework paketlerine eşler. Aşağıdaki her eşleme ve
imza, kurulu paketler incelenerek doğrulanmıştır
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Neden önemli:** **Microsoft Foundry** markasına geçişle birlikte istemci yüzeyi
> `agent_framework.azure`'dan (eski `AzureAI*` sınıfları) **`agent_framework.foundry`**'e
> (`FoundryChatClient`, `FoundryAgent`) taşındı. Eski üst seviye barındırılan araç sınıfları
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) kaldırıldı; barındırılan
> araçlar artık **istemci tarafından** `get_*_tool(...)` fabrikası metotlarıyla oluşturulmaktadır.

---

## 1. İçe aktarma & istemci eşlemesi

| Eski (kurs örnekleri) | Yeni (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → `Agent` döner |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (istemci tarafı MCP) | değişmedi — hâlâ `from agent_framework import MCPStreamableHTTPTool` |

**Kimlik bilgisi parametresi yeniden adlandırıldı:** eski istemciler `async_credential=...` alıyordu;
`FoundryChatClient` `credential=...` alır.

---

## 2. Doğrulanmış imzalar

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # veya AZURE_AI_PROJECT_ENDPOINT ayarla
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # veya model ortam değişkenini ayarla
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Microsoft Araç Kutusu
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # İzlenebilirlik
```

---

## 3. Önce / sonra — barındırılan MCP aracıyla tek ajan

**Önce** (`azure-learning-agent.py`):

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

**Sonra** (Microsoft Foundry):

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

## 4. Önce / sonra — barındırılan dosya araması (vektör deposu)

**Önce** (`employee-search-agent.py`):

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

**Sonra**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Kullanımdan kalkmış asenkron desen

**Önce** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` kullanımdan kalktı. Barındırılan `client.get_mcp_tool(...)`
(manuel bağlantı yok) tercih edin veya eğer istemci tarafı `MCPStreamableHTTPTool` kullanmanız gerekirse,
onu `asyncio.run(...)` veya bir `async with` bağlamıyla sarın.

---

## 6. Bu kursun artık kullandığı gelişmiş yüzeyler

| Yetenek | İçe Aktarma |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Hafıza** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Gözlemlenebilirlik / değerlendirme** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Lokal** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Barındırılan ajan çalışma zamanı** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Not.** Bu kod parçacıkları mevcut paketlere karşı içe aktarma ve imza olarak doğrulanmıştır.
> Uçtan uca yürütme ayrıca bir Microsoft Foundry projesi, konuşma modeli dağıtımı
> ve (dosya araması için) dolu bir vektör deposu gerektirir.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->