# Lesson 2 Agent Development

Welcome to di second lesson of di "Building AI Agent from Zero to Production Course"!

For dis lesson we go cover:

- Di Tools we go use create our AI Agents
  
- Setup Instructions for our Development Resources

- AI Agent Development Best Practices
  
- Code Walkthrough for Creating our AI Agents
  
Make we start by look di tools we go use create our AI Agents.

## Tools and Setup Instructions

### Microsoft Foundry

For access to Large Language Models (LLMs) we go dey use [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). E get cost wey dem dey put for using Foundry so abeg make sure say you follow di instructions for account setup if you never get access before.

### OpenAI Models

Di agent code samples for dis course don setup to use OpenAI models through [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Use dis guide to learn how to deploy model using Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Choose one GPT-4.1 or later model for dis course.

### Microsoft Agent Framework

As we mention before, we go dey use [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) to both create and arrange our AI Agents.

To install Microsoft Agent Framework and other packages we need, run dis command when you dey for root directory of dis project:

```bash
pip install -r requirements.txt
```

### Setup .env Variables

To run di code samples for dis course, you need create `.env` file for di root directory of dis project.

To make am easier, you fit copy di provided `.env.example` file:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document na im wey AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) translate. Even though we try make am correct, abeg sabi say automated translation fit get some mistakes or no too correct. Di original document wey e dey for im own language na di correct one. If na serious matter, na professional human translation you suppose use. We no go take responsibility for any wahala or wrong meaning wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->