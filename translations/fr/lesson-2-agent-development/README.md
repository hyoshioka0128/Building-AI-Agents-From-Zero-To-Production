# Lesson 2 Développement d'Agent

Bienvenue dans la deuxième leçon du cours "Construire un Agent IA de Zéro à la Production" !

Dans cette leçon, nous aborderons :

- Les outils pour créer nos agents IA

- Instructions de configuration pour nos ressources de développement

- Bonnes pratiques de développement d'agents IA

- Parcours du code pour créer nos agents IA

Commençons par examiner les outils que nous utiliserons pour créer nos agents IA.

## Outils et Instructions de Configuration

### Microsoft Foundry

Pour accéder aux grands modèles de langage (LLMs), nous utiliserons [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Des coûts sont associés à l'utilisation de Foundry, alors veuillez suivre les instructions de configuration de compte si vous n'y avez pas déjà accès.

### Modèles OpenAI

Les exemples de code d'agents dans ce cours sont configurés pour utiliser les modèles OpenAI via [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Utilisez ce guide pour apprendre comment déployer un modèle avec Foundry : [Déployer des modèles Microsoft Foundry dans le portail Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Choisissez un modèle GPT-4.1 ou plus récent pour ce cours.

### Microsoft Agent Framework

Comme mentionné précédemment, nous utiliserons le [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) pour créer et orchestrer nos agents IA.

Pour installer le Microsoft Agent Framework et les autres packages requis, exécutez la commande suivante depuis le répertoire racine de ce projet :

```bash
pip install -r requirements.txt
```

### Configuration des variables .env

Pour exécuter les exemples de code de ce cours, vous devrez créer un fichier `.env` dans le répertoire racine de ce projet.

Pour faciliter cela, vous pouvez copier le fichier `.env.example` fourni :

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source officielle. Pour les informations critiques, il est recommandé de faire appel à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->