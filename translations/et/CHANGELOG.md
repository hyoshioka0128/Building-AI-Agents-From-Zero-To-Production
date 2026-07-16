# Muudatuste logi

Kõik olulised muudatused kursuses **Building AI Agents from Zero to Production** on siin dokumenteeritud.

Vorming põhineb lehel [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
See kursus on elav õppekava, mitte versioonitud tarkvarapakett, seega on sissekanded rühmitatud
vastavalt kuupäevale, millal muudatused kasutusele võeti, mitte semantilise versiooninumbri alusel.

## 13. juuli 2026

### Lisatud
- **Repositooriumi hügieen avalikuks jagamiseks** — tugevdatud `.gitignore` koos pühendatud
  Python / märkmikud / saladused / OS sektsiooniga (env-faili variandid, `.pytest_cache/`, `.mypy_cache/`,
  `.ruff_cache/`, `.ipynb_checkpoints/`, `*.egg-info/`), säilitades kõiki jälgitavaid `*.env.example`
  faile. Lisatud see `CHANGELOG.md`, `AGENTS.md` panustaja/agentide juhend ning kursuse oskuste failid.


- Repositoorium valmistatud avalikuks jagamiseks: isiku- ja elukeskkonna identifikaatorid
  (konto, projekti, ressurdivaliku ja identiteedinimed) eemaldatud avaldatud dokumentidest ning sisemine
  moderniseerimise/lüli-analüüsi aruanne eemaldatud repositooriumist (õppijale suunatud kokkuvõte elab
  selles muudatuste logis).




**Microsoft Foundry 2026** platvormiga. Koodi tasandi migratsiooni üksikasjad leiad `MIGRATION-GUIDE.md` failist.


- **Õppetund 5 – tootmises hostitud agendid** (`lesson-5-hosted-agents-production/`): Hostitud agentide vs
  võimekuste hostide võrdlus, bring-your-own Cosmos DB / Storage / AI Search, mälu- ja lõimede püsivus,
  hostitud MCP heakskiidu töövood ning haldusnimekiri.
- **Õppetund 6 – Microsofti tööriistakast** (`lesson-6-toolbox/`): defineeri tööriistad korra ja halda neid
  tsentraalselt, pluss käivitatav tarbimisnäide (`toolbox_agent.py`), mis jõuab tööriistakasti
  ühe MCP lõpp-punkti kaudu.
- **Õppetund 7 – mitmeagendi ja A2A** (`lesson-7-multi-agent-a2a/`): eksponeeri agent avatud
  Agent-agent-le (A2A) protokolli kaudu (`a2a_server.py`) ja tarbi eemalolevat agenti kui eakaaslast
  (`a2a_client.py`). Kontrollitud reaalajas lõpust lõpuni.
- **Ülesande soovitamise agent** (`lesson-2-agent-development/task-recommendation-agent.py`):
  rakendab õppetunni 1 stsenaariumit 2 kasutades GitHubi eemalolevat MCP serverit tööriistana.
- **Vektorpoe seadistusskript** (`setup_vector_store.py`): loob ja täidab vektorpoe,
  millele tugineb töötajate otsimise agent (varem viidatud, kuid puuduv).
- **CI suitsu- ja staatiline värav** (`.github/workflows/smoke-test-hosted-agent.yml`): `static` töö
  kontrollib `py_compile` ja markdown-link-checki iga PR-/push-i puhul; `smoke` töö
  käivitab AI suitsutesti toimingu jõustatud hostitud agendi vastu (OIDC, `workflow_dispatch`).
- **Eeltingimused ja seadistuse juhised** lisatud igale õppetunnile ning juurfaile README-sse
  (Python 3.12+, `az login`, mudeleid käsitlevad juhised, kulud ja koristus).
- **Uus lipulaeva dokument**: `MIGRATION-GUIDE.md`.


- **Brändimuudatus**: *Azure AI Foundry* → **Microsoft Foundry** kogu kursuse ulatuses.
- **SDK migratsioon** viimasele Microsoft Agent Framework pinnale — näited kasutavad nüüd
  `agent-framework` versiooni `1.2.0` koos `FoundryChatClient` ja **Responses API**-ga,
  asendades varasema `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` mustri.
- **Kinnitatud sõltuvused**: `requirements.txt` kinnitab nüüd `agent-framework`, `agent-framework-foundry`
  ja seotud paketid, selle asemel et installida kinnitamata eelversioone, mis muudab näited reprodutseeritavaks.
- **Keskkonnamuutujad** viidud kooskõlla `deploy.py`, `agent.yaml`, `main.py` ja
  `.env.example` failidega.
- README arhitektuuridiagrammid ning agentide/stsenaariumide kataloog on ümber kirjutatud,
  et vastata tarnitud koodile.

### Parandatud
- Parandatud katkine juur-README link õppetundi 4 (`lesson-4-agentdeployment`).
- Kirjutatud varem tühi õppetunni 3 README (hinnangud ja vaatlusvõimalused).
- Asendatud vananenud `asyncio.get_event_loop().run_until_complete` muster
  õppimise soovitamise agendi puhul.

### Vana / eemaldatud
- Kõik kasutused pensionile läinud **GPT-4o / GPT-4.1** mudelitest eemaldatud. Vestlus- ja hindamisnäited kasutavad nüüd
  **gpt-5.1**; kodeerimisnäited kasutavad **gpt-5-codex**.
- Dokumenteeritud, et **GitHub Models** pensionile läheb (30. juuli 2026); kursus kasutab kõiki mudeleid
  Microsoft Foundry kaudu ega sõltu GitHub Models-ist.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->