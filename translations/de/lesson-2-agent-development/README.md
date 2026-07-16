# Lektion 2 Agentenentwicklung

Willkommen zur zweiten Lektion des Kurses "AI-Agent von Grund auf bis zur Produktion entwickeln"!

In dieser Lektion behandeln wir:

- Die Werkzeuge zur Erstellung unserer KI-Agenten
  
- Einrichtungsanweisungen für unsere Entwicklungsressourcen

- Best Practices für die KI-Agentenentwicklung
  
- Code-Durchgang zur Erstellung unserer KI-Agenten
  
Beginnen wir mit einem Blick auf die Werkzeuge, die wir zur Erstellung unserer KI-Agenten verwenden werden.

## Werkzeuge und Einrichtungshinweise

### Microsoft Foundry

Für den Zugriff auf Large Language Models (LLMs) verwenden wir [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Die Nutzung von Foundry ist kostenpflichtig, daher stellen Sie bitte sicher, den Anweisungen zur Kontoeinrichtung zu folgen, falls Sie noch keinen Zugang haben.

### OpenAI-Modelle

Die Agenten-Codebeispiele in diesem Kurs sind so eingerichtet, dass sie OpenAI-Modelle über [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) verwenden.

Verwenden Sie diese Anleitung, um zu lernen, wie man ein Modell mit Foundry bereitstellt: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Wählen Sie für diesen Kurs ein Modell der GPT-5-Serie (z. B. `gpt-5.1`). Vermeiden Sie veraltete Modelle wie GPT-4o und GPT-4.1, die im Jahr 2026 eingestellt werden.

### Microsoft Agent Framework

Wie bereits erwähnt, verwenden wir das [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), um unsere KI-Agenten zu erstellen und zu orchestrieren.

Sie benötigen **Python 3.12 oder höher**. Um das Microsoft Agent Framework und andere erforderliche Pakete zu installieren, führen Sie im Stammverzeichnis dieses Projekts den folgenden Befehl aus:

```bash
pip install -r requirements.txt
```

### Authentifizierung mit Azure

Die Agenten authentifizieren sich bei Microsoft Foundry über Ihre Azure CLI-Anmeldedaten
(`AzureCliCredential`), daher müssen Sie sich vor dem Ausführen eines Beispiels anmelden:

```bash
az login
# Wenn Sie mehr als ein Abonnement haben, wählen Sie dasjenige mit Ihrem Foundry-Projekt aus:
az account set --subscription "<your-subscription-id>"
```

Stellen Sie sicher, dass Ihr Konto die Rolle **Azure AI User** (oder eine gleichwertige) im Foundry-Projekt besitzt,
damit es die Modell- und Agenten-APIs aufrufen kann.

### Einrichtung der .env-Variablen

Um die Codebeispiele in diesem Kurs auszuführen, müssen Sie im Stammverzeichnis dieses Projekts eine `.env`-Datei erstellen.

Zur Vereinfachung können Sie die bereitgestellte `.env.example`-Datei kopieren:

```bash
cp .env.example .env
``` 

Füllen Sie anschließend die beiden Variablen aus, die die Agenten auslesen (der `FoundryChatClient` übernimmt dies
automatisch):

| Variable | Was es ist | Wo zu finden |
|----------|------------|--------------|
| `FOUNDRY_PROJECT_ENDPOINT` | Der Endpunkt Ihres Foundry-**Projekts**, endet mit `/api/projects/<project>` | Foundry Portal → Ihr Projekt → **Übersicht** → *Endpunkte* |
| `FOUNDRY_MODEL` | Der Name der Modellbereitstellung, auf der Ihre Agenten laufen (z. B. `gpt-5.1`) | Foundry Portal → **Modelle + Endpunkte** |

### Erstellen des Mitarbeiter-Vektor-Stores

Ein Beispiel — der **Employee Search Agent** — durchsucht ein Mitarbeiterverzeichnis, das in einem
Microsoft Foundry **Vektor-Store** gespeichert ist. Erstellen Sie diesen einmal und kopieren Sie die ausgegebene ID in Ihre `.env`
als `VECTOR_STORE_ID` (führen Sie das Skript aus dem Repository-Stammverzeichnis aus, damit Ihre `.env` gelesen wird):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### Führen Sie ein Beispiel aus

Jeder Agent läuft mit einer eigenen lokalen DevUI. Zum Beispiel:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

Öffnen Sie danach die ausgegebene URL `http://localhost:<port>` in Ihrem Browser, um mit dem Agenten zu chatten.

## Die Agenten in dieser Lektion

Jedes Beispiel ist ein eigenständiger Agent, der mit dem Microsoft Agent Framework gebaut wurde. Zusammen
implementieren sie die in [Lektion 1](../lesson-1-agent-design/README.md) entworfenen Szenarien:

| Beispiel | Szenario aus Lektion 1 | Verwendetes Tool | Port |
|----------|---------------------|-----------------|------|
| `employee-search-agent.py` | Szenario 1 — Mitarbeitersuche | Foundry-gehostete **Dateisuche** über einen Vektor-Store | 8090 |
| `task-recommendation-agent.py` | Szenario 2 — Aufgabenempfehlung | **GitHub MCP** Server (gehostetes MCP-Tool) | 8095 |
| `azure-learning-agent.py` | Szenario 3 — Code-Assistent (Recherche) | **Microsoft Learn MCP** Server (gehostetes MCP-Tool) | 8092 |
| `coding-agent.py` | Szenario 3 — Code-Assistent (Code) | **Code Interpreter** | 8093 |
| `learning-recommendation-agent.py` | Unterstützender Agent | Learn MCP + Reasoning | 8091 |
| `agent-orchestration.py` | Verknüpft die Szenarien | Multi-Agent-**Übergabe**-Orchestrierung | 8094 |

> **Hinweis zum Task Recommendation Agent.** `task-recommendation-agent.py` benötigt einen
> `GITHUB_PERSONAL_ACCESS_TOKEN` in Ihrer `.env` (erstellen Sie einen unter
> <https://github.com/settings/personal-access-tokens/new>). Er liest die jüngsten
> GitHub-Aktivitäten eines Entwicklers aus und empfiehlt 1–3 offene Issues, die genau zum Szenario 2 passen.
> Dies ist das einzige Beispiel, das GitHub aufruft; die anderen benötigen nur Ihr Foundry-Projekt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->