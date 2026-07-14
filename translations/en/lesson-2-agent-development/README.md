# Lesson 2 Agent Development

Welcome to the second lesson of the "Building AI Agent from Zero to Production Course"!

In this lesson we will cover:

- The Tools to Create our AI Agents
  
- Setup Instructions for our Development Resources

- AI Agent Development Best Practices
  
- Code Walkthrough for Creating our AI Agents
  
Let's start by looking at the tools we will use to create our AI Agents.

## Tools and Setup Instructions

### Microsoft Foundry

For access to Large Language Models (LLMs) we will be using [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). There are costs associated with using Foundry so please make sure to follow the instructions for account setup if you do not already have access.

### OpenAI Models

The agent code samples in this course are set up to use OpenAI models through [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Use this guide to learn how to deploy a model using Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Choose one GPT-5 series model (for example `gpt-5.1`) for this course. Avoid retired models such as GPT-4o and GPT-4.1, which reach end of life in 2026.

### Microsoft Agent Framework

As mentioned earlier, we will be using the [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) to both create and orchestrate our AI Agents.

You will need **Python 3.12 or later**. To install the Microsoft Agent Framework and other required packages, run the following command while in the root directory of this project:

```bash
pip install -r requirements.txt
```

### Authenticate with Azure

The agents authenticate to Microsoft Foundry using your Azure CLI credentials
(`AzureCliCredential`), so you must sign in before running any sample:

```bash
az login
# If you have more than one subscription, select the one with your Foundry project:
az account set --subscription "<your-subscription-id>"
```

Make sure your account has the **Azure AI User** role (or equivalent) on the Foundry
project so it can call the model and agent APIs.

### Setup .env Variables

To run the code samples in this course, you will need to create a `.env` file in the root directory of this project. 

To make it easier, you can copy the provided `.env.example` file:

```bash
cp .env.example .env
``` 

Then fill in the two variables the agents read (the `FoundryChatClient` picks these up
automatically):

| Variable | What it is | Where to find it |
|----------|------------|------------------|
| `FOUNDRY_PROJECT_ENDPOINT` | Your Foundry **project** endpoint, ending in `/api/projects/<project>` | Foundry portal → your project → **Overview** → *Endpoints* |
| `FOUNDRY_MODEL` | The model deployment name your agents run on (for example `gpt-5.1`) | Foundry portal → **Models + endpoints** |

### Create the employee vector store

One sample — the **Employee Search Agent** — searches an employee directory held in a
Microsoft Foundry **vector store**. Create it once and copy the ID it prints into your `.env`
as `VECTOR_STORE_ID` (run from the repository root so it picks up your `.env`):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### Run a sample

Each agent runs its own local DevUI. For example:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

Then open the printed `http://localhost:<port>` URL in your browser to chat with the agent.

## The agents in this lesson

Each sample is a standalone agent built with the Microsoft Agent Framework. Together they
implement the scenarios you designed in [Lesson 1](../lesson-1-agent-design/README.md):

| Sample | Lesson 1 scenario | Tool used | Port |
|--------|-------------------|-----------|------|
| `employee-search-agent.py` | Scenario 1 — Employee Search | Foundry hosted **file search** over a vector store | 8090 |
| `task-recommendation-agent.py` | Scenario 2 — Task Recommendation | **GitHub MCP** server (hosted MCP tool) | 8095 |
| `azure-learning-agent.py` | Scenario 3 — Code Assistant (research) | **Microsoft Learn MCP** server (hosted MCP tool) | 8092 |
| `coding-agent.py` | Scenario 3 — Code Assistant (code) | **Code Interpreter** | 8093 |
| `learning-recommendation-agent.py` | Supporting agent | Learn MCP + reasoning | 8091 |
| `agent-orchestration.py` | Ties the scenarios together | Multi-agent **handoff** orchestration | 8094 |

> **Note on the Task Recommendation Agent.** `task-recommendation-agent.py` needs a
> `GITHUB_PERSONAL_ACCESS_TOKEN` in your `.env` (create one at
> <https://github.com/settings/personal-access-tokens/new>). It reads a developer's recent
> GitHub activity and recommends 1–3 open issues that match — exactly the Scenario 2 design.
> This is the only sample that calls GitHub; the others need only your Foundry project.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->