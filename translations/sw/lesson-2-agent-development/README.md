<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:24:17+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "sw"
}
-->
# Somo la 2 Maendeleo ya Wakala

Karibu kwenye somo la pili la "Kujenga Wakala wa AI kutoka Mwanzo hadi Uzalishaji"!

Katika somo hili tutashughulikia:

- Zana za Kuunda Wakala wetu wa AI
  
- Maelekezo ya Usanidi kwa Rasilimali zetu za Maendeleo

- Misingi Bora ya Maendeleo ya Wakala wa AI
  
- Mwongozo wa Msimbo wa Kuunda Wakala wetu wa AI
  
Tuanze kwa kuangalia zana tutakazotumia kuunda Wakala wetu wa AI.

## Zana na Maelekezo ya Usanidi

### Microsoft Foundry

Kwa kupata Ufikiaji wa Mifano Mikubwa ya Lugha (LLMs) tutatumia [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Kuna gharama zinazohusiana na matumizi ya Foundry hivyo tafadhali hakikisha kufuata maelekezo ya usanidi wa akaunti ikiwa bado huna ufikiaji.

### Mifano ya OpenAI

Mifano ya msimbo wa wakala katika kozi hii imewekwa kutumia mifano ya OpenAI kupitia [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Tumia mwongozo huu kujifunza jinsi ya kuweka mfano kwa kutumia Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Chagua mfano mmoja wa GPT-4.1 au baadaye kwa kozi hii.

### Microsoft Agent Framework

Kama ilivyoelezwa awali, tutatumia [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) kuunda na kuendesha Wakala wetu wa AI.

Ili kusanidi Microsoft Agent Framework na vifurushi vingine vinavyohitajika, tumia amri ifuatayo wakati uko kwenye saraka kuu ya mradi huu:

```bash
pip install -r requirements.txt
```

### Sanidi Vigezo vya .env

Ili kuendesha mifano ya msimbo katika kozi hii, utahitaji kuunda faili `.env` katika saraka kuu ya mradi huu.

Ili iwe rahisi, unaweza nakili faili la `.env.example` lililopo:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tangazo la Msamaha**:
Nyaraka hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kuwa tafsiri za moja kwa moja zinaweza kuwa na makosa au upungufu wa ufafanuzi. Nyaraka ya asili katika lugha yake ya asili inapaswa kuheshimiwa kama chanzo cha msingi. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutofahamu au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->