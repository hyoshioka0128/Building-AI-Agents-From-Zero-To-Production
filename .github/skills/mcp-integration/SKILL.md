---
name: mcp-integration
description: >-
  Help a learner give an agent tools through the Model Context Protocol (MCP) — both client-side MCP
  and Foundry Hosted MCP tools. Use when connecting an agent to an MCP server (e.g. the GitHub MCP
  server), adding a remote tool, or reasoning about MCP approval/governance.
---

# MCP integration

Guidance for adding tools to an agent via the **Model Context Protocol (MCP)**.

## Guardrails (always apply)
- Terminology: **MCP**, **Hosted MCP tools** (Foundry-managed), **Microsoft Learn MCP server**.
- Client-side MCP uses **`MCPStreamableHTTPTool`** from the current `agent-framework` surface. The
  old top-level `HostedMCPTool` symbol is gone — hosted tools are configured through the Foundry
  hosted-tool types.
- Secrets (PATs, tokens) come from `.env` only. In this course the GitHub MCP server is passed a
  Bearer PAT via headers read from `GITHUB_PERSONAL_ACCESS_TOKEN` — never hardcode it.

## Concepts a learner should grasp
1. **Why MCP:** one open protocol lets an agent discover and call tools hosted anywhere, instead of
   bespoke per-tool integrations.
2. **Client MCP vs Hosted MCP:** client-side, your process connects to an MCP endpoint and executes
   tool calls; Hosted MCP runs the connection inside Foundry with managed identity, approvals and
   observability.
3. **Approval workflows:** hosted MCP tools can require human approval before a tool runs — important
   for governance in production (covered in Lesson 5).

## Worked example in this repo
- `lesson-2-agent-development/task-recommendation-agent.py` connects an agent to the **remote GitHub
  MCP server** as a tool (Lesson 1 Scenario 2), passing a Bearer PAT via headers. Use it as the
  reference implementation.

## How to help
- Start from `task-recommendation-agent.py` and adapt the MCP endpoint / headers.
- For hosted/enterprise scenarios, direct the learner to `lesson-5-hosted-agents-production/` for
  the approval-workflow and governance discussion.
- Confirm the target MCP server URL and required auth before writing code.

## Validate
- `python -m py_compile <file>.py`.
- The agent should list/call at least one MCP tool and return a grounded answer.

## References
- `lesson-2-agent-development/README.md` (sample catalog), `lesson-5-hosted-agents-production/README.md`
