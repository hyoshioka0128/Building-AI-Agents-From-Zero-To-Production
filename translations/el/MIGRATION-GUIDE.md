# Οδηγός Μετάβασης — Microsoft Foundry Agent Framework (Ιούλιος 2026)

Αυτός ο οδηγός αντιστοιχίζει την επιφάνεια SDK με την οποία γράφτηκαν αρχικά τα δείγματα μαθήματος
στα **τρέχοντα, δημοσιευμένα** πακέτα Microsoft Agent Framework. Κάθε αντιστοίχιση και
υπογραφή παρακάτω επαληθεύτηκε μέσω της επιθεώρησης των εγκατεστημένων πακέτων
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Γιατί είναι σημαντικό:** με το rebrand σε **Microsoft Foundry**, η επιφάνεια του πελάτη μεταφέρθηκε
> από το `agent_framework.azure` (τις παλιές κλάσεις `AzureAI*`) σε **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Οι παλιές κορυφαίες κλάσεις εργαλείων που φιλοξενούνται
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) αφαιρέθηκαν· τα φιλοξενούμενα
> εργαλεία τώρα δημιουργούνται **από τον πελάτη** μέσω των μεθόδων κατασκευής `get_*_tool(...)`.

---

## 1. Εισαγωγή & αντιστοίχιση πελάτη

| Παλιό (δείγματα μαθήματος) | Νέο (Microsoft Foundry) |
|----------------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → επιστρέφει `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (MCP από πλευράς πελάτη) | αμετάβλητο — εξακολουθεί να είναι `from agent_framework import MCPStreamableHTTPTool` |

**Μετονομασία παραμέτρου διαπιστευτηρίων:** οι παλιοί πελάτες έπαιρναν `async_credential=...`·
ο `FoundryChatClient` παίρνει `credential=...`.

---

## 2. Επαληθευμένες υπογραφές

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # ή ορίστε το AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # ή ορίστε τη μεταβλητή περιβάλλοντος μοντέλου
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Εργαλειοθήκη Microsoft
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Παρατηρησιμότητα
```

---

## 3. Πριν / μετά — ένας μόνος πράκτορας με ένα φιλοξενούμενο εργαλείο MCP

**Πριν** (`azure-learning-agent.py`):

```python
from azure.identity.aio import AzureCliCredential
from agent_framework import HostedMCPTool
from agent_framework.azure import AzureAIClient

client = AzureAIClient(async_credential=AzureCliCredential())
agent = client.create_agent(
    name="LearningPathAgent",
    instructions=AGENT_INSTRUCTIONS,
    tools=HostedMCPTool(
        name="Microsoft Learn MCP",
        url="https://learn.microsoft.com/api/mcp",
        approval_mode="never_require",
    ),
)
```

**Μετά** (Microsoft Foundry):

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    name="LearningPathAgent",
    instructions=AGENT_INSTRUCTIONS,
    tools=client.get_mcp_tool(
        name="Microsoft Learn MCP",
        url="https://learn.microsoft.com/api/mcp",
        approval_mode="never_require",
    ),
)
```

---

## 4. Πριν / μετά — φιλοξενούμενη αναζήτηση αρχείων (αποθηκευτικό χώρο διανυσμάτων)

**Πριν** (`employee-search-agent.py`):

```python
from agent_framework import ChatAgent, HostedFileSearchTool, HostedVectorStoreContent
from agent_framework.azure import AzureAIAgentClient

file_search_tool = HostedFileSearchTool(
    inputs=[HostedVectorStoreContent(vector_store_id=os.environ["VECTOR_STORE_ID"])]
)
agent = ChatAgent(
    chat_client=AzureAIAgentClient(async_credential=AzureCliCredential()),
    instructions="...",
    tools=[file_search_tool],
)
```

**Μετά**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Απαρχαιωμένο ασύγχρονο μοτίβο

**Πριν** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

Το `asyncio.get_event_loop()` είναι απαρχαιωμένο. Προτιμήστε το φιλοξενούμενο `client.get_mcp_tool(...)`
(χωρίς χειροκίνητη σύνδεση), ή αν πρέπει να χρησιμοποιήσετε το `MCPStreamableHTTPTool` από την πλευρά του πελάτη,
το τυλίγετε μέσα σε `asyncio.run(...)` ή σε πλαίσιο `async with`.

---

## 6. Προχωρημένες επιφάνειες που χρησιμοποιεί τώρα αυτό το μάθημα

| Δυνατότητα | Εισαγωγή |
|-----------|---------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observability / αξιολόγηση** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Περιβάλλον εκτέλεσης φιλοξενούμενου πράκτορα** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Σημείωση.** Αυτά τα αποσπάσματα είναι επαληθευμένα ως προς την εισαγωγή και την υπογραφή έναντι των τρεχόντων πακέτων.
> Η ολοκληρωμένη εκτέλεση απαιτεί επίσης ένα έργο Microsoft Foundry, ένα αναπτυγμένο μοντέλο συνομιλίας,
> και (για αναζήτηση αρχείων) έναν πληρωμένο αποθηκευτικό χώρο διανυσμάτων.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->