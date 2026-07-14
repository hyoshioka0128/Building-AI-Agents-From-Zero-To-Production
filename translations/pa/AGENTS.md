# AGENTS.md

ਇਸ ਰਿਪੋਜ਼ਿਟਰੀ ਵਿੱਚ ਕੰਮ ਕਰਨ ਵਾਲੇ AI ਕੋਡਿੰਗ ਏਜੰਟਾਂ (ਅਤੇ ਮਨੁੱਖੀ ਯੋਗਦਾਨਕਾਰਾਂ) ਲਈ ਮਾਰਗਦਰਸ਼ਨ। ਜੇ ਤੁਸੀਂ ਇੱਕ
ਇੱਥੇ ਬਦਲਾਅ ਕਰਨ ਵਾਲਾ ਸੁਚਾਲਿਤ ਏਜੰਟ ਹੋ, ਤਾਂ ਸਭ ਤੋਂ ਪਹਿਲਾਂ ਇਸ ਫਾਇਲ ਨੂੰ ਪੜ੍ਹੋ ਅਤੇ ਇਸ ਦੀ ਪਾਲਣਾ ਕਰੋ।

## ਇਹ ਰਿਪੋਜ਼ਿਟਰੀ ਕੀ ਹੈ

**Building AI Agents from Zero to Production** ਇੱਕ Microsoft ਸਿੱਖਣ ਕੋਰਸ ਹੈ। ਇਹ ਵਿਕਾਸਕਰਤਿਆਂ ਨੂੰ
**Microsoft Foundry** 'ਤੇ AI ਏਜੰਟਾਂ ਨੂੰ ਡਿਜ਼ਾਈਨ, ਬਣਾਉਣ, ਮੁਲਾਂਕਣ, ਡਿਪਲੋਇ ਅਤੇ ਓਪਰੇਟ ਕਰਨ ਲਈ
**Microsoft Agent Framework (MAF)** ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਸਿਖਾਉਂਦਾ ਹੈ। ਸਮੱਗਰੀ ਪਾਠਾਂ ਦੀ ਲੜੀ ਵਜੋਂ ਵਿਵਸਤਤ ਹੈ, ਹਰ ਇੱਕ
`README.md` ਅਤੇ ਚਲਾਉਣ ਯੋਗ Python ਨਮੂਨੇ।

```
lesson-1-agent-design/            Use case + how to design effective agents
lesson-2-agent-development/       Build specialised agents with MAF (multiple runnable samples)
lesson-3-agent-evals/             Evaluations and observability
lesson-4-agentdeployment/         Deploy a hosted agent + OpenAI ChatKit front end
lesson-5-hosted-agents-production/ Hosted Agents vs Capability Hosts, BYO storage, governance
lesson-6-toolbox/                 Microsoft Toolbox: define + govern tools centrally
lesson-7-multi-agent-a2a/         Multi-agent orchestration over the A2A protocol
```

ਮੁੱਖ ਦਸਤਾਵੇਜ਼: `README.md` (ਇਥੋਂ ਸ਼ੁਰੂ ਕਰੋ), `MIGRATION-GUIDE.md` (SDK ਮਾਈਗਰੇਸ਼ਨ ਵਿਵਰਣ), `CHANGELOG.md`.

## ਮਹੱਤਵਪੂਰਨ ਨਿਯਮ

1. **ਕਦੇ ਵੀ ਸਿਕ੍ਰੇਟਸ commit ਨਾ ਕਰੋ।** ਕੇਵਲ `*.env.example` ਫਾਈਲਾਂ ਟ੍ਰੈਕ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ; ਅਸਲ `.env` ਫਾਈਲਾਂ
   git-ignored ਹਨ। ਨਮੂਨਿਆਂ ਜਾਂ ਦਸਤਾਵੇਜ਼ਾਂ ਵਿੱਚ endpoints, keys, tokens, ਜਾਂ connection strings ਨੂੰ ਹਾਰਡਕੋਡ ਨਾ ਕਰੋ।
2. **`translations/` ਜਾਂ `translated_images/` ਨੂੰ ਛੇੜੋ ਨਾ।** ਇਹ ਇੱਕ translation GitHub Action ਦੁਆਰਾ ਆਟੋਮੈਟਿਕ ਤਰੀਕੇ ਨਾਲ ਬਣਾਈਆਂ ਜਾਂਦੀਆਂ ਹਨ।
   ਹੱਥੋਂ-ਹੱਥ ਸੋਧ ਕਦੇ ਵੀ ਨਾ ਕਰੋ; ਸੋਰਸ ਬਦਲਾਅ ਸਿਰਫ ਟੌਪ-ਲੇਵਲ ਪਾਠ
   ਫਾਈਲਾਂ ਵਿੱਚ ਹੀ ਕਰੋ।
