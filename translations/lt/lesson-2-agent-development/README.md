# Pamoka 2 Agentų Kūrimas

Sveiki atvykę į antrąją „Dirbtinio intelekto agentų kūrimas nuo nulio iki gamybos“ kurso pamoką!

Šioje pamokoje aptarsime:

- Įrankius, skirtus kurti mūsų DI agentams
  
- Nustatymo instrukcijas mūsų kūrimo ištekliams

- Geriausias DI agentų kūrimo praktikas
  
- Kodo peržiūrą, kaip kurti mūsų DI agentus
  
Pradėkime nuo įrankių, kuriuos naudosime kurdami DI agentus, apžvalgos.

## Įrankiai ir Nustatymo Instrukcijos

### Microsoft Foundry

Norėdami gauti prieigą prie didelio masto kalbos modelių (LLM), naudosime [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Foundry naudojimas yra mokamas, todėl įsitikinkite, kad sekate paskyros nustatymo instrukcijas, jei dar neturite prieigos.

### OpenAI Modeliai

Šio kurso agentų kodo pavyzdžiai sukonfigūruoti naudoti OpenAI modelius per [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Naudokite šią gidą, kad sužinotumėte, kaip diegti modelį naudodami Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Šiam kursui pasirinkite vieną GPT-4.1 ar naujesnį modelį.

### Microsoft Agent Framework

Kaip minėta anksčiau, naudosime [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), kad sukurtume ir koordinuotume mūsų DI agentus.

Norėdami įdiegti Microsoft Agent Framework ir kitas reikiamas paketas, vykdykite šią komandą būdami pagrindiniame šio projekto kataloge:

```bash
pip install -r requirements.txt
```

### .env Kintamųjų Nustatymas

Norėdami paleisti šio kurso kodo pavyzdžius, turite sukurti `.env` failą pagrindiniame šio projekto kataloge.

Kad tai būtų paprasčiau, galite nukopijuoti pateiktą `.env.example` failą:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, atkreipkite dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus atliktas vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus interpretavimus, kilusius naudojant šį vertimą.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->