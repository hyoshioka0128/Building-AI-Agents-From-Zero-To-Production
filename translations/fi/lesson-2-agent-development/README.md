# Oppitunti 2 Agenttien kehitys

Tervetuloa "Rakennetaan AI-agentti nollasta tuotantoon" -kurssin toiseen oppituntiin!

Tässä oppitunnissa käsittelemme:

- Työkaluja AI-agenttiemme luomiseen
  
- Kehitysympäristön asetukset

- Parhaat käytännöt AI-agenttien kehitykseen
  
- Koodikävely agenttien luomiseksi
  
Aloitetaan katsomalla työkaluja, joita aiomme käyttää AI-agenttiemme luomiseen.

## Työkalut ja asennusohjeet

### Microsoft Foundry

Suurten kielimallien (LLM) käyttöä varten käytämme [Microsoft Foundrya](https://azure.microsoft.com/products/ai-foundry). Foundryn käyttöön liittyy kustannuksia, joten varmista, että seuraat tilin perustamisohjeita, jos sinulla ei vielä ole pääsyä.

### OpenAI-mallit

Kurssin agenttikoodiesimerkit on asetettu käyttämään OpenAI-malleja [Microsoft Foundryn](https://azure.microsoft.com/products/ai-foundry) kautta.

Käytä tätä opasta oppiaksesi mallin käyttöönoton Foundryn avulla: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Valitse tälle kurssille jokin GPT-5 -sarjan malli (esimerkiksi `gpt-5.1`). Vältä elinkaarensa päättäneitä malleja, kuten GPT-4o ja GPT-4.1, jotka poistuvat käytöstä vuonna 2026.

### Microsoft Agent Framework

Kuten aiemmin mainittiin, käytämme [Microsoft Agent Frameworkia](https://github.com/microsoft/agent-framework) AI-agenttiemme luomiseen ja orkestrointiin.

Tarvitset **Python 3.12 tai uudemman**. Asentaaksesi Microsoft Agent Frameworkin ja muut vaaditut paketit, aja seuraava komento tämän projektin juurihakemistossa:

```bash
pip install -r requirements.txt
```

### Todentuminen Azureen

Agentit todentuvat Microsoft Foundryyn Azure CLI -tunnuksillasi
(`AzureCliCredential`), joten sinun tulee kirjautua sisään ennen minkään esimerkin suorittamista:

```bash
az login
# Jos sinulla on useampi kuin yksi tilaus, valitse se, jossa on Foundry-projektisi:
az account set --subscription "<your-subscription-id>"
```

Varmista, että tililläsi on **Azure AI User** -rooli (tai vastaava) Foundryn
projektissa, jotta se voi kutsua mallin ja agenttien API:t.

### .env-muuttujien asetus

Kun haluat suorittaa tämän kurssin koodiesimerkit, sinun täytyy luoda `.env`-tiedosto tämän projektin juurihakemistoon. 

Helpottaaksesi voit kopioida valmiin `.env.example` -tiedoston:

```bash
cp .env.example .env
``` 

Täytä sitten ne kaksi muuttujaa, joita agentit lukevat (FoundryChatClient
poimii ne automaattisesti):

| Muuttuja | Mikä se on | Mistä sen löytää |
|----------|------------|------------------|
| `FOUNDRY_PROJECT_ENDPOINT` | Foundry-projektisi **projektin** päätepiste, joka päättyy `/api/projects/<project>` | Foundry-portaali → projektisi → **Overview** → *Endpoints* |
| `FOUNDRY_MODEL` | Agenttisi käyttämän mallin käyttöönoton nimi (esim. `gpt-5.1`) | Foundry-portaali → **Models + endpoints** |

### Luo työntekijöiden vektoritietovarasto

Yksi esimerkeistä — **Employee Search Agent** — etsii työntekijöiden hakemistoa, joka sijaitsee
Microsoft Foundryn **vektorivarastossa**. Luo se kerran ja kopioi sen tulostama ID `.env`-tiedostoosi
muuttujalla `VECTOR_STORE_ID` (ajettu juurihakemistosta, jotta se löytää `.env`-tiedoston):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### Suorita esimerkki

Jokainen agentti ajaa oman paikallisen DevUI:nsa. Esimerkiksi:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

Avaa sen jälkeen tulostettu `http://localhost:<port>`-osoite selaimessasi keskustellaksesi agentin kanssa.

## Tässä oppitunnissa esitellyt agentit

Jokainen esimerkki on itsenäinen agentti, joka on rakennettu Microsoft Agent Frameworkilla. Yhdessä ne
toteuttavat [Oppitunti 1](../lesson-1-agent-design/README.md) suunnittelemat skenaariot:

| Esimerkki | Oppitunti 1 skenaario | Käytetty työkalu | Portti |
|--------|-------------------|-----------|------|
| `employee-search-agent.py` | Skenaario 1 — Työntekijähaku | Foundryn ylläpitämä **tiedostohaku** vektorivarastossa | 8090 |
| `task-recommendation-agent.py` | Skenaario 2 — Tehtäväsuositus | **GitHub MCP** -palvelin (isännöity MCP-työkalu) | 8095 |
| `azure-learning-agent.py` | Skenaario 3 — Koodiapuri (tutkimus) | **Microsoft Learn MCP** -palvelin (isännöity MCP-työkalu) | 8092 |
| `coding-agent.py` | Skenaario 3 — Koodiapuri (koodaus) | **Code Interpreter** | 8093 |
| `learning-recommendation-agent.py` | Tukirobotti | Learn MCP + päättely | 8091 |
| `agent-orchestration.py` | Yhdistää skenaariot | Moni-agenttien **siirto**-orkestrointi | 8094 |

> **Huomio Tehtäväsuositus-agentista.** `task-recommendation-agent.py` tarvitsee
> `GITHUB_PERSONAL_ACCESS_TOKEN` -muuttujan `.env`-tiedostossasi (luo token osoitteessa
> <https://github.com/settings/personal-access-tokens/new>). Se lukee kehittäjän viimeisimmän
> GitHub-toiminnan ja suosittelee 1–3 avoinna olevaa issuea, jotka vastaavat - juuri Oppitunti 2:n suunnitelmaa.
> Tämä on ainoa esimerkki, joka kutsuu GitHubia; muut tarvitsevat vain Foundry-projektisi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->