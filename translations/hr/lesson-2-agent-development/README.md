<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:28:36+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "hr"
}
-->
# Lekcija 2 Razvoj agenta

Dobrodošli u drugu lekciju tečaja "Izgradnja AI agenta od nule do produkcije"!

U ovoj ćemo lekciji obraditi:

- Alate za stvaranje naših AI agenata
  
- Upute za postavljanje naših razvojnih resursa

- Najbolje prakse za razvoj AI agenata
  
- Pregled koda za izradu naših AI agenata
  
Započet ćemo pregledom alata koje ćemo koristiti za stvaranje naših AI agenata.

## Alati i upute za postavljanje

### Microsoft Foundry

Za pristup velikim jezičnim modelima (LLM) koristit ćemo [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Korištenje Foundryja je povezano s troškovima, stoga molimo da slijedite upute za postavljanje računa ako već nemate pristup.

### OpenAI modeli

Primjere koda agenata u ovom tečaju postavili smo da koriste OpenAI modele preko [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Koristite ovaj vodič da naučite kako implementirati model koristeći Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Za ovaj tečaj odaberite jedan model GPT-4.1 ili noviji.

### Microsoft Agent Framework

Kao što je ranije spomenuto, koristit ćemo [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) za izradu i orkestraciju naših AI agenata.

Za instalaciju Microsoft Agent Frameworka i drugih potrebnih paketa, pokrenite sljedeću naredbu dok ste u korijenskom direktoriju ovog projekta:

```bash
pip install -r requirements.txt
```

### Postavljanje .env varijabli

Za pokretanje primjera koda u ovom tečaju, potrebno je kreirati `.env` datoteku u korijenskom direktoriju ovog projekta.

Da biste olakšali, možete kopirati priloženu `.env.example` datoteku:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Izjava o odricanju od odgovornosti**:
Ovaj dokument preveden je pomoću AI usluge za prijevod [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba se smatrati autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->