# Changelog

All notable changes to **Building AI Agents from Zero to Production** are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This course is a living curriculum rather than a versioned software package, so entries are grouped
by the date a set of changes landed rather than by a semantic version number.

## 13th July 2026

### Added
- **Repository hygiene for public sharing** — hardened `.gitignore` with a dedicated
  Python / notebooks / secrets / OS section (env-file variants, `.pytest_cache/`, `.mypy_cache/`,
  `.ruff_cache/`, `.ipynb_checkpoints/`, `*.egg-info/`), while keeping every `*.env.example`
  tracked. Added this `CHANGELOG.md`, an `AGENTS.md` contributor/agent guide, and course skill
  files.

### Changed
- Prepared the repository for public sharing: scrubbed personal and live-environment identifiers
  (account, project, resource-group and identity names) from published docs, and moved the internal
  modernisation/gap-analysis report out of the repository (its learner-facing summary lives in this
  changelog).

## [2026 Foundry modernisation]

A complete technical, terminology and curriculum refresh aligning the course with the
**Microsoft Foundry 2026** platform. See `MIGRATION-GUIDE.md` for the code-level migration details.

### Added
- **Lesson 5 – Production Hosted Agents** (`lesson-5-hosted-agents-production/`): Hosted Agents vs
  Capability Hosts, bring-your-own Cosmos DB / Storage / AI Search, memory and thread persistence,
  Hosted MCP approval workflows, and a governance checklist.
- **Lesson 6 – Microsoft Toolbox** (`lesson-6-toolbox/`): define tools once and govern them
  centrally, plus a runnable consume sample (`toolbox_agent.py`) that reaches a toolbox through a
  single MCP endpoint.
- **Lesson 7 – Multi-Agent & A2A** (`lesson-7-multi-agent-a2a/`): expose an agent over the open
  Agent-to-Agent (A2A) protocol (`a2a_server.py`) and consume a remote agent as a peer
  (`a2a_client.py`). Validated live end-to-end.
- **Task Recommendation Agent** (`lesson-2-agent-development/task-recommendation-agent.py`):
  implements Lesson 1 Scenario 2 using the GitHub remote MCP server as a tool.
- **Vector-store setup script** (`setup_vector_store.py`): creates and populates the vector store
  that the employee-search agent depends on (previously referenced but missing).
- **CI smoke + static gate** (`.github/workflows/smoke-test-hosted-agent.yml`): a `static` job runs
  `py_compile` and markdown-link-check on every PR/push; a `smoke` job runs the AI Smoke Test
  action against a deployed hosted agent (OIDC, `workflow_dispatch`).
- **Prerequisites and setup guidance** added to every lesson and to the root README
  (Python 3.12+, `az login`, model guidance, cost & cleanup).
- **New flagship doc**: `MIGRATION-GUIDE.md`.

### Changed
- **Rebrand**: *Azure AI Foundry* → **Microsoft Foundry** throughout the course.
- **SDK migration** to the current Microsoft Agent Framework surface — samples now use
  `agent-framework` `1.2.0` with `FoundryChatClient` and the **Responses API**, replacing the
  earlier `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` patterns.
- **Pinned dependencies**: `requirements.txt` now pins `agent-framework`, `agent-framework-foundry`
  and related packages instead of installing unpinned pre-releases, making samples reproducible.
- **Environment variables** aligned across `deploy.py`, `agent.yaml`, `main.py` and the
  `.env.example` files.
- README architecture diagrams and the agent/scenario catalogue rewritten to match the shipped code.

### Fixed
- Corrected the broken root-README link to Lesson 4 (`lesson-4-agentdeployment`).
- Authored the previously empty Lesson 3 README (evaluations + observability).
- Replaced the deprecated `asyncio.get_event_loop().run_until_complete` pattern in the
  learning-recommendation agent.

### Deprecated / Removed
- Removed all use of the retired **GPT-4o / GPT-4.1** models. Chat and evaluation samples now use
  **gpt-5.1**; coding samples use **gpt-5-codex**.
- Documented that **GitHub Models** is being retired (July 30, 2026); the course serves all models
  through Microsoft Foundry and does not depend on GitHub Models.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->