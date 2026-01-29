# Lesson 2 Agent Development

Welcome to the second lesson of the  "Building AI Agent from Zero to Production Course"!

In this lesson we will cover:

- The Tools to Create our AI Agents
  
- Setup Instructions for our Development Resources

- AI Agent Development Best Practices
  
- Code Walkthorough for Creating our AI Agents
  
Let's start by looking at the tools we will use to create our AI Agents.

## Tools and Setup Instructions

### Microsoft Foundry

For access to Large Langauge Models (LLMs) we will be using [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). There are costs associated with using Foundry so please make sure to follow the instructions for account setup if you do not already have access.

### OpenAI Models

The agent code samples in this course are setup to use OpenAI models through [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Use this guide to learn how to deploy a model using Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Choose one GPT-4.1 or later model for this course.

### Microsoft Agent Framework

As mentioned earlier, we will be using the [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) to both create and orchestrate our AI Agents.

To install the Microsoft Agent Framework and other required packages, run the following command while in the root directory of this project:

```bash
pip install -r requirements.txt
```

### Setup .env Variables

To run the code samples in this course, you will need to create a `.env` file in the root directory of this project. 

To make it easier, you can copy the provided `.env.example` file:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->