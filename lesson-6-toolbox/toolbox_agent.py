"""
Toolbox Agent - Consume a Microsoft Foundry Toolbox from an agent via one MCP endpoint

This is the "Consume" side of Lesson 6. A Toolbox exposes all of its tools through a single
MCP-compatible endpoint. Instead of wiring each tool into the agent (as Lesson 2 did with a
hardcoded Learn MCP URL and a file-search vector store), this agent points ONE hosted MCP tool
at the toolbox endpoint and inherits every governed tool the toolbox contains.

Because the agent connects to the toolbox *consumer* endpoint (which always serves the default
version), you can add, remove, or upgrade tools in the toolbox without changing this code.

Prerequisites:
1. Azure CLI credentials configured (run `az login`).
2. A toolbox already created in your Foundry project. The management API is currently in
   preview - create a toolbox from the Foundry portal, the Foundry Toolkit for VS Code, the
   REST API, or a preview SDK build (see this lesson's README, section 3).
3. TOOLBOX_ENDPOINT set in your .env, e.g.
   https://<account>.services.ai.azure.com/api/projects/<project>/toolboxes/<name>/mcp?api-version=v1

Usage:
    python toolbox_agent.py

Then open http://localhost:8096 in your browser.
"""

import logging
import os

from azure.identity.aio import AzureCliCredential
from dotenv import load_dotenv

from agent_framework.foundry import FoundryChatClient

# Enable logging to see tool calls flow through the toolbox
logging.basicConfig(level=logging.INFO)
logging.getLogger("agent_framework").setLevel(logging.DEBUG)

load_dotenv()

toolbox_endpoint = os.environ.get("TOOLBOX_ENDPOINT")
if not toolbox_endpoint:
    raise EnvironmentError(
        "Set TOOLBOX_ENDPOINT in your .env to your toolbox *consumer* MCP endpoint:\n"
        "  https://<account>.services.ai.azure.com/api/projects/<project>"
        "/toolboxes/<name>/mcp?api-version=v1\n"
        "Create a toolbox first (Foundry portal / Foundry Toolkit / REST) - see the README."
    )

AGENT_INSTRUCTIONS = """You are a helpful assistant for new developers at Zava.

You have access to a Microsoft Foundry Toolbox exposed through a single MCP endpoint. The toolbox
may contain web search, MCP servers, Azure AI Search, and other governed tools. Discover the
available tools and use whichever ones best answer the user's question. Be clear about which tool
you used and why."""

# One MCP tool pointed at the toolbox endpoint gives the agent EVERY tool in the toolbox.
# The connection is handled server-side by the Microsoft Foundry Agent Service.
credential = AzureCliCredential()
client = FoundryChatClient(credential=credential)

agent = client.as_agent(
    name="ToolboxAgent",
    instructions=AGENT_INSTRUCTIONS,
    tools=client.get_mcp_tool(
        name="Foundry Toolbox",
        url=toolbox_endpoint,
        approval_mode="never_require",
    ),
)

if __name__ == "__main__":
    from agent_framework.devui import serve

    print("Starting DevUI server at http://localhost:8096")
    serve(entities=[agent], port=8096)
