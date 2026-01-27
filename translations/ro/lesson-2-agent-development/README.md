<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:26:39+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "ro"
}
-->
# Lecția 2 Dezvoltarea Agenților

Bine ați venit la a doua lecție din cursul "Construirea unui Agent AI de la Zero la Producție"!

În această lecție vom acoperi:

- Instrumentele pentru Crearea Agenților noștri AI
  
- Instrucțiunile de Configurare pentru Resursele noastre de Dezvoltare

- Cele Mai Bune Practici în Dezvoltarea Agenților AI
  
- Parcurgerea Codului pentru Crearea Agenților noștri AI
  
Să începem prin a vedea instrumentele pe care le vom folosi pentru a crea Agenții noștri AI.

## Instrumente și Instrucțiuni de Configurare

### Microsoft Foundry

Pentru acces la Modele Mari de Limbaj (LLM) vom folosi [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Există costuri asociate utilizării Foundry, așa că vă rugăm să urmați instrucțiunile pentru configurarea contului dacă nu aveți deja acces.

### Modele OpenAI

Exemplele de cod pentru agenți din acest curs sunt configurate să folosească modelele OpenAI prin [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Folosiți acest ghid pentru a învăța cum să implementați un model folosind Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Alegeți un model GPT-4.1 sau mai recent pentru acest curs.

### Microsoft Agent Framework

După cum am menționat anterior, vom folosi [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) atât pentru a crea, cât și pentru a orchestra Agenții noștri AI.

Pentru a instala Microsoft Agent Framework și alte pachete necesare, rulați comanda următoare din directorul rădăcină al acestui proiect:

```bash
pip install -r requirements.txt
```

### Configurarea Variabilelor .env

Pentru a rula exemplele de cod din acest curs, va trebui să creați un fișier `.env` în directorul rădăcină al acestui proiect.

Pentru a vă ușura sarcina, puteți copia fișierul `.env.example` furnizat:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus utilizând serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot rezulta din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->