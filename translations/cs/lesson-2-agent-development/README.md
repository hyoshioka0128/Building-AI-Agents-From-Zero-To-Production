# Lekce 2 Vývoj agentů

Vítejte v druhé lekci kurzu "Budování AI agenta od nuly do produkce"!

V této lekci pokryjeme:

- Nástroje pro vytváření našich AI agentů
  
- Instrukce pro nastavení našich vývojových zdrojů

- Nejlepší postupy pro vývoj AI agentů
  
- Procházení kódu pro vytváření našich AI agentů
  
Začněme pohledem na nástroje, které použijeme k tvorbě našich AI agentů.

## Nástroje a instrukce k nastavení

### Microsoft Foundry

Pro přístup k velkým jazykovým modelům (LLM) budeme používat [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Používání Foundry je spojeno s náklady, proto se ujistěte, že jste postupovali podle pokynů pro nastavení účtu, pokud již nemáte přístup.

### OpenAI modely

Ukázky kódu agentů v tomto kurzu jsou nastaveny pro použití OpenAI modelů přes [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Použijte tuto příručku, jak nasadit model pomocí Foundry: [Nasazení Microsoft Foundry modelů v portálu Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Pro tento kurz vyberte jeden model GPT-4.1 nebo novější.

### Microsoft Agent Framework

Jak bylo zmíněno dříve, budeme používat [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) k vytvoření i orchestraci našich AI agentů.

Pro instalaci Microsoft Agent Framework a dalších požadovaných balíčků spusťte následující příkaz v kořenovém adresáři tohoto projektu:

```bash
pip install -r requirements.txt
```

### Nastavení proměnných .env

Pro spuštění ukázek kódu v tomto kurzu budete muset vytvořit soubor `.env` v kořenovém adresáři tohoto projektu.

Pro usnadnění můžete zkopírovat poskytnutý soubor `.env.example`:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornění**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro zásadní informace se doporučuje profesionální lidský překlad. Nejsme odpovědni za jakákoliv nedorozumění nebo chybné výklady vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->