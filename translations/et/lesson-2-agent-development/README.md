# 2. õppetund Agendi arendamine

Tere tulemast "AI-agendi loomine nullist tootmisesse" kursuse teise õppetunni juurde!

Selles õppetunnis käsitleme:

- Vahendid meie AI-agentide loomiseks
  
- Seadistamise juhised meie arendusressursside jaoks

- Parimad tavad AI-agentide arendamiseks
  
- Koodi läbilugemine meie AI-agentide loomiseks
  
Alustame vahenditest, mida kasutame oma AI-agentide loomiseks.

## Vahendid ja seadistamise juhised

### Microsoft Foundry

Suurte keelemudelite (LLM) kasutamiseks kasutame [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Foundry kasutamisel kaasnevad kulud, seega veenduge, et järgiksite konto seadistamise juhiseid, kui teil pole juba juurdepääsu.

### OpenAI mudelid

Selle kursuse agendi koodinäited on seadistatud kasutama OpenAI mudeleid läbi [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Kasutage seda juhendit, et õppida, kuidas mudelit Foundry abil juurutada: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Valige selle kursuse jaoks üks GPT-4.1 või uuem mudel.

### Microsoft Agent Framework

Nagu varem mainitud, kasutame AI-agentide loomiseks ja orkestreerimiseks [Microsoft Agent Framework'i](https://github.com/microsoft/agent-framework).

Microsoft Agent Framework'i ja teiste vajalike pakettide installimiseks käivitage järgmine käsk projekti juurkataloogis:

```bash
pip install -r requirements.txt
```

### .env muutujate seadistamine

Selle kursuse koodinäidete käivitamiseks peate looma `.env` faili selle projekti juurkataloogis.

Selle lihtsustamiseks võite kopeerida antud `.env.example` faili:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest vabastamine**:
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüdleme täpsuse poole, palun arvestage, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste ega väärtõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->