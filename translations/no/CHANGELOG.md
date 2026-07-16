# Endringslogg

Alle merkbare endringer i **Building AI Agents from Zero to Production** dokumenteres her.

Formatet er basert på [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Dette kurset er en levende læreplan i stedet for en versjonert programvarepakke, så oppføringer grupperes
etter datoen et sett med endringer ble lansert, i stedet for etter en semantisk versjonsnummer.

## 13. juli 2026

### Lagt til
- **Repository hygiene for offentlig deling** — styrket `.gitignore` med en dedikert
  Python / notatbøker / hemmeligheter / OS-seksjon (env-fil-varianter, `.pytest_cache/`, `.mypy_cache/`,
  `.ruff_cache/`, `.ipynb_checkpoints/`, `*.egg-info/`), samtidig som alle `*.env.example`
  spores. Lagt til denne `CHANGELOG.md`, en `AGENTS.md` bidragsyter-/agentguide, og kursferdighets-
  filer.

### Endret
- Gjort repository klart for offentlig deling: renset personlige og live-miljøidentifikatorer
  (konto-, prosjekt-, ressurs-gruppe- og identitetsnavn) fra publiserte dokumenter, og flyttet den interne
  moderniserings-/gap-analyse rapporten ut av repository (dens oppsummering for lærende finnes i denne
  endringsloggen).

## [2026 Foundry modernisering]

En komplett teknisk, terminologi- og læreplanoppdatering som tilpasser kurset til
**Microsoft Foundry 2026** plattformen. Se `MIGRATION-GUIDE.md` for detaljer om migrering på kode-nivå.

### Lagt til
- **Leksjon 5 – Produksjons-hostede agenter** (`lesson-5-hosted-agents-production/`): Hostede agenter vs
  Capacity Hosts, bring-your-own Cosmos DB / Storage / AI Search, minne- og trådvedvarende,
  Hostede MCP godkjenningsarbeidsflyter, og en styringsjekkliste.
- **Leksjon 6 – Microsoft Toolbox** (`lesson-6-toolbox/`): definer verktøy én gang og styr dem
  sentralt, pluss et kjørbart forbrukseksempel (`toolbox_agent.py`) som når en toolbox gjennom en
  enkelt MCP-endepunkt.
- **Leksjon 7 – Multi-Agent & A2A** (`lesson-7-multi-agent-a2a/`): eksponere en agent over det åpne
  Agent-til-Agent (A2A) protokollen (`a2a_server.py`) og forbruk en ekstern agent som en likemann
  (`a2a_client.py`). Validert live ende-til-ende.
- **Task Recommendation Agent** (`lesson-2-agent-development/task-recommendation-agent.py`):
  implementerer Leksjon 1 Scenario 2 ved bruk av GitHub remote MCP-server som et verktøy.
- **Vector-store oppsettskript** (`setup_vector_store.py`): oppretter og fyller opp vektorbutikken
  som ansatt-søkeagenten er avhengig av (tidligere referert men manglende).
- **CI røyk + statisk gate** (`.github/workflows/smoke-test-hosted-agent.yml`): en `static` jobb kjører
  `py_compile` og markdown-link-check på hver PR/push; en `smoke` jobb kjører AI Smoke Test
  handlingen mot en distribuert hostet agent (OIDC, `workflow_dispatch`).
- **Forutsetninger og oppsettveiledning** lagt til i hver leksjon og til rot-README
  (Python 3.12+, `az login`, modellveiledning, kostnader & opprydding).
- **Nytt flaggskip-dokument**: `MIGRATION-GUIDE.md`.

### Endret
- **Omdøpt**: *Azure AI Foundry* → **Microsoft Foundry** gjennom hele kurset.
- **SDK migrering** til den nåværende Microsoft Agent Framework overflaten — eksempler bruker nå
  `agent-framework` `1.2.0` med `FoundryChatClient` og **Responses API**, som erstatter
  tidligere `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` mønstre.
- **Fastlåste avhengigheter**: `requirements.txt` låser nå `agent-framework`, `agent-framework-foundry`
  og relaterte pakker i stedet for å installere ufikserte forhåndsversjoner, for å gjøre eksempler reproduserbare.
- **Miljøvariabler** tilpasset på tvers av `deploy.py`, `agent.yaml`, `main.py` og
  `.env.example` filene.
- README arkitekturdiagrammer og agent-/scenario-katalog omskrevet for å matche den leverte koden.

### Fikset
- Rettet den ødelagte root-README-lenken til Leksjon 4 (`lesson-4-agentdeployment`).
- Utarbeidet den tidligere tomme Leksjon 3 README (evalueringer + observabilitet).
- Erstattet det utgåtte `asyncio.get_event_loop().run_until_complete` mønsteret i
  læringsanbefalingsagenten.

### Utfaset / Fjernet
- Fjernet all bruk av de pensjonerte **GPT-4o / GPT-4.1** modellene. Chat- og evalueringsprøver bruker nå
  **gpt-5.1**; kodingseksempler bruker **gpt-5-codex**.
- Dokumentert at **GitHub Models** avvikles (30. juli 2026); kurset betjener alle modeller
  gjennom Microsoft Foundry og er ikke avhengig av GitHub Models.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->