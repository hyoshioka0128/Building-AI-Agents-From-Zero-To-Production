# Lekcja 2 Tworzenie Agenta

Witamy w drugiej lekcji kursu „Budowanie Agenta AI od Zera do Produkcji”!

W tej lekcji omówimy:

- Narzędzia do tworzenia naszych Agentów AI
  
- Instrukcje konfiguracji naszych zasobów deweloperskich

- Najlepsze praktyki tworzenia Agentów AI
  
- Przegląd kodu tworzącego naszych Agentów AI
  
Zacznijmy od przyjrzenia się narzędziom, które wykorzystamy do tworzenia naszych Agentów AI.

## Narzędzia i Instrukcje Konfiguracji

### Microsoft Foundry

Aby uzyskać dostęp do dużych modeli językowych (LLM), będziemy korzystać z [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Korzystanie z Foundry wiąże się z kosztami, więc prosimy o dokładne zapoznanie się z instrukcjami dotyczącymi konfiguracji konta, jeśli jeszcze nie masz dostępu.

### Modele OpenAI

Przykładowe kody agentów w tym kursie są skonfigurowane do korzystania z modeli OpenAI za pośrednictwem [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Skorzystaj z tego przewodnika, aby dowiedzieć się, jak wdrożyć model za pomocą Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Wybierz jeden model GPT-4.1 lub nowszy do tego kursu.

### Microsoft Agent Framework

Jak wspomniano wcześniej, będziemy korzystać z [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) do tworzenia i orkiestracji naszych Agentów AI.

Aby zainstalować Microsoft Agent Framework oraz inne wymagane pakiety, uruchom następującą komendę będąc w katalogu głównym tego projektu:

```bash
pip install -r requirements.txt
```

### Konfiguracja Zmiennych .env

Aby uruchomić przykładowe kody w tym kursie, będziesz musiał utworzyć plik `.env` w katalogu głównym tego projektu.

Aby to ułatwić, możesz skopiować dostarczony plik `.env.example`:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najdokładniejsze, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako wiarygodne źródło. W przypadku informacji o krytycznym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->