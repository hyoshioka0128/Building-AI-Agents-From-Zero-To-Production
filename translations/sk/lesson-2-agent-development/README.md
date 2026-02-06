# Lesson 2 Vývoj agenta

Vitajte v druhej lekcii kurzu "Budovanie AI agenta od nuly po produkciu"!

V tejto lekcii si prejdeme:

- Nástroje na vytváranie našich AI agentov
  
- Inštrukcie na nastavenie našich vývojových zdrojov

- Najlepšie postupy vývoja AI agentov
  
- Prechádzku kódom pre tvorbu našich AI agentov
  
Začnime pohľadom na nástroje, ktoré budeme používať na vytváranie našich AI agentov.

## Nástroje a inštrukcie na nastavenie

### Microsoft Foundry

Pre prístup k veľkým jazykovým modelom (LLMs) budeme používať [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Používanie Foundry je spojené s nákladmi, preto sa uistite, že dodržíte inštrukcie na nastavenie účtu, ak ešte nemáte prístup.

### OpenAI modely

Vzorky kódu agentov v tomto kurze sú nastavené na používanie OpenAI modelov prostredníctvom [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Použite tento návod, aby ste sa naučili, ako nasadiť model pomocou Foundry: [Nasadenie modelov Microsoft Foundry v portáli Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Vyberte jeden model GPT-4.1 alebo novší pre tento kurz.

### Microsoft Agent Framework

Ako už bolo spomenuté, budeme používať [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) na vytváranie a orchestráciu našich AI agentov.

Na inštaláciu Microsoft Agent Framework a ďalších potrebných balíkov spustite nasledujúci príkaz, keď ste v hlavnom adresári tohto projektu:

```bash
pip install -r requirements.txt
```

### Nastavenie premenných .env

Na spustenie ukážkového kódu v tomto kurze budete musieť vytvoriť súbor `.env` v hlavnom adresári tohto projektu.

Pre zjednodušenie môžete skopírovať poskytnutý súbor `.env.example`:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o odmietnutí zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, berte prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->