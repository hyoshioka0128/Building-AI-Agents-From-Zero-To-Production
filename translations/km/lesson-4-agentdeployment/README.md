# មេរៀន 4: ការបញ្ចូនភ្នាក់ងារជាមួយ Azure AI Foundry Hosted Agents + ChatKit

មេរៀននេះបង្ហាញពីវិធីបញ្ចូនប្រតិបត្តិការ​មេរោគ​ពហុភ្នាក់ងារ​ទៅ Azure AI Foundry ជាភ្នាក់ងារដែល​ផ្ដល់សេវា និងបង្កើតមុខងារ ChatKit ដើម្បីអន្តរកម្មជាមួយវា។

## សំណុំរចនា

```
┌─────────────────────────────────────────────────────────────────────┐
│                         User's Browser                               │
│                    (ChatKit React Frontend)                          │
│                      localhost:3000                                  │
└───────────────────────────┬─────────────────────────────────────────┘
                            │ HTTP/SSE
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     ChatKit Backend Server                           │
│                    (FastAPI + SQLite Store)                          │
│                      localhost:8001                                  │
└───────────────────────────┬─────────────────────────────────────────┘
                            │ Azure AI Responses API
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    Azure AI Foundry                                  │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │               Hosted Multi-Agent Workflow                      │  │
│  │  ┌─────────────┐  ┌──────────────────┐  ┌───────────────┐     │  │
│  │  │   Triage    │──│ Employee Search  │  │   Learning    │     │  │
│  │  │   Agent     │  │     Agent        │  │    Agent      │     │  │
│  │  │(Coordinator)│  │ (Vector Store)   │  │ (MCP Tool)    │     │  │
│  │  └──────┬──────┘  └──────────────────┘  └───────────────┘     │  │
│  │         │         ┌──────────────────┐                         │  │
│  │         └─────────│  Coding Agent    │                         │  │
│  │                   │ (Code Generation)│                         │  │
│  │                   └──────────────────┘                         │  │
│  └───────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

## លក្ខណៈបណ្តៅ

1. **គំរោង Azure AI Foundry** នៅតំបន់ North Central US
2. **Azure CLI** ដែលបានផ្ទៀងផ្ទាត់身份 (`az login`)
3. **Azure Developer CLI** (`azd`) ត្រូវបានដំឡើងរួច
4. **Python 3.12+** និង **Node.js 18+**
5. **របារទុកទិន្នន័យ Vector Store** ត្រូវបានបង្កើតជាមួយទិន្នន័យនិយោជិក

## ចាប់ផ្តើមរហ័ស

### 1. កំណត់អថេរបរិយាកាស

```bash
cd lesson-4-agentdeployment
cp .env.example .env
# កែសំរួល .env ជាមួយព័ត៌មានលម្អិតគម្រោង Azure AI Foundry របស់អ្នក
```

### 2. បញ្ចូនភ្នាក់ងារដែលផ្ដល់សេវា

**ជម្រើស A: ប្រើ Azure Developer CLI (បានណែនាំ)**

```bash
cd hosted-agent
azd auth login
azd agent deploy
```

**ជម្រើស B: ប្រើ Docker + Azure Container Registry**

```bash
cd hosted-agent

# សង់កុងតឺន័រ
docker build -t developer-onboarding-agent:latest .

# ស្លាកសម្រាប់ ACR
docker tag developer-onboarding-agent:latest <your-acr>.azurecr.io/developer-onboarding-agent:latest

# បញ្ចូនទៅ ACR
az acr login --name <your-acr>
docker push <your-acr>.azurecr.io/developer-onboarding-agent:latest

# ធ្វើការដាក់ប្រើតាមរយៈការចូលប្រើផតថល Azure AI Foundry ឬ SDK
```

### 3. ចាប់ផ្តើមផ្នែកខាងបន្ទាប់ ChatKit

```bash
cd chatkit-server
python -m venv .venv
source .venv/bin/activate  # លើវីនដូៈ .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

ម៉ាស៊ីនបម្រើនឹងចាប់ផ្តើមនៅលើ `http://localhost:8001`

### 4. ចាប់ផ្តើមផ្នែកខាងមុខ ChatKit

```bash
cd chatkit-server/frontend
npm install
npm run dev
```

ផ្នែកខាងមុខនឹងចាប់ផ្តើមនៅលើ `http://localhost:3000`

### 5. សាកល្បងកម្មវិធី

បើក `http://localhost:3000` នៅក្នុងកម្មវិធីរុករករបស់អ្នក ហើយសាកល្បងសំណួរទាំងនេះ៖

**ការស្វែងរកនិយោជិក:**
- "ខ្ញុំថ្មីនៅទីនេះ! តើមាននរណាបានធ្វើការ​នៅ Microsoft ទេ?"
- "តើនរណាម្នាក់មានបទពិសោធន៍ជាមួយ Azure Functions?"

**ធនធានរៀនសូត្រ:**
- "បង្កើតផ្លូវរៀនសម្រាប់ Kubernetes"
- "តើត្រូវបានបញ្ជាក់សញ្ញាសម្រាប់ជំនាញ cloud architecture អ្វីខ្លះ?"

