# Változásnapló

Minden figyelemre méltó változás a **Zero-tól a termelésig épített AI ügynökök** tananyagban itt dokumentált.

A formátum a [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) alapján készült.
Ez a tananyag élő tanterv, nem verziózott szoftvercsomag, ezért a bejegyzéseket
a változások megjelenésének dátuma szerint csoportosítjuk, nem szemantikus verziószám szerint.

## 2026. július 13.

### Hozzáadva
- **Tároló higiénia nyilvános megosztáshoz** — megerősített `.gitignore` dedikált
  Python / jegyzetfüzetek / titkok / OS szekcióval (env-fájl változatok, `.pytest_cache/`, `.mypy_cache/`,
  `.ruff_cache/`, `.ipynb_checkpoints/`, `*.egg-info/`), miközben minden `*.env.example`
  fájl követve maradt. Hozzáadva ez a `CHANGELOG.md`, egy `AGENTS.md` közreműködő/ügynök útmutató, és tanfolyam-készségek
  fájlok.

### Módosítva
- Elkészítettük a tárolót nyilvános megosztáshoz: töröltük a személyes és éles környezeti azonosítókat
  (fiók, projekt, erőforrás-csoport és identitásnevek) a közzétett dokumentumokból, és az
  belső modernizációs/hézag-elemzési jelentést eltávolítottuk a tárolóból (ennek tanulókat érintő összefoglalója ebben a
  változásnaplóban található).

## [2026 Foundry modernizáció]

Teljes műszaki, terminológiai és tananyag frissítés, amely összehangolja a tanfolyamot a
**Microsoft Foundry 2026** platformmal. A kód szintű migráció részletei a `MIGRATION-GUIDE.md` fájlban találhatók.

### Hozzáadva
- **5. lecke – Termelésben üzemeltetett ügynökök** (`lesson-5-hosted-agents-production/`): Ügynökök hosztolása vs
  képességek hosztjai, bring-your-own Cosmos DB / Tárhely / AI Keresés, memória és munkamenet
  állandósítás, hosztolt MCP jóváhagyási munkafolyamatok és irányítási ellenőrzőlista.
- **6. lecke – Microsoft Szerszámosláda** (`lesson-6-toolbox/`): egyszer definiált eszközök központi
  irányítása, valamint futtatható fogyasztási példa (`toolbox_agent.py`), amely egy szerszámosláda
  egyetlen MCP végponton keresztüli elérését teszi lehetővé.
- **7. lecke – Többügynökes & A2A** (`lesson-7-multi-agent-a2a/`): egy ügynök nyilvánossá tétele az
  nyílt Agent-to-Agent (A2A) protokollon keresztül (`a2a_server.py`) és távoli ügynök fogyasztása partnerként
  (`a2a_client.py`). Éles végpontok közötti hitelesített tesztelés.
- **Feladatajánló ügynök** (`lesson-2-agent-development/task-recommendation-agent.py`):
  az 1. lecke 2. forgatókönyvét valósítja meg a GitHub távoli MCP szerver eszközként való használatával.
- **Vektor-tárház beállító szkript** (`setup_vector_store.py`): létrehozza és feltölti a vektor tárolót,
  amelyre a dolgozó-kereső ügynök támaszkodik (korábban hivatkozott, de hiányzó fájl).
- **CI füstteszt + statikus kapu** (`.github/workflows/smoke-test-hosted-agent.yml`): egy `static` feladat
  futtatja a `py_compile` és markdown-link-check teszteket minden PR/push esetén; egy `smoke` feladat
  AI Füstteszt akciót hajt végre egy telepített hosztolt ügynökön (OIDC, `workflow_dispatch`).
- **Előfeltételek és beállítási útmutató** minden leckéhez és a gyökér README fájlhoz
  hozzáadva (Python 3.12+, `az login`, modell útmutató, költség & takarítás).
- **Új zászlóshajó dokumentum**: `MIGRATION-GUIDE.md`.

### Módosítva
- **Új márka**: *Azure AI Foundry* → **Microsoft Foundry** a tanfolyam egészében.
- **SDK migráció** a jelenlegi Microsoft Agent Framework felületre — a példák mostantól
  `agent-framework` `1.2.0`-t használják a `FoundryChatClient` és a **Responses API**-val, lecserélve az
  korábbi `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` mintákat.
- **Letűzött függőségek**: a `requirements.txt` most már letűzött verzióval tartalmazza az `agent-framework`,
  az `agent-framework-foundry` és kapcsolódó csomagokat, így a példák reprodukálhatók.
- **Környezeti változók** összehangolva a `deploy.py`, `agent.yaml`, `main.py` és
  `.env.example` fájlok között.
- A README architektúra ábrák és az ügynök/forgatókönyv katalógus újraírása, hogy megfeleljen a szállított kódnak.

### Javítva
- Javítva a törött gyökér README link a 4. leckéhez (`lesson-4-agentdeployment`).
- Elkészült az eddig üres 3. lecke README (értékelések + megfigyelhetőség).
- Lecserélve a már elavult `asyncio.get_event_loop().run_until_complete` mintázat
  a tanulás-ajánló ügynökben.

### Elavult / Eltávolított
- Eltávolításra kerültek a megszűnt **GPT-4o / GPT-4.1** modellek használatai. A chat és értékelő példák most
  a **gpt-5.1**-et használják; a kódoló példák a **gpt-5-codex** verziót.
- Dokumentáltuk, hogy a **GitHub Models** nyugdíjba vonul (2026. július 30.); a tanfolyam az összes modellt
  a Microsoft Foundry-n keresztül szolgálja ki, és nem függ a GitHub Models-tól.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->