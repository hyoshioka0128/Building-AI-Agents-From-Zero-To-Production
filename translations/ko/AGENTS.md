# AGENTS.md

이 저장소에서 작업하는 AI 코딩 에이전트(및 인간 기여자)를 위한 지침입니다. 만약 자동화된 에이전트로서 이곳에서 변경을 한다면, 먼저 이 파일을 읽고 따르세요.


## 이 저장소란 무엇인가

<strong>제로부터 프로덕션까지 AI 에이전트 구축하기</strong>는 Microsoft 학습 코스입니다. 개발자들에게 <strong>Microsoft Foundry</strong>에서 <strong>Microsoft Agent Framework(MAF)</strong>를 사용하여 AI 에이전트를 설계, 구축, 평가, 배포 및 운영하는 방법을 가르칩니다. 내용은 각각 `README.md`와 실행 가능한 파이썬 샘플이 포함된 일련의 강의로 구성되어 있습니다.




```
lesson-1-agent-design/            Use case + how to design effective agents
lesson-2-agent-development/       Build specialised agents with MAF (multiple runnable samples)
lesson-3-agent-evals/             Evaluations and observability
lesson-4-agentdeployment/         Deploy a hosted agent + OpenAI ChatKit front end
lesson-5-hosted-agents-production/ Hosted Agents vs Capability Hosts, BYO storage, governance
lesson-6-toolbox/                 Microsoft Toolbox: define + govern tools centrally
lesson-7-multi-agent-a2a/         Multi-agent orchestration over the A2A protocol
```

루트 문서: `README.md` (여기서 시작), `MIGRATION-GUIDE.md` (SDK 마이그레이션 세부사항), `CHANGELOG.md`.

## 황금 규칙

1. **비밀 정보를 절대 커밋하지 마십시오.** `*.env.example` 파일만 추적하며 실제 `.env` 파일은 git에서 무시됩니다. 샘플이나 문서에 엔드포인트, 키, 토큰 또는 연결 문자열을 하드코딩하지 마십시오.
2. **`translations/` 또는 `translated_images/`를 건드리지 마십시오.** 이들은 GitHub 번역 작업에 의해 자동으로 생성됩니다. 직접 편집하지 말고 최상위 강의 파일만 소스 변경하세요.
3. **더 이상 사용되지 않는 모델은 사용하지 마십시오.** 채팅/평가에는 **`gpt-5.1`**, 코딩에는 **`gpt-5-codex`**를 사용하세요. `gpt-4o`, `gpt-4.1` 또는 은퇴한 모델은 도입하지 마시고, <em>GitHub Models</em>는 2026년 7월 30일에 중단되므로 사용하지 마십시오 — 모든 모델은 Microsoft Foundry를 통해 제공됩니다.
4. **현재 SDK 인터페이스를 사용하십시오.** 샘플은 `agent-framework` ( `requirements.txt`에 고정)와 `FoundryChatClient`, <strong>Responses API</strong>를 대상으로 합니다. 이전의 `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` 패턴을 다시 사용하지 마십시오.
5. **용어를 최신 상태로 유지하세요:** *Microsoft Foundry* (이전 "Azure AI Foundry" 아님), *Microsoft Agent Framework*, *Hosted Agents*, *Capability Hosts*, *Microsoft Toolbox*, *MCP / Hosted MCP*, *A2A*.









## 설정

```bash
python -m venv .venv
# Windows:  .venv\Scripts\Activate.ps1
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt

az login                     # 샘플은 개발자 신원으로 인증합니다
cp .env.example .env         # 그런 다음 Foundry 프로젝트 엔드포인트와 모델을 입력하세요
```

요구 사항: **Python 3.12+**, **Azure CLI**, 그리고 배포된 GPT-5 시리즈 모델이 있는 **Microsoft Foundry** 프로젝트 접근 권한. 각 강의 README는 필요한 전제 조건과 환경 변수(`.env.example`)를 명시합니다.



## 샘플 실행하기

대부분의 2단계 강의 샘플은 특정 포트(예: 8090–8096)에서 로컬 <strong>DevUI</strong>를 실행하며, 7단계 강의의 A2A 서버는 9000 포트를 사용합니다. 각 샘플의 docstring/README에서 정확한 명령과 포트를 확인하세요. 샘플이 실제 Foundry 엔드포인트를 호출하기 때문에 유효한 `.env` 파일과 `az login`이 필요합니다.



## 변경 사항 검증

단위 테스트 스위트는 없으며, 검증은 정적 검사와 라이브 테스트로 이루어집니다:

- **정적 검사(커밋 전에 통과해야 함):** 모든 샘플을 바이트 컴파일합니다.
  ```bash
  python -m py_compile $(git ls-files '*.py')
  ```
  Windows PowerShell에서:
  ```powershell
  git ls-files '*.py' | ForEach-Object { python -m py_compile $_ }
  ```
- **마크다운 링크:** CI `static` 작업이 `markdown-link-check`를 실행합니다(설정: `.github/workflows/markdown-link-check-config.json`). 신규 외부 링크가 HTTP 200을 반환하는지 확인하세요.
  (설정: `.github/workflows/markdown-link-check-config.json`). 신규 외부 링크가 HTTP 200을 반환하는지 확인하세요.
- **스모크 테스트:** `.github/workflows/smoke-test-hosted-agent.yml`가 배포된 호스티드 에이전트에 대해 AI 스모크 테스트 작업을 수행합니다(`workflow_dispatch`, OIDC). 라이브 에이전트 실행에는 Azure 접근 권한이 필요합니다.






## 커밋 규칙

- 집중된 내용으로 명확하고 명령형인 메시지 작성.
- 에이전트 지원 커밋에는 공동 작성자 트레일러를 포함.
  ```
  Co-authored-by: Copilot App <223556219+Copilot@users.noreply.github.com>
  ```
- 생성된 캐시, 가상 환경, `.env` 파일은 (모두 git 무시) 커밋하지 마세요.

## 특정 변경 위치

| 변경 대상 | 위치 |
|--------|----------|
| 강의 내러티브 / 본문 텍스트 | `lesson-*/README.md` (소스만 — 절대 `translations/` 사용 금지) |
| 실행 가능한 코드 | `lesson-*/**.py`, `setup_vector_store.py` |
| 의존성 | `requirements.txt` (버전 고정 유지) |
| 환경 변수 문서 | `.env.example`, 강의별 `.env.example` |
| CI / 정적 검사 | `.github/workflows/` |
| AI 지원용 강의 스킬 | `.github/skills/` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->