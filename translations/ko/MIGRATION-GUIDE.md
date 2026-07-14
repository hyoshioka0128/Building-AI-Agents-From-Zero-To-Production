# 마이그레이션 가이드 — Microsoft Foundry 에이전트 프레임워크 (2026년 7월)

이 가이드는 과정 샘플이 원래 작성된 SDK 표면을
현재 <strong>공개된</strong> Microsoft Agent Framework 패키지에 매핑합니다. 아래의 모든 매핑 및
시그니처는 설치된 패키지
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`)를 인트로스펙션하여 검증되었습니다.

> **중요한 이유:** <strong>Microsoft Foundry</strong>로 리브랜딩하면서 클라이언트 표면이
> `agent_framework.azure` (이전 `AzureAI*` 클래스)에서 **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`)로 이동했습니다. 이전 최상위 호스팅 도구 클래스
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`)는 제거되었으며; 호스팅된
> 도구는 이제 클라이언트에서 `get_*_tool(...)` 팩토리 메서드를 통해 생성됩니다.

---

## 1. 임포트 및 클라이언트 매핑

| 이전 (과정 샘플) | 새 (Microsoft Foundry) |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → `Agent` 반환 |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (클라이언트 측 MCP) | 변경 없음 — 계속 `from agent_framework import MCPStreamableHTTPTool` |

**자격 증명 매개변수 이름 변경:** 이전 클라이언트는 `async_credential=...`를 사용했지만;
`FoundryChatClient`는 `credential=...`를 사용합니다.

---

## 2. 검증된 시그니처

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # 또는 AZURE_AI_PROJECT_ENDPOINT 설정
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # 또는 모델 환경 변수 설정
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # 마이크로소프트 도구 모음
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # 관측 가능성
```

---

## 3. 이전 / 이후 — 호스팅된 MCP 도구가 있는 단일 에이전트

<strong>이전</strong> (`azure-learning-agent.py`):

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

<strong>이후</strong> (Microsoft Foundry):

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

## 4. 이전 / 이후 — 호스팅된 파일 검색 (벡터 스토어)

<strong>이전</strong> (`employee-search-agent.py`):

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

<strong>이후</strong>:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. 사용 중단된 비동기 패턴

<strong>이전</strong> (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()`는 사용 중단(deprecated)되었습니다. 수동 연결 없이 호스팅된 `client.get_mcp_tool(...)`
를 사용하는 것이 좋으며, 클라이언트 측 `MCPStreamableHTTPTool`을 꼭 사용해야 한다면,
`asyncio.run(...)` 또는 `async with` 컨텍스트로 래핑하세요.

---

## 6. 이 과정에서 이제 사용하는 고급 표면

| 기능 | 임포트 |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **관찰성 / 평가** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **호스팅된 에이전트 런타임** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **참고.** 이 코드 조각들은 현재 패키지와 임포트 및 시그니처가 검증되었습니다.
> 엔드 투 엔드 실행을 위해서는 Microsoft Foundry 프로젝트, 배포된 채팅
> 모델 및 (파일 검색을 위해) 채워진 벡터 스토어가 추가로 필요합니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->