# AGENTS.md

Guidance for AI coding agents (and human contributors) working in this repository. If you are an
automated agent making changes here, read this file first and follow it.

## What this repository is

**Building AI Agents from Zero to Production** is a Microsoft learning course. It teaches developers
to design, build, evaluate, deploy and operate AI agents on **Microsoft Foundry** using the
**Microsoft Agent Framework (MAF)**. The content is organised as a sequence of lessons, each with a
`README.md` and runnable Python samples.

```
lesson-1-agent-design/            Use case + how to design effective agents
lesson-2-agent-development/       Build specialised agents with MAF (multiple runnable samples)
lesson-3-agent-evals/             Evaluations and observability
lesson-4-agentdeployment/         Deploy a hosted agent + OpenAI ChatKit front end
lesson-5-hosted-agents-production/ Hosted Agents vs Capability Hosts, BYO storage, governance
lesson-6-toolbox/                 Microsoft Toolbox: define + govern tools centrally
lesson-7-multi-agent-a2a/         Multi-agent orchestration over the A2A protocol
```

Root docs: `README.md` (start here), `MODERNIZATION-REPORT.md` (gap analysis + validation matrix),
`MIGRATION-GUIDE.md` (SDK migration detail), `CHANGELOG.md`.

## Golden rules

1. **Never commit secrets.** Only `*.env.example` files are tracked; real `.env` files are
   git-ignored. Do not hardcode endpoints, keys, tokens, or connection strings in samples or docs.
2. **Do not touch `translations/` or `translated_images/`.** These are generated automatically by a
   translation GitHub Action. Never hand-edit them; make source changes in the top-level lesson
   files only.
3. **No deprecated models.** Use **`gpt-5.1`** for chat/eval and **`gpt-5-codex`** for coding.
   Do **not** introduce `gpt-4o`, `gpt-4.1`, or any retired model, and do not use *GitHub Models*
   (retiring July 30, 2026) — all models are served through Microsoft Foundry.
4. **Use the current SDK surface.** Samples target `agent-framework` (pinned in `requirements.txt`)
   with `FoundryChatClient` and the **Responses API**. Do not reintroduce the older
   `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` patterns.
5. **Keep terminology current**: *Microsoft Foundry* (not "Azure AI Foundry"), *Microsoft Agent
   Framework*, *Hosted Agents*, *Capability Hosts*, *Microsoft Toolbox*, *MCP / Hosted MCP*, *A2A*.

## Setup

```bash
python -m venv .venv
# Windows:  .venv\Scripts\Activate.ps1
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt

az login                     # samples authenticate with your developer identity
cp .env.example .env         # then fill in your Foundry project endpoint + model
```

Requirements: **Python 3.12+**, the **Azure CLI**, and access to a **Microsoft Foundry** project
with a deployed GPT-5-series model. Each lesson README lists its own prerequisites and the env vars
it needs (see the lesson-level `.env.example` where present).

## Running samples

Most lesson-2 samples launch a local **DevUI** on a dedicated port (for example 8090–8096); the A2A
server in lesson 7 listens on port 9000. Check each sample's docstring/README for the exact command
and port. Because samples call live Foundry endpoints, they need a valid `.env` and `az login`.

## Validating changes

There is no unit-test suite; validation is static + live:

- **Static gate (must pass before commit):** byte-compile every sample.
  ```bash
  python -m py_compile $(git ls-files '*.py')
  ```
  On Windows PowerShell:
  ```powershell
  git ls-files '*.py' | ForEach-Object { python -m py_compile $_ }
  ```
- **Markdown links:** the CI `static` job runs `markdown-link-check`
  (config: `.github/workflows/markdown-link-check-config.json`). Verify any new external links
  resolve (HTTP 200).
- **Smoke test:** `.github/workflows/smoke-test-hosted-agent.yml` runs the AI Smoke Test action
  against a deployed hosted agent (`workflow_dispatch`, OIDC). Live agent runs require Azure access.

CI (`static` job) auto-discovers `.py` files, so new samples are covered without editing the
workflow. Do not commit code that fails `py_compile`.

## Commit conventions

- Write focused commits with clear, imperative messages.
- Include the co-author trailer on agent-assisted commits:
  ```
  Co-authored-by: Copilot App <223556219+Copilot@users.noreply.github.com>
  ```
- Do not commit generated caches, virtual environments, or `.env` files (all git-ignored).

## Where to make specific changes

| Change | Location |
|--------|----------|
| Course narrative / lesson text | `lesson-*/README.md` (source only — never `translations/`) |
| Runnable code | `lesson-*/**.py`, `setup_vector_store.py` |
| Dependencies | `requirements.txt` (keep versions pinned) |
| Env var documentation | `.env.example`, lesson-level `.env.example` |
| CI / static gate | `.github/workflows/` |
| Course skills for AI assistants | `.github/skills/` |
