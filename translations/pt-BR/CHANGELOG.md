# Registro de alterações

Todas as mudanças notáveis em **Construindo Agentes de IA do Zero para Produção** estão documentadas aqui.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Este curso é um currículo vivo, e não um pacote de software versionado, então as entradas são agrupadas
pela data em que um conjunto de alterações foi lançado, e não por um número de versão semântica.

## 13 de julho de 2026

### Adicionado
- **Higiene do repositório para compartilhamento público** — reforço no `.gitignore` com uma seção dedicada
  para Python / notebooks / segredos / SO (variantes de arquivo de ambiente, `.pytest_cache/`, `.mypy_cache/`,
  `.ruff_cache/`, `.ipynb_checkpoints/`, `*.egg-info/`), mantendo todos os arquivos `*.env.example`
  versionados. Adicionado este `CHANGELOG.md`, um guia de contribuidor/agente `AGENTS.md` e arquivos
  de habilidades do curso.

### Alterado
- Preparado o repositório para compartilhamento público: removidos identificadores pessoais e de ambiente ao vivo
  (conta, projeto, grupo de recursos e nomes de identidade) dos documentos publicados e movido o relatório interno
  de modernização/análise de lacunas para fora do repositório (sua síntese para o aluno está neste
  registro de alterações).

## [Modernização Foundry 2026]

Uma completa atualização técnica, terminológica e curricular alinhando o curso com a
**Microsoft Foundry 2026**. Veja `MIGRATION-GUIDE.md` para detalhes da migração a nível de código.

### Adicionado
- **Aula 5 – Agentes Hospedados em Produção** (`lesson-5-hosted-agents-production/`): Agentes Hospedados vs
  Hosts de Capacidades, traga seu próprio Cosmos DB / Storage / AI Search, persistência de memória e de threads,
  fluxos de aprovação MCP hospedados e uma checklist de governança.
- **Aula 6 – Caixa de Ferramentas Microsoft** (`lesson-6-toolbox/`): definir ferramentas uma vez e governá-las
  centralmente, além de um exemplo funcional de consumo (`toolbox_agent.py`) que acessa uma caixa de ferramentas
  por meio de um único endpoint MCP.
- **Aula 7 – Multi-Agente & A2A** (`lesson-7-multi-agent-a2a/`): expor um agente sobre o protocolo aberto
  Agente-para-Agente (A2A) (`a2a_server.py`) e consumir um agente remoto como par
  (`a2a_client.py`). Validado vivo de ponta a ponta.
- **Agente de Recomendação de Tarefas** (`lesson-2-agent-development/task-recommendation-agent.py`):
  implementa o Cenário 2 da Aula 1 usando o servidor MCP remoto do GitHub como ferramenta.
- **Script de configuração do vector-store** (`setup_vector_store.py`): cria e popula o vector store
  do qual o agente de busca de funcionários depende (anteriormente referenciado, mas ausente).
- **Teste rápido de CI + gate estático** (`.github/workflows/smoke-test-hosted-agent.yml`): um job `static` executa
  `py_compile` e verificação de links markdown em cada PR/push; um job `smoke` executa o AI Smoke Test
  action contra um agente hospedado implantado (OIDC, `workflow_dispatch`).
- **Orientação de pré-requisitos e configuração** adicionada a todas as aulas e ao README raiz
  (Python 3.12+, `az login`, orientação sobre modelos, custo e limpeza).
- **Novo documento principal**: `MIGRATION-GUIDE.md`.

### Alterado
- **Rebranding**: *Azure AI Foundry* → **Microsoft Foundry** em todo o curso.
- **Migração do SDK** para a superfície atual do Microsoft Agent Framework — amostras agora usam
  `agent-framework` `1.2.0` com `FoundryChatClient` e a **API de Respostas**, substituindo os
  padrões anteriores `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient`.
- **Dependências fixadas**: `requirements.txt` agora fixa `agent-framework`, `agent-framework-foundry`
  e pacotes relacionados ao invés de instalar pré-lançamentos não fixados, tornando as amostras reproduzíveis.
- **Variáveis de ambiente** alinhadas entre `deploy.py`, `agent.yaml`, `main.py` e os arquivos
  `.env.example`.
- Diagramas de arquitetura do README e catálogo de agentes/cenários reescritos para corresponder ao código entregue.

### Corrigido
- Corrigido o link quebrado do README raiz para a Aula 4 (`lesson-4-agentdeployment`).
- Elaborado o README anteriormente vazio da Aula 3 (avaliações + observabilidade).
- Substituído o padrão deprecated `asyncio.get_event_loop().run_until_complete` no agente de
  recomendação de aprendizado.

### Depreciado / Removido
- Removido todo uso dos modelos aposentados **GPT-4o / GPT-4.1**. Amostras de chat e avaliação agora usam
  **gpt-5.1**; amostras de codificação usam **gpt-5-codex**.
- Documentado que **GitHub Models** está sendo descontinuado (30 de julho de 2026); o curso atende todos os modelos
  através do Microsoft Foundry e não depende do GitHub Models.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->