# Lezione 2 Sviluppo Agenti

Benvenuto alla seconda lezione del corso "Costruire un Agente AI da Zero alla Produzione"!

In questa lezione copriremo:

- Gli Strumenti per Creare i nostri Agenti AI
  
- Istruzioni per la Configurazione delle nostre Risorse di Sviluppo

- Best Practice per lo Sviluppo di Agenti AI
  
- Analisi del Codice per la Creazione dei nostri Agenti AI
  
Iniziamo guardando gli strumenti che useremo per creare i nostri Agenti AI.

## Strumenti e Istruzioni per la Configurazione

### Microsoft Foundry

Per l’accesso a Large Language Models (LLM) useremo [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Ci sono costi associati all’uso di Foundry quindi assicurati di seguire le istruzioni per la configurazione dell’account se non hai già accesso.

### Modelli OpenAI

Gli esempi di codice degli agenti in questo corso sono configurati per usare modelli OpenAI tramite [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Usa questa guida per imparare come distribuire un modello usando Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Scegli un modello della serie GPT-5 (per esempio `gpt-5.1`) per questo corso. Evita modelli dismessi come GPT-4o e GPT-4.1, che raggiungono la fine del ciclo di vita nel 2026.

### Microsoft Agent Framework

Come menzionato prima, useremo il [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) sia per creare che per orchestrare i nostri Agenti AI.

Ti servirà **Python 3.12 o successivo**. Per installare il Microsoft Agent Framework e altri pacchetti necessari, esegui il seguente comando mentre sei nella directory radice di questo progetto:

```bash
pip install -r requirements.txt
```

### Autenticazione con Azure

Gli agenti si autenticano su Microsoft Foundry usando le tue credenziali Azure CLI
(`AzureCliCredential`), quindi devi effettuare il login prima di eseguire qualsiasi esempio:

```bash
az login
# Se hai più di un abbonamento, seleziona quello con il tuo progetto Foundry:
az account set --subscription "<your-subscription-id>"
```

Assicurati che il tuo account abbia il ruolo **Azure AI User** (o equivalente) sul progetto Foundry
così da poter chiamare le API di modello e agente.

### Configura le variabili .env

Per eseguire gli esempi di codice in questo corso, devi creare un file `.env` nella directory radice di questo progetto.

Per facilitare puoi copiare il file `.env.example` fornito:

```bash
cp .env.example .env
``` 

Poi completa le due variabili lette dagli agenti (il `FoundryChatClient` le rileva
automaticamente):

| Variabile | Cosa è | Dove trovarla |
|----------|------------|------------------|
| `FOUNDRY_PROJECT_ENDPOINT` | Endpoint del tuo **progetto** Foundry, che termina con `/api/projects/<project>` | Portale Foundry → il tuo progetto → **Overview** → *Endpoints* |
| `FOUNDRY_MODEL` | Nome della distribuzione del modello su cui girano gli agenti (per esempio `gpt-5.1`) | Portale Foundry → **Models + endpoints** |

### Crea il vettore store dipendenti

Un esempio — l’**Employee Search Agent** — cerca in una directory dipendenti contenuta in un
**vector store** Microsoft Foundry. Crealo una volta e copia l’ID che stampa nel tuo `.env`
come `VECTOR_STORE_ID` (esegui dalla radice del repository per fargli rilevare il `.env`):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### Esegui un esempio

Ogni agente esegue la propria DevUI locale. Per esempio:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

Poi apri l’URL stampato `http://localhost:<port>` nel tuo browser per chattare con l’agente.

## Gli agenti in questa lezione

Ogni esempio è un agente standalone costruito con il Microsoft Agent Framework. Insieme
implementano gli scenari che hai progettato in [Lezione 1](../lesson-1-agent-design/README.md):

| Esempio | Scenario Lezione 1 | Strumento usato | Porta |
|--------|-------------------|-----------|------|
| `employee-search-agent.py` | Scenario 1 — Ricerca Dipendenti | Ricerca **file** ospitata su Foundry tramite vector store | 8090 |
| `task-recommendation-agent.py` | Scenario 2 — Raccomandazione Task | Server **GitHub MCP** (strumento MCP ospitato) | 8095 |
| `azure-learning-agent.py` | Scenario 3 — Assistente Codice (ricerca) | Server **Microsoft Learn MCP** (strumento MCP ospitato) | 8092 |
| `coding-agent.py` | Scenario 3 — Assistente Codice (codifica) | **Code Interpreter** | 8093 |
| `learning-recommendation-agent.py` | Agente di supporto | Learn MCP + ragionamento | 8091 |
| `agent-orchestration.py` | Collega insieme gli scenari | Orchestrazione di **handoff** multi-agente | 8094 |

> **Nota sull’Agente di Raccomandazione Task.** `task-recommendation-agent.py` ha bisogno di un
> `GITHUB_PERSONAL_ACCESS_TOKEN` nel tuo `.env` (creane uno su
> <https://github.com/settings/personal-access-tokens/new>). Legge l’attività recente di un sviluppatore su
> GitHub e raccomanda 1–3 issue aperte che corrispondono — esattamente lo scenario 2 progettato.
> Questo è l’unico esempio che chiama GitHub; gli altri necessitano solo del tuo progetto Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->