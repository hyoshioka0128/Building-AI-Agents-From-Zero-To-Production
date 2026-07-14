# 레슨 2 에이전트 개발

"제로부터 프로덕션까지 AI 에이전트 구축 과정" 두 번째 레슨에 오신 것을 환영합니다!

이번 레슨에서는 다음 내용을 다룹니다:

- AI 에이전트 생성 도구
  
- 개발 리소스 설정 지침

- AI 에이전트 개발 모범 사례
  
- AI 에이전트 생성 코드 워크스루
  
먼저, AI 에이전트를 만드는 데 사용할 도구들을 살펴보겠습니다.

## 도구 및 설정 지침

### Microsoft Foundry

대형 언어 모델(LLM)에 접근하기 위해 [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)를 사용할 것입니다. Foundry 사용에는 비용이 발생하므로, 아직 액세스 권한이 없다면 계정 설정 지침을 반드시 따라주세요.

### OpenAI 모델

이 과정의 에이전트 코드 샘플은 [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)를 통해 OpenAI 모델을 사용하도록 설정되어 있습니다.

Foundry를 사용해 모델을 배포하는 방법은 이 가이드를 참고하세요: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

이 과정에서는 GPT-5 시리즈 모델 중 하나(예: `gpt-5.1`)를 선택하세요. 2026년에 서비스 종료 예정인 GPT-4o 및 GPT-4.1 같은 은퇴 모델은 사용하지 마세요.

### Microsoft Agent Framework

앞서 언급했듯이, AI 에이전트를 생성 및 조율하기 위해 [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)를 사용합니다.

Python 3.12 이상이 필요합니다. Microsoft Agent Framework와 기타 필수 패키지를 설치하려면 이 프로젝트 루트 디렉터리에서 다음 명령을 실행하세요:

```bash
pip install -r requirements.txt
```

### Azure 인증

에이전트는 Azure CLI 자격증명(`AzureCliCredential`)을 사용해 Microsoft Foundry에 인증하므로,
샘플을 실행하기 전에 반드시 로그인해야 합니다:

```bash
az login
# 구독이 여러 개인 경우 Foundry 프로젝트가 포함된 구독을 선택하세요:
az account set --subscription "<your-subscription-id>"
```

계정에 Foundry 프로젝트에서 모델과 에이전트 API를 호출할 수 있도록
**Azure AI User** 역할(또는 이에 상응하는 권한)이 부여되어 있는지 확인하세요.

### .env 변수 설정

본 과정의 코드 샘플을 실행하려면, 이 프로젝트 루트 디렉터리에 `.env` 파일을 생성해야 합니다.

편리하게 제공된 `.env.example` 파일을 복사해 사용할 수 있습니다:

```bash
cp .env.example .env
``` 

그 후, 에이전트가 자동으로 읽어들이는 두 변수를 채워 넣으세요
(`FoundryChatClient`가 이를 자동으로 인식합니다):

| 변수명 | 내용 | 위치 |
|----------|------------|------------------|
| `FOUNDRY_PROJECT_ENDPOINT` | Foundry <strong>프로젝트</strong> 엔드포인트, `/api/projects/<project>`로 끝남 | Foundry 포털 → 프로젝트 선택 → <strong>개요</strong> → <em>엔드포인트</em> |
| `FOUNDRY_MODEL` | 에이전트가 실행할 모델 배포 이름 (예: `gpt-5.1`) | Foundry 포털 → **모델 + 엔드포인트** |

### 직원 벡터 스토어 생성

샘플 중 하나인 — **직원 검색 에이전트** — 는 Microsoft Foundry의 <strong>벡터 스토어</strong>에 저장된 직원 디렉터리를 검색합니다.
한 번 생성한 뒤, 출력되는 ID를 `.env` 파일 내 `VECTOR_STORE_ID` 변수에 복사하세요
(프로젝트 루트에서 실행해야 `.env`를 인식합니다):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### 샘플 실행하기

각 에이전트는 자체 로컬 DevUI를 실행합니다. 예를 들면:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

그런 다음 출력된 `http://localhost:<port>` URL을 브라우저에서 열어 에이전트와 대화할 수 있습니다.

## 이번 레슨의 에이전트들

각 샘플은 Microsoft Agent Framework로 만든 독립 실행형 에이전트입니다. 이들은 함께
[Lesson 1](../lesson-1-agent-design/README.md)에서 설계한 시나리오를 구현합니다.

| 샘플 | Lesson 1 시나리오 | 사용 도구 | 포트 |
|--------|-------------------|-----------|------|
| `employee-search-agent.py` | 시나리오 1 — 직원 검색 | 벡터 스토어 위에서 운영되는 Foundry 호스팅 **파일 검색** | 8090 |
| `task-recommendation-agent.py` | 시나리오 2 — 작업 추천 | **GitHub MCP** 서버 (호스팅 MCP 도구) | 8095 |
| `azure-learning-agent.py` | 시나리오 3 — 코드 어시스턴트 (연구) | **Microsoft Learn MCP** 서버 (호스팅 MCP 도구) | 8092 |
| `coding-agent.py` | 시나리오 3 — 코드 어시스턴트 (코딩) | **코드 인터프리터** | 8093 |
| `learning-recommendation-agent.py` | 지원 에이전트 | Learn MCP + 추론 | 8091 |
| `agent-orchestration.py` | 시나리오들 연결 | 다중 에이전트 <strong>핸드오프</strong> 오케스트레이션 | 8094 |

> **작업 추천 에이전트 관련 참고사항.** `task-recommendation-agent.py`는 `.env` 파일에
> `GITHUB_PERSONAL_ACCESS_TOKEN`이 필요합니다 (https://github.com/settings/personal-access-tokens/new 에서 생성 가능).
> 이 토큰으로 개발자의 최근 GitHub 활동을 읽고 시나리오 2 설계대로
> 일치하는 1~3개의 오픈 이슈를 추천합니다.
> 이 샘플만 GitHub를 호출하며, 다른 샘플들은 Foundry 프로젝트만 필요로 합니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->