# शून्यापासून उत्पादनापर्यंत AI एजंट तयार करणे

![शून्यापासून उत्पादनापर्यंत AI एजंट तयार करणे](../../translated_images/mr/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 बहुभाषिक समर्थन

#### GitHub Action द्वारे समर्थित (स्वयंचलित आणि नेहमी अद्ययावत)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अरेबिक](../ar/README.md) | [बंगाली](../bn/README.md) | [बल्गेरियन](../bg/README.md) | [बर्मिज (म्यानमार)](../my/README.md) | [चिनी (सोपे)](../zh-CN/README.md) | [चिनी (परंपरागत, हॉंगकॉंग)](../zh-HK/README.md) | [चिनी (परंपरागत, मकाऊ)](../zh-MO/README.md) | [चिनी (परंपरागत, तैवान)](../zh-TW/README.md) | [क्रोएशियन](../hr/README.md) | [चेक](../cs/README.md) | [डॅनीश](../da/README.md) | [डच](../nl/README.md) | [एस्टोनियन](../et/README.md) | [फिनिश](../fi/README.md) | [फ्रेंच](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिंदी](../hi/README.md) | [हंगेरियन](../hu/README.md) | [इंडोनेशियन](../id/README.md) | [इटालियन](../it/README.md) | [जपानी](../ja/README.md) | [कन्नड](../kn/README.md) | [कोरियन](../ko/README.md) | [लिथुव्हनियन](../lt/README.md) | [मल्याळम](../ml/README.md) | [मराठी](./README.md) | [नेपाली](../ne/README.md) | [नायजेरियन पिजिन](../pcm/README.md) | [नॉर्वेजियन](../no/README.md) | [फारसी (पर्शियन)](../fa/README.md) | [पोलिश](../pl/README.md) | [पोर्तुगाल (ब्राझील)](../pt-BR/README.md) | [पोर्तुगाल (पोर्तुगाल)](../pt-PT/README.md) | [पंजाबी (गुरमुखी)](../pa/README.md) | [रोमानियन](../ro/README.md) | [रशियन](../ru/README.md) | [सर्बियन (सिरिलीक)](../sr/README.md) | [स्लोव्हाक](../sk/README.md) | [स्लोव्हेनियन](../sl/README.md) | [स्पॅनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्वीडिश](../sv/README.md) | [टॅगलॉग (फिलीपिनो)](../tl/README.md) | [तमिळ](../ta/README.md) | [तेलुगू](../te/README.md) | [थाई](../th/README.md) | [तुर्किश](../tr/README.md) | [युक्रेनीयन](../uk/README.md) | [उर्दू](../ur/README.md) | [व्हिएतनामी](../vi/README.md)

> **स्थानिक रीतीने क्लोन करणे प्राधान्य देता?**

> या रिपॉझिटरीमध्ये ५०+ भाषा अनुवाद समाविष्ट आहेत ज्यामुळे डाउनलोड आकार मोठा होतो. अनुवादांशिवाय क्लोन करण्यासाठी sparse checkout वापरा:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> हे तुम्हाला कोर्स पूर्ण करण्यासाठी आवश्यक सर्व काही जलद डाउनलोडसह देते.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## AI एजंट विकासाच्या जीवनचक्राच्या मूलभूत तत्त्वे शिकवणारा कोर्स

[![GitHub परवाना](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub योगदानकर्ता](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub समस्या](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub पुल-रिक्वेस्ट्स](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs स्वागत आहे](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 सुरुवात

हा कोर्स AI एजंट तयार करणे आणि तैनात करण्याच्या मूलभूत तत्त्वांवर आधारित आहे.

प्रत्येक धडा मागील धड्यावर आधारित आहे, त्यामुळे प्रारंभापासून सुरुवात करणे आणि शेवटपर्यंत काम करण्याची शिफारस केली जाते.

तुम्हाला AI एजंट विषयांबद्दल अधिक जाणून घ्यायचे असल्यास, तुम्ही [AI एजंट्स फॉर बिगिनर्स कोर्स](https://aka.ms/ai-agents-beginners) पाहू शकता.

### इतर शिक्षणार्थींशी भेटा, तुमचे प्रश्न विचारा

जर तुम्हाला अडचण आली किंवा AI एजंट तयार करण्याबाबत काही प्रश्न असतील, तर आमच्या समर्पित Discord चॅनेलमध्ये सहभागी व्हा [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6).

### तुम्हाला काय आवश्यक आहे

प्रत्येक धड्यामध्ये वेगळा कोड नमुना आहे ज्याला तुम्ही स्थानिकरित्या चालवू शकता. तुम्ही [हा repo fork करू शकता](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork) तुमची स्वतःची कॉपी तयार करण्यासाठी.

हा कोर्स सध्या खालील गोष्टी वापरतो:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

कृपया सुरुवात करण्यापूर्वी या सेवा वापरण्याचा अधिकार असल्याची खात्री करा.

मॉडेल होस्टिंग आणि सेवा याबाबत आणखी पर्याय लवकरच येत आहेत. 

## 🗃️ धडे

| **धडा**           | **वर्णन**                                                                                          |
|--------------------|--------------------------------------------------------------------------------------------------|
| [एजंट डिझाइन](./lesson-1-agent-design/README.md)       | आमच्या "डिव्हलपर ऑनबोर्डिंग" एजंट वापर प्रकरणाची ओळख आणि प्रभावी एजंट कसे डिझाइन करायचे त्याविषयी |
| [एजंट विकास](./lesson-2-agent-development/README.md)  | Microsoft Agent Framework (MAF) वापरून नवीन डिव्हलपर ऑनबोर्डिंगसाठी ३ एजंट तयार करा.          |
| [एजंट मूल्यमापन](./lesson-3-agent-evals/README.md)    | Microsoft Foundry वापरून आमचे AI एजंट कसे काम करत आहेत ते तपासा आणि सुधारणा कशी करावी ते शिका.  |
| [एजंट तैनाती](./lesson-4-agent-deployment/README.md)   | होस्टेड एजंट आणि OpenAI Chatkit वापरून AI एजंट उत्पादनात कसा तैनात करायचा हे पाहा.               |


## 🎒 इतर कोर्सेस

आमच्या टीमकडून इतरही कोर्सेस तयार केले गेले आहेत! पाहा:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j फॉर बिगिनर्स](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js फॉर बिगिनर्स](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain फॉर बिगिनर्स](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD फॉर बिगिनर्स](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI फॉर बिगिनर्स](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP फॉर बिगिनर्स](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI एजंट्स फॉर बिगिनर्स](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### जनरेटिव AI सिरीज
[![जनरेटिव AI फॉर बिगिनर्स](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![जनरेटिव AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![जनरेटिव AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![जनरेटिव AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### कोअर शिक्षण
[![ML फॉर बिगिनर्स](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![डेटा सायन्स फॉर बिगिनर्स](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![सुरुवातीसाठी AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![सुरुवातीसाठी सायबरसुरक्षा](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![सुरुवातीसाठी वेब डेव](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![सुरुवातीसाठी IoT](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![सुरुवातीसाठी XR डेव्हलपमेंट](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### कॉपायलट मालिका
[![AI जोडलेल्या प्रोग्रामिंगसाठी Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET साठी Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot साहस](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## योगदान देणे

हा प्रकल्प योगदान आणि सूचना स्वीकारतो. बहुतेक योगदानांसाठी आपल्याला एक 
Contributor License Agreement (CLA) वर सहमत व्हावे लागते ज्यात आपण आपल्या योगदानाचा वापर करण्यासाठी आम्हाला अधिकार दिले असल्याचे घोषित करता. तपशीलांसाठी, भेट द्या <https://cla.opensource.microsoft.com>.

जेव्हा आपण पुल विनंती सादर करता, तेव्हा CLA बॉट आपोआप ठरवेल की आपल्याला CLA प्रदान करणे आवश्यक आहे की नाही आणि PR योग्य प्रकारे (उदा., स्थिती तपासणी, टिप्पणी) साजरे करेल. फक्त बॉटने दिलेल्या सूचनांचे अनुसरण करा. हा कार्य एकदा केल्यावर आपल्या सर्व रेपॉइतून हा प्रक्रिया करावी लागणार नाही.

या प्रकल्पाने [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) स्वीकारले आहे.
अधिक माहितीसाठी [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) पहा किंवा 
कांही अतिरिक्त प्रश्न किंवा टिप्पण्या असतील तर [opencode@microsoft.com](mailto:opencode@microsoft.com) वर संपर्क करा.

## ट्रेडमार्क्स

हा प्रकल्प प्रकल्प, उत्पादनं किंवा सेवा यांचे ट्रेडमार्क किंवा लोगो असू शकतात. Microsoft
ट्रेडमार्क्स किंवा लोगोचा अधिकृत वापर हा
[Microsoft च्या ट्रेडमार्क आणि ब्रँड मार्गदर्शक तत्त्वांचे](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) पालन करणे आवश्यक आहे.
या प्रकल्पाच्या सुधारित आवृत्त्यांमध्ये Microsoft ट्रेडमार्क किंवा लोगोचा वापर केल्यास गोंधळ होऊ नये किंवा Microsoft च्या प्रायोजकत्वाचा संकेत दिला जाऊ नये.
किंवा तृतीय-पक्ष ट्रेडमार्क्स किंवा लोगोचा वापर त्या तृतीय-पक्षांच्या धोरणांच्या अधीन आहे.

## मदत मिळवणे

जर तुम्ही अडकले असाल किंवा AI अ‍ॅप्स तयार करताना कोणतेही प्रश्न असतील, तर येथे सामील व्हा:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

जर तुम्हाला उत्पादनावर अभिप्राय द्यायचा असेल किंवा बांधणी करताना त्रुटी आढळल्या तर भेट द्या:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**सूचना**:
हा दस्तऐवज AI अनुवाद सेवेचा वापर करून अनुवादित केला गेला आहे [Co-op Translator](https://github.com/Azure/co-op-translator). आम्ही अचूकतेसाठी प्रयत्नशील आहोत, परंतु कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा गैरसमज असू शकतात. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाची माहिती असल्यास व्यावसायिक मानव अनुवाद शिफारसीय आहे. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->