# Registo de alterações

Todas as alterações notáveis a **Construção de Agentes de IA desde o Zero até à Produção** estão documentadas aqui.

O formato baseia-se em [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Este curso é um currículo em constante evolução em vez de um pacote de software versionado, por isso as entradas são agrupadas
pela data em que um conjunto de alterações foi introduzido em vez de por um número de versão semântica.

## [Não lançado]

### Adicionado
- **Higiene do repositório para partilha pública** — reforçado o `.gitignore` com uma secção dedicada
  Python / notebooks / secrets / OS section (env-file variants, `.pytest_cache/`, `.mypy_cache/`,
  `.ruff_cache/`, `.ipynb_checkpoints/`, `*.egg-info/`), mantendo, ao mesmo tempo, todos os `*.env.example`
  rastreados. Adicionados este `CHANGELOG.md`, um `AGENTS.md` guia de contribuidores/agentes, e ficheiros de competências do
  curso.

### Alterado
- Preparado o repositório para partilha pública: removidos identificadores pessoais e de ambientes em produção
  (nomes de conta, projeto, grupo de recursos e identidades) dos documentos publicados, e moveu o
  relatório de modernização/análise de lacunas para fora do repositório (o seu resumo dirigido aos aprendentes vive neste
  registo de alterações).

## [Modernização Foundry 2026]

Uma actualização técnica, terminológica e curricular completa, alinhando o curso com a
**Microsoft Foundry 2026** plataforma. Consulte `MIGRATION-GUIDE.md` para os detalhes da migração ao nível do código.

### Adicionado
- **Lição 5 – Agentes Hospedados em Produção** (`lesson-5-hosted-agents-production/`): Agentes hospedados vs
  Hosts de Capacidade, possibilidade de usar Cosmos DB / Storage / AI Search próprios, persistência de memória e de threads,
  fluxos de aprovação MCP hospedados, e uma lista de verificação de governança.
- **Lição 6 – Caixa de Ferramentas Microsoft** (`lesson-6-toolbox/`): definir ferramentas uma vez e governá-las
  centralmente, além de um exemplo executável de consumo (`toolbox_agent.py`) que acede a uma caixa de ferramentas através de um
  único endpoint MCP.
- **Lição 7 – Multi-Agente & A2A** (`lesson-7-multi-agent-a2a/`): expor um agente através do aberto
  protocolo Agent-to-Agent (A2A) (`a2a_server.py`) e consumir um agente remoto como um par
  (`a2a_client.py`). Validado ao vivo de ponta a ponta.
- **Agente de Recomendação de Tarefas** (`lesson-2-agent-development/task-recommendation-agent.py`):
  implementa o Cenário 2 da Lição 1 usando o servidor MCP remoto do GitHub como uma ferramenta.
- **Script de configuração da loja vetorial** (`setup_vector_store.py`): cria e popula a loja vetorial
  da qual o agente de pesquisa de colaboradores depende (anteriormente referenciado mas ausente).
- **CI smoke + static gate** (`.github/workflows/smoke-test-hosted-agent.yml`): um job `static` executa
  `py_compile` e markdown-link-check em cada PR/push; um job `smoke` executa o AI Smoke Test
  action contra um agente hospedado implantado (OIDC, `workflow_dispatch`).
- **Pré-requisitos e orientação de configuração** adicionados a cada lição e ao README raiz
  (Python 3.12+, `az login`, orientações sobre modelos, custos & limpeza).
- **Novo documento principal**: `MIGRATION-GUIDE.md`.

### Alterado
- **Rebranding**: *Azure AI Foundry* → **Microsoft Foundry** ao longo do curso.
- **Migração do SDK** para a superfície actual do Microsoft Agent Framework — os exemplos agora usam
  `agent-framework` `1.2.0` com `FoundryChatClient` e a **Responses API**, substituindo o
  padrões anteriores `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient`.
- **Dependências fixadas**: `requirements.txt` agora fixa `agent-framework`, `agent-framework-foundry`
  e pacotes relacionados em vez de instalar pré-lançamentos não fixados, tornando os exemplos reprodutíveis.
- **Variáveis de ambiente** alinhadas entre `deploy.py`, `agent.yaml`, `main.py` e os
  ficheiros `.env.example`.
- Diagramas de arquitectura do README e o catálogo de agentes/cenários reescritos para corresponder ao código entregue.

### Corrigido
- Corrigido o link quebrado no README raiz para a Lição 4 (`lesson-4-agentdeployment`).
- Elaborado o README anteriormente vazio da Lição 3 (avaliações + observabilidade).
- Substituído o padrão obsoleto `asyncio.get_event_loop().run_until_complete` no
  agente de recomendação de aprendizagem.

### Obsoleto / Removido
- Removido todo o uso dos modelos descontinuados **GPT-4o / GPT-4.1**. Exemplos de chat e avaliação agora usam
  **gpt-5.1**; exemplos de codificação usam **gpt-5-codex**.
- Documentado que **GitHub Models** está a ser descontinuado (30 de julho de 2026); o curso serve todos os modelos
  através do Microsoft Foundry e não depende do GitHub Models.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->