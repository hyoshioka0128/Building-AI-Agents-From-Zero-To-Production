<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b09df38b3188ffe957c7ac8b055967f5",
  "translation_date": "2026-01-16T10:10:04+00:00",
  "source_file": "README.md",
  "language_code": "ml"
}
-->
# സെറോയിൽ നിന്ന് പ്രോഡക്ഷനിലേക്ക് AI ഏജൻറുകൾ നിർമ്മിക്കൽ

![സെറോയിൽ നിന്ന് പ്രോഡക്ഷനിലേക്ക് AI ഏജൻറുകൾ നിർമ്മിക്കൽ](../../../../translated_images/ml/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 ബഹുഭാഷാ പിന്തുണ

#### GitHub ആക്ഷൻ വഴി സാധ്യമാണ് (സ്വയംകൃതവും എന്നും പുതുക്കിപ്പോകുന്നതുമാണ്)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](./README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **സ്ഥാനീയമായി ക്ലോൺ ചെയ്യുന്നത് ഇഷ്ടമാണോ?**

> ഈ റിപ്പോസിറ്ററിയിൽ 50-കൂടി ഭാഷാ പരിഭാഷകളും ഉൾപ്പെടുത്തിയിരിക്കുന്നു, ഇത് ഡൗൺലോഡ് വലുപ്പം ഗണ്യമായി വർദ്ധിപ്പിക്കുന്നു. പരിഭാഷകൾ ഇല്ലാതെ ക്ലോൺ ചെയ്യാൻ sparse checkout ഉപയോഗിക്കുക:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> ഇതുവഴി കോഴ്‌സ് പൂർത്തിയാക്കാൻ വേണ്ട എല്ലാ കാര്യങ്ങളും വളരെ വേഗത്തിലുള്ള ഡൗൺലോഡ് ഉപയോഗിച്ച് ലഭിക്കും.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## AI ഏജന്റ് ഡെവലപ്പ്മെന്റ് ജീവിതചക്രത്തിന്റെ അടിസ്ഥാനങ്ങൾ പഠിപ്പിക്കുന്ന ഒരു കോഴ്‌സ്

[![GitHub ലൈസൻസ്](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub സംഭാവകർ](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub പ്രശ്നങ്ങൾ](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub പുൾ-റിക്വസ്റ്റുകൾ](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![പുൾ-റിക്വസ്റ്റുകൾ സ്വാഗതം ചെയ്യുന്നു](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 തുടക്കമെടുക്കല്‍

ഈ കോഴ്‌സിൽ AI ഏജൻറുകൾ നിർമ്മിക്കൽ, പ്രയോഗിക്കൽ എന്നീ അടിസ്ഥാന കാര്യങ്ങൾ ഉൾപ്പെടുത്തിയിരിക്കുന്ന പാഠങ്ങളുണ്ട്.

ഓരോ പാഠവും മുമ്പുള്ളതിൽനിന്ന് വികസിക്കുന്നു, അതിനാൽ തുടക്കത്തിൽ നിന്ന് ആരംഭിച്ച് അവസാനത്തോടെ എത്തുന്നത് നിങ്ങൾക്ക് ഉത്തമം.

AI ഏജൻറ് വിഷയങ്ങളിൽ കൂടുതൽ പരിശോദിക്കാനുള്ള ഇഷ്ടമുണ്ടെങ്കിൽ, [AI ഏജൻറുകൾ തുടങ്ങുന്നവർക്ക് കോഴ്‌സ്](https://aka.ms/ai-agents-beginners) പരിശോധിക്കാം.

### മറ്റ് പഠിച്ചുകാരെ കാണുക, നിങ്ങളുടെ ചോദ്യങ്ങൾക്ക് ഉത്തരമെടുക്കുക

AI ഏജൻറുകൾ നിർമ്മിക്കുന്നതിൽ തടസ്സമുണ്ടോ? ചോദ്യങ്ങളുണ്ടോ? [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6) ലെ നമ്മുടെ സമർപ്പിത Discord ചാനലിൽ ചേരുക.

### എന്ത് ആവശ്യമാണ്

ഓരോ പാഠത്തിന്റെയും സ്വന്തം കോഡ് സാമ്പിൾ ഉണ്ട്, ഇത് താങ്കൾക്ക് സ്റ്റാൻഡലോൺ ആയി റൺ ചെയ്യാനാകും. നിങ്ങളുടെ സ്വന്തം പകർപ്പ് ഉണ്ടാക്കാൻ [ഈ റിപ്പോ ഫോർക്ക് ചെയ്യാം](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork).

ഈ കോഴ്‌സ് ഇപ്പോൾ താഴെപ്പറയുന്നവയാണ് ഉപയോഗിക്കുന്നത്:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

തുടക്കവരെയൊക്കെ ഈ സേവനങ്ങളെക്കുറിച്ച് ആക്സസ് ഉള്ളതായിരിക്കണമെന്ന് ഉറപ്പാക്കുക.

മോഡൽ ഹോസ്റ്റിംഗും സേവനങ്ങളും സംബന്ധിച്ച കൂടുതൽ ഓപ്ഷനുകൾ വരാനിരിക്കുകയാണ്.

## 🗃️ പാഠങ്ങൾ

| **പാഠം**         | **വിവരണം**                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------|
| [ഏജൻറ് ഡിസൈൻ](./lesson-1-agent-design/README.md)       | ഞങ്ങളുടെ "ഡെവലപ്പർ ഓൺബോർഡിംഗ്" ഏജൻറ് ഉപയോഗകേസും ഫലപ്രദമായ ഏജൻറുകൾ രൂപകൽപ്പന ചെയ്യുന്നതിന്റെയും പ്രവേശനം  |
| [ഏജൻറ് ഡെവലപ്പ്മെന്റ്](./lesson-2-agent-development/README.md)  | Microsoft Agent Framework (MAF) ഉപയോഗിച്ച് പുതിയ ഡെവലപ്പർമാരെ പിന്തുണയ്ക്കാൻ 3 ഏജൻറുകൾ സൃഷ്ടിക്കുക.       |
| [ഏജൻറ് മൂല്യനിർണയം](./lesson-3-agent-evals/README.md)  | Microsoft Foundry ഉപയോഗിച്ച് AI ഏജൻറുകളുടെ പ്രകടനം എത്രമാത്രം മെച്ചമാണ് എന്ന് കണ്ടെത്തുകയും മെച്ചപ്പെടുത്താൻ ശ്രമിക്കുക. |
| [ഏജൻറ് പ്രയോഗം](./lesson-4-agent-deployment/README.md)   | Hosted Agents ഉം OpenAI Chatkit ഉം ഉപയോഗിച്ച് AI ഏജൻറ് പ്രോഡക്ഷൻ പരിസ്ഥിതിയിലേക്ക് എങ്ങനെ പ്രയോഗിക്കാമെന്നും കാണുക.       |


## 🎒 മറ്റു കോഴ്‌സുകൾ

നമ്മുടെ ടീം മറ്റ് കോഴ്‌സുകളും ഉണ്ട്! പരിശോധിക്കൂ:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / എഡ്ജ് / MCP / ഏജൻറുകൾ
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### ജനറേറ്റീവ് AI സീരീസ്
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### കോർ ലേണിംഗ്
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![ആരംഭക്കാർക്ക് സൈബർസെക്യൂരിറ്റി](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![ആരംഭക്കാർക്ക് വെബ് ഡെവ്](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![ആരംഭക്കാർക്ക് ഐഒടി](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![ആരംഭക്കാർക്ക് XR ഡെവലപ്പ്മെന്റ്](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### കോപൈലറ്റ് സീരീസ്
[![AI കൂടിയ ഘടനാപ്രോഗ്രാമിംഗിന് കോപൈലറ്റ്](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET-ക്ക് കോപൈലറ്റ്](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![കോപൈലറ്റ് അഡ്വഞ്ചർ](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## സംഭാവന ചെയ്യൽ

ഈ പ്രോജക്ട് സംഭാവനകളും നിർദേശങ്ങളും സ്വാഗതം ചെയ്യുന്നു. മിക്ക സംഭാവനകൾക്കും നിങ്ങൾക്ക് നിങ്ങളുടെ സംഭാവനയുടെ ഉപയോഗാവകാശം നൽകാനുള്ള അവകാശവും वास्तवമായി അനുവദിക്കുന്നുമാണെന്ന് പ്രഖ്യാപിക്കുന്ന ഒരു 
Contributor License Agreement (CLA) യിൽ համաձայնം നൽകേണ്ടതാണ്. വിശദമായ വിവരങ്ങൾക്ക് <https://cla.opensource.microsoft.com> സന്ദർശിക്കുക.

നിങ്ങൾ pull request സമർപ്പിക്കുമ്പോൾ, CLA ബോട്ട് സ്വയം ഇത് നിർണയിക്കും നിങ്ങൾ CLA നൽകേണ്ടതുണ്ടോ എന്നു, അനുയോജ്യമായ രീതിയിൽ PR അലങ്കരിക്കും (ഉദാഹരണത്തിന്, സ്റ്റാറ്റസ് ചെക്ക്, കമന്റ്). ബോട്ട് നൽകിയ നിർദ്ദേശങ്ങൾ പാലിക്കുക. നമ്മുടെ CLA ഉപയോഗിക്കുന്ന എല്ലാ റിപ്പോസിറ്ററികളിലും നിങ്ങൾക്ക് ഇത് ഒരിക്കൽ മാത്രമേ ചെയ്യേണ്ടതുള്ളൂ.

ഈ പ്രോജക്ട് [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ആണ് സ്വീകരിച്ചിരിക്കുന്നത്.
കൂടുതൽ വിവരങ്ങൾക്ക് [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) കാണുക അല്ലെങ്കിൽ 
[opencode@microsoft.com](mailto:opencode@microsoft.com)  വഴി എന്തെങ്കിലും ചോദ്യങ്ങളോ അഭിപ്രായങ്ങളോ ചോദിക്കുക.

## ട്രേഡ് മാർക്കുകൾ

ഈ പ്രോജക്ടിൽ പ്രോജക്ടുകൾ, ഉൽപ്പന്നങ്ങൾ, സേവനങ്ങൾ എന്നിവയ്ക്ക് ട്രേഡ് മാർക്കുകളോ ലോഗോകളോ ഉണ്ടാകാം. Microsoft ട്രേഡ് മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകൾ അധികൃതി ഉപയോഗം 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) അനുസരിക്കണം.
മാറ്റങ്ങളോടെയോ ഈ പ്രോജക്ടിന്റെ വേര്‍ഷനുകളിലോ Microsoft ട്രേഡ് മാർക്ക് അല്ലെങ്കിൽ ലോഗോകൾ ഉപയോഗിക്കുന്നത് kafa വാൽപെട്ടുതന്നെയോ, അല്ലെങ്കിൽ Microsoftയുടെ സ്പോൺസർഷിപ്പ് സൂചിപ്പിക്കരുത്.
മൂന്ന് পক্ষത്തെ ട്രേഡ് മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകൾ ഉപയോഗിക്കുന്നത് ആ ട്രിഡ് പാർട്ടികളുടെ നയങ്ങൾ അനുസരിച്ചിരിക്കേണ്ടതാണ്.

## സഹായം ലഭിക്കുക

AI ആപ്പുകൾ നിർമ്മിക്കുന്നതിൽ ആശങ്കയോ ചോദ്യങ്ങളോ ഉണ്ടെങ്കിൽ, ചേരുക:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

ഉൽപ്പന്ന പ്രതികരണം നൽകുകയോ പിഴവുകൾ റിപ്പോർട്ട് ചെയ്യുകയോ ചെയ്യുവാൻ സന്ദർശിക്കുക:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**കുറിപ്പാക്കൽ**:  
ഈ പ്രമാണം AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ ശ്രേഷ്ടതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, സ്വയമേവ പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ अथവ അശുദ്ധികൾ ഉണ്ടായിരിക്കാൻ സാധ്യതയുണ്ട്. പ്രമാണത്തിന്റെ മാതൃഭാഷയിൽ ഉള്ള ഉദ്ദേശപ്രകാരം പ്രാമാണികമായ ഉറവിടമായിരിക്കും. പ്രധാനപ്പെട്ട വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യൻ നിർവഹിക്കുന്ന വിവർത്തനം അഭ്യർത്ഥിക്കുന്നു. ഈ വിവർത്തനം ഉപയോഗിച്ചതിനെത്തുടർന്നുണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾക്കും വ്യാഖ്യാനക്കുറവുകൾക്കും ഞങ്ങൾ ഉത്തരവാദിത്വം ഏറ്റെടുക്കുന്നില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->