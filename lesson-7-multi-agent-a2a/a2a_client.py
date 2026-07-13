"""
A2A Client - Call a remote agent over the Agent-to-Agent (A2A) protocol

This connects to an agent exposed as an A2A service (for example the companion
`a2a_server.py`), discovers its Agent Card from the URL, and calls it exactly like a local
Microsoft Agent Framework agent. The transport, discovery, and task handling are handled by
the A2A protocol - your code just calls `agent.run(...)`.

This is the "consume" half of A2A: an orchestrator can hold references to many remote
`A2AAgent`s - each owned by a different team or organisation - and route work to them as
networked peers instead of hardcoding them into one process.

Prerequisites:
1. The A2A server is running: `python a2a_server.py` (in another terminal).

Usage:
    python a2a_client.py "Write a Python function that reverses a string."
"""

import asyncio
import os
import sys

from dotenv import load_dotenv

from agent_framework.a2a import A2AAgent

load_dotenv()

SERVER_URL = os.environ.get("A2A_SERVER_URL", "http://localhost:9000")


async def main() -> None:
    query = (
        " ".join(sys.argv[1:])
        if len(sys.argv) > 1
        else "Write a Python function that reverses a string."
    )

    # Discover and connect to the remote agent by URL (fetches its Agent Card).
    remote_agent = A2AAgent(name="remote-coding-assistant", url=SERVER_URL)

    print(f"Calling remote agent at {SERVER_URL} ...\n")
    result = await remote_agent.run(query)

    # AgentRunResponse exposes .text; fall back to str() for safety.
    print(getattr(result, "text", None) or str(result))


if __name__ == "__main__":
    asyncio.run(main())
