<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b09df38b3188ffe957c7ac8b055967f5",
  "translation_date": "2026-01-16T09:58:47+00:00",
  "source_file": "README.md",
  "language_code": "ta"
}
-->
# பூட்டி எஐ முகவர்கள் உருவாக்குதல் பூஜ்யம் முதல் உற்பத்தி வரை

![பூட்டி எஐ முகவர்கள் உருவாக்குதல் பூஜ்யம் முதல் உற்பத்தி வரை](../../../../translated_images/ta/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 பல்மொழி ஆதரவு

#### GitHub செயல் மூலம் ஆதரவு (தானியங்கி மற்றும் எப்போதும் புதுப்பிக்கப்பட்டது)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](./README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **உள்ளகமாக கிளோன் செய்ய விரும்புகிறீர்களா?**

> இந்த தொகுப்பு 50+ மொழி மொழிபெயர்ப்புகளை கொண்டுள்ளது, இது பதிவிறக்க அளவை மிகவும் அதிகரிக்கிறது. மொழிபெயர்ப்புகளை இல்லாமல் கிளோன் செய்ய sparse checkout ஐ பயன்படுத்தவும்:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> இது பாடத்தை முடிக்க உங்களுக்கு தேவையான அனைத்தையும் மிகவும் சீக்கிரம் பதிவிறக்கம் செய்ய உதவும்.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## எஐ முகவர் மேம்பாடு வாழ்க்கைப் பத்தியின் அடிப்படைகளை கற்றுக் கொடுக்கும் ஒரு பாடநெறி

[![GitHub license](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 துவக்கம்

இந்த பாடநெறியில் எஐ முகவர்களை உருவாக்குவதற்கும் நியமிக்குவதற்கும் அடிப்படைகளை உள்ளடக்கிய பாடங்கள் உள்ளன.

ஒவ்வொரு பாடமும் முந்தையதை அடிப்படையாகக் கொண்டு கட்டியெழுப்பப்படுகிறது, ஆகவே நாங்கள் ஆரம்பத்திலிருந்து தொடங்கி இறுதிவரை தொடர எங்கும் பரிந்துரைக்கிறோம்.

நீங்கள் மேலும் எஐ முகவர் தலைப்புகளை ஆராய விரும்பினால், [AI Agents For Beginners Course](https://aka.ms/ai-agents-beginners) ஐப் பார்க்கலாம்.

### பிற கற்பவர்களை சந்திக்கவும், உங்கள் கேள்விகளுக்கு பதில் பெறவும்

எஐ முகவர்கள் உருவாக்குவதில் கயிற்றில் இருந்தால் அல்லது கேள்விகள் இருந்தால், நமது அர்ப்பணிக்கப்பட்ட Discord சேனலில் சேரவும் [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6).

### உங்களுக்கு தேவையானவை

ஒவ்வொரு பாடத்துக்கும் உங்கள் இயந்திரத்தில் இயக்கக்கூடிய தனிப்பட்ட குறியீட்டு உதாரணங்கள் உள்ளன. உங்கள் சொந்த பிரதியை உருவாக்க இக்கூறை [fork செய்யலாம்](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork).

இந்த பாடநெறி தற்போது பின்வரும் பயன்படுத்துகிறது:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

துவங்குவதற்கு முன், இந்த சேவைகளுக்கு அணுகல் உங்களிடம் இருப்பதை உறுதி செய்யவும்.

மாதிரி ஹோஸ்டிங் மற்றும் சேவைகள் தொடர்பான கூடுதல் விருப்பங்கள் விரைவில் வருகின்றன.

## 🗃️ பாடங்கள்

| **பாடம்**              | **விளக்கம்**                                                                                  |
|------------------------|--------------------------------------------------------------------------------------------------|
| [Agent Design](./lesson-1-agent-design/README.md)       | எங்கள் "Developer Onboarding" முகவர் பயன்பாட்டு வழக்கு அறிமுகம் மற்றும் விளைவூட்டும் முகவர்களை வடிவமைக்கும் முறை |
| [Agent Development](./lesson-2-agent-development/README.md)  | Microsoft Agent Framework (MAF) பயன்படுத்தி புதிய வளர்ப்பவர்களை உதவும் 3 முகவர்களை உருவாக்குதல்.       |
| [Agent Evaluations](./lesson-3-agent-evals/README.md)  | Microsoft Foundry பயன்படுத்தி எங்கள் எஐ முகவர்கள் எவ்வளவு நன்கு செயல்படுகின்றன மற்றும் அவற்றை எப்படி மேம்படுத்துவது காண்போம். |
| [Agent Deployment](./lesson-4-agent-deployment/README.md)   | Hosted Agents மற்றும் OpenAI Chatkit பயன்படுத்தி எஐ முகவர்களை உற்பத்தியில் எப்படி நிகழ்த்துவது தெரிந்துகொள்ளவும்.       |


## 🎒 பிற பாடநெறிகள்

எங்கள் குழு பிற பாடநெறிகளை தயாரிக்கிறது! பாருங்கள்:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Core Learning
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![இலவச பாதுகாப்பு](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![இணைய உருவாக்கம் பயிலுவர்களுக்காக](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![இண்டர்நெட் ஆஃப் திங்ஸ் (IoT) பயிலுவர்களுக்காக](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR அபிவிருத்தி பயிலுவர்களுக்காக](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### கோப்பைலட் தொடர்
[![AI இணைக்கப்பட்ட நிரலாக்கத்திற்கு கோப்பைலட்](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET க்கான கோப்பைலட்](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![கோப்பைலட் சாகசம்](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## பங்களிப்பு செய்யவும்

இந்த திட்டம் பங்களிப்புகளையும் பரிந்துரைகளையும் வரவேற்கிறது. பெரும்பாலான பங்களிப்புகளுக்கு நீங்கள் உங்கள் பங்களிப்பை பயன்படுத்துவதற்கான உரிமைகளை நமக்குக் கொடுக்கிறீர்கள் என்று அறிவிக்கும்
ஒரு பங்களிப்பாளர் உரிமம் ஒப்பந்தத்தை (CLA) ஏற்க வேண்டும். விரிவுகளுக்கு, <https://cla.opensource.microsoft.com> ஐப் பார்க்கவும்.

நீங்கள் ஒரு புல் கோரிக்கையை சமர்ப்பிக்கும் போது, CLA பாட்டி தானாகவே நீங்கள் CLA வழங்க வேண்டுமா என்பதை தீர்மானித்து
PR றுக்கு சரியான சில (e.g., நிலை பரிசோதனை, கருத்து) வழங்கும். பாட்டியின் வழிகாட்டுதல்களை பின்பற்றுங்கள்.
நாம் பயன்படுத்தும் அனைத்து ரெப்போக்களிலும் இது உடனே ஒருமுறை மட்டுமே செய்யவேண்டும்.

இந்த திட்டம் [Microsoft Open Source நடத்தை விதிகள்](https://opensource.microsoft.com/codeofconduct/) ஐ ஏற்றுக்கொண்டுள்ளது.
மேலும் தகவலுக்கு [நடத்தை விதிகள் FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ஐ பார்க்கவும் அல்லது
[opencode@microsoft.com](mailto:opencode@microsoft.com) இல் தொடர்பு கொள்ளவும்.

## வர்த்தகச்சின்னங்கள்

இந்த திட்டத்தில் திட்டங்கள், பொருட்கள் அல்லது சேவைகளுக்கான வர்த்தகச்சின்னங்கள் அல்லது லோகோக்கள் இருக்கலாம். Microsoft 
வர்த்தகச்சின்னங்கள் அல்லது லோகோக்களை அதிகாரப்பூர்வமாக பயன்படுத்துவது [Microsoft வர்த்தகச்சின்ன & பிராண்ட் வழிகாட்டிகள்](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) 
படி செயல்பட வேண்டும்.
Microsoft வர்த்தகச்சின்னங்கள் அல்லது லோகோக்களை மாற்றியமைக்கப்பட்ட பதிப்புகளில் பயன்படுத்துவது குழப்பத்தை ஏற்படுத்த கூடாது அல்லது Microsoft ஆதரவைக் குறிக்கக்கூடாது.
மூன்றாம் தரப்பு வர்த்தகச்சின்னங்கள் அல்லது லோகோக்களைப் பயன்படுத்துவது அந்த மூன்றாம் தரப்பின் கொள்கைகளுக்குட்பட்டது.

## உதவி பெறுவது எப்படி

நீங்கள் கடும் பிரச்சினையில் சிக்கினால் அல்லது AI பயன்பாடுகள் உருவாக்கைப்பற்றி ஏதேனும் கேள்விகள் இருந்தால், இணைக:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

உங்கள் தயாரிப்புப் பின்னூட்டங்கள் அல்லது பிழைகளை உருவாக்கும் போது, பார்வையிட:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு அறிவிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டுள்ளது. நாம் துல்லியத்திற்காக முயற்சி செய்கிறோம் என்றாலும், தானியங்கி மொழிபெயர்ப்புகளில் நிலைமாறுதல்கள் அல்லது துல்லியக்கேடுகள் ஏற்படக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் சொந்த மொழியில் அதிகாரப்பூர்வ ஆதரவாக கருதப்பட வேண்டும். விடுவிக்க அளவிலான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பின் பயன்பாட்டால் ஏற்படும் எந்த அபரிஜிதம் அல்லது தவறான விளக்கத்திற்கும் நாம் பொறுப்பாக இருக்கமாட்டோம்.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->