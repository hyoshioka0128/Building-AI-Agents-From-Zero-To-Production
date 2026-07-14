# Registro de alterações

Todas as alterações notáveis de **Building AI Agents from Zero to Production** estão documentadas aqui.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Este curso é um currículo em evolução em vez de um pacote de software versionado, portanto as entradas são agrupadas
pela data em que um conjunto de alterações foi lançado em vez de por um número de versão semântica.

## [Não lançado]

### Adicionado
- **Higiene do repositório para compartilhamento público** — reforçado `.gitignore` com uma seção dedicada
  Python / notebooks / secrets / OS (variantes de env-file, `.pytest_cache/`, `.mypy_cache/`,
  `.ruff_cache/`, `.ipynb_checkpoints/`, `*.egg-info/`), mantendo todos os `*.env.example`
  rastreados. Adicionados este `CHANGELOG.md`, um guia de contribuidores/agentes `AGENTS.md`, e arquivos de habilidades do curso
  .

### Alterado
- Preparou o repositório para compartilhamento público: removeu identificadores pessoais e de ambiente ao vivo
  (nomes de conta, projeto, resource-group e identidade) dos documentos publicados, e moveu o
  relatório de modernização/análise de lacunas para fora do repositório (o resumo voltado para os alunos está neste
  registro de alterações).

## [2026 Foundry modernisation]

Uma atualização completa técnica, de terminologia e do currículo alinhando o curso à plataforma
**Microsoft Foundry 2026**. Consulte `MIGRATION-GUIDE.md` para os detalhes de migração em nível de código.

### Adicionado
- **Lição 5 – Agentes hospedados em produção** (`lesson-5-hosted-agents-production/`): Hosted Agents vs
  Capability Hosts, bring-your-own Cosmos DB / Storage / AI Search, persistência de memória e de threads,
  fluxos de aprovação do MCP hospedado e uma lista de verificação de governança.
- **Lição 6 – Caixa de ferramentas Microsoft** (`lesson-6-toolbox/`): definir ferramentas uma vez e governá-las
  centralmente, além de um exemplo executável de consumo (`toolbox_agent.py`) que acessa uma caixa de ferramentas através de um
  único endpoint MCP.
- **Lição 7 – Multi-Agente & A2A** (`lesson-7-multi-agent-a2a/`): expor um agente pelo protocolo aberto
  Agent-to-Agent (A2A) protocol (`a2a_server.py`) e consumir um agente remoto como um par
  (`a2a_client.py`). Validado ao vivo de ponta a ponta.
- **Agente de Recomendação de Tarefas** (`lesson-2-agent-development/task-recommendation-agent.py`):
  implementa o Cenário 2 da Lição 1 usando o servidor MCP remoto do GitHub como uma ferramenta.
- **Script de configuração do vector-store** (`setup_vector_store.py`): cria e popula o vector store
  da qual o agente de busca de funcionários depende (anteriormente referenciado, mas ausente).
- **CI smoke + static gate** (`.github/workflows/smoke-test-hosted-agent.yml`): um job `static` executa
  `py_compile` e markdown-link-check em cada PR/push; um job `smoke` executa o AI Smoke Test
  action contra um agente hospedado implantado (OIDC, `workflow_dispatch`).
- **Pré-requisitos e orientações de configuração** adicionados a cada lição e ao README raiz
  (Python 3.12+, `az login`, orientação sobre modelos, custo & limpeza).
- **Novo documento principal**: `MIGRATION-GUIDE.md`.

### Alterado
- **Rebranding**: *Azure AI Foundry* → **Microsoft Foundry** em todo o curso.
- **Migração do SDK** para a interface atual do Microsoft Agent Framework — os exemplos agora usam
  `agent-framework` `1.2.0` com `FoundryChatClient` e a **Responses API**, substituindo o
  padrão anterior `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient`.
- **Dependências fixadas**: `requirements.txt` agora fixa `agent-framework`, `agent-framework-foundry`
  e pacotes relacionados em vez de instalar pré-lançamentos sem versão fixa, tornando os exemplos reprodutíveis.
- **Variáveis de ambiente** alinhadas entre `deploy.py`, `agent.yaml`, `main.py` e os
  arquivos `.env.example`.
- Diagramas de arquitetura do README e o catálogo de agentes/cenários reescritos para coincidir com o código entregue.

### Corrigido
- Corrigido o link quebrado do README raiz para a Lição 4 (`lesson-4-agentdeployment`).
- Redigido o README anteriormente vazio da Lição 3 (avaliações + observabilidade).
- Substituído o padrão obsoleto `asyncio.get_event_loop().run_until_complete` no
  agente de recomendação de aprendizagem.

### Obsoleto / Removido
- Removido todo uso dos modelos aposentados **GPT-4o / GPT-4.1**. Exemplos de chat e avaliação agora usam
  **gpt-5.1**; exemplos de codificação usam **gpt-5-codex**.
- Documentado que **GitHub Models** está sendo aposentado (July 30, 2026); o curso fornece todos os modelos
  através do Microsoft Foundry e não depende do GitHub Models.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->