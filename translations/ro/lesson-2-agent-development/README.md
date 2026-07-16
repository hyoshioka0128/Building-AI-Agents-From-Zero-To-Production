# Lecția 2 Dezvoltarea Agenților  

Bine ați venit la a doua lecție din cursul "Construirea unui Agent AI de la Zero la Producție"!  

În această lecție vom acoperi:  

- Uneltele pentru Crearea Agenților AI  
  
- Instrucțiuni de Configurare pentru Resursele noastre de Dezvoltare  

- Cele mai bune Practici în Dezvoltarea Agenților AI  
  
- Parcurgerea Codului pentru Crearea Agenților AI  
  
Să începem prin a analiza uneltele pe care le vom folosi pentru a crea agenții AI.  

## Unelte și Instrucțiuni de Configurare  

### Microsoft Foundry  

Pentru acces la Modele Mari de Limbaj (LLM) vom utiliza [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Există costuri asociate utilizării Foundry, așa că vă rugăm să urmați instrucțiunile de configurare a contului dacă nu aveți deja acces.  

### Modele OpenAI  

Exemplele de cod pentru agenți din acest curs sunt configurate să folosească modelele OpenAI prin [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).  

Folosiți acest ghid pentru a învăța cum să implementați un model folosind Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)  

Alegeți un model din seria GPT-5 (de exemplu `gpt-5.1`) pentru acest curs. Evitați modelele retrase precum GPT-4o și GPT-4.1, care vor atinge sfârșitul suportului în 2026.  

### Microsoft Agent Framework  

Așa cum s-a menționat anterior, vom folosi [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) atât pentru a crea, cât și pentru a orchestra agenții noștri AI.  

Veți avea nevoie de **Python 3.12 sau o versiune ulterioară**. Pentru a instala Microsoft Agent Framework și alte pachete necesare, executați următoarea comandă din directorul rădăcină al acestui proiect:  

```bash
pip install -r requirements.txt
```
  
### Autentificarea cu Azure  

Agenții se autentifică la Microsoft Foundry folosind acreditările Azure CLI  
(`AzureCliCredential`), deci trebuie să vă autentificați înainte de a rula orice exemplu:  

```bash
az login
# Dacă aveți mai multe abonamente, selectați-l pe cel care corespunde proiectului dumneavoastră Foundry:
az account set --subscription "<your-subscription-id>"
```
  
Asigurați-vă că contul dvs. are rolul **Azure AI User** (sau echivalent) în proiectul Foundry  
pentru a putea apela API-urile modelului și agenților.  

### Configurați variabilele .env  

Pentru a rula exemplele de cod din acest curs, va trebui să creați un fișier `.env` în directorul rădăcină al acestui proiect.  

Pentru a fi mai ușor, puteți copia fișierul `.env.example` oferit:  

```bash
cp .env.example .env
``` 
  
Apoi completați cele două variabile pe care agenții le citesc (clientul `FoundryChatClient` le preia  
automat):  

| Variabilă | Ce este | Unde să o găsiți |  
|----------|------------|------------------|  
| `FOUNDRY_PROJECT_ENDPOINT` | Punctul final al proiectului Foundry, care se termină cu `/api/projects/<project>` | Portal Foundry → proiectul dvs → **Prezentare generală** → *Endpoints* |  
| `FOUNDRY_MODEL` | Numele implementării modelului pe care rulează agenții (de exemplu `gpt-5.1`) | Portal Foundry → **Modele + Endpoints** |  

### Creați magazinul vectorial pentru angajați  

Un exemplu — **Agentul de Căutare a Angajaților** — caută într-un director de angajați găzduit într-un  
magazin vectorial Microsoft Foundry. Creați-l o singură dată și copiați ID-ul pe care îl afișează în `.env`  
ca `VECTOR_STORE_ID` (rulați din rădăcina depozitului pentru a prelua `.env`):  

```bash
python lesson-2-agent-development/setup_vector_store.py
```
  
### Rulați un exemplu  

Fiecare agent rulează propria interfață locală DevUI. De exemplu:  

```bash
python lesson-2-agent-development/employee-search-agent.py
```
  
Apoi deschideți URL-ul afișat `http://localhost:<port>` în browser pentru a conversa cu agentul.  

## Agenții din această lecție  

Fiecare exemplu este un agent independent construit cu Microsoft Agent Framework. Împreună  
implementează scenariile pe care le-ați proiectat în [Lecția 1](../lesson-1-agent-design/README.md):  

| Exemplu | Scenariul Lecția 1 | Unealtă folosită | Port |  
|--------|-------------------|-----------|------|  
| `employee-search-agent.py` | Scenariu 1 — Căutare Angajați | Căutare de fișiere găzduită pe Foundry peste un magazin vectorial | 8090 |  
| `task-recommendation-agent.py` | Scenariul 2 — Recomandare de Sarcini | Server **GitHub MCP** (unealtă MCP găzduită) | 8095 |  
| `azure-learning-agent.py` | Scenariul 3 — Asistent de Cod (cercetare) | Server **Microsoft Learn MCP** (unealtă MCP găzduită) | 8092 |  
| `coding-agent.py` | Scenariul 3 — Asistent de Cod (cod) | **Interpreter de Cod** | 8093 |  
| `learning-recommendation-agent.py` | Agent suport | Learn MCP + raționament | 8091 |  
| `agent-orchestration.py` | Leagă scenariile împreună | Orchestrare multi-agent cu **handoff** | 8094 |  

> **Notă despre Agentul de Recomandare a Sarcinilor.** `task-recommendation-agent.py` are nevoie de un  
> `GITHUB_PERSONAL_ACCESS_TOKEN` în `.env` (creați unul la  
> <https://github.com/settings/personal-access-tokens/new>). Citește activitatea recentă a dezvoltatorului pe GitHub  
> și recomandă 1–3 probleme deschise care se potrivesc — exact designul Scenariului 2.  
> Acesta este singurul exemplu care apelează GitHub; celelalte au nevoie doar de proiectul Foundry.  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->