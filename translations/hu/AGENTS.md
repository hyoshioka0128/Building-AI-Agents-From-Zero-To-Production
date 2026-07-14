# AGENTS.md

Útmutató AI kódoló ügynököknek (és emberi közreműködőknek), akik ebben a tárházban dolgoznak. Ha Ön egy
automatizált ügynök, amely itt módosításokat végez, először olvassa el ezt a fájlt, és kövesse az útmutatót.

## Mi ez a tárház

**AI ügynökök felépítése nulláról a gyártásig** egy Microsoft tanfolyam. Megtanítja a fejlesztőknek,
hogyan tervezzék meg, építsék, értékeljék, telepítsék és üzemeltessék az AI ügynököket a **Microsoft Foundry** platformon a
**Microsoft Agent Framework (MAF)** használatával. A tartalom leckék sorozataként van rendszerezve, mindegyikhez tartozik egy
`README.md` és futtatható Python példák.

```
lesson-1-agent-design/            Use case + how to design effective agents
lesson-2-agent-development/       Build specialised agents with MAF (multiple runnable samples)
lesson-3-agent-evals/             Evaluations and observability
lesson-4-agentdeployment/         Deploy a hosted agent + OpenAI ChatKit front end
lesson-5-hosted-agents-production/ Hosted Agents vs Capability Hosts, BYO storage, governance
lesson-6-toolbox/                 Microsoft Toolbox: define + govern tools centrally
lesson-7-multi-agent-a2a/         Multi-agent orchestration over the A2A protocol
```

Fő dokumentumok: `README.md` (innen kezdje), `MIGRATION-GUIDE.md` (SDK migrációs részletek), `CHANGELOG.md`.

## Aranyszabályok

1. **Soha ne kövessen el titkokat.** Csak a `*.env.example` fájlok vannak nyomon követve; a valódi `.env` fájlok
   git-figyelmen kívül vannak hagyva. Ne kódoljon be végpontokat, kulcsokat, tokeneket vagy kapcsolati karakterláncokat példákba vagy dokumentációba.
2. **Ne nyúljon a `translations/` vagy `translated_images/` mappákhoz.** Ezek automatikusan generálódnak egy
   fordítási GitHub Action által. Soha ne szerkessze kézzel őket; a forrásváltoztatásokat csak a felső szintű lecke
   fájljaiban végezze el.
3. **Nincs elavult modell.** Használja a **`gpt-5.1`** modellt chat/értékeléshez és a **`gpt-5-codex`** modellt kódoláshoz.
   Ne vezessen be `gpt-4o`, `gpt-4.1` vagy bármely nyugdíjazott modellt, és ne használja a *GitHub Modelleket*
   (2026. július 30-án megszűnnek) — minden modellt a Microsoft Foundry szolgál ki.
4. **Használja a jelenlegi SDK felületet.** A példák az `agent-framework`-re céloznak (fix verzió a `requirements.txt`-ben)
   a `FoundryChatClient` és a **Responses API** használatával. Ne vezessen vissza régebbi
   `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` mintákat.
5. **Tartsa naprakészen a terminológiát**: *Microsoft Foundry* (nem „Azure AI Foundry”), *Microsoft Agent
   Framework*, *Hosted Agents*, *Capability Hosts*, *Microsoft Toolbox*, *MCP / Hosted MCP*, *A2A*.

## Beállítás

```bash
python -m venv .venv
# Windows:  .venv\Scripts\Activate.ps1
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt

az login                     # a példák hitelesítése a fejlesztői azonosítójával
cp .env.example .env         # majd töltse ki a Foundry projekt végpontját + modellt
```

Követelmények: **Python 3.12+**, az **Azure CLI**, és hozzáférés egy **Microsoft Foundry** projekthez
ahol telepítve van egy GPT-5-sorozatú modell. Minden lecke README fájlja felsorolja a saját előfeltételeit és az
igényelt környezeti változókat (lásd a lecke szintű `.env.example` fájlokat, ahol vannak).

## Példák futtatása

A legtöbb lecke-2 példány helyi **DevUI**-t indít dedikált porton (például 8090–8096); a lecke 7 A2A
szervere a 9000-es porton hallgat. Ellenőrizze az adott példa docstringjét/README-jét a pontos parancsért
és portért. Mivel a példák élő Foundry végpontokat hívnak, szükségük van érvényes `.env` fájlra és `az login`-ra.

## Változtatások ellenőrzése

Nincs egységteszt készlet; az ellenőrzés statikus + élő:

- **Statikus kapu (köteles átmenni a commit előtt):** minden mintát byte-kódra fordítani.
  ```bash
  python -m py_compile $(git ls-files '*.py')
  ```
  Windows PowerShell-ben:
  ```powershell
  git ls-files '*.py' | ForEach-Object { python -m py_compile $_ }
  ```
- **Markdown linkek:** a CI `static` munkafolyamata futtatja a `markdown-link-check` eszközt
  (konfiguráció: `.github/workflows/markdown-link-check-config.json`). Ellenőrizze, hogy az új külső linkek
  helyesen működjenek (HTTP 200).
- **Smoke teszt:** `.github/workflows/smoke-test-hosted-agent.yml` futtatja az AI Smoke Test akciót
  telepített hosztolt ügynök ellen (workflow_dispatch, OIDC). Az élő ügynök futtatáshoz Azure hozzáférés szükséges.

A CI (`static` munkafolyamat) automatikusan felfedezi a `.py` fájlokat, így az új példákat lefedi a workflow szerkesztése nélkül. Ne commitáljon olyan kódot, amely nem fordul le `py_compile`-al.


## Commit szokások

- Írjon fókuszált commitokat világos, felszólító üzenettel.
- Tartalmazza a co-author záradékot az ügynök által segített commitokon:
  ```
  Co-authored-by: Copilot App <223556219+Copilot@users.noreply.github.com>
  ```
- Ne commitáljon generált cache-eket, virtuális környezeteket vagy `.env` fájlokat (mind git-figyeltlen).

## Hol végezzen konkrét változtatásokat

| Változtatás | Hely |
|--------|----------|
| Tanfolyam narratíva / lecke szöveg | `lesson-*/README.md` (csak forrás — soha ne `translations/`) |
| Futtatható kód | `lesson-*/**.py`, `setup_vector_store.py` |
| Függőségek | `requirements.txt` (tartsa meg a verziókat fixálva) |
| Környezeti változó dokumentáció | `.env.example`, lecke szintű `.env.example` |
| CI / statikus kapu | `.github/workflows/` |
| Tanfolyam készségek AI asszisztenseknek | `.github/skills/` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->