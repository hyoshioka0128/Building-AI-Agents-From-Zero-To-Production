# Guía de migración — Microsoft Foundry Agent Framework (julio 2026)

Esta guía mapea la superficie del SDK contra la cual se escribieron originalmente los ejemplos del curso
sobre los paquetes actuales y publicados de Microsoft Agent Framework. Cada mapeo y
firma a continuación fue verificada inspeccionando los paquetes instalados
(`agent-framework 1.2.0`, `agent-framework-foundry 1.2.0`).

> **Por qué importa:** con el cambio de marca a **Microsoft Foundry**, la superficie cliente se movió
> de `agent_framework.azure` (las antiguas clases `AzureAI*`) a **`agent_framework.foundry`**
> (`FoundryChatClient`, `FoundryAgent`). Las antiguas clases de herramientas alojadas de nivel superior
> (`HostedMCPTool`, `HostedFileSearchTool`, `HostedVectorStoreContent`) fueron eliminadas; las herramientas alojadas
> ahora se crean **desde el cliente** mediante métodos fábrica `get_*_tool(...)`.

---

## 1. Importación y mapeo del cliente

| Antiguo (ejemplos del curso) | Nuevo (Microsoft Foundry) |
|------------------------------|------------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → devuelve `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool` (MCP del lado cliente) | sin cambios — sigue siendo `from agent_framework import MCPStreamableHTTPTool` |

**Parámetro credential renombrado:** los clientes antiguos usaban `async_credential=...`;
`FoundryChatClient` usa `credential=...`.

---

## 2. Firmas verificadas

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # o establezca AZURE_AI_PROJECT_ENDPOINT
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # o establezca la variable de entorno del modelo
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # Caja de herramientas de Microsoft
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # Observabilidad
```

---

## 3. Antes / después — un solo agente con una herramienta MCP alojada

**Antes** (`azure-learning-agent.py`):

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

**Después** (Microsoft Foundry):

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

## 4. Antes / después — búsqueda de archivos alojada (almacén vectorial)

**Antes** (`employee-search-agent.py`):

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

**Después**:

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. Patrón async desaprobado

**Antes** (`learning-recommendation-agent.py`):

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` está desaprobado. Prefiera la herramienta alojada `client.get_mcp_tool(...)`
(sin conectarse manualmente), o si debe usar la `MCPStreamableHTTPTool` del lado cliente, envuélvala
en `asyncio.run(...)` o en un contexto `async with`.

---

## 6. Superficies avanzadas que este curso usa ahora

| Capacidad | Importación |
|-----------|-------------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`, `from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observabilidad / evaluación** | `client.configure_azure_monitor()`, `from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a` (`import agent_framework.a2a`) |
| **Entorno de ejecución de agentes alojados** | `agent-framework-foundry-hosting`, `azure.ai.agentserver` |

> **Nota.** Estos fragmentos están verificados en importaciones y firmas contra los paquetes actuales.
> La ejecución de extremo a extremo también requiere un proyecto Microsoft Foundry, un modelo de chat desplegado,
> y (para búsqueda de archivos) un almacén vectorial poblado.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->