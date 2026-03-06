# ساخت عامل‌های هوش مصنوعی از صفر تا تولید

![ساخت عامل‌های هوش مصنوعی از صفر تا تولید](../../translated_images/fa/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 پشتیبانی چندزبانه

#### پشتیبانی شده از طریق GitHub Action (خودکار و همیشه به‌روز)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[عربی](../ar/README.md) | [بنگالی](../bn/README.md) | [بلغاری](../bg/README.md) | [بورمی (میانمار)](../my/README.md) | [چینی (ساده‌شده)](../zh-CN/README.md) | [چینی (سنتی، هنگ‌کنگ)](../zh-HK/README.md) | [چینی (سنتی، ماکائو)](../zh-MO/README.md) | [چینی (سنتی، تایوان)](../zh-TW/README.md) | [کرواتی](../hr/README.md) | [چکی](../cs/README.md) | [دانمارکی](../da/README.md) | [هلندی](../nl/README.md) | [استونیایی](../et/README.md) | [فنلاندی](../fi/README.md) | [فرانسوی](../fr/README.md) | [آلمانی](../de/README.md) | [یونانی](../el/README.md) | [عبری](../he/README.md) | [هندی](../hi/README.md) | [مجاری](../hu/README.md) | [اندونزیایی](../id/README.md) | [ایتالیایی](../it/README.md) | [ژاپنی](../ja/README.md) | [کانادا](../kn/README.md) | [کره‌ای](../ko/README.md) | [لیتوانیایی](../lt/README.md) | [مالایی](../ms/README.md) | [مالایالام](../ml/README.md) | [مراتی](../mr/README.md) | [نپالی](../ne/README.md) | [پیدجین نیجریه‌ای](../pcm/README.md) | [نروژی](../no/README.md) | [فارسی](./README.md) | [لهستانی](../pl/README.md) | [پرتغالی (برزیل)](../pt-BR/README.md) | [پرتغالی (پرتغال)](../pt-PT/README.md) | [پنجابی (گرموخی)](../pa/README.md) | [رومانیایی](../ro/README.md) | [روسی](../ru/README.md) | [صربستانی (سیریلیک)](../sr/README.md) | [اسلواکی](../sk/README.md) | [اسلوونیایی](../sl/README.md) | [اسپانیایی](../es/README.md) | [سواهیلی](../sw/README.md) | [سوئدی](../sv/README.md) | [تاگالوگ (فیلیپینی)](../tl/README.md) | [تامیلی](../ta/README.md) | [تلوگو](../te/README.md) | [تایلندی](../th/README.md) | [ترکی](../tr/README.md) | [اوکراینی](../uk/README.md) | [اردو](../ur/README.md) | [ویتنامی](../vi/README.md)

> **ترجیح می‌دهید به صورت محلی کلون کنید؟**
>
> این مخزن بیش از ۵۰ ترجمه زبانی دارد که به طور قابل توجهی حجم دانلود را افزایش می‌دهد. برای کلون کردن بدون ترجمه‌ها، از sparse checkout استفاده کنید:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (ویندوز):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> این به شما همه چیز لازم برای تکمیل دوره را با سرعت دانلود بسیار بالاتر می‌دهد.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## دوره‌ای که اصول چرخه عمر توسعه عامل هوش مصنوعی را آموزش می‌دهد

[![مجوز GitHub](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![مشارکت‌کنندگان GitHub](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![مسائل GitHub](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![درخواست‌های pull GitHub](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![درخواست‌های pull خوش آمدید](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 شروع کردن

این دوره درس‌هایی در مورد اصول ساخت و استقرار عامل‌های هوش مصنوعی دارد.

هر درس بر اساس درس قبلی ساخته می‌شود، بنابراین توصیه می‌کنیم از ابتدا شروع کنید و تا انتها پیش بروید.

اگر می‌خواهید بیشتر درباره موضوعات عامل هوش مصنوعی کاوش کنید، می‌توانید دوره [عامل‌های هوش مصنوعی برای مبتدیان](https://aka.ms/ai-agents-beginners) را بررسی کنید.

### ملاقات با سایر یادگیرندگان، دریافت پاسخ به سوالاتتان

اگر گیر کردید یا سوالی درباره ساخت عامل‌های هوش مصنوعی دارید، به کانال دیسکورد اختصاصی ما در [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6) بپیوندید.

### آنچه نیاز دارید

هر درس نمونه کد خاص خود را دارد که می‌توانید به صورت محلی اجرا کنید. می‌توانید این مخزن را [فورک کنید](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork) تا نسخه خودتان را بسازید.

این دوره در حال حاضر از موارد زیر استفاده می‌کند:

- [چارچوب عامل مایکروسافت (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [خدمات Azure OpenAI](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

لطفاً قبل از شروع مطمئن شوید که به این خدمات دسترسی دارید.

گزینه‌های بیشتری برای میزبانی مدل و سرویس‌ها به زودی اضافه خواهند شد.

## 🗃️ درس‌ها

| **درس**            | **توضیحات**                                                                                       |
|--------------------|--------------------------------------------------------------------------------------------------|
| [طراحی عامل](./lesson-1-agent-design/README.md)            | مقدمه‌ای بر مورد استفاده «آشنایی توسعه‌دهنده» و چگونگی طراحی عامل‌های موثر                  |
| [توسعه عامل](./lesson-2-agent-development/README.md)       | استفاده از چارچوب عامل مایکروسافت (MAF)، ساخت ۳ عامل برای کمک به آشنایی توسعه‌دهندگان جدید |
| [ارزیابی عامل](./lesson-3-agent-evals/README.md)           | با استفاده از Microsoft Foundry، بفهمید که عملکرد عامل‌های هوش مصنوعی چگونه است و چگونه بهبود یابند. |
| [استقرار عامل](./lesson-4-agent-deployment/README.md)      | استفاده از عامل‌های میزبانی شده و OpenAI Chatkit برای استقرار عامل هوش مصنوعی در تولید       |


## 🎒 دوره‌های دیگر

تیم ما دوره‌های دیگری هم تولید می‌کند! بررسی کنید:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j برای مبتدیان](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js برای مبتدیان](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain برای مبتدیان](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD برای مبتدیان](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![هوش مصنوعی Edge برای مبتدیان](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP برای مبتدیان](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![عامل‌های هوش مصنوعی برای مبتدیان](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### سری هوش مصنوعی مولد
[![هوش مصنوعی مولد برای مبتدیان](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![هوش مصنوعی مولد (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![هوش مصنوعی مولد (جاوا)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![هوش مصنوعی مولد (جاوا اسکریپت)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### یادگیری اصلی
[![یادگیری ماشین برای مبتدیان](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![علم داده برای مبتدی‌ها](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![هوش مصنوعی برای مبتدی‌ها](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![امنیت سایبری برای مبتدی‌ها](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![توسعه وب برای مبتدی‌ها](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![اینترنت اشیا برای مبتدی‌ها](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![توسعه XR برای مبتدی‌ها](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### مجموعه کپلوت
[![کپلوت برای برنامه‌نویسی جفتی هوش مصنوعی](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![کپلوت برای C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![ماجراجویی کپلوت](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## مشارکت

این پروژه از مشارکت‌ها و پیشنهادها استقبال می‌کند. بیشتر مشارکت‌ها نیازمند این هستند که شما با توافقنامه مجوز مشارکت‌کننده (CLA) موافقت کنید که اعلام می‌کند شما حق دارید و در واقع مجوز استفاده از مشارکت خود را به ما می‌دهید. برای جزئیات به <https://cla.opensource.microsoft.com> مراجعه کنید.

هرگاه یک درخواست Pull ارسال کنید، ربات CLA به‌طور خودکار تعیین می‌کند که آیا نیاز است یک CLA ارائه دهید و وضعیت PR را مطابق آن علامت‌گذاری می‌کند (مثلاً بررسی وضعیت، نظر). فقط کافی است دستورالعمل‌های ارائه شده توسط ربات را دنبال کنید. شما فقط یک بار در کل مخازن از این CLA استفاده خواهید کرد.

این پروژه «کد رفتار متن‌باز مایکروسافت» را پذیرفته است. برای اطلاعات بیشتر [سوالات متداول کد رفتار](https://opensource.microsoft.com/codeofconduct/faq/) را ببینید یا با [opencode@microsoft.com](mailto:opencode@microsoft.com) تماس بگیرید برای سوالات یا نظرات بیشتر.

## علائم تجاری

این پروژه ممکن است شامل علائم تجاری یا لوگوهایی برای پروژه‌ها، محصولات یا خدمات باشد. استفاده مجاز از علائم تجاری یا لوگوهای مایکروسافت مشروط بر رعایت و پیروی از [راهنمای علائم تجاری و برند مایکروسافت](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) است.
استفاده از علائم تجاری یا لوگوهای مایکروسافت در نسخه‌های تغییر یافته این پروژه نباید موجب سردرگمی شود یا دلالت بر حمایت مایکروسافت داشته باشد.
هرگونه استفاده از علائم تجاری یا لوگوهای شخص ثالث مشروط به سیاست‌های آن‌ها است.

## دریافت کمک

اگر مشکلی داشتید یا سوالی درباره ساخت اپلیکیشن‌های هوش مصنوعی داشتید، به:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

بپیوندید.

اگر بازخورد محصول یا خطا در حین ساخت داشتید به:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum) مراجعه کنید.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**توجه**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادقتی‌هایی باشند. سند اصلی به زبان بومی خود منبع معتبر و مورد استناد می‌باشد. برای اطلاعات حیاتی، استفاده از ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سو تفاهم یا برداشت نادرستی که ناشی از استفاده از این ترجمه باشد، نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->