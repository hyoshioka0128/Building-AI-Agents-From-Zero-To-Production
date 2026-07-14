# Tala ng Pagbabago

Lahat ng mga kapansin-pansing pagbabago sa **Building AI Agents from Zero to Production** ay naitala dito.

Ang format ay batay sa [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Ang kursong ito ay isang buhay na kurikulum sa halip na isang bersyonadong software package, kaya ang mga entry ay pinagsama
ayon sa petsa kung kailan naisakatuparan ang isang hanay ng mga pagbabago kaysa sa isang semantic version number.

## 13 Hulyo 2026

### Idinagdag
- **Kalusugan ng repository para sa pampublikong pagbabahagi** — pinatibay na `.gitignore` na may dedikadong
  Python / notebooks / sekreto / OS section (env-file variants, `.pytest_cache/`, `.mypy_cache/`,
  `.ruff_cache/`, `.ipynb_checkpoints/`, `*.egg-info/`), habang pinapanatili bawat `*.env.example`
  na naka-track. Idinagdag ang `CHANGELOG.md` na ito, isang gabay para sa mga kontribyutor/agent sa `AGENTS.md`, at mga skill
  file ng kurso.

### Binago
- Inihanda ang repository para sa pampublikong pagbabahagi: nilinis ang mga personal at live-environment na tagapagkilala
  (account, project, resource-group at mga pangalan ng identidad) mula sa mga inilathalang dokumento, at inilipat ang internal
  modernisation/gap-analysis na ulat palabas ng repository (ang buod nito para sa mga nag-aaral ay nasa changelog na ito).


## [2026 Modernisasyon ng Foundry]

Isang kumpletong teknikal, terminolohiya at kurikulum na rebisyon na nagtutugma sa kurso sa
**Microsoft Foundry 2026** platform. Tingnan ang `MIGRATION-GUIDE.md` para sa mga detalye ng paglipat sa antas ng kodigo.

### Idinagdag
- **Lesson 5 – Production Hosted Agents** (`lesson-5-hosted-agents-production/`): Hosted Agents laban sa
  Capability Hosts, magdala-ng-sariling Cosmos DB / Storage / AI Search, memorya at thread persistence,
  Hosted MCP approval workflows, at isang checklist sa pamamahala.
- **Lesson 6 – Microsoft Toolbox** (`lesson-6-toolbox/`): itakda ang mga kagamitan nang isang beses at pamahalaan ang mga ito
  nang sentralisado, pati na rin isang running consume sample (`toolbox_agent.py`) na umaabot sa isang toolbox sa pamamagitan ng
  isang solong MCP endpoint.
- **Lesson 7 – Multi-Agent & A2A** (`lesson-7-multi-agent-a2a/`): ilahad ang isang agent sa bukas na
  Agent-to-Agent (A2A) protocol (`a2a_server.py`) at gamitin ang isang remote agent bilang kapantay
  (`a2a_client.py`). Nasubok nang live end-to-end.
- **Task Recommendation Agent** (`lesson-2-agent-development/task-recommendation-agent.py`):
  ipinatutupad ang Lesson 1 Scenario 2 gamit ang GitHub remote MCP server bilang isang tool.
- **Vector-store setup script** (`setup_vector_store.py`): lumilikha at nagpapasok ng vector store
  na kinakailangan ng employee-search agent (dating tinukoy ngunit nawawala).
- **CI smoke + static gate** (`.github/workflows/smoke-test-hosted-agent.yml`): isang `static` job ang nagpapatakbo
  ng `py_compile` at markdown-link-check sa bawat PR/push; isang `smoke` job ang nagpapatakbo ng AI Smoke Test
  action laban sa isang na-deploy na hosted agent (OIDC, `workflow_dispatch`).
- **Mga kinakailangan at patnubay sa setup** idinagdag sa bawat lesson at sa pangunahing README
  (Python 3.12+, `az login`, gabay sa modelo, gastos at paglilinis).
- **Bagong pangunahing dokumento**: `MIGRATION-GUIDE.md`.

### Binago
- **Rebrand**: *Azure AI Foundry* → **Microsoft Foundry** sa buong kurso.
- **SDK migration** sa kasalukuyang Microsoft Agent Framework surface — ang mga sample ay gumagamit na ng
  `agent-framework` `1.2.0` gamit ang `FoundryChatClient` at ang **Responses API**, pinalitan ang
  mas naunang `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` na mga pattern.
- **Pinned dependencies**: ang `requirements.txt` ngayon ay nag-pinned ng `agent-framework`, `agent-framework-foundry`
  at mga kaugnay na pakete sa halip na mag-install ng unpinned pre-releases, na ginagawang reproducible ang mga sample.
- **Environment variables** iniharmonisa sa `deploy.py`, `agent.yaml`, `main.py` at ang
  `.env.example` na mga file.
- Muling isinulat ang mga diagram ng arkitektura sa README at ang katalogo ng agent/scenario upang tumugma sa inilabas na kodigo.

### Naayos
- Inayos ang sirang root-README link sa Lesson 4 (`lesson-4-agentdeployment`).
- Nasulat ang dating walang laman na Lesson 3 README (evaluations + observability).
- Pinalitan ang deprecated na `asyncio.get_event_loop().run_until_complete` pattern sa
  learning-recommendation agent.

### Pinawalang Bisa / Inalis
- Inalis ang lahat ng paggamit ng retired na mga modelo **GPT-4o / GPT-4.1**. Ngayon ay gumagamit na ang chat at evaluation samples
  ng **gpt-5.1**; ang mga coding samples ay gumagamit ng **gpt-5-codex**.
- Dinokumento na ang **GitHub Models** ay pinapawalang-bisa na (Hulyo 30, 2026); ang kurso ay nagsisilbi ng lahat ng mga modelo
  sa pamamagitan ng Microsoft Foundry at hindi nakadepende sa GitHub Models.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->