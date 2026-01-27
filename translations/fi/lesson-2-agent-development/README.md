<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:19:34+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "fi"
}
-->
# Oppitunti 2 Agentin kehitys

Tervetuloa "Rakentamassa tekoälyagenttia alusta tuotantoon -kurssin" toiseen oppituntiin!

Tässä oppitunnissa käsittelemme:

- Työkalut tekoälyagenttiemme luomiseen

- Kehitysresurssiemme käyttöönotto-ohjeet

- Tekoälyagenttien kehittämisen parhaat käytännöt

- Koodikierros tekoälyagenttiemme luomiseksi

Aloitetaan katsomalla työkaluja, joita käytämme tekoälyagenttiemme luomiseen.

## Työkalut ja käyttöönotto-ohjeet

### Microsoft Foundry

Suuriin kielimalleihin (LLM) pääsyä varten käytämme [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Foundryn käytöstä aiheutuu kustannuksia, joten varmista, että noudatat tilin käyttöönotto-ohjeita, jos sinulla ei vielä ole käyttöoikeutta.

### OpenAI-mallit

Tämän kurssin agenttikoodiesimerkit on asetettu käyttämään OpenAI-malleja [Microsoft Foundryn](https://azure.microsoft.com/products/ai-foundry) kautta.

Käytä tätä opasta oppiaksesi, miten malli otetaan käyttöön Foundryn avulla: [Ota Microsoft Foundry -mallit käyttöön Foundry-portaalissa](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Valitse kurssia varten joko GPT-4.1 tai uudempi malli.

### Microsoft Agent Framework

Kuten aiemmin mainittiin, käytämme [Microsoft Agent Frameworkia](https://github.com/microsoft/agent-framework) tekoälyagenttiemme luomiseen ja orkestrointiin.

Asentaaksesi Microsoft Agent Frameworkin ja muut tarvittavat paketit, suorita seuraava komento projektin juurikansiossa:

```bash
pip install -r requirements.txt
```

### .env-muuttujien asetukset

Jotta voit suorittaa tämän kurssin koodiesimerkit, sinun tulee luoda `.env`-tiedosto projektin juurikansioon.

Helpottaaksesi voit kopioida valmiin `.env.example`-tiedoston:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttäen tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automatisoidut käännökset voivat sisältää virheitä tai epäjohdonmukaisuuksia. Alkuperäinen asiakirja sen omalla kielellä on pidettävä auktoritatiivisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä mahdollisesti aiheutuvista väärinymmärryksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->