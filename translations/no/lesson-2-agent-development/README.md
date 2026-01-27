<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:19:15+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "no"
}
-->
# Lesson 2 Agent Development

Velkommen til den andre leksjonen i "Bygge AI-agent fra null til produksjon-kurset"!

I denne leksjonen vil vi dekke:

- Verktøyene for å lage våre AI-agenter
  
- Oppsettinstruksjoner for våre utviklingsressurser

- Beste praksis for AI-agentutvikling
  
- Gjennomgang av kode for å lage våre AI-agenter
  
La oss starte med å se på verktøyene vi vil bruke for å lage våre AI-agenter.

## Verktøy og oppsettinstruksjoner

### Microsoft Foundry

For tilgang til store språkmodeller (LLMs) vil vi bruke [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Det påløper kostnader for å bruke Foundry, så sørg for å følge instruksjonene for kontooppsett hvis du ikke allerede har tilgang.

### OpenAI-modeller

Agentkodesnuttene i dette kurset er satt opp til å bruke OpenAI-modeller gjennom [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Bruk denne guiden for å lære hvordan du distribuerer en modell ved hjelp av Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Velg én GPT-4.1 eller senere modell for dette kurset.

### Microsoft Agent Framework

Som nevnt tidligere, vil vi bruke [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) både for å opprette og orkestrere våre AI-agenter.

For å installere Microsoft Agent Framework og andre nødvendige pakker, kjør følgende kommando mens du er i rotkatalogen til dette prosjektet:

```bash
pip install -r requirements.txt
```

### Sett opp .env-variabler

For å kjøre kodesnuttene i dette kurset, må du opprette en `.env`-fil i rotkatalogen til dette prosjektet.

For å gjøre det enklere, kan du kopiere den medfølgende `.env.example`-filen:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår fra bruken av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->