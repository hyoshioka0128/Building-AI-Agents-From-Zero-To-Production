# AGENTS.md

Guía para agentes de codificación de IA (y contribuyentes humanos) que trabajan en este repositorio. Si eres un
agente automatizado haciendo cambios aquí, lee este archivo primero y síguelo.

## Qué es este repositorio

**Construyendo Agentes de IA desde Cero hasta Producción** es un curso de aprendizaje de Microsoft. Enseña a los desarrolladores
a diseñar, construir, evaluar, desplegar y operar agentes de IA en **Microsoft Foundry** usando el
**Microsoft Agent Framework (MAF)**. El contenido está organizado en una secuencia de lecciones, cada una con un
`README.md` y ejemplos en Python ejecutables.

```
lesson-1-agent-design/            Use case + how to design effective agents
lesson-2-agent-development/       Build specialised agents with MAF (multiple runnable samples)
lesson-3-agent-evals/             Evaluations and observability
lesson-4-agentdeployment/         Deploy a hosted agent + OpenAI ChatKit front end
lesson-5-hosted-agents-production/ Hosted Agents vs Capability Hosts, BYO storage, governance
lesson-6-toolbox/                 Microsoft Toolbox: define + govern tools centrally
lesson-7-multi-agent-a2a/         Multi-agent orchestration over the A2A protocol
```

Documentos principales: `README.md` (empieza aquí), `MIGRATION-GUIDE.md` (detalle de migración del SDK), `CHANGELOG.md`.

## Reglas de oro

1. **Nunca comites secretos.** Solo se rastrean archivos `*.env.example`; los archivos `.env` reales están
   ignorados por git. No codifiques de forma fija endpoints, claves, tokens ni cadenas de conexión en ejemplos o documentos.
2. **No toques `translations/` ni `translated_images/`.** Estos se generan automáticamente mediante una
   acción de traducción en GitHub. Nunca los edites manualmente; haz cambios en los archivos fuente sólo a nivel de lección
   superior.
3. **No usar modelos obsoletos.** Usa **`gpt-5.1`** para chat/evaluación y **`gpt-5-codex`** para codificación.
   No introduzcas `gpt-4o`, `gpt-4.1` ni ningún modelo retirado, y no uses *Modelos de GitHub*
   (descontinuados el 30 de julio de 2026): todos los modelos se sirven a través de Microsoft Foundry.
4. **Usa la superficie actual del SDK.** Los ejemplos usan `agent-framework` (fijado en `requirements.txt`)
   con `FoundryChatClient` y la **API de Responses**. No reintroduzcas los patrones antiguos
   `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient`.
5. **Mantén la terminología actualizada**: *Microsoft Foundry* (no "Azure AI Foundry"), *Microsoft Agent
   Framework*, *Hosted Agents*, *Capability Hosts*, *Microsoft Toolbox*, *MCP / Hosted MCP*, *A2A*.

## Configuración

```bash
python -m venv .venv
# Windows:  .venv\Scripts\Activate.ps1
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt

az login                     # las muestras se autentican con tu identidad de desarrollador
cp .env.example .env         # luego completa el endpoint de tu proyecto Foundry + modelo
```

Requisitos: **Python 3.12+**, el **Azure CLI** y acceso a un proyecto de **Microsoft Foundry**
con un modelo desplegado de la serie GPT-5. Cada README de lección enumera sus propios prerrequisitos y las variables de entorno
que necesita (ver el `.env.example` a nivel de lección donde esté presente).

## Ejecución de ejemplos

La mayoría de los ejemplos de lección 2 lanzan una **DevUI** local en un puerto dedicado (por ejemplo 8090–8096); el servidor A2A
en la lección 7 escucha en el puerto 9000. Revisa la cadena de documentación/README de cada ejemplo para el comando
y puerto exactos. Como los ejemplos llaman endpoints vivos de Foundry, necesitan un `.env` válido y `az login`.

## Validación de cambios

No hay un conjunto de pruebas unitarias; la validación es estática + en vivo:

- **Filtro estático (debe pasar antes de hacer commit):** compilar en bytes cada ejemplo.
  ```bash
  python -m py_compile $(git ls-files '*.py')
  ```
  En PowerShell de Windows:
  ```powershell
  git ls-files '*.py' | ForEach-Object { python -m py_compile $_ }
  ```
- **Enlaces Markdown:** el trabajo CI `static` ejecuta `markdown-link-check`
  (configuración: `.github/workflows/markdown-link-check-config.json`). Verifica que cualquier enlace externo nuevo
  resuelva (HTTP 200).
- **Prueba de humo:** `.github/workflows/smoke-test-hosted-agent.yml` ejecuta la acción de Prueba de Humo de IA
  contra un agente alojado desplegado (`workflow_dispatch`, OIDC). Las ejecuciones en agente vivo requieren acceso a Azure.

CI (trabajo `static`) descubre automáticamente archivos `.py`, por lo que los nuevos ejemplos están cubiertos sin editar el
workflow. No cometas código que falle en `py_compile`.

## Convenciones para commits

- Escribe commits enfocados con mensajes claros e imperativos.
- Incluye el remolque de coautoría en commits asistidos por agentes:
  ```
  Co-authored-by: Copilot App <223556219+Copilot@users.noreply.github.com>
  ```
- No cometas caches generados, entornos virtuales ni archivos `.env` (todos ignorados por git).

## Dónde hacer cambios específicos

| Cambio | Ubicación |
|--------|----------|
| Narrativa del curso / texto de la lección | `lesson-*/README.md` (solo fuente — nunca `translations/`) |
| Código ejecutable | `lesson-*/**.py`, `setup_vector_store.py` |
| Dependencias | `requirements.txt` (mantén versiones fijadas) |
| Documentación de variables de entorno | `.env.example`, `.env.example` a nivel de lección |
| CI / filtro estático | `.github/workflows/` |
| Habilidades del curso para asistentes de IA | `.github/skills/` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->