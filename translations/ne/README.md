# शून्यबाट उत्पादनसम्म AI एजेन्टहरू निर्माण गर्दै

![शून्यबाट उत्पादनसम्म AI एजेन्टहरू निर्माण गर्दै](../../translated_images/ne/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 बहुभाषी समर्थन

#### GitHub Action मार्फत समर्थित (स्वचालित र सँधै अद्यावधिक)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अरेबिक](../ar/README.md) | [बंगाली](../bn/README.md) | [बल्गेरियन](../bg/README.md) | [बर्मी (म्यान्मार)](../my/README.md) | [चिनी (सरलीकृत)](../zh-CN/README.md) | [चिनी (परम्परागत, हङकङ)](../zh-HK/README.md) | [चिनी (परम्परागत, मकाउ)](../zh-MO/README.md) | [चिनी (परम्परागत, ताइवान)](../zh-TW/README.md) | [क्रोएशियन](../hr/README.md) | [चेक](../cs/README.md) | [डेनिश](../da/README.md) | [डच](../nl/README.md) | [एस्टोनियन](../et/README.md) | [फिनिश](../fi/README.md) | [फ्रेन्च](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिन्दी](../hi/README.md) | [हंगेरीयन](../hu/README.md) | [इन्डोनिसियन](../id/README.md) | [इटालियन](../it/README.md) | [जापानी](../ja/README.md) | [कन्नड](../kn/README.md) | [कोरियन](../ko/README.md) | [लिथुआनियन](../lt/README.md) | [मलय](../ms/README.md) | [मलयालम](../ml/README.md) | [मराठी](../mr/README.md) | [नेपाली](./README.md) | [नाइजेरियन पिडगिन](../pcm/README.md) | [नर्वेजियन](../no/README.md) | [फारसी (पर्शियन)](../fa/README.md) | [पोलिश](../pl/README.md) | [पोर्तुगाली (ब्राजिल)](../pt-BR/README.md) | [पोर्तुगाली (पोर्चुगल)](../pt-PT/README.md) | [पञ्जाबी (गुरमुखी)](../pa/README.md) | [रोमानियन](../ro/README.md) | [रूसी](../ru/README.md) | [सर्बियन (सिरीलिक)](../sr/README.md) | [स्लोभाक](../sk/README.md) | [स्लोभेनियाली](../sl/README.md) | [स्पेनी](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्विडिश](../sv/README.md) | [ट्यागालोग (फिलिपिनो)](../tl/README.md) | [तमिल](../ta/README.md) | [तेलुगु](../te/README.md) | [थाई](../th/README.md) | [टर्किश](../tr/README.md) | [युक्रेनी](../uk/README.md) | [उर्दू](../ur/README.md) | [भियतनामी](../vi/README.md)

> **स्थानीय स्तरमा क्लोन गर्न मन छ?**

> यो रिपोजिटरी ५०+ भाषा अनुवादहरू समावेश गर्दछ जसले डाउनलोड साइजलाई उल्लेखनीय रूपमा बढाउँछ। अनुवाद बिना क्लोन गर्न, sparse checkout प्रयोग गर्नुहोस्:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> यसले तपाईंलाई छिटो डाउनलोडको साथ कोर्स पूरा गर्न आवश्यक सबै कुरा दिन्छ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## AI एजेन्ट विकास जीवनचक्रका आधारभूत कुराहरू सिकाउने कोर्स

[![GitHub license](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 सुरु कसरी गर्ने

यस कोर्समा AI एजेन्टहरू निर्माण र डिप्लोय गर्ने आधारहरू समेटिएका पाठहरू छन्।

प्रत्येक पाठ अघिल्लो पाठको आधारमा निर्माण भएको छ, त्यसैले सुरुबाट थालेर अन्त्यसम्म जान सिफारिस गरिन्छ।

यदि तपाईं AI एजेन्ट विषयहरूमा थप अन्वेषण गर्न चाहनुहुन्छ भने, तपाईं [AI एजेन्टहरूका लागि प्रारम्भिक कोर्स](https://aka.ms/ai-agents-beginners) पनि हेर्न सक्नुहुन्छ।

### अन्य सिक्नेहरूलाई भेट्नुहोस्, आफ्ना प्रश्नहरूको जवाफ पाउनुहोस्

तपाईं अड्किनुभयो वा AI एजेन्टहरू निर्माण गर्ने बारे कुनै प्रश्न छ भने, हाम्रो समर्पित Discord च्यानलमा सामेल हुनुहोस् [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6) मा।

### तपाईंलाई के चाहिन्छ

प्रत्येक पाठसँग आफ्नो कोड नमुना छ जुन तपाईंले स्थानीय रूपमा चलाउन सक्नुहुन्छ। तपाईं [यो रिपोजिटरी फोर्क](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork) गरेर आफ्नो प्रति बनाउन सक्नुहुन्छ।

यो कोर्सले हाल निम्न सेवा प्रयोग गर्दछ:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

सुरु गर्नुअघि कृपया यी सेवाहरू पहुँच रहेको सुनिश्चित गर्नुहोस्।

मोडेल होस्टिङ र सेवाहरू सम्बन्धी थप विकल्पहरू चाँडै आउँदै छन्।

## 🗃️ पाठहरू

| **पाठ**              | **वर्णन**                                                                                 |
|--------------------|------------------------------------------------------------------------------------------|
| [एजेन्ट डिजाइन](./lesson-1-agent-design/README.md)       | हाम्रो "डेभलपर अनबोर्डिङ" एजेन्ट प्रयोग केस परिचय र प्रभावकारी एजेन्टहरू डिजाइन गर्ने तरिका |
| [एजेन्ट विकास](./lesson-2-agent-development/README.md)   | Microsoft Agent Framework (MAF) प्रयोग गरेर नयाँ डेभलपरहरूलाई सहयोग गर्न ३ एजेन्टहरू बनाउने |
| [एजेन्ट मूल्याङ्कन](./lesson-3-agent-evals/README.md)    | Microsoft Foundry मार्फत हाम्रा AI एजेन्टहरू कत्तिको राम्रो प्रदर्शन गर्दैछन् र सुधार कसरी गर्ने पत्ता लगाउने |
| [एजेन्ट डिप्लोयमेन्ट](./lesson-4-agent-deployment/README.md)  | Hosted Agents र OpenAI Chatkit प्रयोग गरी AI एजेन्टलाई उत्पादनमा कसरी डिप्लोय गर्ने देखाउने  |

## 🎒 अन्य कोर्सहरू

हाम्रो टिमले अन्य कोर्सहरू पनि उत्पादन गर्दछ! हेर्नुहोस्:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![शुरुवातकर्ताहरूका लागि LangChain4j](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![शुरुवातकर्ताहरूका लागि LangChain.js](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / एजेन्टहरू
[![शुरुवातकर्ताहरूका लागि AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![शुरुवातकर्ताहरूका लागि Edge AI](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![शुरुवातकर्ताहरूका लागि MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![शुरुवातकर्ताहरूका लागि AI एजेन्टहरू](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### जेनेरेटिभ AI सिरिज
[![शुरुवातकर्ताहरूका लागि जेनेरेटिभ AI](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![जेनेरेटिभ AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![जेनेरेटिभ AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![जेनेरेटिभ AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### कोर सिकाइ
[![शुरुवातकर्ताहरूका लागि ML](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![शुरुवातकर्ताहरूका लागि डाटा विज्ञान](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![शुरुवातकर्ताहरूका लागि AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![साइबरसुरक्षा शुरुवातीहरूका लागि](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![वेब विकास शुरुवातीहरूका लागि](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT शुरुवातीहरूका लागि](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR विकास शुरुवातीहरूका लागि](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### कोपाइलट सिरिज
[![एआई जोडी प्रोग्रामिङका लागि कोपाइलट](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET को लागि कोपाइलट](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![कोपाइलट साहसिक यात्रा](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## योगदान

यस परियोजनाले योगदान र सुझावहरूलाई स्वागत गर्छ। धेरैजसो योगदानकर्ताले Contributor License Agreement (CLA) मा सहमत हुन आवश्यक छ, जसले तपाईंलाई अधिकार दिन्छ र साँच्चिकै तपाईंले हामीलाई तपाईंको योगदान प्रयोग गर्ने अधिकार दिनुभएको छ भनेर घोषणा गर्दछ। विवरणहरूको लागि, यहाँ जानुहोस्: <https://cla.opensource.microsoft.com>।

जब तपाईं पुल रिक्वेस्ट बुझाउनुहुन्छ, CLA बोट स्वचालित रूपमा निर्धारण गर्नेछ कि तपाईंलाई CLA प्रदान गर्न आवश्यक छ वा छैन र उचित रूपमा PR लाई सजाउनेछ (जस्तै, स्थिति जाँच, टिप्पणी)। बोटले दिएको निर्देशनहरू पालना गर्नुहोस्। तपाईंलाई केवल एकपटक यो प्रक्रिया गर्नु पर्नेछ सबै रिपोजमा हाम्रो CLA प्रयोग गर्दा।

यस परियोजनाले [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) अपनाएको छ।
थप जानकारीका लागि [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) हेर्नुहोस् वा कुनै थप प्रश्न वा टिप्पणीका लागि [opencode@microsoft.com](mailto:opencode@microsoft.com) मा सम्पर्क गर्नुहोस्।

## ट्रेडमार्कहरू

यस परियोजनामा प्रोजेक्ट, उत्पादन वा सेवाहरूका लागि ट्रेडमार्कहरू वा लोगोहरू समावेश हुन सक्छन्। Microsoft ट्रेडमार्कहरू वा लोगोहरूको अधिकृत प्रयोग गर्नु पर्दछ र पालन गर्नु पर्दछ
[Microsoft का ट्रेडमार्क र ब्रान्ड दिशानिर्देशहरू](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)।
परियोजनाको परिमार्जित संस्करणहरूमा Microsoft ट्रेडमार्कहरू वा लोगोहरूको प्रयोगले भ्रम सिर्जना गर्न वा Microsoft को प्रायोजन दर्शाउन नहुनेछ।
तेस्रो पक्षका ट्रेडमार्कहरू वा लोगोहरूको कुनै पनि प्रयोग ती तेस्रो पक्षको नीतिहरूमा आधारित हुनेछ।

## सहायता प्राप्त गर्नुहोस्

यदि तपाईं फस्नुभयो वा AI अनुप्रयोगहरू बनाउने बारे कुनै प्रश्न छ भने, सामेल हुनुस्:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

यदि तपाईंलाई उत्पादन प्रतिक्रियाहरू वा निर्माण गर्दा त्रुटिहरू आइरहेका छन् भने भ्रमण गर्नुहोस्:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**सूचनाः**  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) को प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयासरत छौं, तर कृपया बुझ्नुहोस् कि स्वचालित अनुवादहरूमा त्रुटि वा अशुद्धता हुनसक्छ। मूल भाषामा रहेको दस्तावेजलाई आधिकारिक स्रोत मान्नुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यो अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा दुभ्र्याख्याका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->