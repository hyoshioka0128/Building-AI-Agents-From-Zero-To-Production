# AGENTS.md

Pokyny pro AI programovací agenty (a lidské přispěvatele) pracující v tomto repozitáři. Pokud jste
automatizovaný agent provádějící změny zde, přečtěte si nejprve tento soubor a dodržujte jej.

## Co je tento repozitář

**Budování AI agentů od nuly do produkce** je vzdělávací kurz Microsoftu. Učí vývojáře
navrhovat, vytvářet, hodnotit, nasazovat a provozovat AI agenty na **Microsoft Foundry** pomocí
**Microsoft Agent Framework (MAF)**. Obsah je uspořádán jako posloupnost lekcí, každá s
`README.md` a spustitelnými Python příklady.

```
lesson-1-agent-design/            Use case + how to design effective agents
lesson-2-agent-development/       Build specialised agents with MAF (multiple runnable samples)
lesson-3-agent-evals/             Evaluations and observability
lesson-4-agentdeployment/         Deploy a hosted agent + OpenAI ChatKit front end
lesson-5-hosted-agents-production/ Hosted Agents vs Capability Hosts, BYO storage, governance
lesson-6-toolbox/                 Microsoft Toolbox: define + govern tools centrally
lesson-7-multi-agent-a2a/         Multi-agent orchestration over the A2A protocol
```

Kořenová dokumentace: `README.md` (začněte zde), `MIGRATION-GUIDE.md` (podrobnosti SDK migrace), `CHANGELOG.md`.

## Zlatá pravidla

1. **Nikdy neukládejte tajné informace.** Sledovány jsou pouze soubory `*.env.example`; skutečné `.env` soubory jsou
   ignorované gitem. Nezapisujte do příkladů ani dokumentace žádné endpointy, klíče, tokeny nebo připojovací řetězce.
2. **Nedotýkejte se `translations/` nebo `translated_images/`.** Tyto jsou generovány automaticky pomocí
   GitHub Actions pro překlady. Nikdy je neupravujte ručně; provádějte změny pouze v původních souborech lekcí
   na nejvyšší úrovni.
3. **Nepoužívejte zastaralé modely.** Používejte **`gpt-5.1`** pro chat/hodnocení a **`gpt-5-codex`** pro kódování.
   Nezavádějte `gpt-4o`, `gpt-4.1` ani žádný ukončený model a nepoužívejte *GitHub Models*
   (bude ukončeno 30. července 2026) — všechny modely jsou poskytovány přes Microsoft Foundry.
4. **Používejte aktuální SDK rozhraní.** Příklady cílí na `agent-framework` (verze připnutá v `requirements.txt`)
   s `FoundryChatClient` a **Responses API**. Znovu nezavádějte starší vzory
   `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient`.
5. **Používejte aktuální terminologii**: *Microsoft Foundry* (nikoli „Azure AI Foundry“), *Microsoft Agent
   Framework*, *Hosted Agents*, *Capability Hosts*, *Microsoft Toolbox*, *MCP / Hosted MCP*, *A2A*.

## Nastavení

```bash
python -m venv .venv
# Windows:  .venv\Scripts\Activate.ps1
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt

az login                     # ukázky se autentizují pomocí vašeho vývojářského identity
cp .env.example .env         # pak vyplňte váš Foundry projektový endpoint + model
```

Požadavky: **Python 3.12+**, **Azure CLI** a přístup k **Microsoft Foundry** projektu
s nasazeným GPT-5 modelem. Každá lekce v README uvádí své předpoklady a potřebné env proměnné
(viz lekční `.env.example`, pokud je k dispozici).

## Spouštění příkladů

Většina příkladů v lekci 2 spustí místní **DevUI** na vyhrazeném portu (například 8090–8096); A2A
server v lekci 7 naslouchá na portu 9000. Podívejte se do docstringu/README každého příkladu pro přesný příkaz
a port. Protože příklady volají živé Foundry endpointy, vyžadují platný `.env` a `az login`.

## Validace změn

Neexistuje žádná sada jednotkových testů; validace je statická + živá:

- **Statická kontrola (musí projít před commitem):** byte-kompilace každého příkladu.
  ```bash
  python -m py_compile $(git ls-files '*.py')
  ```
  Ve Windows PowerShell:
  ```powershell
  git ls-files '*.py' | ForEach-Object { python -m py_compile $_ }
  ```
- **Markdown odkazy:** CI Job `static` spouští `markdown-link-check`
  (konfigurace: `.github/workflows/markdown-link-check-config.json`). Ověřte, že nové externí odkazy
  odpovídají (HTTP 200).
- **Smoke test:** `.github/workflows/smoke-test-hosted-agent.yml` spouští AI Smoke Test akci
  proti nasazenému hosted agentu (`workflow_dispatch`, OIDC). Pro běh živého agenta je potřeba přístup k Azure.

CI (`static` job) automaticky detekuje `.py` soubory, takže nové příklady jsou pokryty bez úprav
workflow. Necommitujte kód, který nezkompiluje `py_compile`.

## Zásady commitů

- Pište zaměřené commity s jasnými, příkazovými zprávami.
- Do commitů vytvořených pomocí agentů přidejte co-author trailer:
  ```
  Co-authored-by: Copilot App <223556219+Copilot@users.noreply.github.com>
  ```
- Necommitujte generované cache, virtuální prostředí ani `.env` soubory (vše git-ignorováno).

## Kde provádět konkrétní změny

| Změna | Umístění |
|--------|----------|
| Text kurzu / obsah lekce | `lesson-*/README.md` (pouze zdroj — nikdy `translations/`) |
| Spustitelný kód | `lesson-*/**.py`, `setup_vector_store.py` |
| Závislosti | `requirements.txt` (udržujte verze připnuté) |
| Dokumentace env proměnných | `.env.example`, lekční `.env.example` |
| CI / statická kontrola | `.github/workflows/` |
| Dovednosti kurzu pro AI asistenty | `.github/skills/` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->