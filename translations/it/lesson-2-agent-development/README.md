# Lezione 2 Sviluppo Agenti

Benvenuti alla seconda lezione del corso "Costruire un Agente AI da Zero alla Produzione"!

In questa lezione tratteremo:

- Gli Strumenti per Creare i nostri Agenti AI
  
- Istruzioni di Configurazione per le nostre Risorse di Sviluppo

- Best Practice per lo Sviluppo di Agenti AI
  
- Panoramica del Codice per la Creazione dei nostri Agenti AI
  
Iniziamo guardando gli strumenti che useremo per creare i nostri Agenti AI.

## Strumenti e Istruzioni di Configurazione

### Microsoft Foundry

Per accedere ai Large Language Models (LLM) useremo [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Ci sono costi associati all'uso di Foundry, quindi assicurati di seguire le istruzioni per la configurazione dell'account se non hai ancora accesso.

### Modelli OpenAI

Gli esempi di codice degli agenti in questo corso sono configurati per usare modelli OpenAI tramite [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Usa questa guida per imparare come distribuire un modello usando Foundry: [Distribuire modelli Microsoft Foundry nel portale Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Scegli un modello GPT-4.1 o successivo per questo corso.

### Microsoft Agent Framework

Come menzionato in precedenza, useremo il [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) sia per creare che per orchestrare i nostri Agenti AI.

Per installare il Microsoft Agent Framework e altri pacchetti richiesti, esegui il seguente comando mentre ti trovi nella directory principale di questo progetto:

```bash
pip install -r requirements.txt
```

### Configurazione Variabili .env

Per eseguire gli esempi di codice in questo corso, dovrai creare un file `.env` nella directory principale di questo progetto.

Per semplificarti la cosa, puoi copiare il file `.env.example` fornito:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, è consigliata una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->