**ជំនួយកូដកម្ម:**
- "ជួយខ្ញុំសរសេរកូដ Python សម្រាប់ការតភ្ជាប់ទៅ CosmosDB"
- "បង្ហាញខ្ញុំវិធីបង្កើត Azure Function"

**សំណួរពហុភ្នាក់ងារ:**
- "ខ្ញុំកំពុងចាប់ផ្តើមជាវិស្វករអំបួសមេឃ។ តើខ្ញុំម្នាក់គួរតែភ្ជាប់ជាមួយនរណា និងត្រូវរៀនអ្វីខ្លះ?"

## រចនាសម្ព័ន្ធគំរោង

```
lesson-4-agentdeployment/
├── .env.example                 # Environment variables template
├── implementation-plan.md       # Detailed implementation guide
├── README.md                    # This file
├── hosted-agent/               # Azure AI Foundry hosted agent
│   ├── main.py                 # Multi-agent workflow implementation
│   ├── requirements.txt        # Python dependencies
│   ├── Dockerfile              # Container definition
│   └── agent.yaml              # Agent deployment configuration
└── chatkit-server/             # ChatKit server application
    ├── app.py                  # FastAPI backend
    ├── store.py                # SQLite persistence layer
    ├── requirements.txt        # Python dependencies
    └── frontend/               # React frontend
        ├── package.json
        ├── vite.config.ts
        ├── tsconfig.json
        ├── index.html
        └── src/
            ├── main.tsx
            ├── App.tsx
            ├── App.css
            └── index.css
```

## ប្រតិបត្តិការពហុភ្នាក់ងារ

ភ្នាក់ងារដែលផ្ដល់សេវាវិនិយោគ **HandoffBuilder** ដើម្បីធ្វើដំណើរការភ្នាក់ងារពិសេសបួនរូប៖

| ភ្នាក់ងារ | តួនាទី | ឧបករណ៍ |
|-------|------|-------|
| **ភ្នាក់ងារ Triage** | អ្នករៀបចំ - បញ្ជូនសំណួរទៅអ្នកជំនាញ | គ្មាន |
| **ភ្នាក់ងារ Employee Search** | ស្វែងរកមិត្តរួមការងារ និងសមាជិកក្រុម | HostedFileSearchTool (Vector Store) |
| **ភ្នាក់ងាររៀនសូត្រ Learning Agent** | បង្កើតផ្លូវរៀន និងសេចក្តីផ្តល់អនុសាសន៍ | HostedMCPTool (Microsoft Learn) |
| **ភ្នាក់ងារ Coding Agent** | បង្កើតគំរូកូដ និងការណែនាំ | គ្មាន |

ប្រតិបត្តិការនេះអនុញ្ញាត៖
- Triage → អ្នកជំនាញណាមួយ
- អ្នកជំនាញ → អ្នកជំនាញផ្សេងទៀត (សម្រាប់សំណួរដែលទាក់ទង)
- អ្នកជំនាញ → Triage (សម្រាប់ប្រធានបទថ្មី)

## ការដោះស្រាយបញ្ហា

### ភ្នាក់ងារ​មិនឆ្លើយតប
- ពិនិត្យមើលថា ភ្នាក់ងារដែលផ្ដល់សេវាត្រូវបានបញ្ចូន និងដំណើរការនៅក្នុង Azure AI Foundry
- ពិនិត្យឈ្មោះ `HOSTED_AGENT_NAME` និង បន្ទាន់សម័យ `HOSTED_AGENT_VERSION` ត្រូវនឹងការបញ្ចូនរបស់អ្នក

### បញ្ហាផ្ទុកទិន្នន័យ Vector store
- បញ្ជាក់ថា `VECTOR_STORE_ID` ត្រូវបានកំណត់យ៉ាងត្រឹមត្រូវ
- ពិនិត្យមើលថា របារទុកទិន្នន័យមានទិន្នន័យនិយោជិក

### បញ្ហាផ្ទៀងផ្ទាត់身份
- រត់ `az login` ដើម្បីបំពេញព័ត៌មានអត្តសញ្ញាណឡើងវិញ
- ប្រាកដថាអ្នកមានការចូលដំណើរការទៅគំរោង Azure AI Foundry

## ធនធាន

- [Azure AI Foundry Hosted Agents Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/concepts/hosted-agents)
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)
- [ChatKit Integration Sample](https://github.com/microsoft/agent-framework/tree/main/python/samples/demos/chatkit-integration)
- [Azure Developer CLI](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការជូនដំណឹងវិភាគ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំសម្រាប់ភាពត្រឹមត្រូវ សូមយល់ពីថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាទីបច្ចេកទេសគួរត្រូវបានចាត់ទុកជាឯកសារដើមដ៏មានអំណាច។ សម្រាប់ព័ត៌មានសំខាន់ៗ គួរប្រើការបកប្រែដោយមនុស្សជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->