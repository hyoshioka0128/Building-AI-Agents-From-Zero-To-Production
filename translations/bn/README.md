# শূন্য থেকে প্রোডাকশনে AI এজেন্ট তৈরি করা

![শূন্য থেকে প্রোডাকশনে AI এজেন্ট তৈরি](../../translated_images/bn/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 বহুভাষিক সমর্থন

#### গিটহাব অ্যাকশনের মাধ্যমে সমর্থিত (স্বয়ংক্রিয় এবং সর্বদা হালনাগাদ)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[আরবি](../ar/README.md) | [বাংলা](./README.md) | [বুলগেরীয়](../bg/README.md) | [বর্মিজ (মিয়ানমার)](../my/README.md) | [চীনা (সরলীকৃত)](../zh-CN/README.md) | [চীনা (প্রথাগত, হংকং)](../zh-HK/README.md) | [চীনা (প্রথাগত, ম্যাকাও)](../zh-MO/README.md) | [চীনা (প্রথাগত, তাইওয়ান)](../zh-TW/README.md) | [ক্রোয়েশিয়ান](../hr/README.md) | [চেক](../cs/README.md) | [ডেনিশ](../da/README.md) | [ডাচ](../nl/README.md) | [এস্তোনিয়ান](../et/README.md) | [ফিনিশ](../fi/README.md) | [ফরাসি](../fr/README.md) | [জার্মান](../de/README.md) | [গ্রীক](../el/README.md) | [হিব্রু](../he/README.md) | [হিন্দি](../hi/README.md) | [হাঙ্গেরিয়ান](../hu/README.md) | [ইন্দোনেশিয়ান](../id/README.md) | [ইতালিয়ান](../it/README.md) | [জাপানি](../ja/README.md) | [কন্নড়](../kn/README.md) | [কোরিয়ান](../ko/README.md) | [লিথুয়ানিয়ান](../lt/README.md) | [মালয়](../ms/README.md) | [মালয়ালাম](../ml/README.md) | [মরাঠি](../mr/README.md) | [নেপালি](../ne/README.md) | [নাইজেরিয়ান পিডজিন](../pcm/README.md) | [নরওয়েজিয়ান](../no/README.md) | [ফার্সি (পর্শিয়ান)](../fa/README.md) | [পোলিশ](../pl/README.md) | [পোর্তুগিজ (ব্রাজিল)](../pt-BR/README.md) | [পোর্তুগিজ (পোর্তুগাল)](../pt-PT/README.md) | [পাঞ্জाबी (গুরুমুখি)](../pa/README.md) | [রোমানিয়ান](../ro/README.md) | [রুশি](../ru/README.md) | [সারবিয়ান (সিরিলিক)](../sr/README.md) | [স্লোভাক](../sk/README.md) | [স্লোভেনিয়ান](../sl/README.md) | [স্প্যানিশ](../es/README.md) | [সোয়াহিলি](../sw/README.md) | [সুইডিশ](../sv/README.md) | [টাগালগ (ফিলিপিনো)](../tl/README.md) | [তামিল](../ta/README.md) | [তেলুগু](../te/README.md) | [থাই](../th/README.md) | [তুর্কি](../tr/README.md) | [ইউক্রেনীয়](../uk/README.md) | [উর্দূ](../ur/README.md) | [ভিয়েতনামী](../vi/README.md)

> **স্থানীয়ভাবে ক্লোন করতে চান?**

> এই রিপোজিটরিতে ৫০+ ভাষার অনুবাদ রয়েছে যা ডাউনলোডের আকার অনেক বেশি বাড়ায়। অনুবাদ ছাড়া ক্লোন করতে, স্পার্স চেকআউট ব্যবহার করুন:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> এটি আপনাকে কোর্স সম্পন্ন করার জন্য প্রয়োজনীয় সবকিছু দ্রুত ডাউনলোড করার সুযোগ দেয়।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## AI এজেন্ট ডেভেলপমেন্ট লাইফসাইকেলের মৌলিক বিষয় শেখানোর একটি কোর্স

[![GitHub license](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 শুরু করা

এই কোর্সে AI এজেন্ট তৈরি ও প্রয়োগের মৌলিক বিষয়গুলো শেখানো হয়েছে।

প্রতিটি লেসন পূর্ববর্তী লেসনের উপর ভিত্তি করে তৈরি, তাই আমরা পরামর্শ দিই প্রথম থেকে শুরু করে শেষ পর্যন্ত অগ্রসর হোন।

যদি আপনি AI এজেন্ট বিষয়ক আরও তথ্য জানতে চান, তাহলে [AI Agents For Beginners Course](https://aka.ms/ai-agents-beginners) টি দেখুন।

### অন্যান্য শিক্ষার্থীদের সাথে মেশুন, আপনার প্রশ্নের উত্তর পান

যদি আপনি আটকে যান বা AI এজেন্ট তৈরি সম্পর্কে কোনো প্রশ্ন থাকে, আমাদের দায়িত্বপ্রাপ্ত Discord চ্যানেলে যোগ দিন [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6) এ।

### আপনার কী প্রয়োজন

প্রতিটি লেসনের জন্য আলাদা কোড স্যাম্পল আছে যা আপনি লোকালি চালাতে পারেন। আপনি [এই রিপো ফর্ক](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork) করে নিজের কপি তৈরি করতে পারেন।

এই কোর্স বর্তমানে নিম্নলিখিতগুলি ব্যবহার করছে:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

শুরু করার আগে নিশ্চিত করুন যে আপনি এই পরিষেবাগুলোতে প্রবেশাধিকার পেয়েছেন।

মডেল হোস্টিং এবং পরিষেবাগুলো সম্পর্কিত আরও বিকল্প শিগগিরই আসছে।

## 🗃️ লেসনসমূহ

| **লেসন**             | **বর্ণনা**                                                                                     |
|----------------------|------------------------------------------------------------------------------------------------|
| [Agent Design](./lesson-1-agent-design/README.md)           | আমাদের "ডেভেলপার অনবোর্ডিং" এজেন্ট ব্যবহার কেস এর পরিচিতি এবং কার্যকর এজেন্ট ডিজাইন করার পদ্ধতি  |
| [Agent Development](./lesson-2-agent-development/README.md)  | Microsoft Agent Framework (MAF) ব্যবহার করে ৩টি এজেন্ট তৈরি করুন যা নতুন ডেভেলপারদের অনবোর্ড করতে সাহায্য করবে।  |
| [Agent Evaluations](./lesson-3-agent-evals/README.md)        | Microsoft Foundry ব্যবহার করে আমাদের AI এজেন্টগুলি কত ভালো কাজ করছে এবং কিভাবে উন্নতি করা যায় তা জানুন।                    |
| [Agent Deployment](./lesson-4-agent-deployment/README.md)    | Hosted Agents এবং OpenAI Chatkit ব্যবহার করে AI এজেন্টকে প্রোডাকশনে কীভাবে ডিপ্লয় করবেন দেখুন।                            |


## 🎒 অন্যান্য কোর্স

আমাদের টিম অন্যান্য কোর্স তৈরি করে! দেখুন:

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
 
### Core Learning
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![শুরুতেই কৃত্রিম বুদ্ধিমত্তা](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![শুরুতেই সাইবারসিকিউরিটি](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![শুরুতেই ওয়েব ডেভেলপমেন্ট](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![শুরুতেই আইওটি](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![শুরুতেই এক্সআর ডেভেলপমেন্ট](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### কপাইলট সিরিজ
[![কপাইলট ফর এআই পেয়ারড প্রোগ্রামিং](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![কপাইলট ফর C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![কপাইলট অ্যাডভেঞ্চার](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## অবদান রাখা

এই প্রকল্প অবদান এবং প্রস্তাবনাগুলোকে স্বাগত জানায়। অধিকাংশ অবদানের জন্য আপনাকে একটি অবদানকারী লাইসেন্স চুক্তি (CLA) গ্রহণ করতে হবে যা ঘোষণা করে যে আপনার কাছে আপনার অবদান ব্যবহারের অধিকার আছে এবং আপনি তা দিচ্ছেন। বিস্তারিত জানতে যান <https://cla.opensource.microsoft.com>.

যখন আপনি একটি পুল রিকোয়েস্ট জমা দেবেন, তখন একটি CLA বট স্বয়ংক্রিয়ভাবে নির্ধারণ করবে যে আপনাকে CLA প্রদান করতে হবে কি না এবং উপযুক্তভাবে PR আলংকারিক করবে (যেমন, স্ট্যাটাস চেক, মন্তব্য)। বট প্রদত্ত নির্দেশনা অনুসরণ করুন। আমাদের CLA ব্যবহৃত সকল রিপোজিটরির মধ্যে এটি একবারই করতে হবে।

এই প্রকল্প [মাইক্রোসফট ওপেন সোর্স আচরণবিধি](https://opensource.microsoft.com/codeofconduct/) অনুসরণ করে। আরও তথ্যের জন্য দেখুন [আচরণবিধি FAQ](https://opensource.microsoft.com/codeofconduct/faq/) অথবা অতিরিক্ত প্রশ্ন বা মন্তব্যের জন্য যোগাযোগ করুন [opencode@microsoft.com](mailto:opencode@microsoft.com)।

## ট্রেডমার্ক

এই প্রকল্পে হয়ত প্রকল্প, পণ্য অথবা সার্ভিসের ট্রেডমার্ক বা লোগো থাকতে পারে। Microsoft-এর ট্রেডমার্ক বা লোগোর অনুমোদিত ব্যবহার [Microsoft-এর ট্রেডমার্ক ও ব্র্যান্ড নির্দেশিকা](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) অনুসরণ করতে হবে। Microsoft-এর ট্রেডমার্ক বা লোগোর পরিবর্তিত সংস্করণে ব্যবহার বিভ্রান্তিকর হওয়া বা Microsoft স্পন্সরশিপ সূচিত করা যাবে না। তৃতীয় পক্ষের ট্রেডমার্ক বা লোগো ব্যবহারের ক্ষেত্রে ঐ পক্ষের নীতিমালা প্রযোজ্য।

## সাহায্য পাওয়া

যদি আপনি আটকে যান বা AI অ্যাপ তৈরি সম্পর্কে কোনো প্রশ্ন থাকে, যোগ দিন:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

যদি আপনার পণ্য প্রতিক্রিয়া বা নির্মাণের সময় কোনো ত্রুটি থাকে, যান:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকারোক্তি**:
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসম্ভব সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে দয়া করে মাথায় রাখুন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসম্পূর্ণতা থাকতে পারে। মূল নথিটি তার মাতৃভাষায় কর্তৃত্বপূর্ণ উৎস হিসাবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের ক্ষেত্রে পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনও ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->