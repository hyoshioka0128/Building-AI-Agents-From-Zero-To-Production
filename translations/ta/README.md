# பூட்டி ஏஜெண்டுகளை பூச்சியிலிருந்து உற்பத்திக்கு கட்டமைத்தல்

![பூட்டி ஏஜெண்டுகளை பூச்சியிலிருந்து உற்பத்திக்கு கட்டமைத்தல்](../../translated_images/ta/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 பன்மொழி ஆதரவு

#### GitHub செயல்பாடு மூலம் ஆதரிக்கப்படுகிறது (தானாகவும் எப்போதும் புதுப்பிக்கப்படும்)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](./README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **உள்ளூர் க்ளோன் செய்ய விரும்புகிறீர்களா?**
>
> இந்த களஞ்சியம் 50க்கும் மேற்பட்ட மொழி மொழிபெயர்ப்புகளை கொண்டுள்ளது, இது பதிவிறக்க அளவை பெரிதாக அதிகரிக்கிறது. மொழிபெயர்ப்புகள் இல்லாமல் க்ளோன் செய்ய sparse checkout பயன்படுத்தவும்:
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
> இது உங்களுக்குத் தேவைப்படும் எல்லாவற்றையும் அவ்வெல்லாம் மிக விரைவான பதிவிறக்கம் மூலம் வழங்குகிறது.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## AI ஏஜெண்ட் வளர்ச்சி ஆய்வுக் கட்டுப்பாடுகளின் அடிப்படைகளை கற்பிக்கும் படிப்பு

[![GitHub license](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 துவக்குதல்

இந்தப் பாடத்தில் AI ஏஜெண்டுகளை கட்டமைத்தல் மற்றும் வெளியிடல் ஆகிய அடிப்படைகள் உள்ளடக்கமாக உள்ளன.

ஒவ்வொரு பாடமும் முந்தையதை அடிப்படையாகக் கொண்டு கட்டமைக்கப்படுகின்றன, எனவே ஆரம்பத்திலிருந்து தொடங்கி முடிவுவரை முன்னேற பரிந்துரைக்கப்படுகிறது.

AI ஏஜெண்ட் தலைப்புகளை பற்றி மேலும் ஆராய விரும்பினால், [AI Agents For Beginners Course](https://aka.ms/ai-agents-beginners) ஐ பார்க்கலாம்.

### மற்ற பயனாளர்களை 만나, உங்கள் கேள்விகளுக்கு பதில் பெறுங்கள்

AI ஏஜெண்டுகளை கட்டமைப்பதில் சிக்கலாக இருந்தால் அல்லது கேள்விகள் இருந்தால், எங்கள் [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6) இல் முறைப்படுத்தப்பட்ட Discord சேனலில் சேர்ந்துகொள்ளவும்.

### உங்களுக்கு தேவைப்படும் பொருட்கள்

ஒவ்வொரு பாடத்திலும் தனித்துவமான கோடு மாதிரி உள்ளது, அதை நீங்கள் உள்ளூரில் இயக்கலாம். உங்கள் நகலை உருவாக்க [இந்த களஞ்சியத்தை fork செய்யவும்](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork).

இந்த பாடம் தற்போது கீழ்காணும் தேவைப்படும் சேவைகளைப் பயன்படுத்துகிறது:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

துவங்குவதற்கு முன் இந்த சேவைகளுக்கான 접근த்தை உறுதி செய்யவும்.

மாதிரி ஹோஸ்டிங் மற்றும் சேவைகள் தொடர்பான அதிகமான விருப்பங்கள் விரைவில் கிடைக்கும்.

## 🗃️ பாடங்கள்

| **பாடம்**         | **விளக்கம்**                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------|
| [ஏஜெண்ட் வடிவமைப்பு](./lesson-1-agent-design/README.md)       | நமது "பொருத்தப்பட்ட படைப்பாளர்" ஏஜெண்ட் பயன்பாட்டுக்கான அறிமுகம் மற்றும் திறமையான ஏஜெண்டுகளை வடிவமைப்பது எப்படி |
| [ஏஜெண்ட் வளர்ச்சி](./lesson-2-agent-development/README.md)  | Microsoft Agent Framework (MAF) பயன்படுத்தி, புதிய வளர்ச்சியாளர்களுக்கு உதவும் 3 ஏஜெண்டுகளை உருவாக்குதல்.       |
| [ஏஜெண்ட் மதிப்பீடுகள்](./lesson-3-agent-evals/README.md)  | Microsoft Foundry ஐ பயன்படுத்தி, எங்கள் AI ஏஜெண்ட்கள் எப்படி செயல்படுகின்றன என்றும் எப்படி மேம்படுத்துவது என்றும் கண்டறிதல். |
| [ஏஜெண்ட் வெளியீடு](./lesson-4-agent-deployment/README.md)   | ஹோஸ்ட்டு ஏஜெண்ட்கள் மற்றும் OpenAI Chatkit ஐ பயன்படுத்தி, AI ஏஜெண்டை உற்பத்திக்கு வெளியிடுவது எப்படி என்பதை பார்க்கவும்.       |


## 🎒 பிறபாடங்கள்

எங்கள் குழு பிற பாடங்களை உற்பத்தி செய்கிறது! இதைப் பாருங்கள்:

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
 
### முக்கிய கற்றல்
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot சீரியல்
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## பங்களிப்பு

இந்த திட்டம் பங்களிப்புகளையும் பரிந்துரைகளையும்க்களை வரவேற்கிறது. பெரும்பாலான பங்களிப்புகளுக்கு நீங்கள் பங்களிப்பு உரிமம் ஒப்புதலுக்கு (CLA) சம்மதிக்க வேண்டும் என்பதைத் தேவைப்படுத்துகிறது, இது நீங்கள் பங்களிப்பை வழங்கும் உரிமை வைத்திருப்பதாகவும் அதற்கான உரிமையை எங்களுக்குச் சொல்கிறது. விவரங்களுக்கு, பார்வையிடவும் <https://cla.opensource.microsoft.com>.

நீங்கள் புல் வேண்டுகோளை சமர்ப்பிக்கும் போதும், ஒரு CLA பாட்டு தானாகவே நீங்கள் CLA-வில் உட்பட வேண்டியதா என்பதை தீர்மானித்து, PR-ஐ சரியான முறையில் அலங்கரிக்கும் (எ.கா., நிலை பரிசோதனை, கருத்து). பாட்டின் வழங்கும் வழிமுறைகளைப் பின்பற்றுங்கள். எங்கள் CLA பயன்படுத்தும் அனைத்து ரெப்போர்களிலும் நீங்கள் இதை ஒருமுறை மட்டுமே செய்ய வேண்டும்.

இந்த திட்டம் [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)ஐ ஏற்றுக்கொண்டுள்ளது.
மேலும் தகவலுக்கு [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)யை பார்வையிடவும் அல்லது
[opencode@microsoft.com](mailto:opencode@microsoft.com) முகவரிக்கு எதுவும் கேள்விகள் அல்லது கருத்துக்களுக்காக தொடர்பு கொள்ளவும்.

## வர்த்தக அடையாளங்கள்

இந்த திட்டத்தில் திட்டங்கள், தயாரிப்புகள், அல்லது சேவைகளுக்கான வர்த்தக அடையாளங்கள் அல்லது லோகோகள் இருக்கலாம். Microsoft
வர்த்தக அடையாளங்கள் அல்லது லோகோகளை பயன்படுத்த அதிகாரப்பூர்வமாகும் போது
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)ஐ பின்பற்ற வேண்டும்.
இந்தத் திட்டத்தின் மாற்றப்பட்ட பதிப்புகளில் Microsoft வர்த்தக அடையாளங்கள் அல்லது லோகோகளைப் பயன்படுத்துவது குழப்பத்தை ஏற்படுத்தக்கூடாது அல்லது Microsoft ஆதரவாகக் காட்டக் கூடாது.
மூன்றாம் தரப்பு வர்த்தக அடையாளங்கள் அல்லது லோகோகள் பயன்படுத்தப்படும் போது அப்புறப்பட்டு அவற்றின் கொள்கைகளே பொருந்தும்.

## உதவி பெறுதல்

நீங்கள் சிக்கியிருந்தால் அல்லது AI செயலிகளை கட்டுவதில் ஏதேனும் கேள்விகள் இருந்தால், சேரவும்:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

உங்களுக்கு தயாரிப்பு கருத்துகள் அல்லது பிழைகள் இருந்தால், கட்டும்போது பார்வையிடவும்:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிப்பினும், தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்று தயவுசெய்து கவனியுங்கள். உள்ளூர் மொழியில் உள்ள அசல் ஆவணம் தான் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பை பரிந்துரைக்கிறோம். இத்தரகு மொழிபெயர்ப்பைப் பயன்படுத்தியதன் மூலம் உருவாகும் ஏதேனும் புரிதல் தவறுகளுக்கு அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பேற்காமல் இருக்கின்றோம்.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->