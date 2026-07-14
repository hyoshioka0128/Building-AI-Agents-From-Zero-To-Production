# AGENTS.md

Gabay para sa mga AI coding agent (at mga taong nag-aambag) na nagtatrabaho sa repositoryong ito. Kung ikaw ay isang
awtomatikong agent na gumagawa ng mga pagbabago dito, basahin muna ang file na ito at sundin ito.

## Ano ang repositoryong ito

**Pagtatayo ng AI Agents mula Zero hanggang Production** ay isang kurso sa pag-aaral ng Microsoft. Itinuturo nito sa mga developer
kung paano magdisenyo, bumuo, mag-evaluate, mag-deploy at mag-operate ng mga AI agent sa **Microsoft Foundry** gamit ang
**Microsoft Agent Framework (MAF)**. Ang nilalaman ay nakaayos bilang isang sunod-sunod na mga leksyon, bawat isa ay may
`README.md` at mga maaring patakbuhin na Python sample.

```
lesson-1-agent-design/            Use case + how to design effective agents
lesson-2-agent-development/       Build specialised agents with MAF (multiple runnable samples)
lesson-3-agent-evals/             Evaluations and observability
lesson-4-agentdeployment/         Deploy a hosted agent + OpenAI ChatKit front end
lesson-5-hosted-agents-production/ Hosted Agents vs Capability Hosts, BYO storage, governance
lesson-6-toolbox/                 Microsoft Toolbox: define + govern tools centrally
lesson-7-multi-agent-a2a/         Multi-agent orchestration over the A2A protocol
```

Mga root docs: `README.md` (simulan dito), `MIGRATION-GUIDE.md` (detalye sa SDK migration), `CHANGELOG.md`.

## Mga gintong patakaran

1. **Huwag kailanman mag-commit ng mga lihim.** Tanging `*.env.example` na mga file lang ang sinusubaybayan; ang totoong `.env` na mga file ay
   hindi kasama sa git. Huwag i-hardcode ang mga endpoint, key, token, o connection string sa mga sample o dokumento.
2. **Huwag hawakan ang `translations/` o `translated_images/`.** Ang mga ito ay awtomatikong ginagawa ng isang
   translation GitHub Action. Huwag kailanman mano-manong i-edit ang mga ito; gumawa ng mga pagbabago sa pinagmulan lamang sa level ng gawain
   na mga file.
3. **Walang deprecated na mga modelo.** Gamitin ang **`gpt-5.1`** para sa chat/eval at **`gpt-5-codex`** para sa coding.
   Huwag magpakilala ng `gpt-4o`, `gpt-4.1`, o anumang retiradong modelo, at huwag gumamit ng *GitHub Models*
   (magreretiro sa Hulyo 30, 2026) — lahat ng modelo ay pinagsilbihan sa pamamagitan ng Microsoft Foundry.
4. **Gamitin ang kasalukuyang SDK surface.** Ang mga sample ay nagtatarget sa `agent-framework` (nakapirmi sa `requirements.txt`)
   gamit ang `FoundryChatClient` at ang **Responses API**. Huwag muling ipakilala ang mga lumang
   `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` na mga pattern.
5. **Panatilihing napapanahon ang terminolohiya**: *Microsoft Foundry* (hindi "Azure AI Foundry"), *Microsoft Agent
   Framework*, *Hosted Agents*, *Capability Hosts*, *Microsoft Toolbox*, *MCP / Hosted MCP*, *A2A*.

## Setup

```bash
python -m venv .venv
# Windows:  .venv\Scripts\Activate.ps1
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt

az login                     # mga sample ay magpapatunay gamit ang iyong pagkakakilanlang developer
cp .env.example .env         # pagkatapos ay punan ang endpoint ng iyong proyekto sa Foundry + modelo
```

Mga kinakailangan: **Python 3.12+**, ang **Azure CLI**, at access sa isang **Microsoft Foundry** na proyekto
na may naka-deploy na GPT-5-series na modelo. Bawat lesson README ay naglilista ng sarili nitong mga prerequisites at ang mga env var na
kinakailangan nito (tingnan ang lesson-level `.env.example` kung meron).

## Pagpapatakbo ng mga sample

Karamihan sa mga sample sa lesson-2 ay nagpapaandar ng lokal na **DevUI** sa isang nakalaang port (halimbawa 8090–8096); ang A2A
server sa lesson 7 ay nakikinig sa port 9000. Suriin ang docstring/README ng bawat sample para sa eksaktong utos
at port. Dahil ang mga sample ay tumatawag sa mga live Foundry endpoints, kailangan nila ng valid na `.env` at `az login`.

## Pagpapatunay ng mga pagbabago

Walang unit-test suite; ang pagpapatunay ay static + live:

- **Static gate (dapat pumasa bago mag-commit):** i-byte-compile ang bawat sample.
  ```bash
  python -m py_compile $(git ls-files '*.py')
  ```
  Sa Windows PowerShell:
  ```powershell
  git ls-files '*.py' | ForEach-Object { python -m py_compile $_ }
  ```
- **Mga markdown na link:** ang trabaho sa CI na `static` ay nagpapatakbo ng `markdown-link-check`
  (config: `.github/workflows/markdown-link-check-config.json`). Suriin ang anumang bagong panlabas na link
  kung gumagana (HTTP 200).
- **Smoke test:** `.github/workflows/smoke-test-hosted-agent.yml` ay nagpapatakbo ng AI Smoke Test action
  laban sa isang naka-deploy na hosted agent (`workflow_dispatch`, OIDC). Ang live na pagtakbo ng agent ay nangangailangan ng Azure access.

Ang CI (`static` job) ay awtomatikong naghahanap ng `.py` na mga file, kaya sakop ang mga bagong sample nang hindi ina-edit ang
workflow. Huwag mag-commit ng code na pumapalya sa `py_compile`.

## Mga konbensiyon sa pag-commit

- Magsulat ng mga nakatutok na commit na may malinaw, utos na mensahe.
- Isama ang co-author trailer sa mga commit na tulong ng agent:
  ```
  Co-authored-by: Copilot App <223556219+Copilot@users.noreply.github.com>
  ```
- Huwag mag-commit ng mga generated cache, virtual environment, o `.env` na mga file (lahat ay git-ignored).

## Saan gumawa ng mga partikular na pagbabago

| Pagbabago | Lokasyon |
|--------|----------|
| Kuwento ng kurso / teksto ng leksyon | `lesson-*/README.md` (pinagmulan lamang — huwag kailanman sa `translations/`) |
| Maaaring patakbuhin na code | `lesson-*/**.py`, `setup_vector_store.py` |
| Mga dependencies | `requirements.txt` (panatilihing naka-pin ang mga bersyon) |
| Dokumentasyon ng env var | `.env.example`, lesson-level `.env.example` |
| CI / static gate | `.github/workflows/` |
| Kasanayan sa kurso para sa mga AI assistant | `.github/skills/` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->