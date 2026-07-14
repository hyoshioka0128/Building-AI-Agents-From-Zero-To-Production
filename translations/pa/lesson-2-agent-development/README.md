# ਪਾਠ 2 ਏਜੰਟ ਵਿਕਾਸ

ਇਸ ਕੋਰਸ "Building AI Agent from Zero to Production Course" ਦੇ ਦੂਜੇ ਪਾਠ ਵਿੱਚ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ!

ਇਸ ਪਾਠ ਵਿੱਚ ਅਸੀਂ ਇਹ ਕਵਰ ਕਰਾਂਗੇ:

- ਸਾਡੇ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਟੂਲ
  
- ਵਿਕਾਸ ਸਰੋਤਾਂ ਲਈ ਸੈਟਅਪ ਹਦਾਇਤਾਂ

- AI ਏਜੰਟ ਵਿਕਾਸ ਲਈ ਬਿਹਤਰ ਅਭਿਆਸ
  
- ਸਾਡੇ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਕੋਡ ਵਾਕਥਰੂ
  
ਆਓ ਉਹ ਟੂਲ ਵੇਖ ਕੇ ਸ਼ੁਰੂ ਕਰੀਏ ਜੋ ਅਸੀਂ ਆਪਣੇ AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਵਰਤਾਂਗੇ।

## ਟੂਲ ਅਤੇ ਸੈਟਅਪ ਹਦਾਇਤਾਂ

### Microsoft Foundry

ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ (LLMs) ਤੱਕ ਪਹੁੰਚ ਲਈ ਅਸੀਂ [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) ਦੀ ਵਰਤੋਂ ਕਰਾਂਗੇ। Foundry ਦੀ ਵਰਤੋਂ ਨਾਲ ਲਾਗਤ ਜੁੜੀ ਹੋ ਸਕਦੀ ਹੈ, ਇਸ ਲਈ ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਪਹਿਲਾਂ ਪਹੁੰਚ ਨਹੀਂ ਹੈ ਤਾਂ ਖਾਤਾ ਸੈਟਅਪ ਦੀਆਂ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਨਾ ਕਰੋ।

### OpenAI ਮਾਡਲ

ਇਸ ਕੋਰਸ ਵਿੱਚ ਏਜੰਟ ਕੋਡ ਨਮੂਨੇ [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) ਰਾਹੀਂ OpenAI ਮਾਡਲ ਵਰਤਣ ਲਈ ਸੈਟਅਪ ਕੀਤੇ ਗਏ ਹਨ।

