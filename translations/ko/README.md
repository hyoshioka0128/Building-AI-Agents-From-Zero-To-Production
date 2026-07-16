# AI 에이전트 처음부터 프로덕션까지 구축하기

![Building AI Agents from Zero to Production](../../translated_images/ko/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 다국어 지원

#### GitHub 액션을 통한 지원 (자동화 및 항상 최신 상태 유지)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](./README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **로컬 클론을 선호하나요?**
>
> 이 저장소에는 50개 이상의 언어 번역이 포함되어 있어 다운로드 크기가 크게 증가합니다. 번역 없이 클론하려면 스패어 체크아웃을 사용하세요:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> 이 방법으로 훨씬 빠른 다운로드로 코스 완료에 필요한 모든 것을 얻을 수 있습니다.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## AI 에이전트 개발 라이프사이클의 기본을 가르치는 강좌

[![GitHub license](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 시작하기

이 강좌는 AI 에이전트 구축 및 배포의 기초를 다루는 수업들로 구성되어 있습니다.

각 수업은 이전 수업을 기반으로 하므로 처음부터 시작하여 끝까지 진행하는 것을 권장합니다.

AI 에이전트 주제에 대해 더 탐구하고 싶다면 [AI Agents For Beginners Course](https://aka.ms/ai-agents-beginners)를 확인하세요.

### 다른 학습자 만나기, 질문 답변 받기

AI 에이전트 구축에 막히거나 질문이 있으면 [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6)의 전용 디스코드 채널에 참여하세요.

### 필요한 것


각 레슨에는 로컬에서 실행할 수 있는 코드 샘플이 있습니다. [이 저장소를 포크](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork)하여 자신의 복사본을 만들 수 있습니다.

이 과정에서 현재 다음을 사용합니다:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) — 배포된 **GPT-5 시리즈** 모델(예: `gpt-5.1`)이 포함된 프로젝트입니다. 폐기된 GPT-4o / GPT-4.1 모델은 사용하지 마십시오.
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest) — 샘플을 실행하기 전에 `az login`으로 로그인하세요.
- **Python 3.12 이상**

시작하기 전에 이 서비스들에 접근할 수 있는지 확인해주세요.

> **💰 비용 및 정리.** 실습 레슨은 실제 Azure 리소스를 만듭니다 — Microsoft Foundry
> 프로젝트, 모델 배포, 벡터 저장소 및 (레슨 4–6에서) 호스팅되는 에이전트와 툴박스를 포함합니다.
> 이러한 리소스들은 존재하는 동안 비용이 발생할 수 있습니다. 레슨이나 과정을 마친 후에는 더 이상 필요 없는
> 리소스를 삭제하세요. 가장 간단한 방법은 모든 것을 전용 리소스
> 그룹에 넣고 완료 후 해당 그룹을 삭제하는 것입니다:
>
> ```bash
> az group delete --name <your-resource-group> --yes --no-wait
> ```
>
> 또한 Foundry 포털에서 개별 에이전트, 벡터 저장소 및 툴박스를 삭제할 수 있습니다.

> **모델 관련 참고.** 이 과정은 모든 모델을 <strong>Microsoft Foundry</strong>를 통해 제공합니다. <em>GitHub Models</em>는
> 2026년 7월 30일에 종료되므로 사용하지 않습니다 — Microsoft Foundry가
> 공식 마이그레이션 경로입니다. 이전 코드가 GitHub Models를 호출하는 경우 대신 Foundry
> 모델 배포를 가리키도록 변경하세요.

모델 호스팅 및 서비스 관련 더 많은 옵션이 곧 제공될 예정입니다. 

## 🗃️ 레슨

| <strong>레슨</strong>         | <strong>설명</strong>                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------|
| [에이전트 디자인](./lesson-1-agent-design/README.md)       | "개발자 온보딩" 에이전트 사용 사례 소개 및 효과적인 에이전트 설계 방법                                |
| [에이전트 개발](./lesson-2-agent-development/README.md)  | Microsoft Agent Framework (MAF)를 사용하여 새 개발자를 지원하는 특화된 에이전트 세트 구축          |
| [에이전트 평가](./lesson-3-agent-evals/README.md)  | Microsoft Foundry를 사용하여 AI 에이전트의 성능 평가 및 개선 방법 학습                              |
| [에이전트 배포](./lesson-4-agentdeployment/README.md)   | Microsoft Foundry 호스팅 에이전트 및 OpenAI ChatKit을 활용해 AI 에이전트를 프로덕션에 배포하기       |
| [프로덕션 호스팅 에이전트](./lesson-5-hosted-agents-production/README.md)   | 호스팅 에이전트를 엔터프라이즈 프로덕션에 적용: 호스팅 에이전트 대 능력 호스트, 사용자 저장소, 메모리 및 거버넌스 적용   |
| [Microsoft 툴박스](./lesson-6-toolbox/README.md)   | 도구를 한 번 정의하고 중앙에서 관리: 툴박스를 구축하고 에이전트가 하나의 MCP 엔드포인트를 통해 사용하며 도구 버전을 안전하게 관리  |
| [멀티 에이전트 & A2A](./lesson-7-multi-agent-a2a/README.md)   | 네트워크된 서비스로 에이전트를 구성: 오픈 에이전트-투-에이전트(A2A) 프로토콜로 에이전트를 노출하고 원격 에이전트를 피어로 사용  |


## 🎒 기타 과정

저희 팀은 다른 과정도 제작합니다! 확인해 보세요:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![초보자를 위한 LangChain4j](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![초보자를 위한 LangChain.js](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![초보자를 위한 LangChain](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / 에이전트
[![초보자를 위한 AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 Edge AI](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 AI 에이전트](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 생성 AI 시리즈

[![초보자를 위한 생성 AI](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![생성 AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![생성 AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![생성 AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### 핵심 학습
[![초보자를 위한 기계 학습](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 데이터 과학](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 사이버 보안](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)

[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 코파일럿 시리즈
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 기여하기

이 프로젝트는 기여와 제안을 환영합니다. 대부분의 기여는 당신이 권리를 가지고 있으며 실제로
우리의 기여물 사용 권리를 부여한다는 것을 선언하는
기여자 라이선스 계약서(CLA)에 동의해야 합니다. 자세한 내용은 <https://cla.opensource.microsoft.com>을 방문하세요.

풀 리퀘스트를 제출할 때, CLA 봇이 자동으로 CLA 제공 필요 여부를 판별하고 PR에 적절히 표시합니다(예: 상태 검사, 댓글).
봇이 안내하는 지침을 따르기만 하면 됩니다.
우리 CLA를 사용하는 모든 저장소에서 이 작업은 한 번만 하면 됩니다.

이 프로젝트는 [Microsoft 오픈 소스 행동 강령](https://opensource.microsoft.com/codeofconduct/)을 채택했습니다.
자세한 내용은 [행동 강령 FAQ](https://opensource.microsoft.com/codeofconduct/faq/)를 참조하거나
추가 질문이나 의견이 있으면 [opencode@microsoft.com](mailto:opencode@microsoft.com)으로 연락해 주세요.

## 상표


이 프로젝트에는 프로젝트, 제품 또는 서비스의 상표나 로고가 포함될 수 있습니다. Microsoft 상표 또는 로고의 허가된 사용은 
[Microsoft의 상표 및 브랜드 가이드라인](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)을
준수해야 하며, 이에 따라야 합니다.
수정된 버전의 프로젝트에서 Microsoft 상표나 로고를 사용하는 경우 혼동을 일으키거나 Microsoft 후원을 암시해서는 안 됩니다.

타사 상표 또는 로고의 사용은 해당 타사의 정책에 따릅니다.

## 도움 받기

AI 앱 개발 중에 막히거나 질문이 있는 경우, 다음에 참여하세요:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

제품 피드백이나 빌드 중 오류가 있는 경우 방문하세요:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->