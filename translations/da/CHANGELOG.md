# Ændringslog

Alle bemærkelsesværdige ændringer til **Building AI Agents from Zero to Production** dokumenteres her.

Formatet er baseret på [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Dette kursus er en levende læseplan fremfor en versioneret softwarepakke, så poster grupperes
efter datoen hvor et sæt ændringer blev tilføjet fremfor efter et semantisk versionsnummer.

## [Ikke udgivet]

### Tilføjet
- **Repository hygiene for offentlig deling** — forstærket `.gitignore` med en dedikeret
  Python / notebooks / secrets / OS sektion (env-fil varianter, `.pytest_cache/`, `.mypy_cache/`,
  `.ruff_cache/`, `.ipynb_checkpoints/`, `*.egg-info/`), mens hver `*.env.example`
  bibeholdes sporet. Tilføjet denne `CHANGELOG.md`, en `AGENTS.md` bidragsyder/agent guide, og kursus-færdigheds-
  filer.

### Ændret
- Forberedt repository til offentlig deling: renset personlige og live-miljø identifikatorer
  (konto, projekt, resource-gruppe og identitetsnavne) fra offentliggjorte dokumenter, og flyttet den interne
  moderniserings-/gap-analyse rapport ud af repository (dens elev-orienterede resume findes i denne
  changelog).

## [2026 Foundry modernisering]

En komplet teknisk, terminologi og læseplansopdatering der bringer kurset på linje med
**Microsoft Foundry 2026** platformen. Se `MIGRATION-GUIDE.md` for migrationsdetaljer på kode-niveau.

### Tilføjet
- **Lesson 5 – Production Hosted Agents** (`lesson-5-hosted-agents-production/`): Hosted Agents vs
  Capability Hosts, medbring-din-egen Cosmos DB / Storage / AI Search, hukommelse og tråd-persistens,
  Hosted MCP godkendelses-workflows, og en governance tjekliste.
- **Lesson 6 – Microsoft Toolbox** (`lesson-6-toolbox/`): definer værktøjer én gang og styr dem
  centralt, plus et kørbart consume-eksempel (`toolbox_agent.py`) der når et toolbox gennem en
  enkelt MCP-endpoint.
- **Lesson 7 – Multi-Agent & A2A** (`lesson-7-multi-agent-a2a/`): eksponer en agent over den åbne
  Agent-to-Agent (A2A) protokol (`a2a_server.py`) og konsumér en fjernagent som ligeværdig part
  (`a2a_client.py`). Valideret live end-to-end.
- **Task Recommendation Agent** (`lesson-2-agent-development/task-recommendation-agent.py`):
  implementerer Lesson 1 Scenario 2 ved brug af GitHub fjern-MCP serveren som værktøj.
- **Vector-store opsætningsscript** (`setup_vector_store.py`): opretter og befolker vektorbutikken
  som medarbejder-søgeagenten afhænger af (tidligere refereret, men manglende).
- **CI smoke + statisk gate** (`.github/workflows/smoke-test-hosted-agent.yml`): et `static` job kører
  `py_compile` og markdown-link-check på hver PR/push; et `smoke` job kører AI Smoke Test
  action mod en deployet hosted agent (OIDC, `workflow_dispatch`).
- **Forudsætninger og opsætningsvejledning** tilføjet til hver lektion og til roden README
  (Python 3.12+, `az login`, modelvejledning, omkostninger & oprydning).
- **Nyt hoveddokument**: `MIGRATION-GUIDE.md`.

### Ændret
- **Genbranding**: *Azure AI Foundry* → **Microsoft Foundry** igennem hele kurset.
- **SDK migration** til den nuværende Microsoft Agent Framework overflade — eksempler bruger nu
  `agent-framework` `1.2.0` med `FoundryChatClient` og **Responses API**, der erstatter
  tidligere `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` mønstre.
- **Fastlåste afhængigheder**: `requirements.txt` låser nu `agent-framework`, `agent-framework-foundry`
  og relaterede pakker i stedet for at installere ikke-fastlåste pre-releases, hvilket gør eksempler reproducerbare.
- **Miljøvariabler** afstemt på tværs af `deploy.py`, `agent.yaml`, `main.py` og
  `.env.example` filerne.
- README arkitekturdiagrammer og agent-/scenario-katalog omskrevet for at matche den leverede kode.

### Rettet
- Rettet det brudte rod-README link til Lesson 4 (`lesson-4-agentdeployment`).
- Udarbejdet den tidligere tomme Lesson 3 README (evalueringer + observerbarhed).
- Udskiftet det forældede `asyncio.get_event_loop().run_until_complete` mønster i
  lærings-anbefalingsagenten.

### Forældet / Fjernet
- Fjernet al brug af de udfasede **GPT-4o / GPT-4.1** modeller. Chat og evaluerings-eksempler bruger nu
  **gpt-5.1**; kodeeksempler bruger **gpt-5-codex**.
- Dokumenteret at **GitHub Models** udfases (30. juli 2026); kurset servicerer alle modeller
  gennem Microsoft Foundry og afhænger ikke af GitHub Models.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->