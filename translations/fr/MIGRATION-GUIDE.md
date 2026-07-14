# Guide de migration — Microsoft Foundry Agent Framework (Juillet 2026)

Ce guide fait correspondre la surface du SDK sur laquelle les exemples du cours ont été initialement écrits
avec les packages **actuels et publiés** du Microsoft Agent Framework. Chaque mappage et
signature ci-dessous a été vérifié en inspectant les packages installés
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Pourquoi c’est important :** avec le rebranding vers **Microsoft Foundry**, la surface client est passée
> de `agent_framework.azure` (les anciennes classes `AzureAI*`) à **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Les anciennes classes hébergées de niveau supérieur
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) ont été supprimées ; les outils hébergés
> sont désormais créés **depuis le client** via les méthodes fabriques `get_*_tool(...)`.

---

## 1. Importations & correspondance des clients

| Ancien (exemples du cours) | Nouveau (Microsoft Foundry) |
|---------------------------|------------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → retourne `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (MCP côté client) | inchangé — toujours `from agent_framework import MCPStreamableHTTPTool` |

**Paramètre de crédential renommé:** les anciens clients prenaient `async_credential=...` ;
`FoundryChatClient` prend `credential=...`.

---

## 2. Signatures vérifiées

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # ou définir AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # ou définir la variable d'environnement du modèle
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Boîte à outils Microsoft
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Observabilité
```

---

## 3. Avant / après — un agent unique avec un outil MCP hébergé

**Avant** (`azure-learning-agent.py`) :

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

**Après** (Microsoft Foundry) :

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

## 4. Avant / après — recherche de fichiers hébergée (magasin vectoriel)

**Avant** (`employee-search-agent.py`) :

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

**Après** :

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Pattern async déprécié

**Avant** (`learning-recommendation-agent.py`) :

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` est déprécié. Préférez l’outil hébergé `client.get_mcp_tool(...)`
(pas de connexion manuelle), ou si vous devez utiliser le `MCPStreamableHTTPTool` côté client,
encapsulez-le dans `asyncio.run(...)` ou dans un contexte `async with`.

---

## 6. Surfaces avancées désormais utilisées dans ce cours

| Fonctionnalité | Importation |
|--------------|------------|
| **Boîte à outils Microsoft** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Mémoire Foundry** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observabilité / évaluation** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Runtime agent hébergé** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Note.** Ces extraits ont été vérifiés côté importation et signature avec les packages actuels.
> L’exécution de bout en bout nécessite en plus un projet Microsoft Foundry, un modèle de chat déployé,
> et (pour la recherche de fichiers) un magasin vectoriel peuplé.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->