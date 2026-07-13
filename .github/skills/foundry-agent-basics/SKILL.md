---
name: foundry-agent-basics
description: >-
  Help a learner build their first AI agent with the Microsoft Agent Framework (MAF) on Microsoft
  Foundry. Use when the task is creating a basic agent, wiring up FoundryChatClient, choosing a
  model, running the DevUI, or understanding lesson 1–2 concepts (instructions, tools, threads).
---

# Foundry agent basics

Guidance for building a first agent in this course (Lessons 1–2).

## Guardrails (always apply)
- **Platform:** Microsoft Foundry (never say "Azure AI Foundry"). Framework: Microsoft Agent
  Framework (MAF).
- **SDK:** use the pinned `agent-framework` from `requirements.txt` with **`FoundryChatClient`** and
  the **Responses API**. Do not use `AzureAIClient`, `AzureAIAgentClient`, or `AzureOpenAIChatClient`.
- **Model:** `gpt-5.1` for chat. Never `gpt-4o` / `gpt-4.1` (retired) and never GitHub Models.
- **Auth:** `az login` + `AzureCliCredential`; endpoint/model come from `.env` (never hardcoded).

## What a learner should understand first
1. **Agent = model + instructions + tools + a thread.** Instructions set the persona/task; tools
   extend capability; a thread carries conversation state.
2. **Design before code (Lesson 1):** identify the scenario, the user, the tools needed, and the
   success criteria. The course use case is "Developer Onboarding".
3. **One agent, one job.** Lesson 2 builds several small, specialised agents rather than one
   monolith (employee search, learning recommendation, coding, orchestration, etc.).

## Minimal shape of a sample
- Load env with `python-dotenv`; read the Foundry project endpoint and model name.
- Create a `FoundryChatClient` with `AzureCliCredential`.
- Create the agent with clear `instructions`; attach tools if needed.
- Run it — most lesson-2 samples expose a local **DevUI** on a dedicated port (8090+).

## How to help
- Point the learner at the closest existing sample in `lesson-2-agent-development/` and adapt it,
  rather than writing from scratch.
- Keep instructions specific and scoped; show how to test with a couple of representative prompts.
- Remind them to `pip install -r requirements.txt`, `az login`, and populate `.env` first.

## Validate
- `python -m py_compile <file>.py` must pass.
- The sample should start its DevUI and answer a basic prompt end-to-end.

## References
- `lesson-1-agent-design/README.md`, `lesson-2-agent-development/README.md`
- `MIGRATION-GUIDE.md` for the current SDK patterns.
