---
name: hosted-agent-deployment
description: >-
  Help a learner deploy an agent to production as a Microsoft Foundry Hosted Agent, and decide when
  Capability Hosts are needed. Use for Lessons 4–5: hosted deployment, thread/memory persistence,
  bring-your-own storage, and enterprise governance.
---

# Hosted agent deployment

Guidance for taking an agent to production (Lessons 4–5).

## Guardrails (always apply)
- Terminology: **Hosted Agents**, **Capability Hosts**, **Microsoft Foundry Agent Service**.
- Deploy with the current SDK/Responses API; models `gpt-5.1` (chat) / `gpt-5-codex` (coding).
- Config and secrets via `.env` / managed identity — never hardcode endpoints or keys.

## The key distinction (teach this clearly)
- **Hosted Agents** provide the Microsoft-managed execution environment: compute, scaling, identity,
  observability and session management. You do **not** need a Capability Host just to run a Hosted
  Agent.
- **Capability Hosts** are only required when you want Agent Service to use **customer-owned
  resources** instead of Microsoft-managed storage.
  - Happy with default Microsoft-managed storage, vector search and conversation persistence?
    **No Capability Host configuration is required.**
  - Need data sovereignty, private networking, compliance controls, or storage in **your own**
    Azure Cosmos DB, Azure Storage Account and Azure AI Search? Configure Capability Hosts to
    connect Agent Service to those resources.

## Concepts a learner should grasp
1. **Basic vs standard setup:** basic = Microsoft-managed; standard = bring-your-own resources via
   Capability Hosts + connections.
2. **Persistence:** hosted agents persist threads and memory server-side (long-running conversations).
3. **Governance:** identity, private networking, Hosted MCP approval workflows, cost controls.

## How to help
- Start from `lesson-4-agentdeployment/` for the deploy + ChatKit front end, then
  `lesson-5-hosted-agents-production/` for enterprise/BYO-storage and governance.
- Before recommending Capability Hosts, ask whether the learner actually needs customer-owned
  storage/networking — if not, keep the basic setup.
- Remind them of **cost & cleanup**: delete the resource group when finished.

## Validate
- `python -m py_compile` on any deploy scripts.
- CI smoke test: `.github/workflows/smoke-test-hosted-agent.yml` (workflow_dispatch, OIDC) exercises
  a deployed hosted agent.

## References
- `lesson-4-agentdeployment/README.md`, `lesson-5-hosted-agents-production/README.md`
