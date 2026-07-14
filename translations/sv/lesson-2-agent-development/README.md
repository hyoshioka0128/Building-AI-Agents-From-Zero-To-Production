# Lektion 2 Agentutveckling

Välkommen till den andra lektionen i kursen "Bygga AI-agent från grunden till produktion"!

I denna lektion kommer vi att täcka:

- Verktygen för att skapa våra AI-agenter
  
- Installationsinstruktioner för våra utvecklingsresurser

- Bästa praxis för AI-agentutveckling
  
- Kodgenomgång för att skapa våra AI-agenter
  
Låt oss börja med att titta på verktygen vi kommer använda för att skapa våra AI-agenter.

## Verktyg och installationsinstruktioner

### Microsoft Foundry

För åtkomst till stora språkmodeller (LLMs) kommer vi att använda [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Det finns kostnader förenade med att använda Foundry, så var säker på att följa instruktionerna för kontoinställning om du inte redan har åtkomst.

### OpenAI-modeller

Agentkodexemplen i denna kurs är konfigurerade för att använda OpenAI-modeller via [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Använd denna guide för att lära dig hur man distribuerar en modell med Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Välj en GPT-5-serie modell (till exempel `gpt-5.1`) för denna kurs. Undvik pensionerade modeller såsom GPT-4o och GPT-4.1, som når slutet av sin livscykel 2026.

### Microsoft Agent Framework

Som nämnts tidigare kommer vi att använda [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) både för att skapa och orkestrera våra AI-agenter.

Du behöver **Python 3.12 eller senare**. För att installera Microsoft Agent Framework och andra nödvändiga paket, kör följande kommando i projektets rotkatalog:

```bash
pip install -r requirements.txt
```

### Autentisera med Azure

Agenterna autentiserar sig mot Microsoft Foundry med dina Azure CLI-referenser
(`AzureCliCredential`), så du måste logga in innan du kör något exempel:

```bash
az login
# Om du har fler än en prenumeration, välj den med ditt Foundry-projekt:
az account set --subscription "<your-subscription-id>"
```

Se till att ditt konto har rollen **Azure AI User** (eller motsvarande) på Foundry
projektet så att det kan anropa modell- och agent-API:erna.

### Konfigurera .env-variabler

För att köra kodexemplen i denna kurs behöver du skapa en `.env`-fil i projektets rotkatalog.

För att göra det enklare kan du kopiera den medföljande `.env.example`-filen:

```bash
cp .env.example .env
``` 

Fyll sedan i de två variabler som agenterna hämtar ( `FoundryChatClient` plockar upp dessa
automatiskt):

| Variabel | Vad det är | Var du hittar den |
|----------|------------|------------------|
| `FOUNDRY_PROJECT_ENDPOINT` | Ditt Foundry **projekt** endpoint, som slutar med `/api/projects/<project>` | Foundry-portalen → ditt projekt → **Översikt** → *Endpoints* |
| `FOUNDRY_MODEL` | Namnet på modellimplementeringen som dina agenter kör på (till exempel `gpt-5.1`) | Foundry-portalen → **Modeller + endpoints** |

### Skapa medarbetarens vektorlagring

Ett exempel – **Employee Search Agent** – söker i en medarbetarkatalog som lagras i en
Microsoft Foundry **vektorlagring**. Skapa den en gång och kopiera ID:t som den skriver ut till din `.env`
som `VECTOR_STORE_ID` (kör från projektets rotmapp så att den hämtar din `.env`):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### Kör ett exempel

Varje agent kör sitt eget lokala DevUI. Till exempel:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

Öppna sedan den utskrivna `http://localhost:<port>`-URL:en i din webbläsare för att chatta med agenten.

## Agenterna i denna lektion

Varje exempel är en fristående agent byggd med Microsoft Agent Framework. Tillsammans
implementerar de scenarierna du designade i [Lektion 1](../lesson-1-agent-design/README.md):

| Exempel | Lektion 1 scenario | Verktyg som används | Port |
|--------|-------------------|--------------------|------|
| `employee-search-agent.py` | Scenario 1 — Medarbetarsökning | Foundry-hostad **fil-sökning** över en vektorlagring | 8090 |
| `task-recommendation-agent.py` | Scenario 2 — Uppgiftsrekommendation | **GitHub MCP** server (hostad MCP-tool) | 8095 |
| `azure-learning-agent.py` | Scenario 3 — Kodassistent (forskning) | **Microsoft Learn MCP** server (hostad MCP-tool) | 8092 |
| `coding-agent.py` | Scenario 3 — Kodassistent (kod) | **Code Interpreter** | 8093 |
| `learning-recommendation-agent.py` | Stödjande agent | Learn MCP + resonemang | 8091 |
| `agent-orchestration.py` | Binder samman scenarierna | Multi-agent **överförings** orkestrering | 8094 |

> **Notera angående Task Recommendation Agent.** `task-recommendation-agent.py` behöver en
> `GITHUB_PERSONAL_ACCESS_TOKEN` i din `.env` (skapa en på
> <https://github.com/settings/personal-access-tokens/new>). Den läser en utvecklares senaste
> GitHub-aktivitet och rekommenderar 1–3 öppna ärenden som matchar — precis enligt Scenario 2 design.
> Detta är det enda exemplet som anropar GitHub; de andra behöver endast ditt Foundry-projekt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->