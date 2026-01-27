<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:20:41+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "nl"
}
-->
# Les 2 Agentontwikkeling

Welkom bij de tweede les van de cursus "AI-agent bouwen van nul tot productie"!

In deze les behandelen we:

- De tools om onze AI-agenten te creëren

- Installatie-instructies voor onze ontwikkelingsmiddelen

- Beste praktijken voor AI-agentontwikkeling

- Code walkthrough voor het creëren van onze AI-agenten

Laten we beginnen met de tools te bekijken die we zullen gebruiken om onze AI-agenten te creëren.

## Tools en Installatie-instructies

### Microsoft Foundry

Voor toegang tot Large Language Models (LLM's) zullen we [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) gebruiken. Er zijn kosten verbonden aan het gebruik van Foundry, dus zorg ervoor dat je de instructies voor het instellen van een account volgt als je nog geen toegang hebt.

### OpenAI-modellen

De voorbeeldcode voor agenten in deze cursus is ingesteld om OpenAI-modellen te gebruiken via [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Gebruik deze gids om te leren hoe je een model kunt implementeren met Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Kies voor deze cursus één GPT-4.1 of een later model.

### Microsoft Agent Framework

Zoals eerder genoemd, zullen we het [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) gebruiken om onze AI-agenten zowel te creëren als te orkestreren.

Om het Microsoft Agent Framework en andere vereiste pakketten te installeren, voer je het volgende commando uit vanuit de hoofdmap van dit project:

```bash
pip install -r requirements.txt
```

### Instellen van .env-variabelen

Om de voorbeeldcode in deze cursus uit te voeren, moet je een `.env`-bestand maken in de hoofdmap van dit project.

Om het makkelijker te maken, kun je het meegeleverde `.env.example`-bestand kopiëren:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal dient als gezaghebbende bron te worden beschouwd. Voor kritieke informatie wordt aanbevolen een professionele menselijke vertaling te gebruiken. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->