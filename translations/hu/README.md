<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b09df38b3188ffe957c7ac8b055967f5",
  "translation_date": "2026-01-16T09:28:18+00:00",
  "source_file": "README.md",
  "language_code": "hu"
}
-->
# AI ügynökök létrehozása nulláról a gyártásig

![AI ügynökök létrehozása nulláról a gyártásig](../../../../translated_images/hu/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 Többnyelvű támogatás

#### GitHub Action révén támogatott (automatikus és mindig naprakész)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arab](../ar/README.md) | [Bengáli](../bn/README.md) | [Bolgár](../bg/README.md) | [Burmai (Mianmar)](../my/README.md) | [Kínai (egyszerűsített)](../zh/README.md) | [Kínai (hagyományos, Hongkong)](../hk/README.md) | [Kínai (hagyományos, Makaó)](../mo/README.md) | [Kínai (hagyományos, Tajvan)](../tw/README.md) | [Horvát](../hr/README.md) | [Cseh](../cs/README.md) | [Dán](../da/README.md) | [Holland](../nl/README.md) | [Észt](../et/README.md) | [Finn](../fi/README.md) | [Francia](../fr/README.md) | [Német](../de/README.md) | [Görög](../el/README.md) | [Héber](../he/README.md) | [Hindi](../hi/README.md) | [Magyar](./README.md) | [Indonéz](../id/README.md) | [Olasz](../it/README.md) | [Japán](../ja/README.md) | [Kannada](../kn/README.md) | [Koreai](../ko/README.md) | [Litván](../lt/README.md) | [Maláj](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepáli](../ne/README.md) | [Nigériai Pidzsin](../pcm/README.md) | [Norvég](../no/README.md) | [Perzsa (Farsi)](../fa/README.md) | [Lengyel](../pl/README.md) | [Portugál (Brazília)](../br/README.md) | [Portugál (Portugália)](../pt/README.md) | [Pandzsábi (Gurmukhi)](../pa/README.md) | [Román](../ro/README.md) | [Orosz](../ru/README.md) | [Szerb (cirill)](../sr/README.md) | [Szlovák](../sk/README.md) | [Szlovén](../sl/README.md) | [Spanyol](../es/README.md) | [Szuahéli](../sw/README.md) | [Svéd](../sv/README.md) | [Tagalog (Filippínó)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Török](../tr/README.md) | [Ukrán](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamita](../vi/README.md)

> **Szeretnél inkább helyileg klónozni?**

> Ez a tároló több mint 50 nyelvfordítást tartalmaz, ami jelentősen megnöveli a letöltési méretet. Ha fordítások nélkül szeretnéd klónozni, használj sparse checkout-ot:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Így mindent megkapsz, amire a tanfolyam befejezéséhez szükséged van, de sokkal gyorsabb letöltéssel.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Egy tanfolyam, amely az AI ügynök fejlesztési életciklusának alapjait tanítja meg

[![GitHub licenc](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub közreműködők](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub probléma](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub kérés](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PR-eket szívesen fogadunk](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 Kezdés

Ez a tanfolyam az AI ügynökök építésének és bevetésének alapjait tárgyalja.

Minden lecke az előzőre épül, ezért javasoljuk, hogy kezd az elején, és haladj sorban a végéig.

Ha szeretnél többet megtudni az AI ügynök témákról, megnézheted az [AI ügynökök kezdőknek tanfolyamot](https://aka.ms/ai-agents-beginners).

### Ismerkedj meg más tanulókkal, kapj választ a kérdéseidre

Ha elakadsz vagy kérdésed van az AI ügynökök építésével kapcsolatban, csatlakozz a dedikált Discord csatornánkhoz a [Microsoft Foundry Discordban](https://discord.gg/Kuaw3ktsu6).

### Amire szükséged van

Minden leckéhez tartozik egy saját kódminta, amit helyben futtathatsz. [Forkold ezt a repót](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork), hogy elkészítsd a saját másolatodat.

Ez a tanfolyam jelenleg az alábbiakat használja:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI Szolgáltatás](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

Kérjük, győződj meg arról, hogy hozzáférsz ezekhez a szolgáltatásokhoz, mielőtt elkezdenéd.

Hamarosan további lehetőségek érkeznek modellek hosztolására és szolgáltatásokra.

## 🗃️ Leckék

| **Lecke**              | **Leírás**                                                                                   |
|------------------------|----------------------------------------------------------------------------------------------|
| [Ügynök tervezés](./lesson-1-agent-design/README.md)         | Bevezetés a "Fejlesztői bevezetés" ügynök esettanulmányba és hatékony ügynökök tervezésébe      |
| [Ügynök fejlesztés](./lesson-2-agent-development/README.md)  | A Microsoft Agent Framework (MAF) használata, 3 ügynök létrehozása az új fejlesztők segítésére |
| [Ügynök értékelés](./lesson-3-agent-evals/README.md)          | A Microsoft Foundry segítségével megtudhatod, hogy AI ügynökeink mennyire teljesítenek és hogyan javíthatók |
| [Ügynök bevetés](./lesson-4-agent-deployment/README.md)       | Bevetés a Hosted Agents és OpenAI Chatkit segítségével, hogyan helyezhetsz ügynököt termelésbe    |

## 🎒 Egyéb tanfolyamok

Csapatunk más tanfolyamokat is készít! Nézd meg:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j kezdőknek](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js kezdőknek](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Ügynökök
[![AZD kezdőknek](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI kezdőknek](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP kezdőknek](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI ügynökök kezdőknek](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Generatív AI sorozat
[![Generatív AI kezdőknek](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### Alapvető tanulás
[![ML kezdőknek](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Adattudomány kezdőknek](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI kezdőknek](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kiberbiztonság kezdőknek](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webfejlesztés kezdőknek](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT kezdőknek](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR fejlesztés kezdőknek](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot sorozat
[![Copilot AI páros programozáshoz](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET-hez](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot kaland](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Hozzájárulás

Ez a projekt szívesen fogad hozzájárulásokat és javaslatokat. A legtöbb hozzájáruláshoz el kell fogadnia egy
Hozzájárulói Licenc Megállapodást (CLA), amelyben kijelenti, hogy joga van ehhez, és valóban átadja nekünk
a hozzájárulás használatának jogát. Részletekért látogasson el a <https://cla.opensource.microsoft.com> oldalra.

Amikor pull requestet nyújt be, egy CLA bot automatikusan eldönti, hogy szükséges-e CLA beküldése,
és ennek megfelelően ellátja a PR-t (pl. státusz-ellenőrzés, hozzászólás). Egyszerűen kövesse a bot utasításait.
Ezt csak egyszer kell megtennie az összes, a CLA-t használó repóban.

Ez a projekt elfogadta a [Microsoft nyílt forráskódú magatartási kódexét](https://opensource.microsoft.com/codeofconduct/).
További információért lásd a [Magatartási Kódex GYIK](https://opensource.microsoft.com/codeofconduct/faq/) oldalt vagy
keresse fel az [opencode@microsoft.com](mailto:opencode@microsoft.com) címet további kérdésekkel vagy észrevételekkel.

## Védjegyek

Ez a projekt tartalmazhat védjegyeket vagy logókat projektek, termékek vagy szolgáltatások számára. A Microsoft
védjegyek vagy logók jogosult használata alá esik és követnie kell a
[Microsoft Védjegy- és Márkaszabályzatát](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
A Microsoft védjegyek vagy logók használata a projekt módosított változataiban nem okozhat félreértést vagy nem sugallhat Microsoft támogatást.
Harmadik féltől származó védjegyek vagy logók használata a harmadik felek szabályzataitól függ.

## Segítségkérés

Ha elakad vagy kérdése van AI alkalmazások fejlesztésével kapcsolatban, csatlakozzon:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

Ha termék-visszajelzést vagy hibákat szeretne jelezni fejlesztés közben, látogasson el:

[![Microsoft Foundry fejlesztői fórum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) használatával készült. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hivatalos forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget semmilyen félreértésért vagy félreértelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->