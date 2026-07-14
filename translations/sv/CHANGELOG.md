# Ändringslogg

Alla anmärkningsvärda förändringar i **Building AI Agents from Zero to Production** dokumenteras här.

Formatet är baserat på [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Denna kurs är en levande läroplan snarare än ett versionshanterat mjukvarupaket, så poster grupperas
efter datumet då en uppsättning ändringar landade snarare än efter ett semantiskt versionsnummer.

## [Ej släppt än]

### Tillagt
- **Repository-hygien för offentlig delning** — förbättrad `.gitignore` med en dedikerad
  Python / notebooks / secrets / OS-sektion (varianter för env-fil, `.pytest_cache/`, `.mypy_cache/`,
  `.ruff_cache/`, `.ipynb_checkpoints/`, `*.egg-info/`), samtidigt som varje `*.env.example`
  spåras. Lade till denna `CHANGELOG.md`, en `AGENTS.md` bidrags-/agentguide och kursens
  färdighetsfiler.

### Ändrat
- Förberedde repositoryt för offentlig delning: rensade personliga och live-miljöidentifierare
  (konto-, projekt-, resursgrupps- och identitetsnamn) från publicerade dokument och flyttade den interna
  moderniserings-/gap-analysrapporten utanför repositoryt (dess sammanfattning för deltagare finns i denna
  ändringslogg).

## [Microsoft Foundry 2026 modernisering]

En komplett teknisk, terminologisk och läroplansuppdatering som anpassar kursen med
**Microsoft Foundry 2026**-plattformen. Se `MIGRATION-GUIDE.md` för detaljer kring migrering på kodnivå.

### Tillagt
- **Lektion 5 – Produktion Hostade Agenter** (`lesson-5-hosted-agents-production/`): Hostade Agenter versus
  Capability Hosts, ta med egen Cosmos DB / Storage / AI Search, minnes- och tråd-persistens,
  hostade MCP-godkännande arbetsflöden samt en styrrapport.
- **Lektion 6 – Microsoft Toolbox** (`lesson-6-toolbox/`): definiera verktyg en gång och styra dem
  centralt, plus ett exempel på körbar konsumtion (`toolbox_agent.py`) som når en verktygslåda genom en
  enda MCP-endpoint.
- **Lektion 7 – Multi-Agent & A2A** (`lesson-7-multi-agent-a2a/`): exponera en agent över det öppna
  Agent-to-Agent (A2A) protokollet (`a2a_server.py`) och konsumera en fjärragent som en peer
  (`a2a_client.py`). Validerat live end-to-end.
- **Task Recommendation Agent** (`lesson-2-agent-development/task-recommendation-agent.py`):
  implementerar Lektion 1 Scenario 2 med GitHub-fjärr-MCP-servern som verktyg.
- **Vector-store installationsskript** (`setup_vector_store.py`): skapar och fyller på vektorlagret
  som anställd-sökagenten är beroende av (tidigare refererat men saknat).
- **CI smoke + statisk gate** (`.github/workflows/smoke-test-hosted-agent.yml`): ett `static` jobb kör
  `py_compile` och markdown-link-check på varje PR/push; ett `smoke` jobb kör AI Smoke Test
  åtgärden mot en hostad agent i produktion (OIDC, `workflow_dispatch`).
- **Förutsättningar och installationsanvisningar** tillagda i varje lektion och i root README
  (Python 3.12+, `az login`, modellriktlinjer, kostnad & städning).
- **Ny flaggskeppsdokumentation**: `MIGRATION-GUIDE.md`.

### Ändrat
- **Omprofilering**: *Azure AI Foundry* → **Microsoft Foundry** genom hela kursen.
- **SDK-migrering** till nuvarande Microsoft Agent Framework-gränssnitt — exempel använder nu
  `agent-framework` `1.2.0` med `FoundryChatClient` och **Responses API**, ersätter
  tidigare `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` mönster.
- **Fastkörda beroenden**: `requirements.txt` fixerar nu versioner för `agent-framework`, `agent-framework-foundry`
  och relaterade paket istället för att installera ofixade förhandsversioner, vilket gör exemplen reproducerbara.
- **Miljövariabler** synkroniserade i `deploy.py`, `agent.yaml`, `main.py` och
  `.env.example`-filerna.
- Läsme-arkitekturdiagram och agent-/scenariokatalog omskrivna för att matcha den levererade koden.

### Fikserat
- Korrigerade den brutna roten-README-länken till Lektion 4 (`lesson-4-agentdeployment`).
- Författade den tidigare tomma Lektion 3 README (utvärderingar + övervakning).
- Ersatte det föråldrade `asyncio.get_event_loop().run_until_complete`-mönstret i
  learning-recommendation agenten.

### Föråldrat / Tagits bort
- Tog bort all användning av de pensionerade **GPT-4o / GPT-4.1** modellerna. Chatt- och utvärderingsexempel använder nu
  **gpt-5.1**; kodningsexempel använder **gpt-5-codex**.
- Dokumenterat att **GitHub Models** tas ur bruk (30 juli 2026); kursen använder alla modeller
  genom Microsoft Foundry och är inte beroende av GitHub Models.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->