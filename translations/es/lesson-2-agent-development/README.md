# Lección 2 Desarrollo de Agentes

¡Bienvenido a la segunda lección del curso "Construyendo un Agente de IA desde Cero hasta Producción"!

En esta lección cubriremos:

- Las herramientas para crear nuestros agentes de IA
  
- Instrucciones de configuración para nuestros recursos de desarrollo

- Mejores prácticas para el desarrollo de agentes de IA
  
- Recorrido de código para crear nuestros agentes de IA
  
Comencemos viendo las herramientas que usaremos para crear nuestros agentes de IA.

## Herramientas e instrucciones de configuración

### Microsoft Foundry

Para acceder a Modelos de Lenguaje Grande (LLMs) usaremos [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Hay costos asociados con el uso de Foundry, así que por favor asegúrate de seguir las instrucciones para la configuración de la cuenta si aún no tienes acceso.

### Modelos de OpenAI

Los ejemplos de código de agentes en este curso están configurados para usar modelos de OpenAI a través de [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Usa esta guía para aprender cómo desplegar un modelo usando Foundry: [Implementar modelos de Microsoft Foundry en el portal Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Elige un modelo GPT-4.1 o posterior para este curso.

### Microsoft Agent Framework

Como se mencionó antes, usaremos el [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) para crear y orquestar nuestros agentes de IA.

Para instalar Microsoft Agent Framework y otros paquetes requeridos, ejecuta el siguiente comando mientras estés en el directorio raíz de este proyecto:

```bash
pip install -r requirements.txt
```

### Configurar variables .env

Para ejecutar los ejemplos de código en este curso, necesitarás crear un archivo `.env` en el directorio raíz de este proyecto.

Para facilitarlo, puedes copiar el archivo `.env.example` proporcionado:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos responsabilizamos por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->