# Leçon 1 : Conception d'Agent IA

Bienvenue dans la première leçon du cours "Construire un Agent IA de zéro à la production" !

Dans cette leçon, nous allons couvrir :

- Définir ce que sont les Agents IA
  
- Discuter de l'application Agent IA que nous construisons

- Identifier les outils et services nécessaires pour chaque agent
  
- Architecturer notre Application Agent
  
Commençons par définir ce qu'est un agent et pourquoi nous les utiliserions dans une application.

## Qu'est-ce qu'un Agent IA ?

![What Are AI Agents?](../../../translated_images/fr/what-are-ai-agents.47a544a1d03481ab.webp)

Si c'est la première fois que vous explorez comment construire un Agent IA, vous pourriez avoir des questions sur la façon exacte de définir ce qu'est un Agent IA.

Voici une manière simple de définir ce qu'est un Agent IA à travers les composants qui le constituent :

**Grand Modèle de Langage** - Le LLM alimentera à la fois la capacité à traiter le langage naturel de l'utilisateur pour interpréter la tâche qu'il souhaite accomplir ainsi qu'à interpréter les descriptions des outils disponibles pour accomplir ces tâches.

**Outils** - Ce seront des fonctions, API, bases de données et autres services que le LLM peut choisir d'utiliser pour réaliser les tâches demandées par l'utilisateur.

**Mémoire** - C'est ainsi que nous stockons à la fois les interactions à court terme et à long terme entre l'Agent IA et l'utilisateur. Stocker et récupérer cette information est important pour améliorer et sauvegarder les préférences utilisateur au fil du temps.

## Notre cas d'utilisation d'Agent IA

![What Are We Building?](../../../translated_images/fr/what-are-we-building.1ff3b9a752eb8570.webp)

Pour ce cours, nous allons construire une application Agent IA qui aide les nouveaux développeurs à s'intégrer à notre équipe de développement d'Agents IA !

Avant de faire tout travail de développement, la première étape pour créer une application Agent IA réussie est de définir des scénarios clairs sur la façon dont nous attendons que nos utilisateurs travaillent avec nos Agents IA.

Pour cette application, nous allons travailler avec ces scénarios :

**Scénario 1** : Un nouvel employé rejoint notre organisation et veut en savoir plus sur l'équipe qu'il a intégrée et comment se connecter avec elle.

**Scénario 2 :** Un nouvel employé souhaite savoir quelle serait la meilleure première tâche à commencer.

**Scénario 3 :** Un nouvel employé veut rassembler des ressources d'apprentissage et des exemples de code pour l'aider à commencer à compléter cette tâche.

## Identifier les Outils et Services

Maintenant que nous avons ces scénarios créés, l'étape suivante est de les mapper aux outils et services dont nos agents IA auront besoin pour accomplir ces tâches.

Ce processus relève de l'ingénierie du contexte car nous allons nous concentrer sur le fait de nous assurer que nos Agents IA aient le bon contexte au bon moment pour accomplir les tâches.

Faisons cela scénario par scénario et réalisons une bonne conception agentique en listant pour chaque agent la tâche, les outils et les résultats désirés.

![Agent Design](../../../translated_images/fr/agent-design.07edb7ae37f47803.webp)

### Scénario 1 - Agent de Recherche d'Employés

**Tâche** - Répondre aux questions sur les employés de l'organisation telles que la date d'entrée, l'équipe actuelle, la localisation et le dernier poste.

**Outils** - Base de données de la liste actuelle des employés et organigramme

**Résultats** - Capable de récupérer des informations depuis la base de données pour répondre aux questions générales sur l'organisation et aux questions spécifiques sur les employés.

### Scénario 2 - Agent de Recommandation de Tâches

**Tâche** - En fonction de l'expérience développeur du nouvel employé, proposer 1 à 3 issues sur lesquelles le nouvel employé peut travailler.

**Outils** - Serveur GitHub MCP pour obtenir les issues ouvertes et construire un profil développeur

**Résultats** - Capable de lire les 5 derniers commits d'un profil GitHub et les issues ouvertes sur un projet GitHub et faire des recommandations basées sur une correspondance

### Scénario 3 - Agent Assistant de Code

**Tâche** - Basé sur les issues ouvertes recommandées par l'agent de "Recommandation de Tâches", rechercher et fournir des ressources et générer des extraits de code pour aider l'employé.

**Outils** - Microsoft Learn MCP pour trouver des ressources et Code Interpreter pour générer des extraits de code personnalisés.

**Résultats** - Si l'utilisateur demande une aide supplémentaire, le flux de travail doit utiliser le Serveur Learn MCP pour fournir des liens et extraits vers les ressources puis passer la main à l'agent Code Interpreter pour générer de petits extraits de code avec explications.

## Architecture de notre Application Agent

Maintenant que nous avons défini chacun de nos Agents, créons un diagramme d'architecture qui nous aidera à comprendre comment chaque agent va travailler ensemble et séparément selon la tâche :

![Agent Architecture](../../../translated_images/fr/agent-architecture.4fd5efa371e77a3c.webp)

## Prochaines Étapes

Maintenant que nous avons conçu chaque agent et notre système agentique, passons à la leçon suivante où nous développerons chacun de ces agents !

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatisée [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude de la traduction, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle humaine. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->