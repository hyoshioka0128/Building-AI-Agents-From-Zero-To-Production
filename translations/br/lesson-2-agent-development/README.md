<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:14:06+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "br"
}
-->
# Lesson 2 Desenvolvimento de Agentes

Bem-vindo à segunda lição do curso "Construindo Agentes de IA do Zero à Produção"!

Nesta lição, abordaremos:

- As Ferramentas para Criar nossos Agentes de IA
  
- Instruções de Configuração para nossos Recursos de Desenvolvimento

- Melhores Práticas para Desenvolvimento de Agentes de IA
  
- Passo a passo do Código para Criar nossos Agentes de IA
  
Vamos começar olhando as ferramentas que usaremos para criar nossos Agentes de IA.

## Ferramentas e Instruções de Configuração

### Microsoft Foundry

Para acesso a Grandes Modelos de Linguagem (LLMs) usaremos o [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Existem custos associados ao uso do Foundry, então por favor, certifique-se de seguir as instruções para configuração da conta se você ainda não tiver acesso.

### Modelos OpenAI

Os exemplos de código de agentes neste curso estão configurados para usar modelos OpenAI por meio do [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Use este guia para aprender como implantar um modelo usando o Foundry: [Implantar Modelos Microsoft Foundry no portal Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Escolha um modelo GPT-4.1 ou posterior para este curso.

### Microsoft Agent Framework

Como mencionado anteriormente, usaremos o [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) para criar e orquestrar nossos Agentes de IA.

Para instalar o Microsoft Agent Framework e outros pacotes necessários, execute o seguinte comando estando no diretório raiz deste projeto:

```bash
pip install -r requirements.txt
```

### Configurar Variáveis .env

Para executar os exemplos de código deste curso, você precisará criar um arquivo `.env` no diretório raiz deste projeto.

Para facilitar, você pode copiar o arquivo `.env.example` fornecido:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->