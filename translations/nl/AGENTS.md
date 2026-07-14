# AGENTS.md

Richtlijnen voor AI-codeeragenten (en menselijke bijdragers) die in deze repository werken. Als je een
geautomatiseerde agent bent die hier wijzigingen aanbrengt, lees dit bestand eerst en volg het op.

## Wat deze repository is

**AI-agenten bouwen van nul tot productie** is een Microsoft-leercursus. Het leert ontwikkelaars
om AI-agenten te ontwerpen, bouwen, evalueren, inzetten en beheren op **Microsoft Foundry** met behulp van het
**Microsoft Agent Framework (MAF)**. De inhoud is georganiseerd als een reeks lessen, elk met een
`README.md` en uitvoerbare Python-voorbeelden.

```
lesson-1-agent-design/            Use case + how to design effective agents
lesson-2-agent-development/       Build specialised agents with MAF (multiple runnable samples)
lesson-3-agent-evals/             Evaluations and observability
lesson-4-agentdeployment/         Deploy a hosted agent + OpenAI ChatKit front end
lesson-5-hosted-agents-production/ Hosted Agents vs Capability Hosts, BYO storage, governance
lesson-6-toolbox/                 Microsoft Toolbox: define + govern tools centrally
lesson-7-multi-agent-a2a/         Multi-agent orchestration over the A2A protocol
```

Hoofddocumenten: `README.md` (begin hier), `MIGRATION-GUIDE.md` (details SDK-migratie), `CHANGELOG.md`.

## Gouden regels

1. **Nooit geheimen commiten.** Alleen `*.env.example`-bestanden worden gevolgd; echte `.env`-bestanden worden
   genegeerd door git. Hardcode geen endpoints, sleutels, tokens of verbindingsreeksen in voorbeelden of documentatie.
2. **Raak `translations/` of `translated_images/` niet aan.** Deze worden automatisch gegenereerd door een
   vertaal-GitHub-actie. Bewerk ze nooit handmatig; breng bronwijzigingen alleen aan in de topniveaulessen-
   bestanden.
3. **Geen verouderde modellen.** Gebruik **`gpt-5.1`** voor chat/evaluatie en **`gpt-5-codex`** voor coderen.
   Introduceer **niet** `gpt-4o`, `gpt-4.1` of een met pensioen gegaan model, en gebruik geen *GitHub-models*
   (die stoppen op 30 juli 2026) — alle modellen worden geleverd via Microsoft Foundry.
4. **Gebruik de huidige SDK-interface.** Voorbeelden richten zich op `agent-framework` (gepind in `requirements.txt`)
   met `FoundryChatClient` en de **Responses API**. Breng niet de oudere
   `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` patronen opnieuw in.
5. **Houd terminologie actueel**: *Microsoft Foundry* (niet "Azure AI Foundry"), *Microsoft Agent
   Framework*, *Hosted Agents*, *Capability Hosts*, *Microsoft Toolbox*, *MCP / Hosted MCP*, *A2A*.

## Setup

```bash
python -m venv .venv
# Windows:  .venv\Scripts\Activate.ps1
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt

az login                     # voorbeelden authenticeren met uw ontwikkelaarsidentiteit
cp .env.example .env         # vul vervolgens uw Foundry-projectendpoint + model in
```

Vereisten: **Python 3.12+**, de **Azure CLI**, en toegang tot een **Microsoft Foundry**-project
met een ingezet GPT-5-seriemodel. Elke les-README vermeldt zijn eigen vereisten en de omgevingsvariabelen
die het nodig heeft (zie het `.env.example` op lesniveau waar aanwezig).

## Voorbeelden uitvoeren

De meeste les-2 voorbeelden starten een lokale **DevUI** op een speciale poort (bijvoorbeeld 8090–8096); de A2A
server in les 7 luistert op poort 9000. Controleer de docstring/README van elk voorbeeld voor het exacte commando
en poort. Omdat voorbeelden live Foundry-endpoints aanroepen, hebben ze een geldig `.env` en `az login` nodig.

## Wijzigingen valideren

Er is geen unit-test suite; validatie is statisch + live:

- **Statische poort (moet slagen voor commit):** byte-compileer elk voorbeeld.
  ```bash
  python -m py_compile $(git ls-files '*.py')
  ```
  In Windows PowerShell:
  ```powershell
  git ls-files '*.py' | ForEach-Object { python -m py_compile $_ }
  ```
- **Markdown-links:** de CI `static` taak voert `markdown-link-check` uit
  (configuratie: `.github/workflows/markdown-link-check-config.json`). Controleer of nieuwe externe links
  oplossen (HTTP 200).
- **Smoke test:** `.github/workflows/smoke-test-hosted-agent.yml` voert de AI Smoke Test-actie uit
  tegen een ingezet hosted agent (`workflow_dispatch`, OIDC). Live agent runs vereisen Azure-toegang.

CI (`static` taak) ontdekt automatisch `.py`-bestanden, dus nieuwe voorbeelden worden gedekt zonder de
workflow aan te passen. Commit geen code die faalt voor `py_compile`.

## Commitconventies

- Schrijf gefocuste commits met duidelijke, imperatieve berichten.
- Voeg de co-auteur trailer toe bij agent-ondersteunde commits:
  ```
  Co-authored-by: Copilot App <223556219+Copilot@users.noreply.github.com>
  ```
- Commit geen gegenereerde caches, virtuele omgevingen of `.env`-bestanden (allemaal genegeerd door git).

## Waar specifieke wijzigingen aan te brengen

| Wijziging | Locatie |
|--------|----------|
| Cursusverhaal/lestekst | `lesson-*/README.md` (alleen bron — nooit `translations/`) |
| Uitvoerbare code | `lesson-*/**.py`, `setup_vector_store.py` |
| Afhankelijkheden | `requirements.txt` (houd versies vastgepind) |
| Documentatie omgevingsvariabelen | `.env.example`, lesniveau `.env.example` |
| CI / statische poort | `.github/workflows/` |
| Cursusvaardigheden voor AI-assistenten | `.github/skills/` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->