# Rakennetaan tekoälyagentteja nollasta tuotantoon

![Rakennetaan tekoälyagentteja nollasta tuotantoon](../../translated_images/fi/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 Monikielinen tuki

#### Tuettu GitHub-toiminnon kautta (automaattinen ja aina ajan tasalla)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[arabia](../ar/README.md) | [bengali](../bn/README.md) | [bulgaria](../bg/README.md) | [burma (myanmar)](../my/README.md) | [kiina (yksinkertaistettu)](../zh-CN/README.md) | [kiina (perinteinen, hongkong)](../zh-HK/README.md) | [kiina (perinteinen, macau)](../zh-MO/README.md) | [kiina (perinteinen, taiwan)](../zh-TW/README.md) | [kroatia](../hr/README.md) | [tšekki](../cs/README.md) | [tanska](../da/README.md) | [hollanti](../nl/README.md) | [viro](../et/README.md) | [suomi](./README.md) | [ranska](../fr/README.md) | [saksa](../de/README.md) | [kreikka](../el/README.md) | [heprea](../he/README.md) | [hindi](../hi/README.md) | [unkari](../hu/README.md) | [indonesian](../id/README.md) | [italia](../it/README.md) | [japani](../ja/README.md) | [kannada](../kn/README.md) | [khmer](../km/README.md) | [korea](../ko/README.md) | [liettua](../lt/README.md) | [malaiji](../ms/README.md) | [malayalam](../ml/README.md) | [marathi](../mr/README.md) | [nepali](../ne/README.md) | [nigerian pidgin](../pcm/README.md) | [norja](../no/README.md) | [persia (farsi)](../fa/README.md) | [puola](../pl/README.md) | [portugali (brasilia)](../pt-BR/README.md) | [portugali (portugali)](../pt-PT/README.md) | [pandžabi (gurmukhi)](../pa/README.md) | [romania](../ro/README.md) | [venäjä](../ru/README.md) | [serbia (kyrillinen)](../sr/README.md) | [slovakki](../sk/README.md) | [sloveeni](../sl/README.md) | [espanja](../es/README.md) | [swahili](../sw/README.md) | [ruotsi](../sv/README.md) | [tagalog (filipino)](../tl/README.md) | [tamili](../ta/README.md) | [telugu](../te/README.md) | [thai](../th/README.md) | [turkki](../tr/README.md) | [ukraina](../uk/README.md) | [urdu](../ur/README.md) | [vietnam](../vi/README.md)

> **Haluatko kloonata paikallisesti?**
>
> Tämä arkisto sisältää yli 50 käännöstä eri kielille, mikä lisää merkittävästi latauskokoa. Jos haluat kloonata ilman käännöksiä, käytä harvaa valintaa (sparse checkout):
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
> Tämä antaa sinulle kaiken tarvittavan kurssin suorittamiseen huomattavasti nopeammalla latauksella.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Kurssi, joka opettaa tekoälyagenttien kehityssyklin perusteet

[![GitHub-lisenssi](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub-yhteistyökumppanit](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub-ongelmat](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub-pyynnöt](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PR:t ovat tervetulleita](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 Aloittaminen

Tämä kurssi sisältää oppitunteja tekoälyagenttien rakentamisen ja käyttöönoton perusteista.

Jokainen oppitunti rakentuu edellisen päälle, joten suosittelemme aloittamaan alusta ja etenemään loppuun saakka.

Jos haluat tutustua lisää tekoälyagenttien aiheisiin, voit kurkata [Tekoälyagenttien aloittelijan kurssin](https://aka.ms/ai-agents-beginners).

### Tapaa muita oppijoita, saat vastauksia kysymyksiisi

Jos jäädyt tai sinulla on kysyttävää tekoälyagenttien rakentamisesta, liity omistettuun Discord-kanavaamme [Microsoft Foundry Discordissa](https://discord.gg/Kuaw3ktsu6).

### Mitä tarvitset

Jokaisella oppitunnilla on oma koodinäytteensä, jonka voit ajaa paikallisesti. Voit [forkata tämän arkiston](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork) luodaksesi oman kopiosi.

Tämä kurssi käyttää tällä hetkellä seuraavia:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

Varmista, että sinulla on pääsy näihin palveluihin ennen aloittamista.

Lisää vaihtoehtoja mallien isännöinnille ja palveluille tulossa pian.

## 🗃️ Oppitunnit

| **Oppitunti**         | **Kuvaus**                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------|
| [Agentin suunnittelu](./lesson-1-agent-design/README.md)       | Johdanto “Kehittäjän perehdytys” -agenttikäyttötapaukseemme ja tehokkaiden agenttien suunnitteluun  |
| [Agentin kehitys](./lesson-2-agent-development/README.md)  | Microsoft Agent Frameworkin (MAF) avulla luodaan 3 agenttia auttamaan uusia kehittäjiä perehdytyksessä.       |
| [Agentin arvioinnit](./lesson-3-agent-evals/README.md)  | Microsoft Foundryn avulla selvitetään, miten hyvin tekoälyagenttimme toimivat ja miten niitä voi parantaa. |
| [Agentin käyttöönotto](./lesson-4-agent-deployment/README.md)   | Isännöityjen agenttien ja OpenAI Chatkitin avulla nähdään, miten tekoälyagentti voidaan ottaa tuotantoon.       |


## 🎒 Muut kurssit

Tiimimme tuottaa myös muita kursseja! Tutustu:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j aloittelijoille](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js aloittelijoille](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain aloittelijoille](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agentit
[![AZD aloittelijoille](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI aloittelijoille](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP aloittelijoille](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI-agentit aloittelijoille](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatiivinen tekoälysarja
[![Generatiivinen tekoäly aloittelijoille](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen tekoäly (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen tekoäly (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen tekoäly (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Ydinoppiminen
[![ML aloittelijoille](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Tietojenkäsittelytiede aloittelijoille](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![Tekoäly aloittelijoille](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kyberturvallisuus aloittelijoille](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web-kehitys aloittelijoille](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![Esineiden internet aloittelijoille](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR-kehitys aloittelijoille](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot-sarja
[![Copilot tekoälyn kanssa pariohjelmointiin](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET-kehitykseen](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot-seikkailu](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Osallistuminen

Tämä projekti toivottaa tervetulleeksi panokset ja ehdotukset. Useimmat panokset vaativat, että hyväksyt
Kontribuuttajan lisenssisopimuksen (CLA), jossa ilmoitat, että sinulla on oikeus ja todella myönnät meille
oikeudet käyttää panostasi. Lisätietoja saat osoitteesta <https://cla.opensource.microsoft.com>.

Kun lähetät vetopyynnön, CLA-botti tunnistaa automaattisesti, tarvitseeko sinun toimittaa
CLA ja merkitsee PR:n asianmukaisesti (esim. tilantarkistus, kommentti). Seuraa vain botin antamia ohjeita.
Sinun tarvitsee tehdä tämä vain kerran kaikissa repoissa, jotka käyttävät meidän CLA:a.

Tämä projekti on ottanut käyttöön [Microsoftin avoimen lähdekoodin käytösohjeet](https://opensource.microsoft.com/codeofconduct/).
Lisätietoja löydät [Käytösohjeiden UKK:sta](https://opensource.microsoft.com/codeofconduct/faq/) tai
ota yhteyttä osoitteeseen [opencode@microsoft.com](mailto:opencode@microsoft.com) lisäkysymyksiä tai kommentteja varten.

## Tavara­merkit

Tämä projekti saattaa sisältää tavara­merkkejä tai logoja projekteista, tuotteista tai palveluista. Microsoftin
tavara­merkkien tai logoiden valtuutettu käyttö on voimassa ja noudattaa
[Microsoftin tavara­merkkien & brändin ohjeistuksia](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Muokatuissa versioissa Microsoftin tavara­merkkien tai logoiden käyttö ei saa aiheuttaa sekaannusta eikä viitata Microsoftin sponsoriin.
Kolmansien osapuolten tavara­merkkien tai logoiden käyttö on kyseisten kolmansien osapuolten sääntöjen mukaista.

## Apua

Jos jäät jumiin tai sinulla on kysymyksiä tekoälysovellusten rakentamisesta, liity:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

Jos sinulla on palautetta tuotteesta tai kohtaat virheitä rakentaessa, käy:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälykäännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä pidetään virallisena lähteenä. Tärkeissä asioissa suositellaan ammattilaisen tekemää ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virheellisistä tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->