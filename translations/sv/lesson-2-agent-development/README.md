<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:17:52+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "sv"
}
-->
# Lesson 2 Agent Development

Välkommen till den andra lektionen i kursen "Bygga AI-agent från grunden till produktion"!

I denna lektion kommer vi att täcka:

- Verktygen för att skapa våra AI-agenter
  
- Installationsinstruktioner för våra utvecklingsresurser

- Bästa praxis för utveckling av AI-agenter
  
- Genomgång av kod för att skapa våra AI-agenter
  
Låt oss börja med att titta på verktygen vi kommer att använda för att skapa våra AI-agenter.

## Verktyg och installationsinstruktioner

### Microsoft Foundry

För åtkomst till stora språkmodeller (LLMs) kommer vi att använda [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Det finns kostnader förknippade med att använda Foundry, så se till att följa instruktionerna för konto setup om du inte redan har åtkomst.

### OpenAI-modeller

Agentkodexemplen i denna kurs är inställda att använda OpenAI-modeller via [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Använd denna guide för att lära dig hur du distribuerar en modell med Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Välj en GPT-4.1 eller senare modell för denna kurs.

### Microsoft Agent Framework

Som nämnts tidigare kommer vi att använda [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) för att både skapa och orkestrera våra AI-agenter.

För att installera Microsoft Agent Framework och andra nödvändiga paket, kör följande kommando medan du är i rotmappen för detta projekt:

```bash
pip install -r requirements.txt
```

### Installera .env-variabler

För att köra kodexemplen i denna kurs behöver du skapa en `.env`-fil i rotmappen för detta projekt.

För att göra det enklare kan du kopiera den tillhandahållna `.env.example`-filen:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess modersmål ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->