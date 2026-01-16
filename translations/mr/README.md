<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b09df38b3188ffe957c7ac8b055967f5",
  "translation_date": "2026-01-16T08:40:17+00:00",
  "source_file": "README.md",
  "language_code": "mr"
}
-->
# शून्यापासून उत्पादनापर्यंत एआय एजंट तयार करणे

![शून्यापासून उत्पादनापर्यंत एआय एजंट तयार करणे](../../../../translated_images/mr/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 बहुभाषिक समर्थन

#### GitHub Action द्वारे समर्थित (स्वयंचलित आणि सदैव अद्ययावत)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](./README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **स्थानिकरित्या क्लोन करणे प्राधान्य द्यायचे आहे?**

> या रेपॉजिटरीमध्ये ५०+ भाषांतील अनुवादांचा समावेश आहे ज्यामुळे डाउनलोडचा आकार मोठा होतो. अनुवादांशिवाय क्लोन करण्यासाठी sparse checkout वापरा:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> यामुळे कोर्स पूर्ण करण्यासाठी आपल्याला आवश्यक असलेले सर्व काही मिळते, आणि डाउनलोड खूप वेगाने होते.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## एआय एजंट विकास जीवनचक्राच्या मूलभूत गोष्टी शिकवणारा कोर्स

[![GitHub license](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 सुरुवात करणे

हा कोर्स एआय एजंट तयार करण्याच्या आणि तैनात करण्याच्या मूलभूत गोष्टी शिकवतो.

प्रत्येक धडा मागील धड्यावर आधारित आहे, त्यामुळे आम्ही सुरुवातीपासून सुरू करून शेवटपर्यंत पुढे जाण्याचा सल्ला देतो.

जर तुम्हाला एआय एजंट विषयांबद्दल अधिक जाणून घ्यायचे असेल, तर तुम्ही [AI Agents For Beginners Course](https://aka.ms/ai-agents-beginners) पाहू शकता.

### इतर शिकणाऱ्यांशी भेटा, आपले प्रश्न विचारा

जर तुम्हाला अडचण आली किंवा एआय एजंट तयार करण्याबद्दल कोणतेही प्रश्न असतील, तर आमच्या समर्पित Discord चॅनेलमध्ये [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6) मध्ये सामील व्हा.

### आपल्याला काय हवे आहे

प्रत्येक धड्यात त्याचा स्वतःचा कोड नमुना असतो ज्याला आपण स्थानिकरित्या चालवू शकता. आपली स्वतःची प्रत तयार करण्यासाठी आपण [हा रेपॉजिटरी fork करू शकता](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork).

हा कोर्स सध्या खालील गोष्टी वापरतो:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

कृपया सुरूवात करण्यापूर्वी आपल्याला या सेवा उपलब्ध आहेत याची खात्री करा.

मॉडेल होस्टिंग आणि सेवा यासंबंधी अधिक पर्याय लवकरच येत आहेत.

## 🗃️ धडे

| **धडा**           | **वर्णन**                                                                          |
|--------------------|-----------------------------------------------------------------------------------|
| [Agent Design](./lesson-1-agent-design/README.md)       | आमच्या "डिव्हलपर ऑनबोर्डिंग" एजंट वापर प्रकरणाची ओळख आणि प्रभावी एजंट कसे डिझाइन करायचे  |
| [Agent Development](./lesson-2-agent-development/README.md)  | Microsoft Agent Framework (MAF) वापरून, नवीन डेव्हलपर ऑनबोर्ड करण्यासाठी ३ एजंट तयार करा |
| [Agent Evaluations](./lesson-3-agent-evals/README.md)  | Microsoft Foundry वापरून, आमचे एआय एजंट किती चांगले काम करीत आहेत आणि त्यांना कसे सुधारायचे हे शोधा  |
| [Agent Deployment](./lesson-4-agent-deployment/README.md)   | Hosted Agents आणि OpenAI Chatkit वापरून, एखाद्या AI एजंटला उत्पादनात कसे तैनात करायचे पाहा |

## 🎒 इतर कोर्सेस

आमचा संघ इतर कोर्सेस देखील तयार करतो! पाहा:

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
 
### मुख्य शिक्षण
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![सुरक्षा सुरुवातीसाठी](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![वेब डेव्हलपमेंट सुरुवातीसाठी](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT सुरुवातीसाठी](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR डेव्हलपमेंट सुरुवातीसाठी](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### कॉपायलेट मालिका
[![AI जुळलेल्या प्रोग्रामिंगसाठी कॉपायलेट](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET साठी कॉपायलेट](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![कॉपायलेट साहस](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## योगदान देणे

हा प्रकल्प योगदान आणि सूचना स्वागत करतो. बहुतेक योगदानांसाठी आपण एका
योगदानकर्ता परवाना कराराला (CLA) सहमत होणे आवश्यक आहे जो घोषित करतो की आपल्याकडे अधिकार आहे, आणि प्रत्यक्षात आपण आमच्याकडे
आपले योगदान वापरण्याचा अधिकार दिला आहे. तपशीलांसाठी, भेट द्या <https://cla.opensource.microsoft.com>.

जेव्हां आपण पुल विनंती सादर करता, CLA बॉट आपोआपच ठरवेल की तुम्हाला CLA प्रदान करणे आवश्यक आहे की नाही
आणि योग्यरित्या PR ला सजवेल (उदा., स्थिती पडताळणी, टिप्पणी). फक्त बॉटद्वारे दिलेल्या सूचनांचे पालन करा.
आपल्याला हे सर्व रेपॉजिटरीजवर एकदाच करावे लागेल जे आमच्या CLA चा वापर करतात.

या प्रकल्पाने [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) स्वीकारला आहे.
अधिक माहितीसाठी पाहा [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) किंवा
[opencode@microsoft.com](mailto:opencode@microsoft.com) कडे कोणतेही अतिरिक्त प्रश्न किंवा टिप्पण्या पाठवा.

## ट्रेडमार्क

हा प्रकल्प प्रकल्पांसाठी, उत्पादनांसाठी, किंवा सेवांसाठी ट्रेडमार्क किंवा लोगो असू शकतो. Microsoft चे
ट्रेडमार्क किंवा लोगो अधिकृत वापर Microsoft च्या
[ट्रेडमार्क आणि ब्रँड मार्गदर्शक तत्त्वे](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) नुसार असणे आवश्यक आहे.
या प्रकल्पाच्या बदलेल्या आवृत्त्यांमध्ये Microsoft ट्रेडमार्क किंवा लोगोचा वापर गोंधळ निर्माण करू नये किंवा Microsoft चा प्रायोजक असल्याचा भास होऊ नये.
तृतीय पक्ष ट्रेडमार्क किंवा लोगोचा वापर त्या तृतीय पक्षाच्या धोरणांवर अवलंबून आहे.

## मदत मिळवा

आपण अडकलात किंवा AI अॅप्स तयार करताना कोणतेही प्रश्न असल्यास, सामील व्हा:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

जर आपल्याकडे उत्पादनाबाबत अभिप्राय किंवा त्रुटी असतील तर येथे भेट द्या:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**इंगित**:
हा दस्तऐवज कृत्रिम बुद्धिमत्ता अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये त्रुटी किंवा चुकीची माहिती असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानावा. महत्त्वाची माहिती साठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे झालेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलावासाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->