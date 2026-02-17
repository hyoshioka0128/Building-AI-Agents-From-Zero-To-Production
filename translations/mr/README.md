# शून्यातून उत्पादनापर्यंत AI एजंट बनवणे

![शून्यातून उत्पादनापर्यंत AI एजंट बनवणे](../../translated_images/mr/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 बहुभाषिक समर्थन

#### GitHub Action द्वारे समर्थित (स्वयंचलित आणि सदैव अद्ययावत)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अरबी](../ar/README.md) | [बांग्ला](../bn/README.md) | [बुल्गेरियन](../bg/README.md) | [बर्मी (म्यानमार)](../my/README.md) | [चीनी (सोपे केलेले)](../zh-CN/README.md) | [चीनी (परंपरागत, हॉंगकॉंग)](../zh-HK/README.md) | [चीनी (परंपरागत, मकाउ)](../zh-MO/README.md) | [चीनी (परंपरागत, तैवान)](../zh-TW/README.md) | [क्रोएशियन](../hr/README.md) | [चेक](../cs/README.md) | [डॅनिश](../da/README.md) | [डच](../nl/README.md) | [एस्टोनियन](../et/README.md) | [फिनिश](../fi/README.md) | [फ्रेंच](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिंदी](../hi/README.md) | [हंगेरीयन](../hu/README.md) | [इंडोनेशियन](../id/README.md) | [इटालियन](../it/README.md) | [जपानी](../ja/README.md) | [कन्नड](../kn/README.md) | [कोरियन](../ko/README.md) | [लिथुआनियन](../lt/README.md) | [मलय](../ms/README.md) | [मलयाळम](../ml/README.md) | [मराठी](./README.md) | [नेपाली](../ne/README.md) | [नायजेरियन पिजिन](../pcm/README.md) | [नॉर्वेजियन](../no/README.md) | [फारसी (फारसी)](../fa/README.md) | [पोलिश](../pl/README.md) | [पोर्तुगीज (ब्राझील)](../pt-BR/README.md) | [पोर्तुगीज (पोर्तुगाल)](../pt-PT/README.md) | [पंजाबी (गुरमुखी)](../pa/README.md) | [रोमानियन](../ro/README.md) | [रशियन](../ru/README.md) | [सर्बियन (सिरिलिक)](../sr/README.md) | [स्लोवाक](../sk/README.md) | [स्लोव्हेनियन](../sl/README.md) | [स्पॅनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्वीडिश](../sv/README.md) | [टॅगलॉग (फिलीपिनो)](../tl/README.md) | [तमिळ](../ta/README.md) | [तेलुगू](../te/README.md) | [थाई](../th/README.md) | [तुर्की](../tr/README.md) | [युक्रेनियन](../uk/README.md) | [उर्दू](../ur/README.md) | [व्हिएतनामी](../vi/README.md)

> **स्थानिक प्रत तयार करायची प्राधान्य देतात का?**
>
> या संग्रहात 50+ भाषांतील अनुवाद आहेत ज्यामुळे डाउनलोडचा आकार खूपच वाढतो. अनुवादांशिवाय क्लोन करण्यासाठी sparse checkout वापरा:
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
> या पध्दतीने तुम्हाला कोर्स पूर्ण करण्यासाठी सर्व काही जलद डाउनलोड होईल.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## AI एजंट विकास जीवनचक्राची मूलतत्त्वे शिकणारा कोर्स

[![GitHub परवाना](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub योगदानकर्ता](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub समस्या](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub पुल-रिक्वेस्ट](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs स्वागतार्ह](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 सुरुवात करा

हा कोर्स AI एजंट तयार करण्याच्या मूलभूत गोष्टींचे धडे देतो.

प्रत्येक धडा मागील धड्यावर आधारित आहे, त्यामुळे आम्ही सुरुवातीपासून सुरू करून शेवटपर्यंत जाण्याचा सल्ला देतो.

तुम्हाला AI एजंट विषयांबाबत अधिक जाणून घ्यायचे असल्यास, तुम्ही [AI एजंट्स फॉर बिगिनर्स कोर्स](https://aka.ms/ai-agents-beginners) तपासू शकता.

### इतर शिकणाऱ्यांना भेटा, तुमचे प्रश्न विचारा

जर तुम्हाला अडकले किंवा AI एजंट तयार करण्याबाबत काही प्रश्न असतील, तर आमच्या समर्पित Discord चॅनेलमध्ये सहभागी व्हा [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6).

### तुमच्या गरजा

प्रत्येक धड्याशी संबंधित स्वतःचा कोड नमुना आहे जो तुम्ही स्थानिकपणे रन करू शकता. तुम्ही [हा रेपो fork](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork) करून स्वतःची प्रत तयार करू शकता.

हा कोर्स सध्या खालील गोष्टी वापरतो:

- [Microsoft एजंट फ्रेमवर्क (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

कृपया हे सर्व सेव्हीचा प्रवेश तुम्ही सुरुवात करण्यापूर्वी सुनिश्चित करा.

लवकरच मॉडेल होस्टिंग आणि सेवा संदर्भातील अधिक पर्याय येणार आहेत.

## 🗃️ धडे

| **धडा**         | **वर्णन**                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------|
| [एजंट डिझाइन](./lesson-1-agent-design/README.md)       | आमच्या "डेव्हलपर ऑनबोर्डिंग" एजंट वापर प्रकरणाची ओळख आणि प्रभावी एजंट कसे डिझाइन करावे   |
| [एजंट विकास](./lesson-2-agent-development/README.md)  | Microsoft एजंट फ्रेमवर्क (MAF) वापरून नवीन डेव्हलपरना ऑनबोर्ड करण्यासाठी ३ एजंट तयार करा.       |
| [एजंट मूल्यांकन](./lesson-3-agent-evals/README.md)  | Microsoft Foundry वापरून, आमच्या AI एजंट्सची कामगिरी कशी आहे आणि त्यांना कसे सुधारावे ते पाहा. |
| [एजंट तैनाती](./lesson-4-agent-deployment/README.md)   | Hosted Agents आणि OpenAI Chatkit वापरून, AI एजंट उत्पादनात कसा तैनात करायचा ते पाहा.      |


## 🎒 इतर कोर्सेस

आमचा संघ इतर कोर्सेस तयार करतो! तपासा:

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
 
### कोअर लर्निंग
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### कॉपायलट मालिका
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## योगदान

हा प्रकल्प योगदान आणि सूचना स्वागत करतो. बहुतांश योगदानांसाठी आपल्याला एक
कॉण्ट्रिब्युटर परवाना करार (CLA) सहमत होणे आवश्यक आहे, ज्यात आपण आपल्याकडे योगदानाचा अधिकार असल्याची आणि प्रत्यक्षात आम्हाला
आपल्या योगदानाचा वापर करण्याचा अधिकार दिला आहे असे घोषित करता. तपशीलांसाठी, भेट द्या <https://cla.opensource.microsoft.com>.

जेव्हा आपण पुल विनंती सबमिट करता, तेव्हा एका CLA बॉटद्वारे आपल्याला CLA प्रदान करणे आवश्यक आहे की नाही हे आपोआप ठरवले जाईल
आणि PR योग्यरित्या सजवले जाईल (उदा. स्थिती तपासणी, टिप्पण्या). बॉटने दिलेल्या सूचनांचे पालन करा. आपल्या सर्व रेपॉसाठी आपल्याला हे फक्त एकदाच करावे लागेल ज्यात आमचा CLA वापरला जातो.

हा प्रकल्प Microsoft Open Source Code of Conduct स्वीकारला आहे.
अधिक माहितीसाठी, [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) पहा किंवा अधिक प्रश्न किंवा टिप्पण्या असल्यास [opencode@microsoft.com](mailto:opencode@microsoft.com) वर संपर्क करा.

## ट्रेडमार्क

हा प्रकल्प प्रकल्प, उत्पादने किंवा सेवा यासाठी ट्रेडमार्क किंवा लोगो असू शकतो. Microsoft ट्रेडमार्क
किंवा लोगोचा अधिकृत वापर खालील अधीन आहे आणि त्या नियमांनुसार असावा
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
या प्रकल्पाच्या सुधारित आवृत्त्यांमध्ये Microsoft ट्रेडमार्क किंवा लोगोचा वापर गुंतागुंत निर्माण करू नये किंवा Microsoft प्रायोजकत्व सूचित करू नये.
तृतीय पक्ष ट्रेडमार्क किंवा लोगोचा वापर त्या तृतीय पक्षाच्या धोरणांनुसार असावा.

## मदत मिळवा

जर आपण अडकले किंवा AI अॅप्स बनवण्याबाबत काही प्रश्न असतील, तर सहभागी व्हा:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

आपल्याकडे उत्पादन अभिप्राय किंवा चुकांसाठी:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करीत असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चूका किंवा असत्यता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाची माहितीकरिता व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थांसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->