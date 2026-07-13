---
name: multi-agent-a2a
description: >-
  Help a learner compose agents as networked services using the open Agent-to-Agent (A2A) protocol —
  expose an agent as an A2A server and consume a remote agent as a peer. Use for Lesson 7 tasks:
  multi-agent orchestration and A2A client/server wiring.
---

# Multi-agent & A2A

Guidance for composing agents over the **Agent-to-Agent (A2A)** protocol (Lesson 7).

## Guardrails (always apply)
- Terminology: **A2A (Agent-to-Agent)** — an open protocol for agents to call each other as peers.
- Uses **preview** packages: `agent-framework-a2a`, `a2a-sdk`, and `uvicorn` (pinned in
  `requirements.txt` with a preview note). Present these as preview, not GA.
- Config via `.env`: `A2A_HOST`, `A2A_PORT`, `A2A_SERVER_URL`. Models `gpt-5.1` / `gpt-5-codex`.

## Concepts a learner should grasp
1. **Agents as services:** instead of one process holding every agent, each agent can be exposed
   over A2A and called remotely — enabling reuse, independent scaling and cross-team composition.
2. **Server vs client:** the server publishes an agent (with an agent card) over A2A; the client
   discovers and calls it as a peer using `A2AAgent`.
3. **Orchestration:** a coordinating agent can delegate sub-tasks to specialised remote agents.

## Worked example in this repo (validated live)
- `lesson-7-multi-agent-a2a/a2a_server.py` — exposes a Foundry agent over A2A (default port 9000).
- `lesson-7-multi-agent-a2a/a2a_client.py` — consumes the remote agent as a peer and prints its
  response. This pair was validated end-to-end against a live Foundry agent.

## How to help
- Start the server, then run the client; confirm `A2A_SERVER_URL` matches the server's host/port.
- Adapt the server's underlying agent (instructions/tools) rather than rewriting the A2A plumbing.
- Keep the preview caveat visible when advising on production use.

## Validate
- `python -m py_compile` on both server and client.
- Client should reach the running server and return a real model response.

## References
- `lesson-7-multi-agent-a2a/README.md`
