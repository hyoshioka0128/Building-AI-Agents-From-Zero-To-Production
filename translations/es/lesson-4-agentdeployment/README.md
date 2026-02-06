# Lección 4: Despliegue de Agentes con Azure AI Foundry Hosted Agents + ChatKit

Esta lección muestra cómo desplegar un flujo de trabajo multiagente en Azure AI Foundry como un agente alojado y crear una interfaz basada en ChatKit para interactuar con él.

## Arquitectura

```
┌─────────────────────────────────────────────────────────────────────┐
│                         User's Browser                               │
│                    (ChatKit React Frontend)                          │
│                      localhost:3000                                  │
└───────────────────────────┬─────────────────────────────────────────┘
                            │ HTTP/SSE
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     ChatKit Backend Server                           │
│                    (FastAPI + SQLite Store)                          │
│                      localhost:8001                                  │
└───────────────────────────┬─────────────────────────────────────────┘
                            │ Azure AI Responses API
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    Azure AI Foundry                                  │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │               Hosted Multi-Agent Workflow                      │  │
│  │  ┌─────────────┐  ┌──────────────────┐  ┌───────────────┐     │  │
│  │  │   Triage    │──│ Employee Search  │  │   Learning    │     │  │
│  │  │   Agent     │  │     Agent        │  │    Agent      │     │  │
│  │  │(Coordinator)│  │ (Vector Store)   │  │ (MCP Tool)    │     │  │
│  │  └──────┬──────┘  └──────────────────┘  └───────────────┘     │  │
│  │         │         ┌──────────────────┐                         │  │
│  │         └─────────│  Coding Agent    │                         │  │
│  │                   │ (Code Generation)│                         │  │
│  │                   └──────────────────┘                         │  │
│  └───────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

## Requisitos Previos

1. **Proyecto Azure AI Foundry** en la región North Central US
2. **Azure CLI** autenticado (`az login`)
3. **Azure Developer CLI** (`azd`) instalado
4. **Python 3.12+** y **Node.js 18+**
5. **Vector Store** creado con datos de empleados

## Inicio Rápido

### 1. Configurar Variables de Entorno

```bash
cd lesson-4-agentdeployment
cp .env.example .env
# Edita .env con los detalles de tu proyecto Azure AI Foundry
```

### 2. Desplegar el Agente Alojado

**Opción A: Usando Azure Developer CLI (Recomendado)**

```bash
cd hosted-agent
azd auth login
azd agent deploy
```

**Opción B: Usando Docker + Azure Container Registry**

```bash
cd hosted-agent

# Construir el contenedor
docker build -t developer-onboarding-agent:latest .

# Etiqueta para ACR
docker tag developer-onboarding-agent:latest <your-acr>.azurecr.io/developer-onboarding-agent:latest

# Enviar a ACR
az acr login --name <your-acr>
docker push <your-acr>.azurecr.io/developer-onboarding-agent:latest

# Desplegar a través del portal de Azure AI Foundry o SDK
```

### 3. Iniciar el Backend de ChatKit

```bash
cd chatkit-server
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

El servidor se iniciará en `http://localhost:8001`

### 4. Iniciar el Frontend de ChatKit

```bash
cd chatkit-server/frontend
npm install
npm run dev
```

El frontend se iniciará en `http://localhost:3000`

### 5. Probar la Aplicación

Abra `http://localhost:3000` en su navegador y pruebe estas consultas:

**Búsqueda de Empleados:**
- "¡Soy nuevo aquí! ¿Alguien ha trabajado en Microsoft?"
- "¿Quién tiene experiencia con Azure Functions?"

**Recursos de Aprendizaje:**
- "Crear una ruta de aprendizaje para Kubernetes"
- "¿Qué certificaciones debo obtener para arquitectura en la nube?"

**Ayuda de Programación:**
- "Ayúdame a escribir código Python para conectarme a CosmosDB"
- "Muéstrame cómo crear una Azure Function"

**Consultas Multiagente:**
- "Estoy empezando como ingeniero en la nube. ¿Con quién debo conectarme y qué debo aprender?"

## Estructura del Proyecto

```
lesson-4-agentdeployment/
├── .env.example                 # Environment variables template
├── implementation-plan.md       # Detailed implementation guide
├── README.md                    # This file
├── hosted-agent/               # Azure AI Foundry hosted agent
│   ├── main.py                 # Multi-agent workflow implementation
│   ├── requirements.txt        # Python dependencies
│   ├── Dockerfile              # Container definition
│   └── agent.yaml              # Agent deployment configuration
└── chatkit-server/             # ChatKit server application
    ├── app.py                  # FastAPI backend
    ├── store.py                # SQLite persistence layer
    ├── requirements.txt        # Python dependencies
    └── frontend/               # React frontend
        ├── package.json
        ├── vite.config.ts
        ├── tsconfig.json
        ├── index.html
        └── src/
            ├── main.tsx
            ├── App.tsx
            ├── App.css
            └── index.css
```

## El Flujo de Trabajo Multiagente

El agente alojado usa **HandoffBuilder** para coordinar cuatro agentes especializados:

| Agente | Rol | Herramientas |
|--------|-----|--------------|
| **Agente de Clasificación** | Coordinador - dirige las consultas a especialistas | Ninguna |
| **Agente de Búsqueda de Empleados** | Encuentra colegas y miembros del equipo | HostedFileSearchTool (Vector Store) |
| **Agente de Aprendizaje** | Crea rutas de aprendizaje y recomendaciones | HostedMCPTool (Microsoft Learn) |
| **Agente de Programación** | Genera ejemplos de código y orientación | Ninguna |

El flujo permite:
- Clasificación → Cualquier especialista
- Especialistas → Otros especialistas (para consultas relacionadas)
- Especialistas → Clasificación (para nuevos temas)

## Solución de Problemas

### El agente no responde
- Verifique que el agente alojado esté desplegado y ejecutándose en Azure AI Foundry
- Compruebe que `HOSTED_AGENT_NAME` y `HOSTED_AGENT_VERSION` coincidan con su despliegue

### Errores en el Vector Store
- Asegúrese de que `VECTOR_STORE_ID` está configurado correctamente
- Verifique que el vector store contiene los datos de los empleados

### Errores de autenticación
- Ejecute `az login` para refrescar las credenciales
- Asegúrese de tener acceso al proyecto Azure AI Foundry

## Recursos

- [Documentación de Azure AI Foundry Hosted Agents](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/concepts/hosted-agents)
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)
- [Ejemplo de Integración ChatKit](https://github.com/microsoft/agent-framework/tree/main/python/samples/demos/chatkit-integration)
- [Azure Developer CLI](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables por malentendidos o interpretaciones erróneas derivados del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->