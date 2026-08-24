# 2 pamoka Agentų kūrimas

Sveiki atvykę į antrąją „AI agentų kūrimo nuo nulio iki gamybos“ kurso pamoką!

Šioje pamokoje aptarsime:

- Įrankius mūsų AI agentams kurti
  
- Vystymo išteklių nustatymo instrukcijas

- Geriausias AI agentų kūrimo praktikas
  
- Kodo peržiūrą AI agentų kūrimui
  
Pradėkime pažvelgdami į įrankius, kuriuos naudosime kurdami savo AI agentus.

## Įrankiai ir nustatymo instrukcijos

### Microsoft Foundry

Didelių kalbinių modelių (LLM) prieigai naudosime [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Naudojant Foundry yra susijusios išlaidos, todėl jei dar neturite prieigos, būtinai sekite paskyrų nustatymo instrukcijas.

### OpenAI modeliai

Šio kurso agentų kodo pavyzdžiai yra sukonfigūruoti naudoti OpenAI modelius per [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Naudokite šį vadovą, kad sužinotumėte, kaip diegti modelį naudojant Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Pasirinkite vieną GPT-5 serijos modelį (pavyzdžiui, `gpt-5.1`) šiam kursui. Venkite pasenusių modelių, tokių kaip GPT-4o ir GPT-4.1, kurių gyvavimo laikas baigsis 2026 m.

### Microsoft Agent Framework

Kaip minėta anksčiau, naudosime [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), kad sukurtume ir koordinuotume savo AI agentus.

Jums reikės **Python 3.12 arba naujesnės versijos**. Norėdami įdiegti Microsoft Agent Framework ir kitas reikiamas paketas, paleiskite šią komandą būdami šio projekto šakniniame kataloge:

```bash
pip install -r requirements.txt
```

### Autentifikacija su Azure

Agentai autentifikuojasi Microsoft Foundry naudodami jūsų Azure CLI kredencialus
(`AzureCliCredential`), todėl prieš paleisdami bet kurį pavyzdį turite prisijungti:

```bash
az login
# Jei turite daugiau nei vieną prenumeratą, pasirinkite tą, kuri yra susijusi su jūsų Foundry projektu:
az account set --subscription "<your-subscription-id>"
```

Įsitikinkite, kad jūsų paskyra turi **Azure AI User** rolę (ar lygiavertę) Foundry
projekte, kad galėtų kviesti modelio ir agentų API.

### .env kintamųjų nustatymas

Norėdami paleisti šio kurso kodo pavyzdžius, turėsite sukurti `.env` failą projekto šakniniame kataloge.

Norėdami palengvinti darbą, galite nukopijuoti pateiktą `.env.example` failą:

```bash
cp .env.example .env
``` 

Tada užpildykite du kintamuosius, kuriuos skaito agentai (`FoundryChatClient` juos paima
automatiškai):

| Kintamasis | Kas tai yra | Kur rasti |
|------------|-------------|-----------|
| `FOUNDRY_PROJECT_ENDPOINT` | Jūsų Foundry **projekto** galinis taškas, baigiasi `/api/projects/<project>` | Foundry portalas → jūsų projektas → **Apžvalga** → *Galai* |
| `FOUNDRY_MODEL` | Modelio diegimo pavadinimas, kuriuo veikia jūsų agentai (pvz., `gpt-5.1`) | Foundry portalas → **Modeliai + galai** |

### Sukurkite darbuotojų vektorių saugyklą

Vienas pavyzdys – **Darbuotojų paieškos agentas** – ieško darbuotojų kataloge, saugomame
Microsoft Foundry **vektorių saugykloje**. Sukurkite ją vieną kartą ir nukopijuokite išspausdintą ID į savo `.env`
kaip `VECTOR_STORE_ID` (paleiskite iš saugyklos šaknies, kad būtų paimtas jūsų `.env`):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### Paleiskite pavyzdį

Kiekvienas agentas paleidžia savo vietinį DevUI. Pavyzdžiui:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

Tada atidarykite atspausdintą `http://localhost:<port>` URL savo naršyklėje, kad bendrautumėte su agentu.

## Šios pamokos agentai

Kiekvienas pavyzdys yra savarankiškas agentas, sukurtas naudojant Microsoft Agent Framework. Kartu jie
įgyvendina scenarijus, kuriuos sukūrėte [1 pamokoje](../lesson-1-agent-design/README.md):

| Pavyzdys | 1 pamokos scenarijus | Naudotas įrankis | Prievadas |
|--------|---------------------|------------------|----------|
| `employee-search-agent.py` | Scenarijus 1 — Darbuotojų paieška | Foundry talpinama **failų paieška** per vektorių saugyklą | 8090 |
| `task-recommendation-agent.py` | Scenarijus 2 — Užduočių rekomendacija | **GitHub MCP** serveris (talpinamas MCP įrankis) | 8095 |
| `azure-learning-agent.py` | Scenarijus 3 — Kodo asistentas (tyrimai) | **Microsoft Learn MCP** serveris (talpinamas MCP įrankis) | 8092 |
| `coding-agent.py` | Scenarijus 3 — Kodo asistentas (kodas) | **Kodo interpretatorius** | 8093 |
| `learning-recommendation-agent.py` | Pagalbinis agentas | Learn MCP + loginis ms | 8091 |
| `agent-orchestration.py` | Sujungia scenarijus | Daugiaagentė **perdavimų** koordinacija | 8094 |

> **Pastaba apie Užduočių rekomendavimo agentą.** `task-recommendation-agent.py` reikia
> `GITHUB_PERSONAL_ACCESS_TOKEN` jūsų `.env` faile (sukurkite vieną adresu
> <https://github.com/settings/personal-access-tokens/new>). Jis skaito kūrėjo neseną
> GitHub veiklą ir rekomenduoja 1–3 atvirus klausimus, kurie atitinka – būtent Scenarijų 2 dizainą.
> Tai yra vienintelis pavyzdys, kuris kviečia GitHub; kitiems reikalingas tik jūsų Foundry projektas.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->