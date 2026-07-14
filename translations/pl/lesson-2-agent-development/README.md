# Lekcja 2 Tworzenie Agenta

Witamy w drugiej lekcji kursu "Budowanie Agenta AI od Zera do Produkcji"!

W tej lekcji omówimy:

- Narzędzia do tworzenia naszych Agentów AI
  
- Instrukcje konfiguracji dla naszych zasobów deweloperskich

- Najlepsze praktyki tworzenia Agentów AI
  
- Przegląd kodu do tworzenia naszych Agentów AI
  
Zacznijmy od przyjrzenia się narzędziom, których użyjemy do tworzenia naszych Agentów AI.

## Narzędzia i instrukcje konfiguracji

### Microsoft Foundry

Do dostępu do dużych modeli językowych (LLM) będziemy używać [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Korzystanie z Foundry wiąże się z kosztami, więc upewnij się, że postępujesz zgodnie z instrukcjami konfiguracji konta, jeśli jeszcze nie masz dostępu.

### Modele OpenAI

Przykłady kodu agentów w tym kursie są skonfigurowane do używania modeli OpenAI za pomocą [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Skorzystaj z tego przewodnika, aby dowiedzieć się, jak wdrożyć model za pomocą Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Wybierz jeden model z serii GPT-5 (na przykład `gpt-5.1`) do tego kursu. Unikaj wycofanych modeli takich jak GPT-4o i GPT-4.1, które osiągną koniec życia w 2026 roku.

### Microsoft Agent Framework

Jak wcześniej wspomniano, będziemy używać [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) do tworzenia i orkiestracji naszych Agentów AI.

Będziesz potrzebować **Pythona 3.12 lub nowszego**. Aby zainstalować Microsoft Agent Framework oraz inne wymagane pakiety, uruchom następujące polecenie w katalogu głównym tego projektu:

```bash
pip install -r requirements.txt
```

### Uwierzytelnianie w Azure

Agenci uwierzytelniają się do Microsoft Foundry przy użyciu Twoich danych logowania Azure CLI
(`AzureCliCredential`), więc musisz się zalogować przed uruchomieniem jakiegokolwiek przykładu:

```bash
az login
# Jeśli masz więcej niż jedną subskrypcję, wybierz tę z Twoim projektem Foundry:
az account set --subscription "<your-subscription-id>"
```

Upewnij się, że Twoje konto ma rolę **Azure AI User** (lub równoważną) w projekcie Foundry,
aby można było wywoływać API modelu i agenta.

### Konfiguracja zmiennych .env

Aby uruchomić przykładowy kod w tym kursie, musisz utworzyć plik `.env` w katalogu głównym tego projektu.

Aby było łatwiej, możesz skopiować dostarczony plik `.env.example`:

```bash
cp .env.example .env
``` 

Następnie uzupełnij dwie zmienne, które odczytują agenci (klient `FoundryChatClient` pobiera je
automatycznie):

| Zmienna | Co to jest | Gdzie znaleźć |
|----------|------------|------------------|
| `FOUNDRY_PROJECT_ENDPOINT` | Punkt końcowy Twojego projektu Foundry, kończący się na `/api/projects/<projekt>` | Portal Foundry → Twój projekt → **Przegląd** → *Punkty końcowe* |
| `FOUNDRY_MODEL` | Nazwa wdrożenia modelu, na którym działają Twoi agenci (np. `gpt-5.1`) | Portal Foundry → **Modele + punkty końcowe** |

### Utwórz wektorowy magazyn pracowników

Jeden z przykładów — **Agent Wyszukiwania Pracowników** — przeszukuje katalog pracowników przechowywany w
Microsoft Foundry **wektorowym magazynie**. Utwórz go raz i skopiuj wygenerowane ID do swojego pliku `.env`
jako `VECTOR_STORE_ID` (uruchom z katalogu głównego repozytorium, aby odczytał Twoje `.env`):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### Uruchom przykład

Każdy agent uruchamia swój własny lokalny DevUI. Na przykład:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

Następnie otwórz wyświetlony adres `http://localhost:<port>` w przeglądarce, aby porozmawiać z agentem.

## Agenci w tej lekcji

Każdy przykład to samodzielny agent zbudowany przy użyciu Microsoft Agent Framework. Razem
implementują scenariusze, które zaprojektowałeś w [Lekcji 1](../lesson-1-agent-design/README.md):

| Przykład | Scenariusz z Lekcji 1 | Użyte narzędzie | Port |
|--------|-------------------|-----------|------|
| `employee-search-agent.py` | Scenariusz 1 — Wyszukiwanie pracowników | Wyszukiwanie plików hostowane przez Foundry na wektorowym magazynie | 8090 |
| `task-recommendation-agent.py` | Scenariusz 2 — Rekomendacja zadań | Serwer **GitHub MCP** (hostowane narzędzie MCP) | 8095 |
| `azure-learning-agent.py` | Scenariusz 3 — Asystent kodu (badania) | Serwer **Microsoft Learn MCP** (hostowane narzędzie MCP) | 8092 |
| `coding-agent.py` | Scenariusz 3 — Asystent kodu (kodowanie) | **Code Interpreter** | 8093 |
| `learning-recommendation-agent.py` | Agent wspierający | Learn MCP + rozumowanie | 8091 |
| `agent-orchestration.py` | Łączy scenariusze razem | Wieloagentowa orkiestracja **przekazania** | 8094 |

> **Uwaga dotycząca Agenta Rekomendacji Zadań.** `task-recommendation-agent.py` wymaga
> `GITHUB_PERSONAL_ACCESS_TOKEN` w pliku `.env` (utwórz token na
> <https://github.com/settings/personal-access-tokens/new>). Odczytuje on ostatnią aktywność dewelopera
> na GitHub i rekomenduje 1–3 otwarte problemy pasujące do scenariusza 2 — dokładnie jak zaprojektowano.
> To jest jedyny przykład korzystający z GitHub; pozostałe wymagają tylko Twojego projektu Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->