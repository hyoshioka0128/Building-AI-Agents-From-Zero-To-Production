<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b09df38b3188ffe957c7ac8b055967f5",
  "translation_date": "2026-01-16T09:59:44+00:00",
  "source_file": "README.md",
  "language_code": "et"
}
-->
# Tehisintellekti agentide loomine nullist tootmisse

![Tehisintellekti agentide loomine nullist tootmisse](../../../../translated_images/et/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 Mitmekeelne tugi

#### Toetatud GitHub Action’i kaudu (automaatne ja alati ajakohane)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[araabia](../ar/README.md) | [bengali](../bn/README.md) | [bulgaaria](../bg/README.md) | [burma (Myanmar)](../my/README.md) | [hiina (lihtsustatud)](../zh/README.md) | [hiina (traditsiooniline, Hongkong)](../hk/README.md) | [hiina (traditsiooniline, Macao)](../mo/README.md) | [hiina (traditsiooniline, Taiwan)](../tw/README.md) | [horvaadi](../hr/README.md) | [tšehhi](../cs/README.md) | [taani](../da/README.md) | [hollandi](../nl/README.md) | [eesti](./README.md) | [soome](../fi/README.md) | [prantsuse](../fr/README.md) | [saksa](../de/README.md) | [kreeka](../el/README.md) | [heebrea](../he/README.md) | [hindi](../hi/README.md) | [ungari](../hu/README.md) | [indoneesia](../id/README.md) | [itaalia](../it/README.md) | [jaapani](../ja/README.md) | [kannada](../kn/README.md) | [korea](../ko/README.md) | [leedu](../lt/README.md) | [malai](../ms/README.md) | [malajalami](../ml/README.md) | [marathi](../mr/README.md) | [nepali](../ne/README.md) | [Nigeeria pidgin](../pcm/README.md) | [norra](../no/README.md) | [päritud (Farsi)](../fa/README.md) | [poola](../pl/README.md) | [portugali (Brasiilia)](../br/README.md) | [portugali (Portugal)](../pt/README.md) | [pandžabi (Gurmukhi)](../pa/README.md) | [rumeenia](../ro/README.md) | [vene](../ru/README.md) | [serbia (kirillitsa)](../sr/README.md) | [slovaki](../sk/README.md) | [sloveeni](../sl/README.md) | [hispaania](../es/README.md) | [suahiili](../sw/README.md) | [rootsi](../sv/README.md) | [tagalogi (filipino)](../tl/README.md) | [tamiili](../ta/README.md) | [telugu](../te/README.md) | [tai](../th/README.md) | [türgi](../tr/README.md) | [ukraina](../uk/README.md) | [urdu](../ur/README.md) | [vietnami](../vi/README.md)

> **Eelistad kloonida lokaalselt?**

> See hoidla sisaldab üle 50 keele tõlget, mis suurendab allalaadimise mahtu märkimisväärselt. Tõlgeteta kloonimiseks kasuta sparse checkout’i:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> See annab sulle kogu vajaliku kursuse läbimiseks palju kiirema allalaadimise.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Kursus, mis õpetab sulle tehisintellekti agendi arendusprotsessi põhialuseid

[![GitHub litsents](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub panustajad](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub probleemid](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub päringud](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PR-d on teretulnud](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 Alustamine

See kursus sisaldab õppetunde, mis käsitlevad tehisintellekti agentide loomise ja kasutuselevõtu põhialuseid.

Iga õppetund tugineb eelnevale, seega soovitame alustada algusest ja liikuda järk-järgult lõpuni.

Kui soovid AI agentide teemadel rohkem teada saada, võid vaadata [AI Agents For Beginners Course](https://aka.ms/ai-agents-beginners).

### Tutvu teiste õppijatega, saa oma küsimustele vastused

Kui jääd hätta või sul on küsimusi tehisintellekti agentide ehitamise kohta, liitu meie spetsiaalse Discordi kanaliga [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6).

### Mida vajad

Igal õppetunnil on oma näidiskood, mida saad kohalikult käivitada. Saad selle hoidla [forkida](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork) ja luua oma koopia.

See kursus kasutab hetkel järgmisi vahendeid:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI teenus](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

Palun veendu, et sul oleks juurdepääs neile teenustele enne alustamist.

Peagi lisanduvad rohkem võimalusi mudelite majutamise ja teenuste kohta.

## 🗃️ Õppetunnid

| **Õppetund**                  | **Kirjeldus**                                                                                 |
|----------------------------|------------------------------------------------------------------------------------------------|
| [Agendi disain](./lesson-1-agent-design/README.md)               | Sissejuhatus meie "Arendaja juhendamise" agendi kasutusjuhusse ja tõhusate agentide loomisesse |
| [Agendi arendus](./lesson-2-agent-development/README.md)         | Microsoft Agent Frameworki (MAF) abil loo 3 agenti, et aidata uutel arendajatel sisse elada.   |
| [Agendi hindamine](./lesson-3-agent-evals/README.md)              | Microsoft Foundryt kasutades saad teada, kui hästi meie AI agentidel läheb ja kuidas neid paremaks teha. |
| [Agendi juurutamine](./lesson-4-agent-deployment/README.md)      | Kasutades hostitud agente ja OpenAI Chatkit’i, õpi, kuidas AI agenti tootmisse lansseerida.   |


## 🎒 Teised kursused

Meie meeskond loob ka teisi kursuseid! Tutvu nendega:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j algajatele](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js algajatele](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agendid
[![AZD algajatele](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI algajatele](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP algajatele](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI agendid algajatele](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatiivse AI sari
[![Generatiivne AI algajatele](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatiivne AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatiivne AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatiivne AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Põhiteadmised
[![ML algajatele](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Andmeteadus algajatele](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI algajatele](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot'i sari
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Panustamine

See projekt tervitab panuseid ja ettepanekuid. Enamik panustest nõuab, et nõustuksite
panustajate litsentsilepingu (CLA) tingimustega, milles kinnitate, et teil on õigus ja te tegelikult annate meile õiguse kasutada teie panust. Lisateabe saamiseks külastage <https://cla.opensource.microsoft.com>.

Kui esitate tõmbepäringu (pull request), määrab CLA bot automaatselt, kas teil on vaja CLA-d esitada
ning märgistab PR sobivalt (nt oleku kontroll, kommentaar). Järgige lihtsalt boti juhiseid. Seda tuleb
kõigi CLA-ga kasutatavate hoidlate puhul teha vaid üks kord.

See projekt on vastu võtnud [Microsofti avatud lähtekoodi käitumiskoodeksi](https://opensource.microsoft.com/codeofconduct/).
Lisateabe saamiseks vaadake [käitumiskoodeksi KKK-d](https://opensource.microsoft.com/codeofconduct/faq/) või võtke ühendust aadressil [opencode@microsoft.com](mailto:opencode@microsoft.com) lisaküsimuste või kommentaaride korral.

## Kaubamärgid

See projekt võib sisaldada projektide, toodete või teenuste kaubamärke või logosid. Microsofti
kaubamärkide või logode volitatud kasutamine peab vastama
[Microsofti kaubamärkide ja brändijuhistele](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Microsofti kaubamärkide või logode kasutamine selle projekti muudetud versioonides ei tohi põhjustada segadust ega viidata Microsofti sponsorlusele.
Kolmandate osapoolte kaubamärkide või logode kasutamine kuulub nende osapoolte poliitikate alla.

## Abi saamine

Kui jääte ummikusse või teil on küsimusi AI rakenduste ehitamise kohta, liituge:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

Kui teil on tootepalaute või ehitamisel ilmnevaid vigu, külastage:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest vabastamine**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse professionaalset inimese poolt tehtud tõlget. Me ei vastuta selle tõlke kasutamisest tingitud arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->