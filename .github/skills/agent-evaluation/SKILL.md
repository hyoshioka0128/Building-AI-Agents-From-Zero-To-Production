---
name: agent-evaluation
description: >-
  Help a learner evaluate and observe an AI agent on Microsoft Foundry — quality/safety evaluators,
  tracing, and reading results. Use for Lesson 3 tasks: measuring agent performance, adding
  observability, or interpreting evaluation output.
---

# Agent evaluation & observability

Guidance for measuring and improving agents (Lesson 3).

## Guardrails (always apply)
- Platform: Microsoft Foundry; framework: Microsoft Agent Framework.
- Use the **evaluation/observability APIs from the current `agent-framework` surface** (Foundry
  evals + tracing). Model for any judge/eval step: **`gpt-5.1`** (never `gpt-4o` / `gpt-4.1`).
- Endpoints/models from `.env`; `az login` for auth.

## Concepts a learner should grasp
1. **Why evaluate:** agents are non-deterministic — you need repeatable metrics (groundedness,
   relevance, coherence, safety) to know whether a change helped or hurt.
2. **Observability vs evaluation:** tracing captures *what happened* on each run (spans, tool calls,
   tokens); evaluation *scores* those runs against criteria.
3. **Close the loop:** trace → evaluate → adjust instructions/tools → re-evaluate.

## How to help
- Point the learner at `lesson-3-agent-evals/` and its README for the exact evaluator setup.
- Encourage a small, fixed test set of prompts so results are comparable across runs.
- When an eval fails, look at the trace first (bad tool call? missing context? weak instructions?)
  before changing the model.
- Keep evaluation runs cheap: small datasets, and delete resources afterward (see cost & cleanup).

## Validate
- `python -m py_compile <file>.py`.
- An evaluation run should produce per-criterion scores you can compare between versions.

## References
- `lesson-3-agent-evals/README.md`
- `MIGRATION-GUIDE.md` (current SDK patterns)
