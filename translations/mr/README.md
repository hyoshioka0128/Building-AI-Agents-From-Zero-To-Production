# शून्यापासून उत्पादनासाठी AI एजंट तयार करणे

![शून्यापासून उत्पादनासाठी AI एजंट तयार करणे](../../translated_images/mr/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 बहुभाषिक समर्थन

#### GitHub Action द्वारे समर्थित (स्वयंचलित आणि नेहमी अद्यतनित)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अरेबिक](../ar/README.md) | [बंगाली](../bn/README.md) | [बल्गेरियन](../bg/README.md) | [बर्मीज (म्यानमार)](../my/README.md) | [चायनीज (सामान्यीकृत)](../zh-CN/README.md) | [चायनीज (परंपरागत, हॉंग कॉंग)](../zh-HK/README.md) | [चायनीज (परंपरागत, मकाऊ)](../zh-MO/README.md) | [चायनीज (परंपरागत, तैवान)](../zh-TW/README.md) | [क्रोएशियन](../hr/README.md) | [चेक](../cs/README.md) | [डॅनिश](../da/README.md) | [डच](../nl/README.md) | [एस्टोनियन](../et/README.md) | [फिनिश](../fi/README.md) | [फ्रेंच](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिंदी](../hi/README.md) | [हंगेरीयन](../hu/README.md) | [इंडोनेशियन](../id/README.md) | [इटालियन](../it/README.md) | [जपानी](../ja/README.md) | [कन्नड](../kn/README.md) | [खмер](../km/README.md) | [कोरियन](../ko/README.md) | [लिथुआनीयन](../lt/README.md) | [मलय](../ms/README.md) | [मल्याळम](../ml/README.md) | [मराठी](./README.md) | [नेपाळी](../ne/README.md) | [नायजेरियन पिद्गिन](../pcm/README.md) | [नॉर्वेजियन](../no/README.md) | [फारसी (पर्शियन)](../fa/README.md) | [पोलिश](../pl/README.md) | [पोर्तुगिज (ब्राझील)](../pt-BR/README.md) | [पोर्तुगिज (पोर्तुगाल)](../pt-PT/README.md) | [पंजाबी (गुरमुखी)](../pa/README.md) | [रोमेनियन](../ro/README.md) | [रशियन](../ru/README.md) | [सर्बियन (सिरिलिक)](../sr/README.md) | [स्लोवाक](../sk/README.md) | [स्लोव्हेनियन](../sl/README.md) | [स्पॅनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्विडिश](../sv/README.md) | [टागालॉग (फिलिपिनो)](../tl/README.md) | [तमिळ](../ta/README.md) | [तेलुगू](../te/README.md) | [थाई](../th/README.md) | [तुर्की](../tr/README.md) | [युक्रेनियन](../uk/README.md) | [उर्दू](../ur/README.md) | [व्हिएतनामीज](../vi/README.md)

> **स्थानिक क्लोन करणे प्राधान्य द्यायचे आहे?**
>
> या रिपॉझिटरीमध्ये 50+ भाषांमध्ये भाषांतर केलेले आहे ज्यामुळे डाउनलोड आकार लक्षणीय वाढतो. भाषांतरांशिवाय क्लोन करण्यासाठी sparse checkout वापरा:
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
> हे आपल्याला आवश्यक असलेली सर्व काही देतो, ज्यामुळे कोर्स पूर्ण करण्यासाठी डाउनलोड तुलनेत जलद होते.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## AI एजंट विकास जीवनचक्राच्या मूलभूत तत्त्वांचे शिक्षण देणारा कोर्स

[![GitHub परवाना](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub योगदानकर्ता](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub समस्या](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub पुल-रिक्वेस्ट](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs स्वागतार्ह](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 सुरुवात कशी करावी

हा कोर्स AI एजंट तयार करण्याच्या आणि तैनात करण्याच्या मूलभूत गोष्टींची शिकवण देतो.

प्रत्येक धडा मागील धड्यावर आधारित असतो, त्यामुळे आम्ही शिफारस करतो की सुरुवातीपासून प्रारंभ करा आणि शेवटपर्यंत क्रमवार जा.

जर तुम्हाला AI एजंट विषयांची अधिक माहिती घ्यायची असेल, तर तुम्ही [AI Agents For Beginners Course](https://aka.ms/ai-agents-beginners) पाहू शकता.

### इतर शिकणाऱ्यांना भेटा, आपले प्रश्न भरतकाल उत्तर मिळवा

जर तुम्ही अडकलात किंवा एखाद्या AI एजंट तयार करण्याबाबत कोणतीही प्रश्न असतील तर, आमच्या समर्पित Discord चॅनलमध्ये सहभागी व्हा:[Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6).

### आपल्याला काय लागेल

प्रत्येक धड्यामागे त्याचा स्वतःचा कोड नमुना असतो जो तुम्ही स्थानिकपणे चालवू शकता. तुम्ही [हा रिपॉझिटरी फोर्क करू शकता](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork) आणि स्वतःची प्रत तयार करू शकता.

हा कोर्स सध्या खालील गोष्टी वापरतो:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI सेवा](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

कृपया सुरू करण्यापूर्वी आपल्या कडे या सेवांची प्रवेश असणे सुनिश्चित करा.

मॉडेल होस्टिंग आणि सेवा संदर्भातील अधिक पर्याय लवकरच येत आहेत.

## 🗃️ धडे

| **धडा**              | **वर्णन**                                                                                          |
|--------------------|--------------------------------------------------------------------------------------------------|
| [एजंट डिझाइन](./lesson-1-agent-design/README.md)         | "डेव्हलपर ऑनबोर्डिंग" एजंट युज केसचे परिचय आणि प्रभावी एजंट डिझाइन कसे करावे                       |
| [एजंट डेव्हलपमेंट](./lesson-2-agent-development/README.md)  | Microsoft Agent Framework (MAF) वापरून, नवीन डेव्हलपरना ऑनबोर्ड करण्यासाठी 3 एजंट तयार करा       |
| [एजंट मूल्यमापन](./lesson-3-agent-evals/README.md)       | Microsoft Foundry वापरून, आमचे AI एजंट किती चांगले कार्य करत आहेत आणि त्यांना कसे सुधारावे ते जाणून घ्या. |
| [एजंट तैनाती](./lesson-4-agent-deployment/README.md)        | Hosted Agents आणि OpenAI Chatkit चा वापर करून AI एजंट उत्पादनात कसा तैनात करायचा ते पाहा               |


## 🎒 इतर कोर्सेस

आमचा संघ इतर कोर्सेसही तयार करतो! पाहा:

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
 
### मुख्य शिक्षण 
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![नवशिकासाठी डेटा सायन्स](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![नवशिकासाठी एआय](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![नवशिकासाठी सायबरसुरक्षा](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![नवशिकासाठी वेब डेव्हलपमेंट](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![नवशिकासाठी IoT](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![नवशिकासाठी XR विकास](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### कोपायलट मालिका
[![एआय जोडलेल्या प्रोग्रामिंगसाठी कोपायलट](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET साठी कोपायलट](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![कोपायलट साहस](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## सहकार्य करणे

हा प्रकल्प योगदान आणि सूचना स्वीकारतो. बहुतेक योगदानासाठी तुम्हाला Contributor License Agreement (CLA) स्वीकारावे लागते ज्यात तुम्ही दावा करता की तुम्हाला तुमचे योगदान वापरण्याचा अधिकार आहे आणि प्रत्यक्षात तुम्ही त्यास परवानगी देता. तपशीलासाठी, भेट द्या <https://cla.opensource.microsoft.com>.

जेव्हा तुम्ही पुल विनंती सादर करता, तेव्हा CLA बॉट आपोआप ठरवेल की तुम्हाला CLA देणे आवश्यक आहे का आणि पुल विनंती योग्य प्रकारे देखावे (उदा., स्थिती तपासणी, टिप्पण्या). फक्त बॉटने दिलेल्या सूचना अनुसरा. आमच्या CLA वापरणाऱ्या सर्व रेपॉमध्ये तुम्हाला हे एकदाच करावे लागेल.

हा प्रकल्प [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) स्वीकारतो.
अधिक माहितीसाठी [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) पाहा किंवा 
[opencode@microsoft.com](mailto:opencode@microsoft.com) वर अतिरिक्त प्रश्न किंवा टिप्पणींसाठी संपर्क करा.

## ट्रेडमार्क

या प्रकल्पात प्रकल्प, उत्पादने किंवा सेवा यांचे ट्रेडमार्क किंवा लोगो असू शकतात. Microsoft ट्रेडमार्क किंवा लोगोचा अधिकृत वापर [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) च्या अधीन आहे आणि त्यांचे पालन करणे आवश्यक आहे.
Microsoft ट्रेडमार्क किंवा लोगोचा या प्रकल्पाच्या बदललेल्या आवृत्त्यांसह वापर केल्यास गोंधळ किंवा Microsoft च्या प्रायोजकत्वाचा अर्थ लावू नये.
तृतीय पक्षाच्या ट्रेडमार्क किंवा लोगोचा कोणताही वापर त्या तृतीय पक्षांच्या धोरणांनुसार होईल.

## मदत मिळवा

जर तुम्हाला अडचण आली किंवा AI अॅप्स तयार करण्याबाबत काही प्रश्न असतील, तर या लिंकवर सामील व्हा:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

तुमच्याकडे उत्पादनाबाबत अभिप्राय किंवा त्रुटी असल्यास, या लिंकवर भेट द्या:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये त्रुटी किंवा अचूकतेच्या समस्या असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाच्या वापरामुळे होणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थग्रहणांसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->