# ശൂന്യത്തില്‍ നിന്ന് ഉത്പാദനത്തിലേക്കുള്ള AI ഏജന്റുകള്‍ നിർമ്മിക്കല്‍

![Building AI Agents from Zero to Production](../../translated_images/ml/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 ബഹുഭാഷാ പിന്തുണ

#### GitHub ആക്ഷനിലൂടെ പിന്തുണ (സ്വയം چلിക്കുകയും എല്ലായ്പ്പോഴും പുതുക്കുകയും ചെയ്യുന്നു)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](./README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **പ്രാദേശികമായി ക്ലോൺ ചെയ്യാൻ ആഗ്രഹിക്കുന്നുവോ?**

> ഈ റിപോസിറ്ററിയിൽ 50-ത്തിലധികം ഭാഷാ പരിഭാഷകൾ ഉണ്ട്, ഇത് ഡൗൺലോഡ് വലിപ്പം കൂടുതലാക്കും. പരിഭാഷകൾ ഇല്ലാതെ ക്ലോൺ ചെയ്യാൻ sparse checkout ഉപയോഗിക്കുക:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> ഇത് നിങ്ങൾക്ക് കോഴ്സ് പൂര്‍ത്തിയാക്കാൻ വേണ്ടിയുള്ള എല്ലാ കാര്യങ്ങളും ലഭ്യമാക്കും, കൂടാതെ ഡൗൺലോഡ് വേഗത വളരെ കൂടുതലാകും.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## AI ഏജന്റ് വികസന ജീവിതചക്രം അടിസ്ഥാനപരമായി പഠിപ്പിക്കുന്ന ഒരു കോഴ്‌സ്

[![GitHub license](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 ആരംഭിക്കൽ

ഈ കോഴ്‌സിൽ AI ഏജന്റുകൾ നിർമ്മിക്കൽ, വിനിയോഗിക്കൽ എന്നിവയുടെ അടിസ്ഥാനങ്ങൾ പഠിപ്പിക്കുന്നു.

ഓരോ പാഠവും മുൻപത്തെ പാഠത്തെ അടിസ്ഥാനമാക്കി നിർമ്മിക്കപ്പെട്ടതാണ്, അതിനാൽ ആദ്യം മുതൽ ആരംഭിച്ച് അവസാനം വരെ തുടരാൻ ഞങ്ങൾ ശുപാർശ ചെയ്യുന്നു.

AI ഏജന്റ് വിഷയങ്ങളിൽ കൂടുതൽ പഠിക്കാൻ ആഗ്രഹിക്കുന്നുവെങ്കിൽ, [AI Agents For Beginners Course](https://aka.ms/ai-agents-beginners) സന്ദർശിക്കാം.

### മറ്റു പഠനാർത്ഥികളുമായി പരിചിതരാകുക, നിങ്ങളുടെ ചോദ്യങ്ങൾക്കുള്ള ഉത്തരങ്ങൾ നേടുക

AI ഏജന്റുകൾ നിർമ്മിക്കുന്നതിനുള്ള ചോദ്യങ്ങൾ ഉണ്ടെങ്കിൽ, ഞങ്ങളുടെ Microsoft Foundry Discord ൽ ഉള്ള സമർപ്പിത Discord ചാനലിൽ ചേരുക: [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6).

### നിങ്ങൾക് വേണ്ടത്

ഓരോ പാഠത്തിനും പ്രാദേശികമായി ഓടിക്കാൻ കഴിയുന്ന സ്വന്തം കോഡ് സാമ്പിൾ ഉണ്ട്. നിങ്ങളുടെ സ്വന്തം പകർപ്പ് സൃഷ്ടിക്കാൻ [ഈ റിപൊഫോർക്കുചെയ്യാം](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork).

ഈ കോഴ്‌സ് നിലവിൽ ഇവ വിനിയോഗിക്കുന്നു:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

കൂടുതൽ തുടങ്ങുന്നതിന് മുമ്പ് ഈ സേവനങ്ങൾക്ക് നിങ്ങൾക്ക് പ്രവേശനം ഉണ്ടെന്ന് ഉറപ്പാക്കുക.

മോഡൽ ഹോസ്റ്റിങ്ങ്, സേവനങ്ങൾ സംബന്ധിച്ച് മറ്റ് ഓപ്ഷനുകളും ഉടൻ വരുന്നു.

## 🗃️ പാഠങ്ങൾ

| **പാഠം**         | **വിവരണം**                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------|
| [Agent Design](./lesson-1-agent-design/README.md)       | ഞങ്ങളുടെ "ഡെവലപ്പർ ഓൺബോർഡിങ്" ഏജന്റ് ഉപയോഗകേസിലും എഫക്റ്റീവ് ഏജന്റുകൾ രൂപകല്‍പ്പന ചെയ്യുന്നതിനും ഒരു പരിചയം   |
| [Agent Development](./lesson-2-agent-development/README.md)  | Microsoft Agent Framework (MAF) ഉപയോഗിച്ച്, പുതിയ ഡെവലപ്പർമാർ ഓൺബോർഡ് ചെയ്യാൻ 3 ഏജന്റുകൾ സൃഷ്ടിക്കുക.       |
| [Agent Evaluations](./lesson-3-agent-evals/README.md)  | Microsoft Foundry ഉപയോഗിച്ച്, ഞങ്ങളുടെ AI ഏജന്റുകൾ എത്രത്തോളം നന്നായി പ്രവർത്തിക്കുന്നു എന്ന് കണ്ടെത്തുകയും മെച്ചപ്പെടുത്തുക. |
| [Agent Deployment](./lesson-4-agent-deployment/README.md)   | ഹോസ്റ്റുചെയ്ത ഏജന്റുകളും OpenAI Chatkitഉം ഉപയോഗിച്ച്, ഉത്പാദനത്തിന് AI ഏജന്റിനെ എങ്ങനെ വിനിയോഗിക്കാമെന്ന് കാണുക.       |


## 🎒 മറ്റ് കോഴ്‌സുകൾ

ഞങ്ങളുടെ ടീം മറ്റ് കോഴ്‌സുകളും നല്കുന്നു! പരിശോധിക്കുക:

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
 
### മുഖ്യ പഠനം
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![ആരംഭക്കാർക്കുള്ള AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![ആരംഭക്കാർക്കുള്ള സൈബർസെക്യൂരിറ്റി](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![ആരംഭക്കാർക്കുള്ള വെബ് ഡെവ്](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![ആരംഭക്കാർക്കുള്ള IoT](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![ആരംഭക്കാർക്കുള്ള XR ഡെവലപ്മെന്റ്](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### കോപിലോട്ട് സീരീസ്
[![AI സഹയോക്തൃ പ്രോഗ്രാമിങ്ങിനുള്ള കോപിലോട്ട്](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET കോപിലോട്ട്](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![കോപിലോട്ട് അഡ്വഞ്ചർ](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## സംഭാവന

ഈ പ്രൊജക്റ്റ് സംഭാവനകളും നിർദ്ദേശങ്ങളും സ്വാഗതം ചെയ്യുന്നു.  പല സംഭാവനകളും Contributor License Agreement (CLA)–യോട് സമ്മതിക്കുക എന്നത് ആവശ്യമാണ്, അത് നിങ്ങൾക്കുള്ള അവകാശങ്ങൾ ഇവിടെ നൽകിയ സംഭാവന ഉപയോഗിക്കാൻ നൽകുന്നതാണെന്ന് നിങ്ങൾ പ്രഖ്യാപിക്കുന്നതാണ്. വിശദാംശങ്ങൾക്ക് <https://cla.opensource.microsoft.com> സന്ദർശിക്കുക.

നീங்கள் ഒരു പുള്‍ അഭ്യർത്ഥന സമർപ്പിക്കുമ്പോൾ, CLA ബോട്ട് നിങ്ങളുടെ CLA നൽകേണ്ടതുണ്ടോ എന്ന് സ്വയം നിർണയിക്കുകയും പിആർ വേണ്ട രീതിയിൽ (ഉദാ., സ്ഥിതിയുടെ പരിശോധന, പരാമർശം) അലങ്കരിക്കുകയും ചെയ്യും. ബോട്ട് നൽകിയ നിർദേശങ്ങളെ അനുസരിക്കുക. ഞങ്ങളുടെ CLA ഉപയോഗിക്കുന്ന എല്ലാ റിപോസിറ്ററികളിലും ഇത് ഒരുമിച്ചുള്ള കാര്യമാണ്.

ഈ പ്രോജക്റ്റ് [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) സ്വീകരിക്കുന്നു. കൂടുതൽ വിവരങ്ങൾക്ക് [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) കാണുക അല്ലെങ്കിൽ കൂടുതൽ ചോദിക്കുകയാണെങ്കിൽ [opencode@microsoft.com](mailto:opencode@microsoft.com) എന്ന വിലാസത്തിലേക്ക് ബന്ധപ്പെടുക.

## ട്രേഡ്‌മാർക്കുകൾ

ഈ പ്രോജക്റ്റിൽ പ്രോജക്റ്റുകൾ, ഉൽപ്പന്നങ്ങൾ, സേവനങ്ങൾ എന്നിവയ്ക്ക് ട്രേഡ്‌മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകൾ ഉണ്ടാകാം. മൈക്രോസോഫ്റ്റിന്റെ ട്രേഡ്‌മാർക്കുകളോ ലോഗോകളോ ഉള്ള അംഗീകൃത ഉപയോഗം [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) അനുയോജ്യമായും പാലിക്കേണ്ടതാണ്. മൈക്രോസോഫ്റ്റിന്റെ ട്രേഡ്‌മാർക്കുകളോ ലോഗോകളോ ഉള്ള ഈ പ്രോജക്റ്റിന്റെ മാറ്റിയ പതിപ്പുകളിൽ ഉപയോഗം 혼란മോ മൈക്രോസോഫ്റ്റ് അദ്ധ്യക്ഷത imply ചെയ്യുന്നതോ ആയിരിക്കരുത്. മൂന്നാം പാര്‍ട്ടി ട്രേഡ്‌മാർക്കുകളോ ലോഗോകളോ ഉള്ള എല്ലാ ഉപയോഗവും ആ മൂന്നാം പാർട്ടി നയങ്ങൾക്ക് വിധേയമാണ്.

## സഹായം നേടുക

നിങ്ങൾ കുടുങ്ങിയാൽ അല്ലെങ്കിൽ AI ആപ്പുകൾ നിർമ്മിക്കുമ്പോൾ എന്തെങ്കിലും സംശയങ്ങൾ ഉണ്ടെങ്കിൽ, ചേരുക:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

നിങ്ങൾക്ക് ഉൽപ്പന്ന ഫീഡ്ബാക്ക് ലഭിക്കുകയാണെങ്കിൽ അല്ലെങ്കിൽ നിർമ്മാണത്തിൽ പിഴവുകൾ ഉണ്ടെങ്കിൽ സന്ദർശിക്കുക:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ ഡോക്യുമെന്റ് AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്‌തിരിക്കുന്നു. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിഴവുകൾ അല്ലെങ്കിൽ അശുദ്ധികളാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. നിലവിലുള്ള ഭാഷയിലുള്ള ഒറിജിനൽ ഡോക്യുമെന്റാണ് പ്രാമാണികമായ ഉറവിടം. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിനാൽ ഉണ്ടാകുന്ന ഏതു പശ്ചാത്തലങ്ങളോ തെറ്റിദ്ധാരണകൾക്കോ നാം ഉത്തരവാദികൾ അല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->