# Changelog

All beta change dem for **Building AI Agents from Zero to Production** dey inside here.

The format na based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Dis course na beta curriculum wey dem dey dey update live, no be software wey dem dey version am, so entries dey group
by the date wey dem drop di changes instead of semantic version number.

## [Unreleased]

### Added
- **Repository hygiene for public sharing** — hardened `.gitignore` with dedicated
  Python / notebooks / secrets / OS section (env-file variants, `.pytest_cache/`, `.mypy_cache/`,
  `.ruff_cache/`, `.ipynb_checkpoints/`, `*.egg-info/`), meanwhile we still dey keep each `*.env.example`
  tracked. Add this `CHANGELOG.md`, an `AGENTS.md` contributor/agent guide, plus course skill
  files.

### Changed
- Prepare di repository for public share: clean personal and live-environment identifiers
  (account, project, resource-group and identity names) dem comot for published docs, plus move the internal
  modernisation/gap-analysis report comot from the repository (the summary for learners dey inside this
  changelog).

## [2026 Foundry modernisation]

Full technical, terminology and curriculum update wey align the course with
**Microsoft Foundry 2026** platform. Check `MIGRATION-GUIDE.md` for code-level migration details.

### Added
- **Lesson 5 – Production Hosted Agents** (`lesson-5-hosted-agents-production/`): Hosted Agents vs
  Capability Hosts, make your own Cosmos DB / Storage / AI Search, memory and thread persistence,
  Hosted MCP approval workflows, and governance checklist.
- **Lesson 6 – Microsoft Toolbox** (`lesson-6-toolbox/`): define tools once and govern dem
  centrally, plus a runnable consume sample (`toolbox_agent.py`) wey fit reach toolbox through
  one MCP endpoint.
- **Lesson 7 – Multi-Agent & A2A** (`lesson-7-multi-agent-a2a/`): expose one agent for open
  Agent-to-Agent (A2A) protocol (`a2a_server.py`) and consume remote agent as peer
  (`a2a_client.py`). Validate live end-to-end.
- **Task Recommendation Agent** (`lesson-2-agent-development/task-recommendation-agent.py`):
  implement Lesson 1 Scenario 2 using GitHub remote MCP server as tool.
- **Vector-store setup script** (`setup_vector_store.py`): create and fill vector store
  wey employee-search agent depend on (before e dey referenced but e no dey).
- **CI smoke + static gate** (`.github/workflows/smoke-test-hosted-agent.yml`): `static` job dey run
  `py_compile` and markdown-link-check for every PR/push; `smoke` job run AI Smoke Test
  action against deployed hosted agent (OIDC, `workflow_dispatch`).
- **Prerequisites and setup guidance** added to all lesson and to root README
  (Python 3.12+, `az login`, model guidance, cost & cleanup).
- **New flagship doc**: `MIGRATION-GUIDE.md`.

### Changed
- **Rebrand**: *Azure AI Foundry* → **Microsoft Foundry** for everywhere for course.
- **SDK migration** to current Microsoft Agent Framework surface — samples dey use now
  `agent-framework` `1.2.0` with `FoundryChatClient` and **Responses API**, replace
  old `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` patterns.
- **Pinned dependencies**: `requirements.txt` now fix `agent-framework`, `agent-framework-foundry`
  and related packages so sample fit reproduce well, no install unpinned pre-releases.
- **Environment variables** align for `deploy.py`, `agent.yaml`, `main.py` and
  `.env.example` files.
- README architecture diagrams and agent/scenario catalogue rewrite to match code wey dem ship.

### Fixed
- Fix broken root-README link to Lesson 4 (`lesson-4-agentdeployment`).
- Write previously empty Lesson 3 README (evaluations + observability).
- Replace deprecated `asyncio.get_event_loop().run_until_complete` pattern for
  learning-recommendation agent.

### Deprecated / Removed
- Remove all use of retired **GPT-4o / GPT-4.1** models. Chat and evaluation samples now use
  **gpt-5.1**; coding samples use **gpt-5-codex**.
- Document say **GitHub Models** dey retired (July 30, 2026); course dey serve all models
  through Microsoft Foundry and no depend on GitHub Models.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->