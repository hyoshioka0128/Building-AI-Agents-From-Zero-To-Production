<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:24:41+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "hu"
}
-->
# Lesson 2 Agent Development

Üdvözlünk a „Zero-tól a Termelésig AI Ügynök Készítés” tanfolyam második leckéjében!

Ebben a leckében az alábbiakat fogjuk áttekinteni:

- Az AI ügynökeink létrehozásához szükséges eszközök

- Fejlesztési erőforrásaink beállítási utasításai

- AI ügynök fejlesztési legjobb gyakorlatok

- Kód átvizsgálás az AI ügynökeink létrehozásához

Kezdjük azzal, hogy megnézzük azokat az eszközöket, amelyeket AI ügynökeink létrehozásához fogunk használni.

## Eszközök és beállítási utasítások

### Microsoft Foundry

A Nagy Nyelvi Modellekhez (LLM-ekhez) való hozzáféréshez a [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) szolgáltatást fogjuk használni. A Foundry használata költségekkel jár, ezért kérjük, hogy ha még nincs hozzáférésed, kövesd a fiókbeállítási utasításokat.

### OpenAI modellek

A tanfolyam ügynök kódmintái az OpenAI modelleket használják a [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) révén.

Használd ezt az útmutatót, hogy megtanuld, hogyan telepíts modell a Foundry használatával: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Válassz ki egy GPT-4.1 vagy újabb modellt ehhez a tanfolyamhoz.

### Microsoft Agent Framework

Ahogy korábban említettük, a [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) keretrendszert fogjuk használni AI ügynökeink létrehozásához és irányításához.

A Microsoft Agent Framework és a szükséges további csomagok telepítéséhez futtasd a következő parancsot a projekt gyökérkönyvtárában:

```bash
pip install -r requirements.txt
```

### .env változók beállítása

A tanfolyam kódmintáinak futtatásához létre kell hoznod egy `.env` fájlt a projekt gyökérkönyvtárában.

A könnyebbség kedvéért lemásolhatod a mellékelt `.env.example` fájlt:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot a [Co-op Translator](https://github.com/Azure/co-op-translator) nevű mesterséges intelligencia fordító szolgáltatás segítségével fordítottuk le. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén profi, emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->