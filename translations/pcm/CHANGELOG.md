# Changelog

All beta beta changes wey dey **Building AI Agents from Zero to Production** dem dey put for here.

The format na from [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Dis course na living curriculum no be versioned software package, so we go group entries
by the date wey changes land instead of semantic version number.

## 13th July 2026

### Added
- **Repository hygiene for public sharing** — we make `.gitignore` strong with dedicated
  Python / notebooks / secrets / OS section (env-file variants, `.pytest_cache/`, `.mypy_cache/`,
  `.ruff_cache/`, `.ipynb_checkpoints/`, `*.egg-info/`), but we still dey keep every `*.env.example`
  wey we dey track. Add this `CHANGELOG.md`, `AGENTS.md` contributor/agent guide, plus course skill
  files.

### Changed
- We prepare repository for public; scrub all personal and live-environment identifiers
  (account, project, resource-group and identity names) out from published docs, and move internal
  modernisation/gap-analysis report comot for repository (the summary wey fain learner dey for this
  changelog).

## [2026 Foundry modernisation]

Complete technical, terminology and curriculum refresh to align the course with the
**Microsoft Foundry 2026** platform. Check `MIGRATION-GUIDE.md` for code-level migration details.

### Added
- **Lesson 5 – Production Hosted Agents** (`lesson-5-hosted-agents-production/`): Hosted Agents vs
  Capability Hosts, bring-your-own Cosmos DB / Storage / AI Search, memory and thread persistence,
  Hosted MCP approval workflows, and governance checklist.
- **Lesson 6 – Microsoft Toolbox** (`lesson-6-toolbox/`): define tools once and govern dem
  centrally, plus a runable consume sample (`toolbox_agent.py`) wey dey reach toolbox through one
  MCP endpoint.
- **Lesson 7 – Multi-Agent & A2A** (`lesson-7-multi-agent-a2a/`): expose agent over the open
  Agent-to-Agent (A2A) protocol (`a2a_server.py`) and consume remote agent as peer
  (`a2a_client.py`). E don test live end-to-end.
- **Task Recommendation Agent** (`lesson-2-agent-development/task-recommendation-agent.py`):
  e implement Lesson 1 Scenario 2 using GitHub remote MCP server as tool.
- **Vector-store setup script** (`setup_vector_store.py`): e create and populate vector store
  wey employee-search agent dey rely on (e dey referenced before but e bin dey miss).
- **CI smoke + static gate** (`.github/workflows/smoke-test-hosted-agent.yml`): `static` job dey run
  `py_compile` and markdown-link-check on every PR/push; `smoke` job dey run AI Smoke Test
  action against deployed hosted agent (OIDC, `workflow_dispatch`).
- **Prerequisites and setup guidance** add for every lesson and for root README
  (Python 3.12+, `az login`, model guidance, cost & cleanup).
- **New flagship doc**: `MIGRATION-GUIDE.md`.

### Changed
- **Rebrand**: *Azure AI Foundry* → **Microsoft Foundry** all over di course.
- **SDK migration** to current Microsoft Agent Framework surface — samples now dey use
  `agent-framework` `1.2.0` with `FoundryChatClient` and **Responses API**, wey replace
  old `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` patterns.
- **Pinned dependencies**: `requirements.txt` now pin `agent-framework`, `agent-framework-foundry`
  and related packages instead of installing unpinned pre-releases, to make samples reproducible.
- **Environment variables** e align for `deploy.py`, `agent.yaml`, `main.py` and
  `.env.example` files.
- README architecture diagrams and agent/scenario catalogue e rewrite to match shipped code.

### Fixed
- We fix broken root-README link to Lesson 4 (`lesson-4-agentdeployment`).
- We write the previously empty Lesson 3 README (evaluations + observability).
- We replace deprecated `asyncio.get_event_loop().run_until_complete` pattern for
  learning-recommendation agent.

### Deprecated / Removed
- We remove all use of retired **GPT-4o / GPT-4.1** models. Chat and evaluation samples now dey use
  **gpt-5.1**; coding samples dey use **gpt-5-codex**.
- We document say **GitHub Models** dey retire (July 30, 2026); the course dey serve all models
  through Microsoft Foundry and e no dey depend on GitHub Models.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->