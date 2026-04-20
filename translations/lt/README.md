# Dirbtinio intelekto agentų kūrimas nuo nulio iki produkcijos

![Dirbtinio intelekto agentų kūrimas nuo nulio iki produkcijos](../../translated_images/lt/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 Daugiafunkcinė kalbų palaikymas

#### Palaikoma per GitHub Action (automatizuota ir visada atnaujinta)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](./README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Norite išklonuoti vietoje?**
>
> Šis saugykla turi daugiau nei 50 kalbų vertimų, todėl žymiai padidėja atsisiuntimo dydis. Norėdami klonuoti be vertimų, naudokite dalinę ištrauką (sparse checkout):
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Tai suteiks jums viską, ko reikia, norint greičiau atsisiųsti kursą ir jį įvykdyti.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Kursas apie AI agentų kūrimo gyvavimo ciklo pagrindus

[![GitHub licencija](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub bendradarbiai](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub problemos](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-užklausos](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs laukiami](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 Pradžia

Šis kursas apima pamokas apie AI agentų kūrimo ir diegimo pagrindus.

Kiekviena pamoka grindžiama ankstesne, todėl rekomenduojame pradėti nuo pradžios ir žingsnis po žingsnio siekti pabaigos.

Jei norite sužinoti daugiau apie AI agentų temas, galite patikrinti [AI agentų pradedančiųjų kursą](https://aka.ms/ai-agents-beginners).

### Susipažinkite su kitais besimokančiais ir gaukite atsakymus į savo klausimus

Jei užstrigote ar turite klausimų apie AI agentų kūrimą, prisijunkite prie specialaus Discord kanalo [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6).

### Ko jums reikia

Kiekviena pamoka turi savo kodo pavyzdį, kurį galite paleisti vietoje. Galite [forkinti šį saugyklą](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork) ir sukurti savo kopiją.

Šiame kurse šiuo metu naudojame:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI paslauga](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

Prieš pradėdami, įsitikinkite, kad turite prieigą prie šių paslaugų.

Netolimoje ateityje planuojamos kitos galimybės modelių talpinimui ir paslaugoms.

## 🗃️ Pamokos

| **Pamoka**         | **Aprašymas**                                                                                     |
|--------------------|-------------------------------------------------------------------------------------------------|
| [Agentų dizainas](./lesson-1-agent-design/README.md)       | Įvadas į mūsų "Kūrėjo įtraukimą" agentų naudojimo atvejį ir kaip kurti veiksmingus agentus       |
| [Agentų kūrimas](./lesson-2-agent-development/README.md)  | Naudojant Microsoft Agent Framework (MAF) sukurkite 3 agentus, kurie padėtų naujiems kūrėjams     |
| [Agentų vertinimas](./lesson-3-agent-evals/README.md)     | Naudojant Microsoft Foundry sužinokite, kaip gerai veikia mūsų AI agentai ir kaip juos galima pagerinti |
| [Agentų diegimas](./lesson-4-agent-deployment/README.md)  | Naudojant Hosted Agents ir OpenAI Chatkit pamatykite, kaip diegti AI agentą gamyboje             |

## 🎒 Kiti kursai

Mūsų komanda kuria ir kitus kursus! Peržiūrėkite:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j pradedantiesiems](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js pradedantiesiems](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain pradedantiesiems](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agentai
[![AZD pradedantiesiems](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI pradedantiesiems](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP pradedantiesiems](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI agentai pradedantiesiems](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatyviojo dirbtinio intelekto serija
[![Generatyviojo DI pradedantiesiems](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatyviojo DI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatyviojo DI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatyviojo DI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Pagrindinis mokymasis
[![ML pradedantiesiems](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Duomenų mokslas pradedantiesiems](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![DI pradedantiesiems](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kibernetinis saugumas pradedantiesiems](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Interneto svetainių kūrimas pradedantiesiems](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![Daiktų internetas pradedantiesiems](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![Imersinių technologijų kūrimas pradedantiesiems](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot serija
[![Copilot dirbant kartu su DI programuojant](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET programuotojams](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot nuotykiai](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Prisidėjimas

Šis projektas laukia indėlių ir pasiūlymų. Daugumai indėlių reikia, kad sutiktumėte su
Indėlio davėjo licencijos sutartimi (Contributor License Agreement, CLA), kurioje teigiate, kad turite teisę ir iš tiesų suteikiate mums
teisę naudoti jūsų indėlį. Daugiau informacijos rasite <https://cla.opensource.microsoft.com>.

Pateikus šakos užklausą (pull request), CLA robotas automatiškai nustatys, ar jums reikia pateikti CLA,
ir pažymės šią PR atitinkamai (pvz., statuso patikra, komentaras). Tiesiog sekite
roboto nurodymus. Tai reikės padaryti tik kartą visuose repozitorijuose, naudojančiuose mūsų CLA.

Šis projektas priėmė [Microsoft atvirojo kodo elgesio kodeksą](https://opensource.microsoft.com/codeofconduct/).
Daugiau informacijos rasite [Elgesio kodekso DUK](https://opensource.microsoft.com/codeofconduct/faq/) arba
kreipkitės į [opencode@microsoft.com](mailto:opencode@microsoft.com) su papildomais klausimais ar komentarais.

## Prekės ženklai

Šis projektas gali turėti projektų, produktų ar paslaugų prekių ženklų arba logotipų. Leidžiamas Microsoft
prekių ženklų ar logotipų naudojimas priklauso ir turi atitikti
[Microsoft prekės ženklų ir prekės ženklo vadovus](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Modifikuotose projekto versijose Microsoft prekių ženklų ar logotipų naudojimas negali sukelti painiavos ar reikšti Microsoft rėmimą.
Trečiųjų šalių prekių ženklų ar logotipų naudojimas priklauso tų trečiųjų šalių politikoms.

## Pagalba

Jei įstringate arba turite klausimų apie DI programėlių kūrimą, prisijunkite prie:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

Jei turite produktų atsiliepimų ar klaidų, susijusių su kūrimu, apsilankykite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojame naudoti profesionalų žmogaus vertimą. Mes neatsakome už bet kokius nesusipratimus ar neteisingus interpretavimus, kilusius naudojant šį vertimą.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->