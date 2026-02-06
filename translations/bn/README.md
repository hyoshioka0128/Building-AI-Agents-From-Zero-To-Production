# শূন্য থেকে উৎপাদনে AI এজেন্ট তৈরি করা

![শূন্য থেকে উৎপাদনে AI এজেন্ট তৈরি করা](../../translated_images/bn/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 বহু-ভাষা সমর্থন

#### গিটহাব অ্যাকশনের মাধ্যমে সমর্থিত (স্বয়ংক্রিয় এবং সর্বদা আপ-টু-ডেট)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](./README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **স্থানীয়ভাবে ক্লোন করতে চান?**

> এই রিপোজিটরিতে ৫০+ ভাষার অনুবাদ অন্তর্ভুক্ত রয়েছে যা ডাউনলোডের আকার উল্লেখযোগ্যভাবে বাড়ায়। অনুবাদ ছাড়া ক্লোন করতে, sparse checkout ব্যবহার করুন:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> এটি আপনাকে কোর্স সম্পন্ন করার জন্য প্রয়োজনীয় সবকিছু আরও দ্রুত ডাউনলোড করার সুযোগ দেয়।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## AI এজেন্ট ডেভেলপমেন্ট লাইফসাইকেলের ভিত্তিগুলো শেখানোর একটি কোর্স

[![GitHub license](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 শুরু করা

এই কোর্সে AI এজেন্ট তৈরি এবং মোতায়েনের ভিত্তি ভিত্তিক পাঠ রয়েছে।

প্রতিটি পাঠ পূর্বেরটির উপর ভিত্তি করে নির্মিত, তাই আমরা শুরু থেকে শুরু করে শেষ পর্যন্ত কাজ করার পরামর্শ দিই।

যদি আপনি AI এজেন্ট বিষয়গুলি আরও অনুসন্ধান করতে চান, তাহলে আপনি [AI Agents For Beginners Course](https://aka.ms/ai-agents-beginners) পরীক্ষা করতে পারেন।

### অন্যান্য শিক্ষার্থীদের সাথে দেখা করুন, আপনার প্রশ্নের উত্তর পান

যদি আপনি আটকে যান বা AI এজেন্ট তৈরি সম্পর্কে কোন প্রশ্ন থাকে, তাহলে আমাদের নিবেদিত ডিসকর্ড চ্যানেল এ যোগ দিন [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6)।

### আপনার যা প্রয়োজন

প্রতিটি পাঠের নিজস্ব কোড স্যাম্পল রয়েছে যা আপনি স্থানীয়ভাবে চালাতে পারবেন। আপনি [এই রিপোজিটরি ফরক করতে পারেন](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork) আপনার নিজস্ব কপি তৈরির জন্য।

এই কোর্স বর্তমানে নিচেরগুলোর ব্যবহার করে:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

শুরু করার আগে নিশ্চিত করুন যে আপনার কাছে এই পরিষেবাগুলোর অ্যাক্সেস রয়েছে।

মডেল হোস্টিং এবং সার্ভিসের আরও বিকল্প শীঘ্রই আসছে।

## 🗃️ পাঠসমূহ

| **পাঠ**                  | **বর্ণনা**                                                                                     |
|--------------------------|------------------------------------------------------------------------------------------------|
| [Agent Design](./lesson-1-agent-design/README.md)              | আমাদের "ডেভেলপার অনবোর্ডিং" এজেন্ট ইউজ কেসের একটি পরিচিতি এবং কীভাবে কার্যকর এজেন্ট ডিজাইন করবেন |
| [Agent Development](./lesson-2-agent-development/README.md)    | Microsoft Agent Framework (MAF) ব্যবহার করে, নতুন ডেভেলপারদের সহায়তার জন্য ৩টি এজেন্ট তৈরি করুন |
| [Agent Evaluations](./lesson-3-agent-evals/README.md)          | Microsoft Foundry ব্যবহার করে, আমাদের AI এজেন্টগুলি কতটা ভালো কাজ করছে এবং কীভাবে উন্নত করা যায় তা জানুন |
| [Agent Deployment](./lesson-4-agent-deployment/README.md)      | Hosted Agents এবং OpenAI Chatkit ব্যবহার করে, একটি AI এজেন্ট প্রোডাকশনে মোতায়েন করার উপায় দেখুন |

## 🎒 অন্যান্য কোর্স

আমাদের টিম অন্যান্য কোর্স তৈরি করে! পরীক্ষা করুন:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### ল্যাঙ্গচেইন
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### এজুর / এজ / MCP / এজেন্টস
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### জেনেরেটিভ AI সিরিজ
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### মূল শিক্ষা
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![নতুনদের জন্য সাইবারসিকিউরিটি](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![নতুনদের জন্য ওয়েব ডেভ](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![নতুনদের জন্য আইওটি](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![নতুনদের জন্য এক্সআর ডেভেলপমেন্ট](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### কপাইলট সিরিজ
[![কপাইলট ফর AI যুগল প্রোগ্রামিং](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![কপাইলট ফর C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![কপাইলট অ্যাডভেঞ্চার](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## অবদান রাখা

এই প্রকল্প অবদান ও প্রস্তাবনার স্বাগত জানায়। বেশিরভাগ অবদানের জন্য আপনাকে একটি অবদানকারী লাইসেন্স চুক্তি (CLA) এ সম্মতি দিতে হবে, যা ঘোষণা করে যে আপনার অধিকার আছে এবং আপনি প্রকৃতপক্ষে আমাদেরকে আপনার অবদান ব্যবহারের অধিকার দিচ্ছেন। বিস্তারিত জানতে <https://cla.opensource.microsoft.com> পরিদর্শন করুন।

যখন আপনি একটি পুল রিকুয়েস্ট জমা দেবেন, একটি CLA বট স্বয়ংক্রিয়ভাবে নির্ধারণ করবে যে আপনার CLA প্রদান করা প্রয়োজন কিনা এবং উপযুক্তভাবে PR টি সাজেবে (যেমন, স্ট্যাটাস চেক, মন্তব্য)। বট প্রদত্ত নির্দেশনাগুলো অনুসরণ করুন। আমাদের CLA ব্যবহার করা সব রেপোজে একবারই এটি করতে হবে।

এই প্রকল্প [মাইক্রোসফট ওপেন সোর্স আচরণবিধি](https://opensource.microsoft.com/codeofconduct/) গ্রহণ করেছে।
আরও তথ্যের জন্য দেখুন [আচরণবিধি FAQ](https://opensource.microsoft.com/codeofconduct/faq/) অথবা কোনো অতিরিক্ত প্রশ্ন বা মন্তব্যের জন্য [opencode@microsoft.com](mailto:opencode@microsoft.com) এ যোগাযোগ করুন।

## ট্রেডমার্কস

এই প্রকল্পে প্রকল্প, পণ্য বা সেবার ট্রেডমার্ক বা লোগো থাকতে পারে। মাইক্রোসফট ট্রেডমার্ক বা লোগোর অনুমোদিত ব্যবহার [মাইক্রোসফট ট্রেডমার্ক ও ব্র্যান্ড নির্দেশিকা](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) অনুসরণ করতে হবে এবং এর আওতাধীন।

মাইক্রোসফট ট্রেডমার্ক বা লোগোর সংশোধিত সংস্করণে ব্যবহার বিভ্রান্তি সৃষ্টি করতে বা মাইক্রোসফট পৃষ্ঠপোষকতার ইঙ্গিত দিতে পারবে না।
তৃতীয় পক্ষের ট্রেডমার্ক বা লোগোর কোন ব্যবহার তাদের নিজস্ব নীতিমালা অনুসরণ করবে।

## সাহায্য পাওয়া

যদি আপনি আটকে যান বা AI অ্যাপ্লিকেশন নির্মাণ সম্পর্কে কোনো প্রশ্ন থাকে, যোগ দিন:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

যদি পণ্য প্রতিক্রিয়া বা নির্মাণকালে ত্রুটি থাকে, পরিদর্শন করুন:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, কিন্তু স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে তা অনুগ্রহ করে মনে রাখবেন। মূল নথির নিজস্ব ভাষাই কর্তৃপক্ষপ্রাপ্ত উৎস হিসেবে বিবেচিত হবে। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদকর দ্বারা অনুবাদ করানোই শ্রেয়। এই অনুবাদের ব্যবহারে উদ্ভূত যেকোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নয়।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->