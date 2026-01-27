<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:02:29+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "fr"
}
-->
# Leçon 2 Développement d'Agent

Bienvenue dans la deuxième leçon du cours "Créer un agent IA de zéro à la production" !

Dans cette leçon, nous allons couvrir :

- Les outils pour créer nos agents IA
  
- Instructions d'installation pour nos ressources de développement

- Bonnes pratiques de développement des agents IA
  
- Parcours du code pour la création de nos agents IA
  
Commençons par examiner les outils que nous allons utiliser pour créer nos agents IA.

## Outils et instructions d'installation

### Microsoft Foundry

Pour accéder aux modèles de langage étendu (LLM), nous utiliserons [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). L'utilisation de Foundry entraîne des coûts, veuillez donc suivre les instructions pour la configuration du compte si vous n'avez pas encore accès.

### Modèles OpenAI

Les exemples de code des agents dans ce cours sont configurés pour utiliser les modèles OpenAI via [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Utilisez ce guide pour apprendre à déployer un modèle avec Foundry : [Déployer des modèles Microsoft Foundry dans le portail Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Choisissez un modèle GPT-4.1 ou plus récent pour ce cours.

### Microsoft Agent Framework

Comme mentionné précédemment, nous utiliserons le [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) pour créer et orchestrer nos agents IA.

Pour installer le Microsoft Agent Framework et les autres packages requis, exécutez la commande suivante depuis le répertoire racine de ce projet :

```bash
pip install -r requirements.txt
```

### Configuration des variables .env

Pour exécuter les exemples de code de ce cours, vous devez créer un fichier `.env` dans le répertoire racine de ce projet.

Pour faciliter la tâche, vous pouvez copier le fichier `.env.example` fourni :

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatisée [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d'assurer la précision, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour des informations critiques, il est recommandé de faire appel à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->