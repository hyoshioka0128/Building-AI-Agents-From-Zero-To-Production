# Copyright (c) Microsoft. All rights reserved.

import os

from agent_framework.foundry import FoundryChatClient
# pyright: ignore[reportUnknownVariableType]
from azure.ai.agentserver.agentframework import from_agent_framework
from azure.identity import DefaultAzureCredential

# Configuration from environment (set by the deployment; see .env.example)
PROJECT_ENDPOINT = os.environ.get("AZURE_AI_PROJECT_ENDPOINT")
MODEL_DEPLOYMENT = os.environ.get("MODEL_DEPLOYMENT", "gpt-5.1")
VECTOR_STORE_ID = os.environ.get("VECTOR_STORE_ID")


def main():
    # Create the Microsoft Foundry chat client. Endpoint and model are read from
    # the same environment variables the deployment provides (AZURE_AI_PROJECT_ENDPOINT,
    # MODEL_DEPLOYMENT) so local runs and hosted runs stay consistent.
    client = FoundryChatClient(
        project_endpoint=PROJECT_ENDPOINT,
        model=MODEL_DEPLOYMENT,
        credential=DefaultAzureCredential(),
    )

    # Create the hosted file search tool for the employee directory
    file_search_tool = client.get_file_search_tool(
        vector_store_ids=[VECTOR_STORE_ID]
    )

    # Create a single Developer Onboarding Agent with MCP and File Search tools
    agent = client.as_agent(
        name="DevOnboardingAgent",
        instructions="""You are a comprehensive Developer Onboarding Assistant. You help new developers with three key areas:

## 1. Employee Search & Connections
Use the file search tool to find information about employees when asked questions like:
- "Who should I connect with about [topic]?"
- "Who works on the [team name] team?"
- "Find colleagues with experience in [technology]"
- "Who is the manager for [team]?"
- "List employees who came from [company]"

When searching for employees, provide helpful details about their role, team, and expertise.

## 2. Learning & Training
Use the Microsoft Learn MCP tool for:
- Finding training resources and learning paths
- Creating customized learning paths based on role and goals
- Recommending certifications and training programs
- Finding documentation for specific technologies
- Prioritizing foundational knowledge before advanced topics

## 3. Coding Assistance
- Generate code samples in multiple languages (Python, C#, JavaScript, etc.)
- Explain coding patterns and best practices
- Help debug and troubleshoot code issues
- Provide Azure-specific code examples and SDK usage
- Write clean, well-commented, production-ready code

Always be welcoming, helpful, and provide actionable recommendations.""",
        tools=[
            file_search_tool,
            client.get_mcp_tool(
                name="Microsoft Learn MCP",
                url="https://learn.microsoft.com/api/mcp",
                approval_mode="never_require",
            ),
        ],
    )

    # Run the agent as a hosted agent
    from_agent_framework(agent).run()


if __name__ == "__main__":
    main()
