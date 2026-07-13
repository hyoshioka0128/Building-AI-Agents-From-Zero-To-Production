# Leçon 2 Développement d'Agent

Bienvenue à la deuxième leçon du cours "Construire un agent IA de zéro à la production" !

Dans cette leçon, nous couvrirons :

- Les outils pour créer nos agents IA
  
- Instructions de configuration pour nos ressources de développement

- Bonnes pratiques de développement d’agents IA
  
- Présentation du code pour créer nos agents IA
  
Commençons par examiner les outils que nous utiliserons pour créer nos agents IA.

## Outils et instructions de configuration

### Microsoft Foundry

Pour accéder aux modèles de langage large (LLMs), nous utiliserons [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). L’utilisation de Foundry engendre des coûts, veuillez donc suivre les instructions de configuration de compte si vous n’y avez pas encore accès.

### Modèles OpenAI

Les exemples de code d’agents dans ce cours sont configurés pour utiliser les modèles OpenAI via [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Utilisez ce guide pour apprendre à déployer un modèle avec Foundry : [Déployer les modèles Microsoft Foundry dans le portail Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Choisissez un modèle de la série GPT-5 (par exemple `gpt-5.1`) pour ce cours. Évitez les modèles retirés comme GPT-4o et GPT-4.1, qui atteindront la fin de vie en 2026.

### Microsoft Agent Framework

Comme mentionné précédemment, nous utiliserons le [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) pour créer et orchestrer nos agents IA.

Vous aurez besoin de **Python 3.12 ou plus récent**. Pour installer le Microsoft Agent Framework et les autres paquets requis, exécutez la commande suivante dans le répertoire racine de ce projet :

```bash
pip install -r requirements.txt
```

### Authentification avec Azure

Les agents s’authentifient auprès de Microsoft Foundry en utilisant vos identifiants Azure CLI
(`AzureCliCredential`), vous devez donc vous connecter avant d’exécuter un exemple :

```bash
az login
# Si vous avez plus d'un abonnement, sélectionnez celui avec votre projet Foundry :
az account set --subscription "<your-subscription-id>"
```

Assurez-vous que votre compte dispose du rôle **Azure AI User** (ou équivalent) sur le projet Foundry
afin de pouvoir appeler les API des modèles et des agents.

### Configurer les variables .env

Pour exécuter les exemples de code de ce cours, vous devrez créer un fichier `.env` dans le répertoire racine de ce projet.

Pour faciliter la tâche, vous pouvez copier le fichier `.env.example` fourni :

```bash
cp .env.example .env
``` 

Ensuite, remplissez les deux variables lues par les agents (le `FoundryChatClient` les récupère
automatiquement) :

| Variable | Qu’est-ce que c’est | Où la trouver |
|----------|--------------------|---------------|
| `FOUNDRY_PROJECT_ENDPOINT` | Le point de terminaison **project** de votre Foundry, se terminant par `/api/projects/<project>` | Portail Foundry → votre projet → **Aperçu** → *Points de terminaison* |
| `FOUNDRY_MODEL` | Le nom du déploiement du modèle sur lequel vos agents fonctionnent (par exemple `gpt-5.1`) | Portail Foundry → **Modèles + points de terminaison** |

### Créer le magasin vectoriel des employés

Un exemple — l’**Agent de recherche d’employés** — interroge un annuaire d’employés stocké dans un
**magasin vectoriel** Microsoft Foundry. Créez-le une fois puis copiez l’ID qu’il affiche dans votre `.env`
sous `VECTOR_STORE_ID` (exécutez depuis la racine du dépôt pour qu’il récupère votre `.env`) :

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### Exécuter un exemple

Chaque agent exécute sa propre interface DevUI locale. Par exemple :

```bash
python lesson-2-agent-development/employee-search-agent.py
```

Ensuite, ouvrez l’URL imprimée `http://localhost:<port>` dans votre navigateur pour discuter avec l’agent.

## Les agents de cette leçon

Chaque exemple est un agent autonome construit avec le Microsoft Agent Framework. Ensemble, ils
implémentent les scénarios conçus dans la [leçon 1](../lesson-1-agent-design/README.md) :

| Exemple | Scénario de la leçon 1 | Outil utilisé | Port |
|--------|-----------------------|--------------|------|
| `employee-search-agent.py` | Scénario 1 — Recherche d’employés | Recherche de fichiers hébergée Foundry sur un magasin vectoriel | 8090 |
| `task-recommendation-agent.py` | Scénario 2 — Recommandation de tâches | Serveur **GitHub MCP** (outil MCP hébergé) | 8095 |
| `azure-learning-agent.py` | Scénario 3 — Assistant de code (recherche) | Serveur **Microsoft Learn MCP** (outil MCP hébergé) | 8092 |
| `coding-agent.py` | Scénario 3 — Assistant de code (code) | **Interpréteur de code** | 8093 |
| `learning-recommendation-agent.py` | Agent de support | Learn MCP + raisonnement | 8091 |
| `agent-orchestration.py` | Lie les scénarios ensemble | Orchestration multi-agent de **transfert** | 8094 |

> **Note concernant l’agent de recommandation de tâches.** `task-recommendation-agent.py` nécessite un
> `GITHUB_PERSONAL_ACCESS_TOKEN` dans votre `.env` (créez-en un à
> <https://github.com/settings/personal-access-tokens/new>). Il lit l’activité GitHub récente d’un développeur
> et recommande 1 à 3 issues ouvertes correspondantes — exactement comme prévu dans le scénario 2.
> C’est le seul exemple qui appelle GitHub ; les autres n’ont besoin que de votre projet Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->