# பூமிக்குத் தொடங்கி வேலை விளைவாகி வரும் ஏ.ஐ முகவர்கள் உருவாக்குதல்

![பூமிக்குத் தொடங்கி வேலை விளைவாகி வரும் ஏ.ஐ முகவர்கள் உருவாக்குதல்](../../translated_images/ta/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 பன்மொழி ஆதரவு

#### GitHub செயல்பாட்டின் மூலம் ஆதரவு (தானியங்கி & எப்போதும் புதுப்பித்தல்)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](./README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **உள்ளூரில் கிளோன் செய்ய விரும்புகிறீர்களா?**

> இந்த ரெப்போவில் 50+ மொழி மொழிபெயர்ப்புகள் உள்ளன, இது பதிவிறக்க அளவை பெரிதாக அதிகரிக்கிறது. மொழிபெயர்ப்புகள் இல்லாமல் கிளோன் செய்ய sparse checkout ஐ பயன்படுத்தவும்:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> இது நீங்கள் விரைவாகவும், முழுமையாக பாடநெறியை முடிக்க தேவையான அனைத்தையும் தருகிறது.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## ஏ.ஐ முகவர் மேம்பாட்டு வாழ்க்கை சுற்றுப்பாதையின் அடிப்படைகளை கற்பிக்கும் ஒரு பாடநெறி

[![GitHub உரிமம்](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub பங்களிப்பாளர்கள்](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub பிரச்சினைகள்](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub புல்-ரிக்வெஸ்ட்](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs வரவேற்கப்படுகிறது](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 தொடங்குதல்

இந்த பாடநெறியில் ஏ.ஐ முகவர்களை உருவாக்கும் மற்றும் வெளியிடும் அடிப்படைகள் உள்ளன.

ஒவ்வொரு பாடமும் முந்தைய பாடத்தை அடிப்படையாகக் கொண்டு கட்டப்படுகிறது, எனவே தொடக்கம் முதல் முடிவுவரை படிப்பதற்கு பரிந்துரைக்கப்படுகிறது.

நீங்கள் ஏ.ஐ முகவர் தலைப்புகளை மேலும் ஆராய விரும்பினால், [AI Agents For Beginners Course](https://aka.ms/ai-agents-beginners)ஐ பார்க்கலாம்.

### பிற கற்றாளர்களை சந்தியுங்கள், உங்கள் கேள்விகளுக்கு பதில்களை பெறுங்கள்

அமைதி பெற முடியவில்லையெனில் அல்லது ஏ.ஐ முகவர்களை உருவாக்குவதில் சந்தேகம் இருந்தால், நமது Microsoft Foundry Discord இல் உள்ள தனி Discord சேனலுடன் இணைக.

### நீங்கள் தேவையெனும் பொருட்கள்

ஒவ்வொரு பாடத்திற்கும் உள்ளூர் இயங்கும் தனிப்பட்ட குறியீட்டு மாதிரிகள் உள்ளன. நீங்கள் [இந்த வேதியினை fork செய்யலாம்](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork) உங்கள் தனிப்பட்ட நகலை உருவாக்க.

இந்த பாடநெறியில் தற்போது பயன்படுத்தப்படுவது:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

தொடங்குவதற்கு முன், இந்த சேவைகளுக்கு அணுகல் இருப்பதை உறுதிப்படுத்தவும்.

மாடல் ஹோஸ்டிங் மற்றும் சேவைகள் குறித்த கூடுதல் விருப்பங்கள் விரைவில் வரவிருக்கின்றன.

## 🗃️ பாடங்கள்

| **பாடம்**          | **விளக்கம்**                                                                                      |
|--------------------|--------------------------------------------------------------------------------------------------|
| [Agent Design](./lesson-1-agent-design/README.md)       | "Developer Onboarding" முகவர் பயன்பாட்டின் அறிமுகம் மற்றும் பயனுள்ள முகவர்கள் வடிவமைப்பு பற்றி  |
| [Agent Development](./lesson-2-agent-development/README.md)  | Microsoft Agent Framework (MAF) பயன்படுத்தி புதிய டெவலப்பர்கள் அணுக உதவும் 3 முகவர்களை உருவாக்குதல்.       |
| [Agent Evaluations](./lesson-3-agent-evals/README.md)  | Microsoft Foundry பயன்படுத்தி எங்கள் ஏ.ஐ முகவர்கள் எப்படி செயல்படுகின்றன மற்றும் மேம்படுத்துவது எப்படி என்பதை கண்டறிதல். |
| [Agent Deployment](./lesson-4-agent-deployment/README.md)   | Hosted Agents மற்றும் OpenAI Chatkit பயன்படுத்தி ஏ.ஐ முகவர்களை தயாரிப்புக்கு வெளியிடுவது எப்படி என்பதை காண்க.       |


## 🎒 பிற பாடநெறிகள்

எங்கள் குழு மற்ற பாடநெறிகளையும் உருவாக்குகிறது! பாருங்கள்:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
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
 
### கோர் கற்றல்
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![தொடங்குபவர்கள் க்கு AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![தொடங்குபவர்கள் க்கு சைபர் பாதுகாப்பு](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![தொடங்குபவர்கள் க்கு வலை மேம்பாடு](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![தொடங்குபவர்கள் க்கு ஐஓடி](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![தொடங்குபவர்கள் க்கு XR மேம்பாடு](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### கோபைலட் தொடர்
[![AI இணையான நிரலாக்கத்துக்கு கோபைலட்](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET க்கு கோபைலட்](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![கோபைலட் சாகசங்கள்](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## பங்களிப்பது

இந்த திட்டம் பங்களிப்புகளையும் பரிந்துரைகளையும் வரவேற்கிறது. பெரும்பாலான பங்களிப்புகள் நீங்கள் பங்களிப்பை பயன்படுத்தும் உரிமை இருக்கிறது என்றும் நீங்கள் உண்மையில் அத்துடன் அந்த உரிமைகளை கொடுக்கின்றீர்கள் என்றும் விளக்கும்
பங்களிப்பாளர் உரிமம் ஒப்பந்தத்திற்கு (CLA) உடன்பட வேண்டும். விவரங்களுக்கு, <https://cla.opensource.microsoft.com> ஐ பார்வையிடவும்.

நீங்கள் ஒரு புல் கோரிக்கையை சமர்ப்பிக்கும் பொழுது, CLA பொட்டர் தானாகவே நீங்கள் CLA வழங்க வேண்டுமா என்பதைத் தீர்மானித்து
PR-ஐ ஏற்புடைய முறையில் (மாறி பொருந்தும் நிலையியல் சரிபார்ப்பு, கருத்து) அலங்கரிக்கும். பாட்டரின் வழங்கும் வழிமுறைகளைப் பின்பற்றவும்.
இதனை உங்கள் அனைத்து ரிபோக்களிலும் ஒருமுறை மட்டுமே செய்ய வேண்டும்.

இந்த திட்டம்  [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ஐ ஏற்கிறது.
மேலும் தகவலுக்கு [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) பார்க்கவும் அல்லது
எந்தவொரு கூடுதல் கேள்விகளுக்கும் கருத்துகளுக்கும் [opencode@microsoft.com](mailto:opencode@microsoft.com) அணுகவும்.

## வர்த்தகக் குறிகள்

இந்த திட்டத்தில் திட்டங்களுக்கான, தயாரிப்புகளுக்கான அல்லது சேவைகளுக்கான வர்த்தகக் குறியீடுகள் அல்லது லோகோக்கள் இருக்கலாம். Microsoft வர்த்தகக் குறி
அல்லது லோகோக்களை அனுமதிக்கப்பட்ட முறையில் பயன்படுத்துவது [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ஐப் பின்பற்ற வேண்டும்.
இந்த திட்டத்தின் மாறித்தெருமாற்றப்பட்ட பதிப்புகளில் Microsoft வர்த்தகக் குறிகள் அல்லது லோகோக்களின் பயன்பாடு குழப்பம் ஏற்படுத்தக்கூடாது அல்லது Microsoft ஆதரவைக் குறிக்கக்கூடாது.
மூன்றாம் தரப்பவர்களின் வர்த்தகக் குறிகள் அல்லது லோகோக்களின் எந்தவொரு பயன்பாடும் அந்த மூன்றாம் தரப்பவர்களின் கொள்கைகளுக்கு உட்பட்டது.

## உதவியைப் பெறுதல்

நீங்கள் சிக்கிக் கொண்டால் அல்லது AI பயன்பாடுகள் உருவாக்குவதில் ஏதேனும் கேள்விகள் இருந்தால் சேரவும்:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

உற்பத்தியின் பின்னூட்டங்கள் அல்லது பிழைகள் இருந்தால் படைப்பு செய்வதற்காக பார்க்கவும்:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**புறக்கணிப்பு**:  
இந்த ஆவணம் AI மொழி மாற்ற சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டுள்ளது. நாம் துல்லியம் பெறுகையை முன்னிலைப்படுத்தினாலும், தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறானதாக்கங்கள் இருக்கலாம் என்பதைக் கவனிக்கவும். இதன் அசல் ஆவணம் அதன் சொந்த மொழியில் கிடைக்கும், அதை அதிகாரபூர்வ מקורமாக கருதுங்கள். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழி மாற்றத்தை பரிந்துரைக்கிறோம். இந்த மொழிபெயர்ப்பின் பயன்பாட்டினால் ஏற்படக்கூடிய எந்த தவறுணர்வு அல்லது தவறான புரிதலுக்குமே நாம் பொறுப்பல்ல என்பதை அறிவிக்கிறோம்.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->