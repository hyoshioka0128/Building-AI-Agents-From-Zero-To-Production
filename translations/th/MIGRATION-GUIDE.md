# คู่มือการย้าย — Microsoft Foundry Agent Framework (กรกฎาคม 2026)

คู่มือนี้จัดทำแผนที่พื้นผิว SDK ที่ตัวอย่างคอร์สเขียนไว้เดิม
ไปยังแพ็กเกจ Microsoft Agent Framework **เวอร์ชันปัจจุบันที่เผยแพร่** ทุกการแมปและ
ลายเซ็นด้านล่างได้รับการตรวจสอบโดยการตรวจสอบแพ็กเกจที่ติดตั้ง
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`) แล้ว

> **ทำไมเรื่องนี้จึงสำคัญ:** เมื่อมีการเปลี่ยนชื่อเป็น **Microsoft Foundry** พื้นผิวไคลเอนต์ย้าย
> จาก `agent_framework.azure` (คลาส `AzureAI*` เดิม) ไปยัง **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`) คลาสเครื่องมือโฮสต์ระดับบนเดิม
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) ถูกลบออก; เครื่องมือโฮสต์
> จะถูกสร้าง **จากไคลเอนต์** ผ่านเมธอดแฟคทอรี `get_*_tool(...)`

---

## 1. การนำเข้าและการแมปไคลเอนต์

| เดิม (ตัวอย่างคอร์ส) | ใหม่ (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → คืนค่า `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (MCP ฝั่งไคลเอนต์) | ไม่เปลี่ยนแปลง — ยังคง `from agent_framework import MCPStreamableHTTPTool` |

**พารามิเตอร์การรับรองชื่อถูกเปลี่ยน:** ไคลเอนต์เดิมใช้ `async_credential=...`;
`FoundryChatClient` ใช้ `credential=...`

---

## 2. ลายเซ็นที่ตรวจสอบแล้ว

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # หรือกำหนด AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # หรือกำหนดตัวแปรสภาพแวดล้อมของโมเดล
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # กล่องเครื่องมือของ Microsoft
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # การสังเกตการณ์
```

---

## 3. ก่อน / หลัง — เอเย่นต์ตัวเดียวกับเครื่องมือ MCP โฮสต์

**ก่อน** (`azure-learning-agent.py`):

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

**หลัง** (Microsoft Foundry):

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

## 4. ก่อน / หลัง — การค้นหาไฟล์โฮสต์ (เวคเตอร์สโตร์)

**ก่อน** (`employee-search-agent.py`):

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

**หลัง**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. รูปแบบ async ที่เลิกใช้

**ก่อน** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` ถูกเลิกใช้ โปรดใช้เครื่องมือโฮสต์ `client.get_mcp_tool(...)`
(ไม่ต้องเชื่อมต่อเอง), หรือถ้าต้องใช้ `MCPStreamableHTTPTool` ฝั่งไคลเอนต์ ให้ห่อไว้ด้วย
`asyncio.run(...)` หรือใช้บริบท `async with`

---

## 6. พื้นผิวขั้นสูงที่คอร์สนี้ใช้ตอนนี้

| ความสามารถ | การนำเข้า |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **การสังเกตการณ์ / การประเมินผล** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **เวลารันโฮสต์เอเย่นต์** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **หมายเหตุ.** โค้ดตัวอย่างเหล่านี้ได้รับการตรวจสอบการนำเข้าและลายเซ็นเทียบกับแพ็กเกจปัจจุบันแล้ว
> การรันตั้งแต่ต้นจนจบยังต้องมีโปรเจกต์ Microsoft Foundry, โมเดลแชทที่ถูกปรับใช้,
> และ (สำหรับการค้นหาไฟล์) เวคเตอร์สโตร์ที่มีข้อมูล

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->