Foundry ਵਰਤ ਕੇ ਮਾਡਲ ਡਿਪਲੋਇ ਕਰਨ ਬਾਰੇ ਸਿੱਖਣ ਲਈ ਇਸ ਗਾਈਡ ਦੀ ਵਰਤੋਂ ਕਰੋ: [Foundry ਪੋਰਟਲ ਵਿੱਚ Microsoft Foundry ਮਾਡਲ ਡਿਪਲੋਯ ਕਰੋ](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

ਇਸ ਕੋਰਸ ਲਈ ਇੱਕ GPT-5 ਸੀਰੀਜ਼ ਮਾਡਲ ਚੁਣੋ (ਉਦਾਹਰਣ ਲਈ `gpt-5.1`)। GPT-4o ਅਤੇ GPT-4.1 ਵਰਗੇ ਰਿਟਾਇਰ ਹੋ ਚੁੱਕੇ ਮਾਡਲਾਂ ਤੋਂ ਬਚੋ, ਜੋ 2026 ਵਿੱਚ end of life 'ਤੇ ਪਹੁੰਚਦੇ ਹਨ।

### Microsoft Agent Framework

ਜਿਵੇਂ ਪਹਿਲਾਂ ਜ਼ਿਕਰ ਕੀਤਾ ਗਿਆ, ਅਸੀਂ ਆਪਣੇ AI ਏਜੰਟ ਬਣਾਉਣ ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ ਅਨੁਸ਼ਾਸਿਤ (orchestrate) ਕਰਨ ਲਈ [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) ਦੀ ਵਰਤੋਂ ਕਰਾਂਗੇ।

ਤੁਹਾਨੂੰ **Python 3.12 or later** ਦੀ ਲੋੜ ਹੋਵੇਗੀ। Microsoft Agent Framework ਅਤੇ ਹੋਰ ਲੋੜੀਂਦੇ ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰਨ ਲਈ, ਇਸ ਪ੍ਰੋਜੈਕਟ ਦੀ ਰੂਟ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਹੋ ਕੇ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾਓ:

```bash
pip install -r requirements.txt
```

### Azure ਨਾਲ ਪ੍ਰਮਾਣਿਕਰਨ

ਏਜੰਟ ਤੁਹਾਡੇ Azure CLI ਕ੍ਰੈਡੈਂਸ਼ਲਜ਼
(`AzureCliCredential`), ਇਸ ਲਈ ਕਿਸੇ ਵੀ ਸੈਂਪਲ ਨੂੰ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਤੁਹਾਨੂੰ ਸਾਈਨ ਇਨ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ:

```bash
az login
# ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ ਤੋਂ ਵੱਧ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਹਨ, ਤਾਂ ਉਸ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਨੂੰ ਚੁਣੋ ਜਿਸ ਵਿੱਚ ਤੁਹਾਡਾ Foundry ਪ੍ਰੋਜੈਕਟ ਹੈ:
az account set --subscription "<your-subscription-id>"
```

ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਖਾਤੇ ਕੋਲ Foundry
ਪ੍ਰੋਜੈਕਟ 'ਤੇ **Azure AI User** ਰੋਲ (ਜਾਂ ਸਮਾਨ) ਹੈ ਤਾਂ ਜੋ ਇਹ ਮਾਡਲ ਅਤੇ ਏਜੰਟ APIs ਨੂੰ ਕੌਲ ਕਰ ਸਕੇ।

### .env ਵੇਰੀਐਬਲ ਸੈਟਅਪ

ਇਸ ਕੋਰਸ ਦੇ ਕੋਡ ਨਮੂਨੇ ਚਲਾਉਣ ਲਈ, ਤੁਹਾਨੂੰ ਇਸ ਪ੍ਰੋਜੈਕਟ ਦੀ ਰੂਟ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਇੱਕ `.env` ਫਾਈਲ ਬਣਾਉਣੀ ਪਵੇਗੀ। 

ਆਸਾਨੀ ਲਈ, ਤੁਸੀਂ ਦਿੱਤੀ `.env.example` ਫਾਈਲ ਨੂੰ ਕਾਪੀ ਕਰ ਸਕਦੇ ਹੋ:

```bash
cp .env.example .env
``` 

ਫਿਰ ਉਹ ਦੋ ਵੇਰੀਏਬਲ ਭਰੋ ਜੋ ਏਜੰਟ ਪੜ੍ਹਦੇ ਹਨ (ਇਹਨਾਂ ਨੂੰ `FoundryChatClient` ਆਪਣੇ ਆਪ ਲੈ ਲੈਂਦਾ ਹੈ
ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ):

| Variable | ਇਹ ਕੀ ਹੈ | ਕਿੱਥੋਂ ਲੱਭੇਗਾ |
|----------|------------|------------------|
| `FOUNDRY_PROJECT_ENDPOINT` | ਤੁਹਾਡੇ Foundry **project** ਐਂਡਪੋਇੰਟ, ਜੋ `/api/projects/<project>` 'ਤੇ ਖਤਮ ਹੁੰਦਾ ਹੈ | Foundry portal → your project → **Overview** → *Endpoints* |
| `FOUNDRY_MODEL` | ਉਹ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਨਾਂ ਜਿਸ ਉੱਤੇ ਤੁਹਾਡੇ ਏਜੰਟ ਚਲਦੇ ਹਨ (ਉਦਾਹਰਨ ਲਈ `gpt-5.1`) | Foundry portal → **Models + endpoints** |

### ਕਰਮਚਾਰੀ ਵੇਕਟਰ ਸਟੋਰ ਬਣਾਓ

ਇੱਕ ਨਮੂਨਾ — **Employee Search Agent** — ਇੱਕ ਕਰਮਚਾਰੀ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਖੋਜ ਕਰਦਾ ਹੈ ਜੋ
Microsoft Foundry **vector store** ਵਿੱਚ ਰੱਖੀ ਹੁੰਦੀ ਹੈ। ਇਸਨੂੰ ਇਕ ਵਾਰੀ ਬਣਾਓ ਅਤੇ ਜੋ ID ਇਹ ਛਾਪਦਾ ਹੈ ਉਸਨੂੰ ਆਪਣੀ `.env` ਵਿੱਚ ਕਾਪੀ ਕਰੋ
ਜਿਵੇਂ `VECTOR_STORE_ID` (ਰਿਪੋਜ਼ਿਟਰੀ ਰੂਟ ਤੋਂ ਚਲਾਓ ਤਾਂ ਇਹ ਤੁਹਾਡੀ `.env` ਫਾਈਲ ਪਕੜ ਲਏਗਾ):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### ਇੱਕ ਨਮੂਨਾ ਚਲਾਓ

ਹਰ ਏਜੰਟ ਆਪਣਾ ਲੋਕਲ DevUI ਚਲਾਉਂਦਾ ਹੈ। ਉਦਾਹਰਣ ਵਜੋਂ:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

ਫਿਰ ਛਪਿਆ ਹੋਇਆ `http://localhost:<port>` URL ਆਪਣੇ ਬ੍ਰਾਉਜ਼ਰ ਵਿੱਚ ਖੋਲ੍ਹੋ ਤਾਂ ਜੋ ਤੁਸੀ ਏਜੰਟ ਨਾਲ ਗੱਲਬਾਤ ਕਰ ਸਕੋ।

## ਇਸ ਪਾਠ ਦੇ ਏਜੰਟ

ਹਰ ਨਮੂਨਾ ਇੱਕ standalone ਏਜੰਟ ਹੈ ਜੋ Microsoft Agent Framework ਨਾਲ ਬਣਾਇਆ ਗਿਆ ਹੈ। ਇਕੱਠੇ ਇਹ
ਉਹ ਸਿਨੇਰੀਓਜ਼ ਲਾਗੂ ਕਰਦੇ ਹਨ ਜੋ ਤੁਸੀਂ [ਪਾਠ 1](../lesson-1-agent-design/README.md) ਵਿੱਚ ਡਿਜ਼ਾਈਨ ਕੀਤੇ ਸਨ:

| ਨਮੂਨਾ | ਪਾਠ 1 ਦਾ ਸਿਨੇਰੀਓ | ਵਰਤਿਆ ਟੂਲ | ਪੋਰਟ |
|--------|-------------------|-----------|------|
| `employee-search-agent.py` | ਸਿਨੇਰੀਓ 1 — ਕਰਮਚਾਰੀ ਖੋਜ | Foundry ਹੋਸਟ ਕੀਤੀ **file search** ਇੱਕ vector store 'ਤੇ | 8090 |
| `task-recommendation-agent.py` | ਸਿਨੇਰੀਓ 2 — ਟਾਸਕ ਸਿਫਾਰਸ਼ | **GitHub MCP** server (hosted MCP tool) | 8095 |
| `azure-learning-agent.py` | ਸਿਨੇਰੀਓ 3 — ਕੋਡ ਸਹਾਇਕ (ਰੀਸਰਚ) | **Microsoft Learn MCP** server (hosted MCP tool) | 8092 |
| `coding-agent.py` | ਸਿਨੇਰੀਓ 3 — ਕੋਡ ਸਹਾਇਕ (ਕੋਡ) | **Code Interpreter** | 8093 |
| `learning-recommendation-agent.py` | ਸਹਾਇਕ ਏਜੰਟ | Learn MCP + ਤਰਕ | 8091 |
| `agent-orchestration.py` | ਸਿਨੇਰੀਓਆਂ ਨੂੰ ਇਕੱਠਾ ਕਰਦਾ ਹੈ | Multi-agent **handoff** orchestration | 8094 |

> **ਟਾਸਕ ਸਿਫਾਰਸ਼ ਏਜੰਟ ਬਾਰੇ ਨੋਟ।** `task-recommendation-agent.py` ਲਈ ਇੱਕ
> `GITHUB_PERSONAL_ACCESS_TOKEN` ਤੁਹਾਡੇ `.env` ਵਿੱਚ ਲੋੜੀਂਦਾ ਹੈ (ਇੱਕ ਬਣਾਉਣ ਲਈ
> <https://github.com/settings/personal-access-tokens/new>). ਇਹ ਡਿਵੈਲਪਰ ਦੀ ਹਾਲੀਆ
> GitHub ਗਤੀਵਿਧੀ ਪੜ੍ਹਦਾ ਹੈ ਅਤੇ 1–3 ਖੁੱਲੇ ਇਸ਼ੂਜ਼ ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦਾ ਹੈ ਜੋ ਮਿਲਦੇ ਹਨ — ਬਿਲਕੁਲ ਸਿਨੇਰੀਓ 2 ਡਿਜ਼ਾਇਨ ਵਾਂਗ।
> ਇਹ ਇਕੱਲਾ ਨਮੂਨਾ ਹੈ ਜੋ GitHub ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ; ਹੋਰ ਸਾਰੇ ਨਮੂਨੇ ਸਿਰਫ਼ ਤੁਹਾਡੇ Foundry ਪ੍ਰੋਜੈਕਟ ਦੀ ਲੋੜ ਰੱਖਦੇ ਹਨ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->