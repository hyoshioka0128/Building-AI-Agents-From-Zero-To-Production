<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b09df38b3188ffe957c7ac8b055967f5",
  "translation_date": "2026-01-16T08:23:29+00:00",
  "source_file": "README.md",
  "language_code": "ur"
}
-->
# زیرو سے پروڈکشن تک AI ایجنٹس کی تعمیر

![زیرو سے پروڈکشن تک AI ایجنٹس کی تعمیر](../../../../translated_images/ur/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 کثیر الزبان کی حمایت

#### گٹ ہب ایکشن کے ذریعے معاونت (خودکار اور ہمیشہ جدید)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[عربی](../ar/README.md) | [بنگالی](../bn/README.md) | [بلغاریائی](../bg/README.md) | [برمی (میانمار)](../my/README.md) | [چینی (آسان)](../zh/README.md) | [چینی (روایتی، ہانگ کانگ)](../hk/README.md) | [چینی (روایتی، ماکاؤ)](../mo/README.md) | [چینی (روایتی، تائیوان)](../tw/README.md) | [کروشیائی](../hr/README.md) | [چیک](../cs/README.md) | [ڈینش](../da/README.md) | [ڈچ](../nl/README.md) | [ایسٹونین](../et/README.md) | [فنلش](../fi/README.md) | [فرانسیسی](../fr/README.md) | [جرمن](../de/README.md) | [یونانی](../el/README.md) | [عبرانی](../he/README.md) | [ہندی](../hi/README.md) | [ہنگیرین](../hu/README.md) | [انڈونیشین](../id/README.md) | [اطالوی](../it/README.md) | [جاپانی](../ja/README.md) | [کنڑ](../kn/README.md) | [کوریائی](../ko/README.md) | [لتھوانین](../lt/README.md) | [مالے](../ms/README.md) | [مالایالم](../ml/README.md) | [مہاراشٹرا](../mr/README.md) | [نیپالی](../ne/README.md) | [نائجیریائی پیڈجن](../pcm/README.md) | [ناروے](../no/README.md) | [فارسی (فارس)](../fa/README.md) | [پولش](../pl/README.md) | [پرتگالی (برازیل)](../br/README.md) | [پرتگالی (پرتگال)](../pt/README.md) | [پنجابی (گرمکھی)](../pa/README.md) | [رومانیائی](../ro/README.md) | [روسی](../ru/README.md) | [سربیائی (سریلیک)](../sr/README.md) | [سلواک](../sk/README.md) | [سلووینین](../sl/README.md) | [ہسپانوی](../es/README.md) | [سواحلی](../sw/README.md) | [سویڈش](../sv/README.md) | [ٹاگالوگ (فلپائنی)](../tl/README.md) | [تمل](../ta/README.md) | [تلگو](../te/README.md) | [تھائی](../th/README.md) | [ترکی](../tr/README.md) | [یوکرینیائی](../uk/README.md) | [اردو](./README.md) | [ویتنامی](../vi/README.md)

> **کیا آپ مقامی طور پر کلون کرنا پسند کریں گے؟**

> اس ریپوزیٹری میں 50+ زبانوں کے تراجم شامل ہیں جو ڈاؤن لوڈ کے سائز کو نمایاں بڑھاتے ہیں۔ بغیر تراجم کے کلون کرنے کے لیے sparse checkout استعمال کریں:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> اس سے آپ کو کورس مکمل کرنے کے لیے ہر چیز بہت تیز ڈاؤن لوڈ کے ساتھ ملے گی۔
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## ایک کورس جو آپ کو AI ایجنٹ ڈیولپمنٹ کی بنیادیات سکھاتا ہے

[![GitHub لائسنس](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub ٹربیوشن کنندگان](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub ایشوز](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub پل-ریکویسٹس](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs خوش آمدید](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 شروع کرنا

یہ کورس AI ایجنٹس کی تعمیر اور تعیناتی کی بنیادیات پر مشتمل ہے۔

ہر سبق پچھلے سبق کی بنیاد پر بنتا ہے، لہذا ہم تجویز کرتے ہیں کہ شروع سے شروع کریں اور آخر تک کام کریں۔

اگر آپ AI ایجنٹ کے موضوعات کے بارے میں مزید جاننا چاہتے ہیں، تو آپ [AI Agents For Beginners کورس](https://aka.ms/ai-agents-beginners) دیکھ سکتے ہیں۔

### دیگر سیکھنے والوں سے ملیں، اپنے سوالات کے جواب پائیں

اگر آپ پھنس جائیں یا AI ایجنٹس کی تعمیر کے بارے میں کوئی سوال ہو، تو ہمارے مخصوص Discord چینل میں شامل ہوں جو [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6) پر موجود ہے۔

### آپ کو کیا چاہیے

ہر سبق کے پاس اپنا کوڈ نمونہ ہے جسے آپ لوکل چل سکتے ہیں۔ آپ [اس ریپو کو فورک](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork) کر کے اپنی کاپی بنا سکتے ہیں۔

یہ کورس اس وقت مندرجہ ذیل استعمال کرتا ہے:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

براہ کرم شروع کرنے سے پہلے ان خدمات تک رسائی کو یقینی بنائیں۔

ماڈل ہوسٹنگ اور خدمات کے متعلق مزید اختیارات جلد آ رہے ہیں۔

## 🗃️ اسباق

| **سبق**              | **تفصیل**                                                                                      |
|-----------------------|------------------------------------------------------------------------------------------------|
| [Agent Design](./lesson-1-agent-design/README.md)         | ہمارے "Developer Onboarding" Agent Use Case کا تعارف اور مؤثر ایجنٹس کے ڈیزائن کا طریقہ          |
| [Agent Development](./lesson-2-agent-development/README.md)    | Microsoft Agent Framework (MAF) کے استعمال سے 3 ایجنٹس بنائیں جو نئے ڈیولپرز کی مدد کریں۔       |
| [Agent Evaluations](./lesson-3-agent-evals/README.md)      | Microsoft Foundry کے ذریعے جانیں کہ ہمارے AI ایجنٹس کتنے اچھے کام کر رہے ہیں اور انہیں کیسے بہتر بنایا جائے۔ |
| [Agent Deployment](./lesson-4-agent-deployment/README.md)       | Hosted Agents اور OpenAI Chatkit کا استعمال کرتے ہوئے AI ایجنٹس کو پروڈکشن میں تعینات کرنے کا طریقہ۔    |

## 🎒 دیگر کورسز

ہماری ٹیم دیگر کورسز بھی تیار کرتی ہے! دیکھیں:

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
 
### Core Learning
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![ابتدائیوں کے لیے سائبر سیکیورٹی](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![ابتدائیوں کے لیے ویب ڈویلپمنٹ](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![ابتدائیوں کے لیے آئی او ٹی](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![ابتدائیوں کے لیے ایکس آر ڈویلپمنٹ](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### کوپائلٹ سیریز
[![اے آئی جوڑے ہوئے پروگرامنگ کے لئے کوپائلٹ](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET کے لئے کوپائلٹ](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![کوپائلٹ ایڈونچر](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## تعاون

یہ پروجیکٹ تعاون اور تجاویز کو خوش آمدید کہتا ہے۔ زیادہ تر تعاون کے لیے آپ کو ایک
کنٹریبیوٹر لائسنس ایگریمنٹ (CLA) سے اتفاق کرنا ضروری ہے جو اس بات کا اعلان کرتا ہے کہ آپ کے پاس یہ حق ہے، اور واقعی، ہمیں اپنے تعاون کو استعمال کرنے کے حقوق دیتے ہیں۔ تفصیلات کے لیے ملاحظہ کریں <https://cla.opensource.microsoft.com>۔

جب آپ کوئی پل ریکوئسٹ جمع کراتے ہیں، تو CLA بوٹ خود بخود یہ تعین کرے گا کہ آیا آپ کو CLA فراہم کرنے کی ضرورت ہے اور پل ریکوئسٹ کو مناسب طریقے سے نشاندہی کرے گا (مثلاً، اسٹیٹس چیک، کمنٹس)۔ بس بوٹ کی جانب سے دی گئی ہدایات پر عمل کریں۔ آپ کو یہ ایک بار تمام ریپوز میں CLA کے ذریعہ استعمال کرنے کے لیے کرنا ہوگا۔

اس پروجیکٹ نے مائیکروسافٹ کی اوپن سورس کوڈ آف کنڈکٹ کو اپنایا ہے۔
مزید معلومات کے لیے [کوڈ آف کنڈکٹ FAQ](https://opensource.microsoft.com/codeofconduct/faq/) دیکھیں یا
کسی اضافی سوالات یا تبصروں کے لیے [opencode@microsoft.com](mailto:opencode@microsoft.com) سے رابطہ کریں۔

## تجارتی نشان

یہ پروجیکٹ ممکن ہے کہ منصوبوں، مصنوعات، یا خدمات کے لیے تجارتی نشان یا لوگوز پر مشتمل ہو۔ مائیکروسافٹ کے
تجارتی نشان یا لوگوز کے مجاز استعمال کو اور اس کی پیروی کرنا ہوگی
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)۔
اس پروجیکٹ کے ترمیم شدہ ورژن میں مائیکروسافٹ کے تجارتی نشان یا لوگوز کا استعمال الجھن نہیں پیدا کرنا چاہیے یا مائیکروسافٹ کی سرپرستی کا تاثر نہیں دینا چاہیے۔
تیسرے فریق کے تجارتی نشان یا لوگوز کا کوئی بھی استعمال ان تیسرے فریقوں کی پالیسیوں کے تابع ہے۔

## مدد حاصل کریں

اگر آپ بند ہو جائیں یا AI ایپس بنانے کے دوران کوئی سوال ہو تو شامل ہوں:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

اگر آپ کے پاس مصنوعات کی رائے یا تعمیر کے دوران غلطیاں ہوں تو ملاحظہ کریں:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈی کلیئرشن**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم نوٹ کریں کہ خودکار ترجموں میں غلطیاں یا کمی بیشی ہو سکتی ہے۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جائے گی۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمہ کے استعمال سے پیدا ہونے والے کسی بھی غلط فہمی یا غلط تشریحات کی ذمہ داری ہم پر عائد نہیں ہوتی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->