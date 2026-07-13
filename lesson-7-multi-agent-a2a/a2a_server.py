"""
A2A Server - Expose a Microsoft Foundry agent as an Agent-to-Agent (A2A) service

This wraps a Microsoft Agent Framework agent with `A2AExecutor` and serves it over the
open Agent-to-Agent (A2A) protocol using the `a2a` SDK. Any A2A-capable client - including
the companion `a2a_client.py`, another framework, or a different organisation's agent - can
then discover this agent's **Agent Card** and call it as a networked peer.

Contrast with Lesson 2's `agent-orchestration.py`: there, agents hand off inside a single
process and share one graph. Here, the agent is an independent **service** with its own URL,
identity, and lifecycle - the pattern you use to compose agents across teams, repos, or
organisational boundaries.

Prerequisites:
1. Azure CLI credentials configured (run `az login`).
2. FOUNDRY_PROJECT_ENDPOINT and FOUNDRY_MODEL set in your .env (see the course README).

Usage:
    # Terminal 1 - start the A2A server
    python a2a_server.py

    # Terminal 2 - call it with the A2A client
    python a2a_client.py

The Agent Card is published at http://localhost:9000/.well-known/agent-card.json
"""

import os

import uvicorn
from azure.identity.aio import AzureCliCredential
from dotenv import load_dotenv

from agent_framework.a2a import A2AExecutor
from agent_framework.foundry import FoundryChatClient

from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill

load_dotenv()

HOST = os.environ.get("A2A_HOST", "localhost")
PORT = int(os.environ.get("A2A_PORT", "9000"))

# 1. Build a normal Microsoft Foundry agent (the coding specialist from the onboarding scenario)
credential = AzureCliCredential()
client = FoundryChatClient(credential=credential, model="gpt-5-codex")

agent = client.as_agent(
    name="coding-assistant",
    instructions=(
        "You are a coding assistant for new developers. Generate clean, well-documented, "
        "runnable code samples with type hints and a short explanation. Keep answers focused."
    ),
)

# 2. Describe the agent with an Agent Card - this is how other agents DISCOVER what it can do
agent_card = AgentCard(
    name="Coding Assistant",
    description="Generates runnable code samples to help new developers get started.",
    url=f"http://{HOST}:{PORT}/",
    version="1.0.0",
    capabilities=AgentCapabilities(streaming=True),
    default_input_modes=["text"],
    default_output_modes=["text"],
    skills=[
        AgentSkill(
            id="generate-code",
            name="Generate code",
            description="Write a runnable, well-documented code snippet for a described task.",
            tags=["code", "python", "onboarding"],
            examples=["Write a Python function that reverses a string."],
        )
    ],
)

# 3. Wrap the agent as an A2A executor and mount it on an A2A HTTP application
request_handler = DefaultRequestHandler(
    agent_executor=A2AExecutor(agent),
    task_store=InMemoryTaskStore(),
)

app = A2AStarletteApplication(agent_card=agent_card, http_handler=request_handler).build()


if __name__ == "__main__":
    print(f"A2A server for '{agent_card.name}' listening on http://{HOST}:{PORT}")
    print(f"Agent Card: http://{HOST}:{PORT}/.well-known/agent-card.json")
    uvicorn.run(app, host=HOST, port=PORT)
