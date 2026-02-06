# Lesson 4 : Déploiement d’Agent avec Azure AI Foundry Hosted Agents + ChatKit

Cette leçon montre comment déployer un workflow multi-agent sur Azure AI Foundry en tant qu’agent hébergé et créer une interface frontend basée sur ChatKit pour interagir avec lui.

## Architecture

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

## Prérequis

1. **Projet Azure AI Foundry** dans la région North Central US  
2. **Azure CLI** authentifié (`az login`)  
3. **Azure Developer CLI** (`azd`) installé  
4. **Python 3.12+** et **Node.js 18+**  
5. **Vector Store** créé avec les données des employés  

## Démarrage rapide

### 1. Configurer les variables d’environnement

```bash
cd lesson-4-agentdeployment
cp .env.example .env
# Modifiez .env avec les détails de votre projet Azure AI Foundry
```

### 2. Déployer l’agent hébergé

**Option A : Utiliser Azure Developer CLI (Recommandé)**

```bash
cd hosted-agent
azd auth login
azd agent deploy
```

**Option B : Utiliser Docker + Azure Container Registry**

```bash
cd hosted-agent

# Construire le conteneur
docker build -t developer-onboarding-agent:latest .

# Tag pour ACR
docker tag developer-onboarding-agent:latest <your-acr>.azurecr.io/developer-onboarding-agent:latest

# Pousser vers ACR
az acr login --name <your-acr>
docker push <your-acr>.azurecr.io/developer-onboarding-agent:latest

# Déployer via le portail Azure AI Foundry ou le SDK
```

### 3. Démarrer le backend ChatKit

```bash
cd chatkit-server
python -m venv .venv
source .venv/bin/activate  # Sur Windows : .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Le serveur démarrera sur `http://localhost:8001`

### 4. Démarrer le frontend ChatKit

```bash
cd chatkit-server/frontend
npm install
npm run dev
```

Le frontend démarrera sur `http://localhost:3000`

### 5. Tester l’application

Ouvrez `http://localhost:3000` dans votre navigateur et essayez ces requêtes :

**Recherche d’employés :**  
- « Je suis nouveau ici ! Quelqu’un a-t-il déjà travaillé chez Microsoft ? »  
- « Qui a de l’expérience avec Azure Functions ? »

**Ressources d’apprentissage :**  
- « Crée un parcours d’apprentissage pour Kubernetes »  
- « Quelles certifications devrais-je obtenir pour l’architecture cloud ? »

**Aide au codage :**  
- « Aide-moi à écrire du code Python pour me connecter à CosmosDB »  
- « Montre-moi comment créer une Azure Function »

**Requêtes multi-agents :**  
- « Je commence en tant qu’ingénieur cloud. Avec qui devrais-je me connecter et qu’est-ce que je devrais apprendre ? »

## Structure du projet

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

## Le workflow multi-agent

L’agent hébergé utilise **HandoffBuilder** pour orchestrer quatre agents spécialisés :

| Agent | Rôle | Outils |
|-------|------|--------|
| **Agent de triage** | Coordinateur – dirige les requêtes vers les spécialistes | Aucun |
| **Agent de recherche d’employés** | Trouve collègues et membres de l’équipe | HostedFileSearchTool (Vector Store) |
| **Agent d’apprentissage** | Crée des parcours d’apprentissage et recommandations | HostedMCPTool (Microsoft Learn) |
| **Agent de codage** | Génère exemples de code et conseils | Aucun |

Le workflow permet :  
- Triage → Tout spécialiste  
- Spécialistes → Autres spécialistes (pour requêtes connexes)  
- Spécialistes → Triage (pour nouveaux sujets)  

## Résolution des problèmes

### Agent ne répond pas  
- Vérifiez que l’agent hébergé est déployé et en cours d’exécution dans Azure AI Foundry  
- Assurez-vous que `HOSTED_AGENT_NAME` et `HOSTED_AGENT_VERSION` correspondent à votre déploiement  

### Erreurs de Vector store  
- Vérifiez que `VECTOR_STORE_ID` est bien défini  
- Vérifiez que le vector store contient les données des employés  

### Erreurs d’authentification  
- Exécutez `az login` pour actualiser les informations d’identification  
- Assurez-vous d’avoir accès au projet Azure AI Foundry  

## Ressources

- [Documentation Azure AI Foundry Hosted Agents](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/concepts/hosted-agents)  
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)  
- [Exemple d’intégration ChatKit](https://github.com/microsoft/agent-framework/tree/main/python/samples/demos/chatkit-integration)  
- [Azure Developer CLI](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Clause de non-responsabilité** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->