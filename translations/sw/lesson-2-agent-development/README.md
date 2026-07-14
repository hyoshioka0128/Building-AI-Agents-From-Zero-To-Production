# Somo la 2 Maendeleo ya Wakala

Karibu somo la pili la "Kozi ya Kujenga Wakala wa AI kutoka Mwanzo hadi Uzalishaji"!

Katika somo hili tutashughulikia:

- Zana za Kuunda Wakala wetu wa AI
  
- Maelekezo ya Usanidi kwa Rasilimali zetu za Maendeleo

- Mbinu Bora za Maendeleo ya Wakala wa AI
  
- Maelekezo ya Kufuatilia Msimbo wa Kuunda Wakala wetu wa AI
  
Tuanze kwa kuangalia zana tutakazotumia kuunda Wakala wetu wa AI.

## Zana na Maelekezo ya Usanidi

### Microsoft Foundry

Kwa ajili ya kupata Mfano Mrefu wa Lugha (LLMs) tutatumia [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Kuna gharama zinazohusiana na kutumia Foundry kwa hivyo tafadhali hakikisha kufuata maelekezo ya usanidi wa akaunti ikiwa bado huna ufikiaji.

### Mifano ya OpenAI

Sampuli za msimbo wa wakala katika kozi hii zimesanidiwa kutumia mifano ya OpenAI kupitia [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Tumia mwongozo huu kujifunza jinsi ya kuzindua mfano kwa kutumia Foundry: [Tumia Mifano ya Microsoft Foundry katika lango la Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Chagua mfano mmoja wa mfululizo wa GPT-5 (kwa mfano `gpt-5.1`) kwa kozi hii. Epuka mifano iliyohamishwa kama GPT-4o na GPT-4.1, ambayo itafikia mwisho wa maisha mwaka 2026.

### Mfumo wa Wakala wa Microsoft

Kama ilivyotajwa awali, tutatumia [Mfumo wa Wakala wa Microsoft](https://github.com/microsoft/agent-framework) kuunda na kuratibu Wakala wetu wa AI.

Utahitaji **Python 3.12 au baadaye**. Ili kusanidi Mfumo wa Wakala wa Microsoft na vifurushi vingine vinavyohitajika, endesha amri ifuatayo ukiwa kwenye saraka kuu ya mradi huu:

```bash
pip install -r requirements.txt
```

### Thibitisha na Azure

Wakala hujithibitisha kwa Microsoft Foundry kwa kutumia vyeti vyako vya Azure CLI
(`AzureCliCredential`), kwa hivyo lazima uingie kabla ya kuendesha sampuli yoyote:

```bash
az login
# Ikiwa una usajili zaidi ya mmoja, chagua ule ulio na mradi wako wa Foundry:
az account set --subscription "<your-subscription-id>"
```

Hakikisha akaunti yako ina jukumu la **Azure AI User** (au sawa nalo) kwenye mradi wa Foundry
ili iweze kuita API za mfano na wakala.

### Sanidi Vigezo vya .env

Ili kuendesha sampuli za msimbo katika kozi hii, utahitaji kuunda faili `.env` katika saraka kuu ya mradi huu. 

Ili kuwezesha hili, unaweza kunakili faili lililotolewa la `.env.example`:

```bash
cp .env.example .env
``` 

Kisha jaza vigezo viwili ambavyo wakala husoma (kile wanachokipata kwa `FoundryChatClient`
kiotomatiki):

| Kigezo | Nini kilicho | Mahali pa kukipata |
|----------|------------|------------------|
| `FOUNDRY_PROJECT_ENDPOINT` | Kituo cha **mradi** wako wa Foundry, kinachoishia `/api/projects/<project>` | Lango la Foundry → mradi wako → **Muhtasari** → *Endpoints* |
| `FOUNDRY_MODEL` | Jina la uzinduzi wa mfano ambao wakala wako hutumia (kwa mfano `gpt-5.1`) | Lango la Foundry → **Mifano + vituo** |

### Unda duka la vector la wafanyakazi

Sampuli moja — **Wakala wa Utafutaji Wafanyakazi** — hutafuta kwenye orodha ya wafanyakazi iliyohifadhiwa katika
duka la vector la Microsoft Foundry. Unda mara moja na nakili kitambulisho kinachochapishwa katika `.env` yako
kama `VECTOR_STORE_ID` (endesha kutoka saraka kuu ya kumbukumbu ili ipate `.env` yako):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### Endesha sampuli

Kila wakala anaendesha DevUI yake ya ndani. Kwa mfano:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

Kisha fungua URL iliyochapishwa `http://localhost:<port>` kwenye kivinjari chako kuzungumza na wakala.

## Wakala katika somo hili

Kila sampuli ni wakala huru aliyojengwa na Mfumo wa Wakala wa Microsoft. Pamoja
hutekeleza hali ulizobuni katika [Somo la 1](../lesson-1-agent-design/README.md):

| Sampuli | Hali ya Somo la 1 | Zana iliyotumiwa | Porti |
|--------|-------------------|-----------|------|
| `employee-search-agent.py` | Hali 1 — Utafutaji Wafanyakazi | Utafutaji wa faili uliodhibitiwa na Foundry juu ya duka la vector | 8090 |
| `task-recommendation-agent.py` | Hali 2 — Mapendekezo ya Kazi | Seva ya **GitHub MCP** (zana ya MCP iliyohudumiwa) | 8095 |
| `azure-learning-agent.py` | Hali 3 — Msaidizi wa Msimbo (tafiti) | Seva ya **Microsoft Learn MCP** (zana ya MCP iliyohudumiwa) | 8092 |
| `coding-agent.py` | Hali 3 — Msaidizi wa Msimbo (msimbo) | **Mfasiri wa Msimbo** | 8093 |
| `learning-recommendation-agent.py` | Wakala wa msaada | Learn MCP + hoja | 8091 |
| `agent-orchestration.py` | Inahusisha hali zote pamoja | Uratibu wa kuhamishiana kwa mawakala wengi | 8094 |

> **Kumbuka kuhusu Wakala wa Mapendekezo ya Kazi.** `task-recommendation-agent.py` inahitaji
> `GITHUB_PERSONAL_ACCESS_TOKEN` katika `.env` yako (unda moja huko
> <https://github.com/settings/personal-access-tokens/new>). Husoma shughuli za hivi karibuni za mendeveloper
> GitHub na kupendekeza masuala wazi 1–3 yanayofanana — hasa muundo wa Hali ya 2.
> Hii ni sampuli pekee inayoiita GitHub; zingine zinahitaji tu mradi wako wa Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->