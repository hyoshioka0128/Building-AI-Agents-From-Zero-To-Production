# Course skills

This folder contains **skill files** for the *Building AI Agents from Zero to Production* course.

Each skill is a self-contained `SKILL.md` (with `name` + `description` frontmatter) that an AI
assistant — such as GitHub Copilot — can load to help a learner with one area of the course. The
skills encode the course's **guardrails** (current Microsoft Foundry terminology, the pinned
Microsoft Agent Framework SDK, the Responses API, and the approved `gpt-5.1` / `gpt-5-codex` models)
so assistant guidance stays consistent with the lessons.

| Skill | Helps with | Maps to |
|-------|------------|---------|
| [`foundry-agent-basics`](./foundry-agent-basics/SKILL.md) | Build a first agent with MAF + Foundry | Lessons 1–2 |
| [`mcp-integration`](./mcp-integration/SKILL.md) | Add tools via MCP / Hosted MCP | Lessons 2, 5 |
| [`agent-evaluation`](./agent-evaluation/SKILL.md) | Evaluate and observe agents | Lesson 3 |
| [`hosted-agent-deployment`](./hosted-agent-deployment/SKILL.md) | Deploy hosted agents, Capability Hosts | Lessons 4–5 |
| [`microsoft-toolbox`](./microsoft-toolbox/SKILL.md) | Define and govern tools centrally | Lesson 6 |
| [`multi-agent-a2a`](./multi-agent-a2a/SKILL.md) | Compose agents over the A2A protocol | Lesson 7 |

These skills are documentation for humans and assistants; they do not change how the samples run.
See [`AGENTS.md`](../../AGENTS.md) for repository-wide contributor and agent rules.