3. **ਕੋਈ deprecated ਮਾਡਲ ਨਹੀਂ।** ਚੈਟ/ਮੁਲਾਂਕਣ ਲਈ **`gpt-5.1`** ਅਤੇ ਕੋਡਿੰਗ ਲਈ **`gpt-5-codex`** ਵਰਤੋ।
   ਕਿਰਪਾ ਕਰਕੇ **ਨਵੇਂ** `gpt-4o`, `gpt-4.1`, ਜਾਂ ਕਿਸੇ ਵੀ ਰਿਟਾਇਰ ਹੋਏ ਮਾਡਲ ਨੂੰ ਨਹੀਂ ਲਿਆਓ, ਅਤੇ *GitHub Models*
   (retiring July 30, 2026) — ਸਾਰੇ ਮਾਡਲ Microsoft Foundry ਰਾਹੀਂ ਸਰਵ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।
4. **ਮੌਜੂਦਾ SDK surface ਵਰਤੋ।** ਨਮੂਨੇ `agent-framework` (ਜੋ `requirements.txt` ਵਿੱਚ pinned ਹੈ)
   `FoundryChatClient` ਅਤੇ **Responses API** ਨਾਲ। ਪੁਰਾਣੇ
   `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` ਪੈਟਰਨਸ ਨੂੰ ਮੁੜ ਨਾ ਲਿਆਓ।
5. **ਸ਼ਬਦਾਵਲੀ ਨਵੀਨਤਮ ਰੱਖੋ**: *Microsoft Foundry* (not "Azure AI Foundry"), *Microsoft Agent
   Framework*, *Hosted Agents*, *Capability Hosts*, *Microsoft Toolbox*, *MCP / Hosted MCP*, *A2A*.

## ਸੈੱਟਅੱਪ

```bash
python -m venv .venv
# ਵਿੰਡੋਜ਼:  .venv\Scripts\Activate.ps1
# macOS/ਲਿਨਕਸ:  source .venv/bin/activate
pip install -r requirements.txt

az login                     # ਸੈਂਪਲ ਤੁਹਾਡੀ ਡਿਵੈਲਪਰ ਆਈਡੈਂਟੀਟੀ ਨਾਲ ਪ੍ਰਮਾਣਿਕਤਾ ਕਰਦੇ ਹਨ
cp .env.example .env         # ਫਿਰ ਆਪਣਾ Foundry ਪ੍ਰੋਜੈਕਟ ਐਂਡਪਾਇੰਟ + ਮਾਡਲ ਭਰੋ
```

ਲੋੜਾਂ: **Python 3.12+**, **Azure CLI**, ਅਤੇ ਇੱਕ **Microsoft Foundry** ਪ੍ਰੋਜੈਕਟ ਤੱਕ ਪਹੁੰਚ
ਜਿਸ ਉੱਤੇ ਇੱਕ ਡਿਪਲੋਇਡ GPT-5-series ਮਾਡਲ ਹੋਵੇ। ਹਰ ਪਾਠ README ਆਪਣੀਆਂ ਜਰੂਰੀਆਂ ਸ਼ਰਤਾਂ ਅਤੇ env vars ਨੂੰ ਸੂਚੀਬੱਧ ਕਰਦਾ ਹੈ
ਇਹਦੀ ਲੋੜਾਂ ਲਈ (ਜਿੱਥੇ ਉਪਲਬਧ ਹੋਵੇ ਤਾਂ lesson-ਲੇਵਲ `.env.example` ਵੇਖੋ)।

## ਨਮੂਨੇ ਚਲਾਉਣਾ

ਜ਼ਿਆਦਾਤਰ lesson-2 ਨਮੂਨੇ ਇੱਕ ਸਮਰਪਿਤ ਪੋਰਟ 'ਤੇ ਲੋਕਲ **DevUI** ਲਾਂਚ ਕਰਦੇ ਹਨ (ਉਦਾਹਰਣ ਲਈ 8090–8096); A2A
ਸਰਵਰ ਪਾਠ 7 ਵਿੱਚ ਪੋਰਟ 9000 'ਤੇ ਸੁਣਦਾ ਹੈ। ਸਹੀ ਕਮਾਂਡ ਅਤੇ ਪੋਰਟ ਲਈ ਹਰ ਨਮੂਨੇ ਦੀ docstring/README ਚੈੱਕ ਕਰੋ।
ਕਿਉਂਕਿ ਨਮੂਨੇ ਲਾਈਵ Foundry endpoints ਨੂੰ ਕਾਲ ਕਰਦੇ ਹਨ, ਉਹਨਾਂ ਨੂੰ ਇੱਕ ਵੈਧ `.env` ਅਤੇ `az login` ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।

