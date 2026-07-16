# Ændringslog

Alle bemærkelsesværdige ændringer til **Building AI Agents from Zero to Production** er dokumenteret her.

Formatet er baseret på [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Dette kursus er en levende læseplan snarere end en versionsstyret softwarepakke, så poster grupperes
efter den dato, et sæt ændringer landede snarere end efter et semantisk versionsnummer.

## 13. juli 2026

### Tilføjet
- **Repository-hygiejne til offentlig deling** — udvidet `.gitignore` med en dedikeret
  Python / notebooks / secrets / OS sektion (env-fil varianter, `.pytest_cache/`, `.mypy_cache/`,
  `.ruff_cache/`, `.ipynb_checkpoints/`, `*.egg-info/`), samtidig med at hver `*.env.example`
  bibeholdes sporet. Tilføjet denne `CHANGELOG.md`, en `AGENTS.md` bidragsyder/agent guide, og kursuskompetence
  filer.

### Ændret
- Forberedt repository til offentlig deling: renset personlige og live-miljø identifikatorer
  (konto, projekt, ressourcegruppe og identitetsnavne) fra offentliggjorte dokumenter, og flyttet den interne
  moderniserings-/gap-analyse rapport ud af repository (dens elevrettede resumé findes i denne
  changelog).

## [2026 Foundry-modernisering]

En komplet teknisk, terminologi- og læseplansopdatering der tilpasser kurset til
**Microsoft Foundry 2026** platformen. Se `MIGRATION-GUIDE.md` for detaljer om kode-niveau migrationen.

### Tilføjet
- **Lektion 5 – Produktion Hostede Agenter** (`lesson-5-hosted-agents-production/`): Hostede Agenter vs
  Capability Hosts, medbring-eget Cosmos DB / Storage / AI Search, hukommelse og tråd-persistens,
  Hostede MCP godkendelses-workflows, og en styringscheckliste.
- **Lektion 6 – Microsoft Toolbox** (`lesson-6-toolbox/`): definer værktøjer én gang og styr dem
  centralt, plus et kørbart forbrugseksempel (`toolbox_agent.py`) der når et toolbox via en
  enkelt MCP endpoint.
- **Lektion 7 – Multi-Agent & A2A** (`lesson-7-multi-agent-a2a/`): eksponer en agent over den åbne
  Agent-til-Agent (A2A) protokol (`a2a_server.py`) og forbrug en ekstern agent som en peer
  (`a2a_client.py`). Valideret live end-to-end.
- **Task Recommendation Agent** (`lesson-2-agent-development/task-recommendation-agent.py`):
  implementerer Lektion 1 Scenario 2 ved brug af GitHub eksternt MCP server som værktøj.
- **Vector-store opsætningsscript** (`setup_vector_store.py`): opretter og udfylder vector-storen
  som employee-search agenten afhænger af (tidligere refereret men manglende).
- **CI smoke + statisk gate** (`.github/workflows/smoke-test-hosted-agent.yml`): et `static` job kører
  `py_compile` og markdown-link-check på hver PR/push; et `smoke` job kører AI Smoke Test
  action mod en deployeret hosted agent (OIDC, `workflow_dispatch`).
- **Forudsætninger og opsætningsvejledning** tilføjet til hver lektion og til roden README
  (Python 3.12+, `az login`, modelvejledning, omkostninger & oprydning).
- **Nyt hoveddokument**: `MIGRATION-GUIDE.md`.

### Ændret
- **Rebranding**: *Azure AI Foundry* → **Microsoft Foundry** gennem hele kurset.
- **SDK migration** til den nuværende Microsoft Agent Framework surface — eksempler bruger nu
  `agent-framework` `1.2.0` med `FoundryChatClient` og **Responses API**, som erstatter
  tidligere `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` mønstre.
- **Fastlåste afhængigheder**: `requirements.txt` fastlåser nu `agent-framework`, `agent-framework-foundry`
  og relaterede pakker i stedet for at installere upinned pre-releases, hvilket gør eksempler reproducerbare.
- **Miljøvariabler** tilpasset på tværs af `deploy.py`, `agent.yaml`, `main.py` og
  `.env.example` filer.
- README arkitekturdiagrammer og agent-/scenario katalog omskrevet for at matche den udgivne kode.

### Rettet
- Korrigeret det brudte rod-README link til Lektion 4 (`lesson-4-agentdeployment`).
- Udarbejdet den tidligere tomme Lektion 3 README (evalueringer + observabilitet).
- Udskiftet det forældede `asyncio.get_event_loop().run_until_complete` mønster i
  learning-recommendation agenten.

### Forældet / Fjernet
- Fjernet al brug af de pensionerede **GPT-4o / GPT-4.1** modeller. Chat- og evalueringsprøver bruger nu
  **gpt-5.1**; kodningsprøver bruger **gpt-5-codex**.
- Dokumenteret at **GitHub Models** udfases (30. juli 2026); kurset bruger alle modeller
  gennem Microsoft Foundry og er ikke afhængigt af GitHub Models.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->