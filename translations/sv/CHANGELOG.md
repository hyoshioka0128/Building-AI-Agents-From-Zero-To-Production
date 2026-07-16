# Ändringslogg

Alla viktiga förändringar för **Building AI Agents from Zero to Production** dokumenteras här.

Formatet är baserat på [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Denna kurs är en levande läroplan snarare än ett versionshanterat mjukvarupaket, så poster grupperas
efter datum då en uppsättning ändringar genomfördes snarare än efter ett semantiskt versionsnummer.

## 13 juli 2026

### Tillagt
- **Arkivhygien för offentlig delning** — förstärkt `.gitignore` med en dedikerad
  Python / notebooks / secrets / OS-sektion (varianter av env-fil, `.pytest_cache/`, `.mypy_cache/`,
  `.ruff_cache/`, `.ipynb_checkpoints/`, `*.egg-info/`), samtidigt som varje `*.env.example`
  spåras. Tillagt denna `CHANGELOG.md`, en `AGENTS.md` bidrags-/agentguide och kursfärdighets-
  filer.

### Ändrat
- Förberett arkivet för offentlig delning: rensat personliga och live-miljö-identifierare
  (konto, projekt, resursgrupp och identitetsnamn) från publicerad dokumentation, och flyttat den interna
  moderniserings-/gap-analysrapporten utanför arkivet (dess sammanfattning för deltagare finns i denna
  ändringslogg).

## [2026 Foundry-modernisering]

En komplett teknisk, terminologisk och kursuppdatering som anpassar kursen till
**Microsoft Foundry 2026**-plattformen. Se `MIGRATION-GUIDE.md` för detaljer om migrering på kodnivå.

### Tillagt
- **Lektion 5 – Produktionshostade agenter** (`lesson-5-hosted-agents-production/`): Hostade agenter kontra
  kapabilitetsvärdar, ta med egen Cosmos DB / Storage / AI Search, minne och tråd-persistens,
  Hostade MCP godkännandeflöden och en styrningschecklista.
- **Lektion 6 – Microsoft Verktygslåda** (`lesson-6-toolbox/`): definiera verktyg en gång och styr dem
  centralt, samt ett körbart exempel för konsumtion (`toolbox_agent.py`) som når en verktygslåda genom en
  enda MCP-endpoint.
- **Lektion 7 – Multi-Agent & A2A** (`lesson-7-multi-agent-a2a/`): exponera en agent över det öppna
  agent-till-agent (A2A) protokollet (`a2a_server.py`) och konsumera en fjärragent som en peer
  (`a2a_client.py`). Validerad live end-to-end.
- **Task Recommendation Agent** (`lesson-2-agent-development/task-recommendation-agent.py`):
  implementerar Lektion 1 Scenario 2 med GitHub remote MCP-servern som ett verktyg.
- **Skript för uppsättning av vektor-lager** (`setup_vector_store.py`): skapar och fyller vektorlager
  som sökagenten för anställda är beroende av (refererades tidigare men saknades).
- **CI rök- och statisk grind** (`.github/workflows/smoke-test-hosted-agent.yml`): ett `static`-jobb kör
  `py_compile` och markdown-länk-kontroll på varje PR/push; ett `smoke`-jobb kör AI-röktestet
  åtgärden mot en distribuerad hostad agent (OIDC, `workflow_dispatch`).
- **Förutsättningar och installationsvägledning** tillagt till varje lektion och till rot-README
  (Python 3.12+, `az login`, modellriktlinjer, kostnad och städning).
- **Nytt flaggskepps-dokument**: `MIGRATION-GUIDE.md`.

### Ändrat
- **Omprofilering**: *Azure AI Foundry* → **Microsoft Foundry** genom hela kursen.
- **SDK-migrering** till den aktuella Microsoft Agent Framework-yta — exemplen använder nu
  `agent-framework` `1.2.0` med `FoundryChatClient` och **Responses API**, som ersätter
  tidigare `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient`-mönster.
- **Fastställda beroenden**: `requirements.txt` låser nu `agent-framework`, `agent-framework-foundry`
  och relaterade paket istället för att installera ofasta förhandsversioner, vilket gör exemplen reproducerbara.
- **Miljövariabler** harmoniserade över `deploy.py`, `agent.yaml`, `main.py` och
  `.env.example`-filer.
- README arkitekturdiagram och agent-/scenariokatalog omskrivna för att matcha den levererade koden.

### Fixed
- Korrigerade den brutna roten-README-länken till Lektion 4 (`lesson-4-agentdeployment`).
- Författade den tidigare tomma Lektion 3 README (utvärderingar + observabilitet).
- Ersatte det föråldrade `asyncio.get_event_loop().run_until_complete`-mönstret i
  lärande-rekommendationsagenten.

### Avvecklat / Borttaget
- Tog bort all användning av de utgångna **GPT-4o / GPT-4.1** modellerna. Chat- och utvärderingsexempel använder nu
  **gpt-5.1**; kodexempel använder **gpt-5-codex**.
- Dokumenterat att **GitHub Models** avvecklas (30 juli 2026); kursen tillhandahåller alla modeller
  via Microsoft Foundry och är inte beroende av GitHub Models.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->