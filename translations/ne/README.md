# शून्यबाट उत्पादनसम्म एआई एजेन्टहरू निर्माण गर्दै

![शून्यबाट उत्पादनसम्म एआई एजेन्टहरू निर्माण गर्दै](../../translated_images/ne/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 बहुभाषी समर्थन

#### GitHub Action मार्फत समर्थित (स्वचालित र सधैं अपडेट हुने)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अरेबिक](../ar/README.md) | [बंगाली](../bn/README.md) | [बुल्गेरियन](../bg/README.md) | [बर्मेली (म्यान्मार)](../my/README.md) | [चिनी (सरलीकृत)](../zh-CN/README.md) | [चिनी (परम्परागत, होङकङ)](../zh-HK/README.md) | [चिनी (परम्परागत, मकाउ)](../zh-MO/README.md) | [चिनी (परम्परागत, ताइवान)](../zh-TW/README.md) | [क्रोएशियन](../hr/README.md) | [चेक](../cs/README.md) | [डेनिश](../da/README.md) | [डच](../nl/README.md) | [एस्टोनियन](../et/README.md) | [फिनिश](../fi/README.md) | [फ्रेन्च](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिन्दी](../hi/README.md) | [हंगेरियन](../hu/README.md) | [इन्डोनेशियन](../id/README.md) | [इटालियन](../it/README.md) | [जापानी](../ja/README.md) | [कन्नड](../kn/README.md) | [कोरियन](../ko/README.md) | [लिथुआनियन](../lt/README.md) | [मलय](../ms/README.md) | [मलयालम](../ml/README.md) | [मराठी](../mr/README.md) | [नेपाली](./README.md) | [नाइजीरियन पिड्गिन](../pcm/README.md) | [नर्वेजियन](../no/README.md) | [फारसी (पर्सियन)](../fa/README.md) | [पोलिश](../pl/README.md) | [पोर्चुगिज (ब्राजिल)](../pt-BR/README.md) | [पोर्चुगिज (पोर्टुगल)](../pt-PT/README.md) | [पन्जाबी (गुरुमुखी)](../pa/README.md) | [रोमानियन](../ro/README.md) | [रशियन](../ru/README.md) | [सर्बियन (सिरिलिक)](../sr/README.md) | [स्लोभाक](../sk/README.md) | [स्लोभेनियन](../sl/README.md) | [स्पेनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्वीडिश](../sv/README.md) | [तागालोग (फिलिपिनो)](../tl/README.md) | [तमिल](../ta/README.md) | [तेलुगु](../te/README.md) | [थाई](../th/README.md) | [टर्किश](../tr/README.md) | [युक्रेनीयन](../uk/README.md) | [उर्दू](../ur/README.md) | [भियतनामी](../vi/README.md)

> **स्थानीय रूपमा क्लोन गर्न चाहनुहुन्छ?**

> यस रिपोजिटरीमा ५०+ भाषा अनुवादहरू समावेश छन् जसले डाउनलोड आकारलाई उल्लेखनीय रूपमा वृद्धि गर्छ। अनुवादहरू बिना क्लोन गर्न, sparse checkout प्रयोग गर्नुहोस्:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> यसले तपाईंलाई कोर्स पूरा गर्न आवश्यक सबै कुरा छिटो डाउनलोड गर्न अनुमति दिन्छ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## एआई एजेन्ट विकास जीवनचक्रका आधारभूत कुरा सिकाउने कोर्स

[![GitHub license](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 सुरु गर्दै

यस कोर्समा एआई एजेन्टहरू निर्माण र तैनाथ गर्ने आधारभूत पाठहरू छन्।

हरेक पाठले अघिल्लो पाठलाई आधार मानेर बनाइएको छ, त्यसैले हामी सुरुबाट सुरु गरी अन्त्यसम्म काम गर्न सिफारिस गर्छौं।

यदि तपाईं एआई एजेन्ट विषयहरूमा थप अन्वेषण गर्न चाहनुहुन्छ भने, तपाईं [एआई एजेन्टहरूका लागि सुरु गर्नेहरू कोर्स](https://aka.ms/ai-agents-beginners) हेर्न सक्नुहुन्छ।

### अन्य सिक्नेहरूलाई भेट्नुहोस्, तपाईंका प्रश्नहरूको उत्तर पाउनुहोस्

यदि तपाईं अड्किनुहुन्छ वा एआई एजेन्टहरू बनाउने बारे कुनै प्रश्नहरू छन् भने, हाम्रो समर्पित Discord च्यानलमा सहभागी हुनुहोस् [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6) मा।

### तपाईंलाई के चाहिन्छ

हरेक पाठसँग यसको आफ्नै कोड नमूना छ जुन तपाईं स्थानीय रूपमा चलाउन सक्नुहुन्छ। तपाईं [यस रिपोजिटरीलाई fork गर्न सक्नुहुन्छ](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork) आफ्नो प्रतिलिपि बनाउन।

यस कोर्सले हाल निम्न कुराहरू प्रयोग गर्दछ:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI सेवा](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

कृपया सुरु गर्नु अघि यी सेवाहरूमा पहुँच हुन सुनिश्चित गर्नुहोस्।

मोडेल होस्टिंग र सेवाहरू सम्बन्धी थप विकल्पहरू जल्दै आउँदै छन्।

## 🗃️ पाठहरू

| **पाठ**         | **वर्णन**                                                                                  |
|-----------------|--------------------------------------------------------------------------------------------|
| [एजेन्ट डिजाइन](./lesson-1-agent-design/README.md)       | हाम्रो "डेभलपर अनबोर्डिङ" एजेन्ट उपयोग केसको परिचय र प्रभावकारी एजेन्टहरू कसरी डिजाइन गर्ने                      |
| [एजेन्ट विकास](./lesson-2-agent-development/README.md)  | Microsoft Agent Framework (MAF) प्रयोग गरी नयाँ डेभलपरहरूलाई मद्दत गर्ने ३ एजेन्टहरू सिर्जना गर्ने                  |
| [एजेन्ट मूल्यांकन](./lesson-3-agent-evals/README.md)     | Microsoft Foundry प्रयोग गर्दै हाम्रा एआई एजेन्टहरू कत्तिको राम्रो प्रदर्शन गरिरहेका छन् र सुधार गर्न के गर्ने देखाउने     |
| [एजेन्ट तैनाथीकरण](./lesson-4-agent-deployment/README.md) | Hosted Agents र OpenAI Chatkit मार्फत एआई एजेन्ट उत्पादनमा कसरी तैनाथ गर्ने                                       |


## 🎒 अन्य कोर्सहरू

हाम्रो टिमले अन्य कोर्सहरू पनि उत्पादन गर्दछ! जाँच गर्नुहोस्:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j शुरुवातीहरूका लागि](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js शुरुवातीहरूका लागि](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain शुरुवातीहरूका लागि](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / एजेन्टहरू
[![AZD शुरुवातीहरूका लागि](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI शुरुवातीहरूका लागि](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP शुरुवातीहरूका लागि](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![एआई एजेन्टहरू शुरुवातीहरूका लागि](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### जेनरेटिभ एआई शृंखला
[![जेनरेटिभ एआई शुरुवातीहरूका लागि](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![जेनरेटिभ एआई (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![जेनरेटिभ एआई (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![जेनरेटिभ एआई (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### मुख्य सिकाइ
[![एमएल शुरुवातीहरूका लागि](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![डेटा विज्ञान शुरुवातीहरूका लागि](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![शुरुवातीहरूका लागि AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![शुरुवातीहरूका लागि साइबर सुरक्षा](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![शुरुवातीहरूका लागि वेब विकास](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![शुरुवातीहरूका लागि IoT](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![शुरुवातीहरूका लागि XR विकास](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### कोपाइलट श्रृंखला
[![AI जोडी प्रोग्रामिंगका लागि कोपाइलट](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET का लागि कोपाइलट](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![कोपाइलट साहसिक](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## योगदान

यस परियोजनाले योगदान र सिफारिसहरूलाई स्वागत गर्दछ। अधिकांश योगदानहरूले तपाईंलाई
एक योगदानकर्ता अनुबंध (CLA) मा सहमति जनाउन आवश्यक पर्छ जसले तपाईंले यो अधिकार राख्नु भएको र वास्तवमै हामीलाई तपाईंको योगदान प्रयोग गर्ने अधिकार दिनु भएको पुष्टि गर्दछ।
विवरणहरूका लागि <https://cla.opensource.microsoft.com> मा जानुहोस्।

जब तपाईं पुल अनुरोध सबमिट गर्नुहुन्छ, CLA बोटले स्वचालित रूपमा निर्धारण गर्नेछ कि तपाईंले CLA प्रदान गर्न आवश्यक छ वा छैन र PR लाई उचित रूपमा चिन्ह लगाउनेछ (जस्तै, स्थिति जाँच, टिप्पणी)।
सिर्फ बोटले प्रदान गर्ने निर्देशहरू पालना गर्नुहोस्। तपाईंले यो केवल एक पटक गर्नुपर्नेछ सबै रिपोहरूमा हाम्रो CLA प्रयोग गर्ने क्रममा।

यस परियोजनाले [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) लाई अपनाएको छ।
थप जानकारीका लागि [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) हेर्नुहोस् वा कुनै थप प्रश्न वा सुझावका लागि [opencode@microsoft.com](mailto:opencode@microsoft.com) मा सम्पर्क गर्नुहोस्।

## ट्रेडमार्कहरू

यस परियोजनामा परियोजना, उत्पादन वा सेवाहरूका ट्रेडमार्कहरू वा लोगोहरू समावेश हुनसक्छन्। Microsoft
ट्रेडमार्क वा लोगोहरूको अधिकृत प्रयोग
[Microsoft को ट्रेडमार्क र ब्रान्ड मार्गनिर्देशनहरू](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) को अधीनमा हुन्छ र तिनीहरूको पालन गर्नुपर्दछ।
यस परियोजनाका परिवर्तन गरिएका संस्करणहरूमा Microsoft ट्रेडमार्क वा लोगोहरूको प्रयोगले भ्रम उत्पन्न गर्नु हुँदैन वा Microsoft प्रायोजनलाई संकेत गर्नु हुँदैन।
तेस्रो-पक्ष ट्रेडमार्क वा लोगोहरूको कुनै पनि प्रयोग ती तेस्रो-पक्षहरूको नीतिहरूको अधीनमा हुन्छ।

## मद्दत प्राप्त गर्ने तरिका

यदि तपाईं अड्किनु भएको छ वा AI एपहरू बनाउन सम्बन्धि कुनै प्रश्न छ भने, सामेल हुनुहोस्:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

यदि तपाईंलाई उत्पादन सम्बन्धि प्रतिक्रिया वा त्रुटिहरू छन् भने, बनाउन क्रममा भ्रमण गर्नुहोस्:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यो दस्तावेज़लाई AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सटीकताको प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटि वा गलत असर हुन सक्दछ। मूल दस्तावेज़ आफ्नो मूल भाषामा आधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीको लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको उपयोगबाट आउने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->