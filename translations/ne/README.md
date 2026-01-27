<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b09df38b3188ffe957c7ac8b055967f5",
  "translation_date": "2026-01-16T08:41:22+00:00",
  "source_file": "README.md",
  "language_code": "ne"
}
-->
# शून्यदेखि उत्पादनसम्म AI एजेन्ट निर्माण

![शून्यदेखि उत्पादनसम्म AI एजेन्ट निर्माण](../../../../translated_images/ne/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 बहुभाषी समर्थन

#### GitHub Action मार्फत समर्थित (स्वचालित र सधैं अद्यावधिक)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](./README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **स्थानीय रूपमा क्लोन गर्न चाहनुहुन्छ?**

> यस भण्डारणमा ५०+ भाषाहरूको अनुवादहरू समावेश छन् जसले डाउनलोड आकारलाई महत्वपूर्ण रूपमा बढाउँछ। अनुवादहरू बिना क्लोन गर्न, sparse checkout प्रयोग गर्नुहोस्:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> यसले तपाईंलाई पाठ्यक्रम पूरा गर्न आवश्यक सबै कुरा द्रुत डाउनलोडको साथ प्रदान गर्दछ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## AI एजेन्ट विकास चक्रका आधारभूत कुरा सिकाउने पाठ्यक्रम

[![GitHub license](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 सुरु गर्ने

यस पाठ्यक्रममा AI एजेन्टहरूको निर्माण र परिनियोजनका आधारभूत विषयहरू कभर गरिन्छ।

हरेक पाठले अघिल्लो पाठमा निर्माण हुन्छ, त्यसैले सुरुबाट सुरु गरेर अन्तसम्म काम गर्ने सल्लाह दिइन्छ।

यदि तपाईँ AI एजेन्ट विषयहरूमा थप अन्वेषण गर्न चाहनुहुन्छ भने, तपाईँले [AI Agents For Beginners Course](https://aka.ms/ai-agents-beginners) जाँच गर्न सक्नुहुन्छ।

### अन्य विद्यार्थीहरूलाई भेट्नुहोस्, तपाईँका प्रश्नहरूको जवाफ पाउनुहोस्

यदि तपाईँ अड्किनुभयो वा AI एजेन्टहरू निर्माण गर्ने कुनै प्रश्न भएमा, हाम्रो समर्पित Discord च्यानल [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6) मा सामेल हुनुहोस्।

### के आवश्यक छ

हरेक पाठसँग आफ्नो कोड नमूना हुन्छ जुन तपाईँ स्थानीय रूपमा चलाउन सक्नुहुन्छ। तपाईँ [यस रिपो फोर्क](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork) गरी आफ्नो प्रतिलिपि बनाउन सक्नुहुन्छ।

यस पाठ्यक्रमले हाल निम्न प्रयोग गर्दछ:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

सुरु गर्नु अघि कृपया यी सेवाहरूमा पहुँच भएको सुनिश्चित गर्नुहोस्।

मोडेल होस्टिङ र सेवाहरूका वरिपरि थप विकल्पहरू छिट्टै आउँदैछन्।

## 🗃️ पाठहरू

| **पाठ**         | **विवरण**                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------|
| [एजेन्ट डिजाइन](./lesson-1-agent-design/README.md)       | हाम्रो "Developer Onboarding" एजेन्ट प्रयोग केस र प्रभावकारी एजेन्टहरू कसरी डिजाइन गर्ने परिचय  |
| [एजेन्ट विकास](./lesson-2-agent-development/README.md)  | Microsoft Agent Framework (MAF) प्रयोग गरी नयाँ विकासकर्ताहरूलाई सहयोग गर्न ३ एजेन्टहरू बनाउने।       |
| [एजेन्ट मूल्याङ्कन](./lesson-3-agent-evals/README.md)  | Microsoft Foundry प्रयोग गरी हाम्रो AI एजेन्टहरू कति राम्रो प्रदर्शन गर्दैछन् र तिनीहरूलाई कसरी सुधार गर्ने पत्ता लगाउने। |
| [एजेन्ट परिनियोजन](./lesson-4-agent-deployment/README.md)   | Hosted Agents र OpenAI Chatkit प्रयोग गरी AI एजेन्टलाई उत्पादनमा कसरी तैनाथ गर्ने।       |


## 🎒 अन्य पाठ्यक्रमहरू

हाम्रो टीमले अन्य पाठ्यक्रमहरू उत्पादन गर्छ! यहाँ जाँच गर्नुहोस्:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / एजेन्टहरू
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI श्रृंखला
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### कोर सिकाइ
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![साइबरसुरक्षा बिगिनर्सका लागि](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![वेब विकास बिगिनर्सका लागि](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![आईओटी बिगिनर्सका लागि](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![एक्सआर विकास बिगिनर्सका लागि](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### कोपाइलट सिरिज
[![एआई पेयर्ड प्रोग्रामिङका लागि कोपाइलट](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET का लागि कोपाइलट](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![कोपाइलट एड्भेञ्चर](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## योगदान

यो परियोजनाले योगदान र सुझावहरूलाई स्वागत गर्दछ। अधिकांश योगदानहरूका लागि तपाईंले
कन्ट्रीब्युटर लाइसेन्स सम्झौता (CLA) सँग सहमत हुनुपर्ने हुन्छ जसले तपाईंलाई अधिकार दिन्छ,
र साँच्चिकै दिनुहुन्छ, हामीलाई तपाइँको योगदान प्रयोग गर्ने अधिकार। विवरणका लागि, कृपया <https://cla.opensource.microsoft.com> मा जानुहोस्।

जब तपाईं पुल अनुरोध पठाउनुहुन्छ, CLA बोटले स्वचालित रूपमा निर्धारण गर्नेछ कि तपाईंलाई CLA प्रदान गर्न आवश्यक छ र अनुरोधलाई उपयुक्त रूपमा चिन्हित गर्नेछ (जस्तै, स्थिति जाँच, टिप्पणी)। बोटले दिएको निर्देशनहरू पालना गर्नुहोस्। तपाईंले हामीले प्रयोग गर्ने सबै रिपोजमा एकपटक मात्र यस्तो गर्नु पर्नेछ।

यस परियोजनाले [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) अपनाएको छ।
थप जानकारीको लागि [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) हेर्नुहोस् वा
कुनै पनि थप प्रश्न वा टिप्पणीका लागि [opencode@microsoft.com](mailto:opencode@microsoft.com) लाई सम्पर्क गर्नुहोस्।

## ट्रेडमार्कहरू

यस परियोजनाले परियोजनाहरू, उत्पादनहरू, वा सेवाहरूका लागि ट्रेडमार्क वा लोगोहरू समावेश गर्न सक्छ। माइक्रोसफ्ट ट्रेडमार्कहरू वा लोगोहरूको प्राधिकृत प्रयोग
माइक्रोसफ्टका [Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) लाई पालन
गर्नुपर्छ। यस परियोजनाको परिमार्जित संस्करणहरूमा माइक्रोसफ्ट ट्रेडमार्क वा लोगोहरूको प्रयोगले भ्रम पैदा हुनु हुँदैन वा माइक्रोसफ्टको प्रायोजन जनाउनु हुँदैन।
तृतीय-पक्ष ट्रेडमार्क वा लोगोहरूको कुनै पनि प्रयोग ति तृतीय-पक्षहरूको नीतिहरूको अधीन हुनेछ।

## सहायता प्राप्त गर्नुहोस्

यदि तपाईं अड्किनुभयो वा एआई एपहरू निर्माण गर्दा कुनै प्रश्न छ भने, सहभागी होइन्:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

यदि तपाईंले उत्पादन प्रतिक्रिया वा निर्माण गर्दा त्रुटिहरू देख्नुभयो भने, भिजिट गर्नुहोस्:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं भने पनि, कृपया बुझ्नुहोस् कि स्वतः अनुवादमा त्रुटिहरू वा कुनै अकुराकताहरू हुन सक्छन्। मूल भाषामा रहेको दस्तावेजलाई अधिकारिक स्रोतको रूपमा ग्रहण गर्नुपर्नेछ। महत्त्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा भ्रमका लागि हामी कुनै उत्तरदायी हौंँन।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->