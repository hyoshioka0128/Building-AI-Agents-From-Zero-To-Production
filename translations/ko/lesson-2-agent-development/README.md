<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:09:56+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "ko"
}
-->
# Lesson 2 에이전트 개발

"제로부터 프로덕션까지 AI 에이전트 구축 코스" 두 번째 수업에 오신 것을 환영합니다!

이 수업에서는 다음 내용을 다룹니다:

- AI 에이전트를 만들기 위한 도구
  
- 개발 리소스 설정 지침

- AI 에이전트 개발 모범 사례
  
- AI 에이전트 생성 코드 워크스루
  
먼저 AI 에이전트를 만들 때 사용할 도구들을 살펴보겠습니다.

## 도구 및 설정 지침

### Microsoft Foundry

대규모 언어 모델(LLM)에 접근하기 위해 [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)를 사용합니다. Foundry 사용에는 비용이 발생하므로 아직 접근 권한이 없는 경우 계정 설정 지침을 꼭 따라 주세요.

### OpenAI 모델

이 코스의 에이전트 코드 샘플은 [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)를 통해 OpenAI 모델을 사용하도록 설정되어 있습니다.

Foundry를 사용하여 모델을 배포하는 방법은 이 가이드를 참고하세요: [Foundry 포털에서 Microsoft Foundry 모델 배포하기](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

이 코스에서는 GPT-4.1 이상 모델 중 하나를 선택하세요.

### Microsoft Agent Framework

앞서 언급했듯이, AI 에이전트를 생성하고 조율하기 위해 [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)를 사용할 것입니다.

Microsoft Agent Framework 및 필요한 다른 패키지를 설치하려면 이 프로젝트의 루트 디렉터리에서 다음 명령어를 실행하세요:

```bash
pip install -r requirements.txt
```

### .env 변수 설정

이 코스의 코드 샘플을 실행하려면 이 프로젝트 루트 디렉터리에 `.env` 파일을 생성해야 합니다.

더 쉽게 하려면 제공된 `.env.example` 파일을 복사할 수 있습니다:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 내용이 포함될 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->