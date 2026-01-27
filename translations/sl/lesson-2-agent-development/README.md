<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:28:57+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "sl"
}
-->
# Lekcija 2 Razvoj Agenta

Dobrodošli v drugi lekciji tečaja "Ustvarjanje AI agentov od nič do produkcije"!

V tej lekciji bomo obravnavali:

- Orodja za ustvarjanje naših AI agentov
  
- Navodila za nastavitev naših razvojnih virov

- Najboljše prakse za razvoj AI agentov
  
- Pregled kode za ustvarjanje naših AI agentov
  
Začnimo z ogledom orodij, ki jih bomo uporabljali za ustvarjanje naših AI agentov.

## Orodja in navodila za nastavitev

### Microsoft Foundry

Za dostop do velikih jezikovnih modelov (LLM) bomo uporabljali [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Uporaba Foundry je povezana s stroški, zato prosimo, da dosledno sledite navodilom za nastavitev računa, če še nimate dostopa.

### OpenAI modeli

Vzorec kode agentov v tem tečaju je nastavljen za uporabo OpenAI modelov prek [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Za uporabo poglejte vodič za nameščanje modela s pomočjo Foundry: [Nameščanje Microsoft Foundry modelov v portalu Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Za ta tečaj izberite en model GPT-4.1 ali novejši.

### Microsoft Agent Framework

Kot je bilo omenjeno prej, bomo uporabljali [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) za ustvarjanje in usklajevanje naših AI agentov.

Za namestitev Microsoft Agent Framework in drugih potrebnih paketov zaženite naslednji ukaz v korenskem imeniku tega projekta:

```bash
pip install -r requirements.txt
```

### Nastavitev spremenljivk .env

Za zagon vzorcev kode v tem tečaju boste morali ustvariti datoteko `.env` v korenskem imeniku tega projekta.

Za lažje delo lahko kopirate priloženo datoteko `.env.example`:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku naj se šteje kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->