## ਬਦਲਾਵਾਂ ਦੀ ਜਾਂਚ

ਇੱਥੇ ਕੋਈ ਯੂਨਿਟ-ਟੈਸਟ ਸੂਟ ਨਹੀਂ ਹੈ; ਵੇਰੀਫਿਕੇਸ਼ਨ static + live ਹੈ:

- **Static gate (must pass before commit):** ਹਰ ਨਮੂਨੇ ਨੂੰ byte-compile ਕਰੋ।
  ```bash
  python -m py_compile $(git ls-files '*.py')
  ```
  Windows PowerShell 'ਤੇ:
  ```powershell
  git ls-files '*.py' | ForEach-Object { python -m py_compile $_ }
  ```
- **Markdown links:** CI `static` job `markdown-link-check` ਚਲਾਂਦਾ ਹੈ
  (config: `.github/workflows/markdown-link-check-config.json`). ਕਿਸੇ ਵੀ ਨਵੇਂ ਬਾਹਰੀ ਲਿੰਕ ਦੀ ਜਾਂਚ ਕਰੋ
  ਕਿ ਉਹ ਸਹੀ ਤਰੀਕੇ ਨਾਲ resolve ਹੁੰਦੇ ਹਨ (HTTP 200)।
- **Smoke test:** `.github/workflows/smoke-test-hosted-agent.yml` AI Smoke Test action ਚਲਾਉਂਦਾ ਹੈ
  ਇਕ ਡਿਪਲੋਇਡ ਹੋਸਟਡ ਏਜੰਟ ਦੇ ਖਿਲਾਫ (`workflow_dispatch`, OIDC). ਲਾਈਵ ਏਜੰਟ ਚਲਾਉਣ ਲਈ Azure ਪਹੁੰਚ ਲਾਜ਼ਮੀ ਹੈ।

CI (`static` job) ਆਪਮੈਟਿਕ ਤੌਰ ` .py` ਫਾਈਲਾਂ ਨੂੰ ਖੋਜਦਾ ਹੈ, ਇਸ ਲਈ ਨਵੇਂ ਨਮੂਨੇ workflow ਸੋਧਣ ਬਿਨਾਂ ਕਵਰ ਹੋ ਜਾਂਦੇ ਹਨ।
workflow. `py_compile` ਫੇਲ ਹੋਣ ਵਾਲਾ ਕੋਡ commit ਨਾ ਕਰੋ।

## Commit ਰੀਤੀਆਂ

- ਧਿਆਨ ਕੇਂਦਰਿਤ commits ਲਿਖੋ ਜਿਨ੍ਹਾਂ ਦੇ ਸੁਨੇਹੇ ਸਪਸ਼ਟ ਅਤੇ ਹੁਕਮਵਾਧਕ ਹੋਣ।
- agent-ਸਹਾਇਤ commits 'ਤੇ co-author trailer ਸ਼ਾਮਿਲ ਕਰੋ:
  ```
  Co-authored-by: Copilot App <223556219+Copilot@users.noreply.github.com>
  ```
- ਤਿਆਰ ਕੀਤੀਆਂ caches, virtual environments, ਜਾਂ `.env` ਫਾਈਲਾਂ (ਸਭ git-ignored) commit ਨਾ ਕਰੋ।

## ਖਾਸ ਬਦਲਾਅ ਕਿੱਥੇ ਕਰਨੇ ਹਨ

| ਬਦਲਾਅ | ਸਥਾਨ |
|--------|----------|
| ਕੋਰਸ ਵਰਣਨ / ਪਾਠ ਦਾ ਲਿਖਤ | `lesson-*/README.md` (source only — never `translations/`) |
| ਚਲਣਯੋਗ ਕੋਡ | `lesson-*/**.py`, `setup_vector_store.py` |
| ਨਿਰਭਰਤਾਵਾਂ | `requirements.txt` (keep versions pinned) |
| Env var ਦਸਤਾਵੇਜ਼ਕਰਨ | `.env.example`, lesson-level `.env.example` |
| CI / ਸਟੈਟਿਕ ਗੇਟ | `.github/workflows/` |
| AI ਸਹਾਇਕਾਂ ਲਈ ਕੋਰਸ ਸਕਿਲਜ਼ | `.github/skills/` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->