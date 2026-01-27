<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:23:12+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "tl"
}
-->
# Lesson 2 Pagbuo ng Ahente

Maligayang pagdating sa ikalawang aralin ng "Building AI Agent from Zero to Production Course"!

Sa araling ito, tatalakayin natin ang mga sumusunod:

- Mga Kagamitan para Lumikha ng ating mga AI Ahente
  
- Mga Tagubilin sa Pagsasaayos para sa ating mga Pinagkukunan ng Pag-unlad

- Mga Pinakamahusay na Gawi sa Pagbuo ng AI Ahente
  
- Pagsusuri ng Kodigo para sa Paglikha ng ating mga AI Ahente
  
Sisimulan natin sa pagtingin sa mga kagamitan na gagamitin natin para likhain ang ating mga AI Ahente.

## Mga Kagamitan at Mga Tagubilin sa Pagsasaayos

### Microsoft Foundry

Para sa access sa Malalaking Modelo ng Wika (LLMs) gagamitin natin ang [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). May mga gastos na konektado sa paggamit ng Foundry kaya pakiusap siguraduhing sundin ang mga tagubilin sa pagsasaayos ng account kung wala ka pang access.

### Mga Modelo ng OpenAI

Ang mga halimbawa ng kodigo para sa ahente sa kursong ito ay nakaayos upang gamitin ang mga modelo ng OpenAI sa pamamagitan ng [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Gamitin ang gabay na ito upang matutunan kung paano mag-deploy ng modelo gamit ang Foundry: [I-deploy ang Microsoft Foundry Models sa Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Pumili ng isang GPT-4.1 o mas mataas pang modelo para sa kursong ito.

### Microsoft Agent Framework

Tulad ng nabanggit kanina, gagamit tayo ng [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) para parehong likhain at ayusin ang ating mga AI Ahente.

Para i-install ang Microsoft Agent Framework at iba pang kinakailangang mga package, patakbuhin ang sumusunod na utos habang nasa root directory ng proyektong ito:

```bash
pip install -r requirements.txt
```

### Pagsasaayos ng Mga .env Variables

Para patakbuhin ang mga halimbawa ng kodigo sa kursong ito, kakailanganin mong gumawa ng `.env` na file sa root directory ng proyektong ito.

Para mapadali, maaari mong kopyahin ang ibinigay na `.env.example` na file:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI na pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat aming pinagsisikapang maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga kamalian o kapabayaan. Ang orihinal na dokumento sa orihinal na wika nito ang dapat ituring na pangunahing pinagkukunan. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o mali-maling pag-unawa na nagmumula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->