# Les 2 Agentontwikkeling

Welkom bij de tweede les van de cursus "AI-agent bouwen van nul tot productie"!

In deze les behandelen we:

- De tools om onze AI-agenten te creëren
  
- Installatie-instructies voor onze ontwikkelbronnen

- Beste praktijken voor AI-agentontwikkeling
  
- Code walkthrough voor het maken van onze AI-agenten
  
Laten we beginnen met een kijkje te nemen naar de tools die we gebruiken om onze AI-agenten te maken.

## Tools en installatie-instructies

### Microsoft Foundry

Voor toegang tot Large Language Models (LLM's) gebruiken we [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Er zijn kosten verbonden aan het gebruik van Foundry, dus zorg ervoor dat je de instructies voor accountinstelling volgt als je nog geen toegang hebt.

### OpenAI-modellen

De agentcodevoorbeelden in deze cursus zijn ingesteld om OpenAI-modellen te gebruiken via [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Gebruik deze gids om te leren hoe je een model kunt uitrollen met Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Kies één GPT-5-seriemodel (bijvoorbeeld `gpt-5.1`) voor deze cursus. Vermijd afgeschreven modellen zoals GPT-4o en GPT-4.1, die in 2026 end-of-life zijn.

### Microsoft Agent Framework

Zoals eerder genoemd, gebruiken we het [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) voor zowel het creëren als het orkestreren van onze AI-agenten.

Je hebt **Python 3.12 of hoger** nodig. Om het Microsoft Agent Framework en andere vereiste pakketten te installeren, voer je het volgende commando uit in de rootdirectory van dit project:

```bash
pip install -r requirements.txt
```

### Authenticeren met Azure

De agenten authenticeren bij Microsoft Foundry met je Azure CLI-inloggegevens
(`AzureCliCredential`), dus je moet aanmelden voordat je een voorbeeld uitvoert:

```bash
az login
# Als u meer dan één abonnement hebt, selecteer dan degene met uw Foundry-project:
az account set --subscription "<your-subscription-id>"
```

Zorg ervoor dat je account de rol **Azure AI-gebruiker** (of vergelijkbaar) heeft binnen het Foundry
project zodat het de model- en agent-API's kan aanroepen.

### Setup .env-variabelen

Om de codevoorbeelden in deze cursus uit te voeren, moet je een `.env`-bestand maken in de rootdirectory van dit project.

Om het makkelijker te maken, kun je het meegeleverde `.env.example`-bestand kopiëren:

```bash
cp .env.example .env
``` 

Vul vervolgens de twee variabelen in die de agenten lezen (de `FoundryChatClient` haalt deze
automatisch op):

| Variabele | Wat het is | Waar te vinden |
|----------|------------|------------------|
| `FOUNDRY_PROJECT_ENDPOINT` | Jouw Foundry **project** endpoint, eindigend op `/api/projects/<project>` | Foundry portal → jouw project → **Overzicht** → *Endpoints* |
| `FOUNDRY_MODEL` | De naam van de modelimplementatie waarop je agenten draaien (bijvoorbeeld `gpt-5.1`) | Foundry portal → **Modellen + endpoints** |

### Maak de vector store van werknemers aan

Eén voorbeeld — de **Employee Search Agent** — zoekt een werknemersdirectory opgeslagen in een
Microsoft Foundry **vector store**. Maak deze één keer aan en kopieer het ID dat hij afdrukt naar je `.env`
als `VECTOR_STORE_ID` (voer dit uit vanuit de hoofddirectory van de repository zodat hij je `.env` laadt):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### Een voorbeeld uitvoeren

Elke agent draait een eigen lokale DevUI. Bijvoorbeeld:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

Open dan de afgedrukte `http://localhost:<port>` URL in je browser om met de agent te chatten.

## De agenten in deze les

Elk voorbeeld is een zelfstandige agent opgebouwd met het Microsoft Agent Framework. Samen
implementeren ze de scenario's die je hebt ontworpen in [Les 1](../lesson-1-agent-design/README.md):

| Voorbeeld | Les 1 scenario | Gebruikte tool | Poort |
|----------|----------------|---------------|--------|
| `employee-search-agent.py` | Scenario 1 — Werknemers zoeken | Foundry gehoste **bestandszoekfunctie** via een vector store | 8090 |
| `task-recommendation-agent.py` | Scenario 2 — Taanaanbeveling | **GitHub MCP** server (gehoste MCP-tool) | 8095 |
| `azure-learning-agent.py` | Scenario 3 — Code-assistent (onderzoek) | **Microsoft Learn MCP** server (gehoste MCP-tool) | 8092 |
| `coding-agent.py` | Scenario 3 — Code-assistent (coderen) | **Code Interpreter** | 8093 |
| `learning-recommendation-agent.py` | Ondersteunende agent | Learn MCP + redeneren | 8091 |
| `agent-orchestration.py` | Verbindt de scenario's met elkaar | Multi-agent **overdracht** orkestratie | 8094 |

> **Opmerking over de Task Recommendation Agent.** `task-recommendation-agent.py` heeft een
> `GITHUB_PERSONAL_ACCESS_TOKEN` nodig in je `.env` (maak er een aan op
> <https://github.com/settings/personal-access-tokens/new>). Het leest recente GitHub-activiteiten van een ontwikkelaar
> en beveelt 1–3 open issues aan die overeenkomen — precies het ontwerp van Scenario 2.
> Dit is het enige voorbeeld dat GitHub aanroept; de andere hebben alleen je Foundry-project nodig.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->