# AGENTS.md

Gairės AI programavimo agentams (ir žmogaus prisidėjėjams), dirbantiems šiame saugykloje. Jei esate
automatizuotas agentas, kuris čia daro pakeitimus, pirmiausia perskaitykite šį failą ir jo laikykitės.

## Kas yra ši saugykla

**AI agentų kūrimas nuo nulio iki gamybos** yra Microsoft mokymo kursas. Jis moko kūrėjus
projektuoti, kurti, vertinti, diegti ir valdyti AI agentus **Microsoft Foundry** naudojant
**Microsoft Agent Framework (MAF)**. Turinys pateiktas kaip pamokų seka, kiekviena turi
`README.md` ir paleidžiamus Python pavyzdžius.

```
lesson-1-agent-design/            Use case + how to design effective agents
lesson-2-agent-development/       Build specialised agents with MAF (multiple runnable samples)
lesson-3-agent-evals/             Evaluations and observability
lesson-4-agentdeployment/         Deploy a hosted agent + OpenAI ChatKit front end
lesson-5-hosted-agents-production/ Hosted Agents vs Capability Hosts, BYO storage, governance
lesson-6-toolbox/                 Microsoft Toolbox: define + govern tools centrally
lesson-7-multi-agent-a2a/         Multi-agent orchestration over the A2A protocol
```

Šakninių dokumentų rinkinys: `README.md` (pradžiai), `MIGRATION-GUIDE.md` (SDK migracijos detalės), `CHANGELOG.md`.

## Aukso taisyklės

1. **Niekada neįsipareigokite slaptų duomenų.** Stebimi tik `*.env.example` failai; tikri `.env` failai
   yra įtraukti į git ignore sąrašą. Neskelbkite galutinių taškų, raktų, žetonų ar prisijungimo
   grandinių pavyzdžiuose ar dokumentacijoje.
2. **Neliesti `translations/` ar `translated_images/`.** Jie generuojami automatiškai per
   GitHub veiksmo vertimą. Nekurkite rankinių redagavimų; atlikite pakeitimus tik aukščiausio lygio pamokų failuose.
3. **Be pasenusių modelių.** Naudokite **`gpt-5.1`** pokalbiams / vertinimui ir **`gpt-5-codex`** programavimui.
   Nenaudokite `gpt-4o`, `gpt-4.1` ar jokių pasitraukusių modelių, taip pat nenaudokite *GitHub Modelių*
   (nutraukiamų 2026 m. liepos 30 d.) – visi modeliai aptarnaujami per Microsoft Foundry.
4. **Naudokite dabartinę SDK sąsają.** Pavyzdžiai taikomi `agent-framework` (užrakinamas `requirements.txt`)
   su `FoundryChatClient` ir **Atsakymų API**. Nereikia naudoti senesnių
   `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` šablonų.
5. **Laikykitės dabartinės terminologijos**: *Microsoft Foundry* (ne "Azure AI Foundry"), *Microsoft Agent
   Framework*, *Hostinami agentai*, *Gebėjimų šeimininkai*, *Microsoft Toolbox*, *MCP / Hostinamas MCP*, *A2A*.

## Diegimas

```bash
python -m venv .venv
# Windows:  .venv\Scripts\Activate.ps1
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt

az login                     # pavyzdžiai prisijungia su jūsų kūrėjo tapatybe
cp .env.example .env         # tada įrašykite savo Foundry projekto galinį tašką + modelį
```

Reikalavimai: **Python 3.12+**, **Azure CLI** ir prieiga prie **Microsoft Foundry** projekto
su įdiegtu GPT-5 serijos modeliu. Kiekvienos pamokos README nurodo savo reikalavimus ir
reikalingus aplinkos kintamuosius (žr. pamokos lygmens `.env.example`, jei yra).

## Pavyzdžių paleidimas

Dauguma antros pamokos pavyzdžių paleidžia vietinį **DevUI** prievade (pvz., 8090–8096); A2A
serveris septintoje pamokoje klausosi prievade 9000. Patikrinkite kiekvieno pavyzdžio dokumentaciją/README dėl tikslios
komandos ir prievado. Kadangi pavyzdžiai kreipiasi į gyvus Foundry galutinius taškus, jiems reikalinga galiojanti `.env` ir `az login`.

## Pakeitimų tikrinimas

Unit testų nėra; tikrinimas yra statinis + gyvas:

- **Statinis saugiklis (privalomas prieš commit):** byte-kompiliuoti kiekvieną pavyzdį.
  ```bash
  python -m py_compile $(git ls-files '*.py')
  ```
  Windows PowerShell:
  ```powershell
  git ls-files '*.py' | ForEach-Object { python -m py_compile $_ }
  ```
- **Markdown nuorodos:** CI užduotis `static` vykdo `markdown-link-check`
  (konfigūracija: `.github/workflows/markdown-link-check-config.json`). Patikrinti, ar visos naujos išorinės nuorodos
  yra pasiekiamos (HTTP 200).
- **Dūmų testas:** `.github/workflows/smoke-test-hosted-agent.yml` paleidžia AI dūmų testo veiksmą
  prieš įdiegtą hostinamą agentą (`workflow_dispatch`, OIDC). Gyvi agentai reikalauja Azure prieigos.

CI (`static` užduotis) automatiškai aptinka `.py` failus, todėl nauji pavyzdžiai yra įtraukti be darbo srauto redagavimo. Nekomituokite kodo, kuris nepraeina `py_compile`.


## Commit'o konvencijos

- Rašykite aiškius, tikslinius_commitus, turinčius imperatyvius pranešimus.
- Pridėkite ko-autoriaus antraštę prie commitų, padarytų su agentų pagalba:
  ```
  Co-authored-by: Copilot App <223556219+Copilot@users.noreply.github.com>
  ```
- Nekomituokite sugeneruotų kešų, virtualių aplinkų ar `.env` failų (visi yra git ignoruojami).

## Kur daryti konkrečius pakeitimus

| Pakeitimas | Vieta |
|--------|----------|
| Kurso pasakojimas / pamokos tekstas | `lesson-*/README.md` (tik šaltinis — niekada `translations/`) |
| Paleidžiamas kodas | `lesson-*/**.py`, `setup_vector_store.py` |
| Priklausomybės | `requirements.txt` (laikyti versijas užrakintas) |
| Aplinkos kintamųjų dokumentacija | `.env.example`, pamokos lygmens `.env.example` |
| CI / statinis saugiklis | `.github/workflows/` |
| Kurso įgūdžiai AI asistentams | `.github/skills/` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->