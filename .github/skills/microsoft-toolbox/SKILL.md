---
name: microsoft-toolbox
description: >-
  Help a learner use Microsoft Toolbox to define tools once and govern them centrally, then consume
  a toolbox from an agent through a single MCP endpoint. Use for Lesson 6 tasks: tool discovery,
  registration, governance, and versioning.
---

# Microsoft Toolbox

Guidance for centralised tool governance (Lesson 6).

## Guardrails (always apply)
- Terminology: **Microsoft Toolbox** (define/govern tools centrally), consumed by agents over an
  **MCP** endpoint.
- The **consume** side works with the pinned `agent-framework` SDK. The Toolbox **management** API
  (`project.toolboxes.*`) is **preview** and is **not** in the pinned SDK — call this out and avoid
  presenting it as GA.
- Endpoint via `TOOLBOX_ENDPOINT` in `.env`; auth via `az login`.

## Concepts a learner should grasp
1. **Why a toolbox:** define a tool once, govern it centrally (access, versioning, approvals), and
   let many agents consume it — instead of each agent re-implementing tools.
2. **Consume via one MCP endpoint:** an agent points at the toolbox's MCP endpoint and gets its
   governed tools, rather than wiring each tool individually.
3. **Governance & versioning:** central control makes it safe to update or retire a tool without
   breaking every agent.

## Worked example in this repo
- `lesson-6-toolbox/toolbox_agent.py` is the **consume** sample: it reaches a toolbox through a
  single MCP endpoint and uses its tools. Use it as the reference.

## How to help
- Start from `toolbox_agent.py`; adapt the toolbox endpoint.
- If the learner asks to *create/manage* toolboxes in code, explain the management API is preview and
  may require a newer SDK than the pinned one; prefer the portal/preview docs and keep the sample on
  the consume side.

## Validate
- `python -m py_compile lesson-6-toolbox/toolbox_agent.py`.
- The agent should discover and call at least one governed tool via the toolbox endpoint.

## References
- `lesson-6-toolbox/README.md`
