"""
Task Recommendation Agent - Uses the GitHub MCP Server with FoundryChatClient and DevUI

This implements Scenario 2 from Lesson 1: based on a new employee's recent GitHub
activity, recommend 1-3 open issues they could pick up. It uses the Microsoft Foundry
hosted MCP tool (`client.get_mcp_tool(...)`) pointed at GitHub's remote MCP server, so
the MCP connection is handled server-side by the Microsoft Foundry Agent Service.

Prerequisites:
1. Azure CLI credentials configured (run `az login`).
2. A GitHub Personal Access Token in your .env as GITHUB_PERSONAL_ACCESS_TOKEN.
   Create one at https://github.com/settings/personal-access-tokens/new
   (read access to the repositories and profile you want the agent to look at).

Usage:
    python task-recommendation-agent.py

Then open http://localhost:8095 in your browser.
"""

import logging
import os

from azure.identity.aio import AzureCliCredential
from dotenv import load_dotenv

from agent_framework.foundry import FoundryChatClient

# Enable logging to see tool calls
logging.basicConfig(level=logging.INFO)
logging.getLogger("agent_framework").setLevel(logging.DEBUG)

# Load environment variables from .env file
load_dotenv()

# GitHub's remote MCP server. The Foundry Agent Service connects to it server-side.
GITHUB_MCP_URL = "https://api.githubcopilot.com/mcp/"

github_pat = os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN")
if not github_pat:
    raise EnvironmentError(
        "Set GITHUB_PERSONAL_ACCESS_TOKEN in your .env. Create a token at "
        "https://github.com/settings/personal-access-tokens/new"
    )

# Agent instructions - implements Lesson 1, Scenario 2
AGENT_INSTRUCTIONS = """You are a task recommendation assistant that helps a new developer find good first issues to work on.

You have access to the GitHub MCP Server. Use it to build a picture of the developer and match them to work.

When the user gives you a GitHub username and a repository (owner/repo), follow these steps:

1. **Build a developer profile**: Use the GitHub MCP tools to read the developer's most recent activity - look at their last ~5 commits and the languages/technologies they appear in. Summarise their apparent experience level and areas of strength.

2. **List candidate work**: Use the GitHub MCP tools to list the OPEN issues on the target repository. Prefer issues labelled things like "good first issue", "help wanted", "bug", or "documentation" when they exist.

3. **Match and recommend**: Recommend 1-3 open issues that best fit the developer's profile. For each recommendation include:
   - The issue number, title, and link.
   - One or two sentences on WHY it fits this developer (tie it back to their recent commits/skills).
   - A rough difficulty estimate (easy / medium / hard).

4. **Be honest**: If you cannot find a good match, say so rather than forcing a recommendation. If you need the username or repository, ask for it.

Keep the tone encouraging and practical - this is someone's first week."""

# Create credential and Microsoft Foundry chat client
credential = AzureCliCredential()
client = FoundryChatClient(credential=credential)

# Create agent with a hosted MCP tool for the GitHub MCP Server.
# The PAT is passed as an Authorization header; Foundry injects it server-side.
agent = client.as_agent(
    name="TaskRecommendationAgent",
    instructions=AGENT_INSTRUCTIONS,
    tools=client.get_mcp_tool(
        name="GitHub MCP",
        url=GITHUB_MCP_URL,
        approval_mode="never_require",
        headers={"Authorization": f"Bearer {github_pat}"},
    ),
)

if __name__ == "__main__":
    from agent_framework.devui import serve

    print("Starting DevUI server at http://localhost:8095")
    serve(entities=[agent], port=8095)
