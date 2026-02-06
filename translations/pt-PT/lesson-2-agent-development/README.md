# Lesson 2 Desenvolvimento de Agentes

Bem-vindo à segunda aula do "Curso Construindo Agentes de IA do Zero até à Produção"!

Nesta aula vamos cobrir:

- As Ferramentas para Criar os nossos Agentes de IA
  
- Instruções de Configuração para os nossos Recursos de Desenvolvimento

- Melhores Práticas no Desenvolvimento de Agentes de IA
  
- Revisão de Código para Criar os nossos Agentes de IA
  
Vamos começar por olhar para as ferramentas que iremos utilizar para criar os nossos Agentes de IA.

## Ferramentas e Instruções de Configuração

### Microsoft Foundry

Para acesso a Modelos de Linguagem Grande (LLMs) iremos usar o [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Existem custos associados ao uso do Foundry, por favor certifique-se de seguir as instruções para configuração da conta caso ainda não tenha acesso.

### Modelos OpenAI

Os exemplos de código para agentes neste curso estão configurados para usar modelos da OpenAI através do [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Use este guia para aprender como implementar um modelo usando o Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Escolha um modelo GPT-4.1 ou posterior para este curso.

### Microsoft Agent Framework

Como mencionado anteriormente, iremos usar o [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) tanto para criar como para orquestrar os nossos Agentes de IA.

Para instalar o Microsoft Agent Framework e outros pacotes necessários, execute o seguinte comando enquanto estiver no diretório raiz deste projeto:

```bash
pip install -r requirements.txt
```

### Configurar Variáveis .env

Para executar os exemplos de código deste curso, precisa de criar um ficheiro `.env` no diretório raiz deste projeto. 

Para facilitar, pode copiar o ficheiro `.env.example` fornecido:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->