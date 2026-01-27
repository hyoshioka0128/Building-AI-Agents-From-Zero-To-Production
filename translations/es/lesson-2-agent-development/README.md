<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:02:49+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "es"
}
-->
# Lección 2 Desarrollo de Agentes

¡Bienvenido a la segunda lección del curso "Construyendo un Agente de IA desde Cero hasta Producción"!

En esta lección cubriremos:

- Las Herramientas para Crear nuestros Agentes de IA
  
- Instrucciones de Configuración para nuestros Recursos de Desarrollo

- Mejores Prácticas para el Desarrollo de Agentes de IA
  
- Recorrido de Código para Crear nuestros Agentes de IA
  
Comencemos viendo las herramientas que usaremos para crear nuestros Agentes de IA.

## Herramientas e Instrucciones de Configuración

### Microsoft Foundry

Para el acceso a Modelos de Lenguaje Grande (LLMs) usaremos [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Hay costos asociados con el uso de Foundry, así que asegúrate de seguir las instrucciones para la configuración de la cuenta si aún no tienes acceso.

### Modelos OpenAI

Los ejemplos de código de agentes en este curso están configurados para usar modelos OpenAI a través de [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Usa esta guía para aprender cómo desplegar un modelo usando Foundry: [Desplegar Modelos Microsoft Foundry en el portal Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Elige un modelo GPT-4.1 o posterior para este curso.

### Microsoft Agent Framework

Como se mencionó anteriormente, usaremos el [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) tanto para crear como para orquestar nuestros Agentes de IA.

Para instalar el Microsoft Agent Framework y otros paquetes requeridos, ejecuta el siguiente comando estando en el directorio raíz de este proyecto:

```bash
pip install -r requirements.txt
```

### Configurar Variables .env

Para ejecutar los ejemplos de código en este curso, necesitarás crear un archivo `.env` en el directorio raíz de este proyecto.

Para facilitarlo, puedes copiar el archivo `.env.example` proporcionado:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos responsabilizamos por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->