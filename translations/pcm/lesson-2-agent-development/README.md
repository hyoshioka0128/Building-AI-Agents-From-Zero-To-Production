# Lesson 2 Agent Development

Welcome to the second lesson of the  "Building AI Agent from Zero to Production Course"!

For dis lesson, we go cover:

- Di Tools wey we go use create our AI Agents
  
- Setup Instructions for our Development Resources

- AI Agent Development Best Practices
  
- Code Walkthorough for Creating our AI Agents
  
Make we start by look di tools wey we go use create our AI Agents.

## Tools and Setup Instructions

### Microsoft Foundry

To get access to Large Langauge Models (LLMs), we go dey use [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). E get cost wey come wit using Foundry so abeg make sure say you follow di instructions to set your account if you never get access before.

### OpenAI Models

Di agent code samples inside dis course dem set to use OpenAI models through [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Use dis guide to learn how to deploy model with Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Choose one GPT-5 series model (for example `gpt-5.1`) for dis course. No use retired models like GPT-4o and GPT-4.1, cuz dem go finish for 2026.

### Microsoft Agent Framework

As we talk before, we go dey use di [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) to create and manage our AI Agents.

You go need **Python 3.12 or newer**. To install Microsoft Agent Framework and other packages, run dis command when you dey inside di root directory of dis project:

```bash
pip install -r requirements.txt
```

### Authenticate with Azure

Di agents dey authenticate to Microsoft Foundry with your Azure CLI credentials
(`AzureCliCredential`), so you gats sign in before you run any sample:

```bash
az login
# If yu get pass one subscription, choose di one wey get your Foundry project:
az account set --subscription "<your-subscription-id>"
```

Make sure your account get **Azure AI User** role (or something similar) for di Foundry
project so e fit call di model and agent APIs.

### Setup .env Variables

To run di code samples for dis course, you go need create `.env` file for inside root directory of di project.

To make am easy, you fit copy di `.env.example` file wey dem give:

```bash
cp .env.example .env
``` 

Then put di two variables wey di agents dey read (di `FoundryChatClient` go grab dem
automatically):

| Variable | Wetin e be | Where you go find am |
|----------|------------|------------------|
| `FOUNDRY_PROJECT_ENDPOINT` | Your Foundry **project** endpoint, wey go end for `/api/projects/<project>` | Foundry portal → your project → **Overview** → *Endpoints* |
| `FOUNDRY_MODEL` | Di model deployment name wey your agents go run on top (like `gpt-5.1`) | Foundry portal → **Models + endpoints** |

### Create di employee vector store

One sample — di **Employee Search Agent** — dey search employee directory wey dey inside
Microsoft Foundry **vector store**. Create am once, then copy di ID wey e print into your `.env`
as `VECTOR_STORE_ID` (run am from repository root make e fit use your `.env`):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### Run sample

Each agent dey run hin own local DevUI. For example:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

Then open di URL wey e print `http://localhost:<port>` inside your browser to dey talk with di agent.

## Di agents for dis lesson

Each sample na standalone agent wey dem build with Microsoft Agent Framework. Together dem
dey carry out di scenarios wey you design for [Lesson 1](../lesson-1-agent-design/README.md):

| Sample | Lesson 1 scenario | Tool wey dem use | Port |
|--------|-------------------|-----------|------|
| `employee-search-agent.py` | Scenario 1 — Employee Search | Foundry hosted **file search** over a vector store | 8090 |
| `task-recommendation-agent.py` | Scenario 2 — Task Recommendation | **GitHub MCP** server (hosted MCP tool) | 8095 |
| `azure-learning-agent.py` | Scenario 3 — Code Assistant (research) | **Microsoft Learn MCP** server (hosted MCP tool) | 8092 |
| `coding-agent.py` | Scenario 3 — Code Assistant (code) | **Code Interpreter** | 8093 |
| `learning-recommendation-agent.py` | Supporting agent | Learn MCP + reasoning | 8091 |
| `agent-orchestration.py` | Ties di scenarios together | Multi-agent **handoff** orchestration | 8094 |

> **Note on the Task Recommendation Agent.** `task-recommendation-agent.py` need one
> `GITHUB_PERSONAL_ACCESS_TOKEN` for your `.env` (make one at
> <https://github.com/settings/personal-access-tokens/new>). E dey check developer recent
> GitHub activity and go recommend 1–3 open issues wey match — na exactly di Scenario 2 design.
> Dis na di only sample wey dey call GitHub; di others just need your Foundry project.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->