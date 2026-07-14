# Leksjon 2 Agentutvikling

Velkommen til den andre leksjonen i "Bygge AI-Agent fra null til produksjon-kurset"!

I denne leksjonen vil vi dekke:

- Verktøyene for å lage våre AI-agenter
  
- Oppsettsinstruksjoner for våre utviklingsressurser

- Beste praksis for AI-agentutvikling
  
- Kodegjennomgang for å lage våre AI-agenter
  
La oss starte med å se på verktøyene vi vil bruke for å lage våre AI-agenter.

## Verktøy og oppsettsinstruksjoner

### Microsoft Foundry

For tilgang til store språkmodeller (LLMs) vil vi bruke [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Det påløper kostnader ved bruk av Foundry, så sørg for å følge instruksjonene for kontooppsett hvis du ikke allerede har tilgang.

### OpenAI-modeller

Agentkodesamplet i dette kurset er satt opp til å bruke OpenAI-modeller gjennom [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Bruk denne guiden for å lære hvordan du distribuerer en modell med Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Velg én GPT-5-serie modell (for eksempel `gpt-5.1`) for dette kurset. Unngå pensjonerte modeller som GPT-4o og GPT-4.1, som når slutten av livssyklusen i 2026.

### Microsoft Agent Framework

Som nevnt tidligere, vil vi bruke [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) både for å lage og orkestrere våre AI-agenter.

Du trenger **Python 3.12 eller nyere**. For å installere Microsoft Agent Framework og andre nødvendige pakker, kjør følgende kommando mens du er i rotmappen av dette prosjektet:

```bash
pip install -r requirements.txt
```

### Autentiser med Azure

Agentene autentiserer til Microsoft Foundry ved å bruke dine Azure CLI-legitimasjoner
(`AzureCliCredential`), så du må logge inn før du kjører noen eksempler:

```bash
az login
# Hvis du har mer enn ett abonnement, velg det med Foundry-prosjektet ditt:
az account set --subscription "<your-subscription-id>"
```

Sørg for at kontoen din har **Azure AI User**-rollen (eller tilsvarende) på Foundry
prosjektet slik at den kan kalle modell- og agent-APIene.

### Sett opp .env-variabler

For å kjøre kodesamples i dette kurset, må du lage en `.env`-fil i rotmappen av dette prosjektet.

For å gjøre det enklere kan du kopiere den medfølgende `.env.example`-filen:

```bash
cp .env.example .env
``` 

Fyll så inn de to variablene agentene leser ( `FoundryChatClient` plukker disse opp
automatisk):

| Variabel | Hva det er | Hvor du finner den |
|----------|------------|------------------|
| `FOUNDRY_PROJECT_ENDPOINT` | Din Foundry **prosjekt** endepunkt, som ender med `/api/projects/<project>` | Foundry-portalen → ditt prosjekt → **Oversikt** → *Endepunkter* |
| `FOUNDRY_MODEL` | Navnet på modellutplasseringen agentene dine kjører på (for eksempel `gpt-5.1`) | Foundry-portalen → **Modeller + endepunkter** |

### Lag vektorbutikken for ansatte

Ett eksempel — **Employee Search Agent** — søker i en ansattkatalog som holdes i en
Microsoft Foundry **vektorbutikk**. Lag den én gang og kopier ID-en den skriver ut inn i din `.env`
som `VECTOR_STORE_ID` (kjør fra rotmappen i repositoriet slik at den leser `.env`-filen):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### Kjør et eksempel

Hver agent kjører sitt eget lokale DevUI. For eksempel:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

Så åpner du den printede `http://localhost:<port>` URL-en i nettleseren for å chatte med agenten.

## Agentene i denne leksjonen

Hvert eksempel er en frittstående agent bygget med Microsoft Agent Framework. Sammen
implementerer de scenariene du designet i [Leksjon 1](../lesson-1-agent-design/README.md):

| Eksempel | Scenario fra leksjon 1 | Verktøy brukt | Port |
|--------|-------------------|-----------|------|
| `employee-search-agent.py` | Scenario 1 — Ansattsøk | Foundry hostet **fil-søk** over en vektorbutikk | 8090 |
| `task-recommendation-agent.py` | Scenario 2 — Oppgaveanbefaling | **GitHub MCP** server (hostet MCP-verktøy) | 8095 |
| `azure-learning-agent.py` | Scenario 3 — Kodeassistent (forskning) | **Microsoft Learn MCP** server (hostet MCP-verktøy) | 8092 |
| `coding-agent.py` | Scenario 3 — Kodeassistent (kode) | **Kodefortolker** | 8093 |
| `learning-recommendation-agent.py` | Støtteagent | Learn MCP + resonnement | 8091 |
| `agent-orchestration.py` | Binder scenariene sammen | Multi-agent **overleverings** orkestrering | 8094 |

> **Merk om Oppgaveanbefalingsagenten.** `task-recommendation-agent.py` trenger en
> `GITHUB_PERSONAL_ACCESS_TOKEN` i din `.env` (lag en på
> <https://github.com/settings/personal-access-tokens/new>). Den leser en utviklers nylige
> GitHub-aktivitet og anbefaler 1–3 åpne issues som matcher – akkurat som Scenario 2-designet.
> Dette er det eneste eksemplet som kontakter GitHub; de andre trenger kun ditt Foundry-prosjekt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->