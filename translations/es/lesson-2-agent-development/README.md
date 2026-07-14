# Lección 2 Desarrollo de Agentes

¡Bienvenido a la segunda lección del curso "Construyendo Agentes de IA desde Cero hasta Producción"!

En esta lección cubriremos:

- Las Herramientas para Crear nuestros Agentes de IA
  
- Instrucciones de Configuración para nuestros Recursos de Desarrollo

- Buenas Prácticas para el Desarrollo de Agentes de IA
  
- Revisión de Código para Crear nuestros Agentes de IA
  
Comencemos mirando las herramientas que usaremos para crear nuestros Agentes de IA.

## Herramientas e Instrucciones de Configuración

### Microsoft Foundry

Para acceder a Modelos de Lenguaje Grande (LLMs) usaremos [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Hay costos asociados con el uso de Foundry, así que asegúrate de seguir las instrucciones para configurar la cuenta si aún no tienes acceso.

### Modelos OpenAI

Las muestras de código de agentes en este curso están configuradas para usar modelos OpenAI a través de [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Usa esta guía para aprender cómo desplegar un modelo usando Foundry: [Desplegar modelos de Microsoft Foundry en el portal de Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Elige un modelo de la serie GPT-5 (por ejemplo `gpt-5.1`) para este curso. Evita modelos retirados como GPT-4o y GPT-4.1, que llegarán al fin de su vida útil en 2026.

### Microsoft Agent Framework

Como se mencionó antes, usaremos el [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) para crear y orquestar nuestros Agentes de IA.

Necesitarás **Python 3.12 o superior**. Para instalar el Microsoft Agent Framework y otros paquetes requeridos, ejecuta el siguiente comando estando en el directorio raíz de este proyecto:

```bash
pip install -r requirements.txt
```

### Autenticarse con Azure

Los agentes se autentican con Microsoft Foundry usando tus credenciales de Azure CLI
(`AzureCliCredential`), así que debes iniciar sesión antes de ejecutar cualquier muestra:

```bash
az login
# Si tiene más de una suscripción, seleccione la que contiene su proyecto Foundry:
az account set --subscription "<your-subscription-id>"
```

Asegúrate de que tu cuenta tenga el rol de **Azure AI User** (o equivalente) en el proyecto Foundry
para que pueda llamar a las APIs de modelo y agentes.

### Configurar Variables .env

Para ejecutar las muestras de código en este curso, necesitarás crear un archivo `.env` en el directorio raíz de este proyecto.

Para facilitarlo, puedes copiar el archivo `.env.example` proporcionado:

```bash
cp .env.example .env
``` 

Luego completa las dos variables que leen los agentes (el `FoundryChatClient` las toma
automáticamente):

| Variable | Qué es | Dónde encontrarla |
|----------|------------|------------------|
| `FOUNDRY_PROJECT_ENDPOINT` | El endpoint de tu **proyecto** Foundry, terminando en `/api/projects/<project>` | Portal Foundry → tu proyecto → **Overview** → *Endpoints* |
| `FOUNDRY_MODEL` | El nombre del despliegue del modelo en el que se ejecutan tus agentes (por ejemplo `gpt-5.1`) | Portal Foundry → **Models + endpoints** |

### Crear la tienda vectorial de empleados

Una muestra — el **Agente de Búsqueda de Empleados** — busca en un directorio de empleados almacenado en una
**tienda vectorial** de Microsoft Foundry. Créala una vez y copia la ID que imprime en tu `.env`
como `VECTOR_STORE_ID` (ejecuta desde la raíz del repositorio para que detecte tu `.env`):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### Ejecutar una muestra

Cada agente corre su propia DevUI local. Por ejemplo:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

Luego abre la URL impresa `http://localhost:<port>` en tu navegador para chatear con el agente.

## Los agentes en esta lección

Cada muestra es un agente independiente construido con Microsoft Agent Framework. Juntos
implementan los escenarios que diseñaste en la [Lección 1](../lesson-1-agent-design/README.md):

| Muestra | Escenario de la Lección 1 | Herramienta usada | Puerto |
|--------|-------------------|-----------|------|
| `employee-search-agent.py` | Escenario 1 — Búsqueda de Empleados | Búsqueda **file search** alojada en Foundry sobre una tienda vectorial | 8090 |
| `task-recommendation-agent.py` | Escenario 2 — Recomendación de Tareas | Servidor **GitHub MCP** (herramienta MCP alojada) | 8095 |
| `azure-learning-agent.py` | Escenario 3 — Asistente de Código (investigación) | Servidor **Microsoft Learn MCP** (herramienta MCP alojada) | 8092 |
| `coding-agent.py` | Escenario 3 — Asistente de Código (código) | **Code Interpreter** | 8093 |
| `learning-recommendation-agent.py` | Agente de soporte | Learn MCP + razonamiento | 8091 |
| `agent-orchestration.py` | Une los escenarios | Orquestación de **handoff** multiagente | 8094 |

> **Nota sobre el Agente de Recomendación de Tareas.** `task-recommendation-agent.py` necesita un
> `GITHUB_PERSONAL_ACCESS_TOKEN` en tu `.env` (crea uno en
> <https://github.com/settings/personal-access-tokens/new>). Lee la actividad reciente
> de GitHub de un desarrollador y recomienda de 1 a 3 issues abiertos que coincidan — exactamente el diseño del Escenario 2.
> Esta es la única muestra que llama a GitHub; las otras solo necesitan tu proyecto Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->