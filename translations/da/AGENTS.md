# AGENTS.md

Vejledning til AI-kodeagenter (og menneskelige bidragydere), der arbejder i dette repository. Hvis du er en
automatiseret agent, der laver ændringer her, skal du læse denne fil først og følge den.

## Hvad dette repository er

**Building AI Agents from Zero to Production** er et Microsoft læringskursus. Det lærer udviklere
at designe, bygge, evaluere, implementere og drive AI-agentersystemer på **Microsoft Foundry** ved hjælp af
**Microsoft Agent Framework (MAF)**. Indholdet er organiseret som en række lektioner, hver med en
`README.md` og kørbare Python-eksempler.

```
lesson-1-agent-design/            Use case + how to design effective agents
lesson-2-agent-development/       Build specialised agents with MAF (multiple runnable samples)
lesson-3-agent-evals/             Evaluations and observability
lesson-4-agentdeployment/         Deploy a hosted agent + OpenAI ChatKit front end
lesson-5-hosted-agents-production/ Hosted Agents vs Capability Hosts, BYO storage, governance
lesson-6-toolbox/                 Microsoft Toolbox: define + govern tools centrally
lesson-7-multi-agent-a2a/         Multi-agent orchestration over the A2A protocol
```

Rod-dokumenter: `README.md` (start her), `MIGRATION-GUIDE.md` (SDK-migrationsdetaljer), `CHANGELOG.md`.

## Gyldne regler

1. **Aldrig commit hemmeligheder.** Kun `*.env.example` filer bliver sporet; rigtige `.env` filer er
   git-ignorert. Indkod ikke endpoints, nøgler, tokens eller forbindelsesstrenge i eksempler eller dokumenter.
2. **Rør ikke `translations/` eller `translated_images/`.** Disse genereres automatisk af en
   oversættelses-GitHub Action. Rediger dem aldrig manuelt; foretag kun kildeændringer i lektionernes
   topniveau-filer.
3. **Ingen forældede modeller.** Brug **`gpt-5.1`** til chat/evaluering og **`gpt-5-codex`** til kodning.
   Indfør **ikke** `gpt-4o`, `gpt-4.1` eller nogen pensioneret model, og brug ikke *GitHub Models*
   (pensioneres 30. juli 2026) — alle modeller leveres via Microsoft Foundry.
4. **Brug det nuværende SDK-surface.** Eksempler målretter `agent-framework` (fastsat i `requirements.txt`)
   med `FoundryChatClient` og **Responses API**. Genindfør ikke de ældre
   `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` mønstre.
5. **Hold terminologien opdateret**: *Microsoft Foundry* (ikke "Azure AI Foundry"), *Microsoft Agent
   Framework*, *Hosted Agents*, *Capability Hosts*, *Microsoft Toolbox*, *MCP / Hosted MCP*, *A2A*.

## Opsætning

```bash
python -m venv .venv
# Windows:  .venv\Scripts\Activate.ps1
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt

az login                     # prøver autentificerer med din udvikleridentitet
cp .env.example .env         # udfyld derefter dit Foundry projekt-endpoint + model
```

Krav: **Python 3.12+**, **Azure CLI** og adgang til et **Microsoft Foundry** projekt
med en implementeret GPT-5-serie model. Hver lektion README angiver sine egne forudsætninger og de miljø-variabler
den behøver (se lektionens `.env.example`, hvor det findes).

## Kørsel af eksempler

De fleste lektion-2 eksempler starter en lokal **DevUI** på en dedikeret port (for eksempel 8090–8096); A2A
serveren i lektion 7 lytter på port 9000. Tjek hvert eksempels docstring/README for præcis kommando
og port. Fordi eksempler kalder live Foundry endpoints, kræver de en gyldig `.env` og `az login`.

## Validering af ændringer

Der er ikke noget enhedstest-suite; validering er statisk + live:

- **Statisk port (skal passere inden commit):** byte-compile hvert eksempel.
  ```bash
  python -m py_compile $(git ls-files '*.py')
  ```
  På Windows PowerShell:
  ```powershell
  git ls-files '*.py' | ForEach-Object { python -m py_compile $_ }
  ```
- **Markdown links:** CI `static` job kører `markdown-link-check`
  (konfiguration: `.github/workflows/markdown-link-check-config.json`). Bekræft at nye eksterne links
  virker (HTTP 200).
- **Smoke test:** `.github/workflows/smoke-test-hosted-agent.yml` kører AI Smoke Test action
  mod en deployeret hosted agent (`workflow_dispatch`, OIDC). Live agent kørsler kræver Azure adgang.

CI (`static` job) opdager automatisk `.py` filer, så nye eksempler er dækket uden redigering af
workflowfilen. Commit ikke kode, der fejler `py_compile`.

## Commit-konventioner

- Skriv fokuserede commits med klare, imperativ-formulerede beskeder.
- Inkluder medforfatter-sporingslinjen på agent-assisterede commits:
  ```
  Co-authored-by: Copilot App <223556219+Copilot@users.noreply.github.com>
  ```
- Commit ikke genererede caches, virtuelle miljøer eller `.env` filer (alle git-ignorert).

## Hvor man skal lave specifikke ændringer

| Ændring | Placering |
|--------|----------|
| Kursusfortælling / lektionstekst | `lesson-*/README.md` (kun kilde — aldrig `translations/`) |
| Kørbar kode | `lesson-*/**.py`, `setup_vector_store.py` |
| Afhængigheder | `requirements.txt` (hold versioner fastlåste) |
| Dokumentation til miljøvariabler | `.env.example`, lektion-niveau `.env.example` |
| CI / statisk port | `.github/workflows/` |
| Kursusfærdigheder til AI-assistenter | `.github/skills/` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->