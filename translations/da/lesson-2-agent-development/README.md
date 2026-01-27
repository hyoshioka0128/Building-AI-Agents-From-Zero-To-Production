<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:18:55+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "da"
}
-->
# Lesson 2 Agent Development

Velkommen til anden lektion af "Bygning af AI Agent fra Start til Produktion Kursus"!

I denne lektion vil vi dække:

- Værktøjerne til at skabe vores AI-agenter
  
- Opsætningsinstruktioner for vores udviklingsressourcer

- Bedste praksis for AI-agentudvikling
  
- Gennemgang af kode til at skabe vores AI-agenter
  
Lad os starte med at se på de værktøjer, vi vil bruge til at skabe vores AI-agenter.

## Værktøjer og opsætningsinstruktioner

### Microsoft Foundry

For adgang til store sprogmodeller (LLMs) vil vi bruge [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Der er omkostninger forbundet med brug af Foundry, så sørg for at følge instruktionerne for kontooprettelse, hvis du ikke allerede har adgang.

### OpenAI-modeller

Eksempelagentkoderne i dette kursus er sat op til at bruge OpenAI-modeller gennem [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Brug denne vejledning til at lære, hvordan du implementerer en model ved hjælp af Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Vælg én GPT-4.1 eller nyere model til dette kursus.

### Microsoft Agent Framework

Som nævnt tidligere, vil vi bruge [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) både til at skabe og orkestrere vores AI-agenter.

For at installere Microsoft Agent Framework og andre nødvendige pakker skal du køre følgende kommando, mens du er i roddirektoriet af dette projekt:

```bash
pip install -r requirements.txt
```

### Opsæt .env-variabler

For at køre eksempelkoden i dette kursus skal du oprette en `.env`-fil i roddirektoriet af dette projekt.

For at gøre det lettere kan du kopiere den medfølgende `.env.example`-fil:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For afgørende information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->