# 🗺️ Roadmap du Projet – Mental Health Assistant

## 🧠 Objectif principal

Développer un assistant virtuel capable de générer des réponses empathiques et utiles en matière de bien-être mental, sans se substituer à un professionnel de santé.

---

## 🗓️ Semaine 1 – Lancement & Exploration

* [x] Définir les objectifs précis du projet
* [x] Comparer les modèles : GPT-2, DistilGPT-2, BERT, T5
* [x] Créer un tableau comparatif (capacité de génération, efficacité sur CPU, complexité)

## 🗓️ Semaine 2 – Préparation des Données

* [x] Collecte du dataset (EmpatheticDialogues, etc.)
* [x] Nettoyage : doublons, formatage
* [x] Tokenisation + analyse (longueur, type d'émotions)

## 🗓️ Semaine 3 – Prototype Simple + Pipeline

* [ ] Construire un prototype avec Hugging Face
* [ ] Tester la génération simple avec DistilGPT-2 (non fine-tuné)
* [ ] Créer un prompt de test (dialogues simulés)

## 🗓️ Semaine 4 – Fine-tuning sur CPU

* [ ] Fine-tuning DistilGPT-2 avec `Trainer` (batch size réduit, accumulation de gradient)
* [ ] Entraînement court (3 époques)
* [ ] Journalisation des performances et résultats

## 🗓️ Semaine 5 – Ajustements & Re-Entraînement

* [ ] Ajustement hyperparamètres (learning rate, époques)
* [ ] Évaluation qualitative : empathie, cohérence
* [ ] Test optionnel de BERT pour la détection d'émotions

## 🗓️ Semaine 6 – Interface Gradio

* [ ] Prototyper une interface utilisateur (Gradio)
* [ ] Ajouter éléments rassurants et doux (UI)
* [ ] Tests locaux de l’interface

## 🗓️ Semaine 7 – Validation & Tests Utilisateurs

* [ ] Panel de testeurs (pairs, étudiants)
* [ ] Questionnaire d’évaluation : empathie, utilité, feedback
* [ ] Collecte et synthèse des retours

## 🗓️ Semaine 8 – Finitions & Lancement

* [ ] Amélioration finale de l’UI
* [ ] Création README et doc éthique claire
* [ ] Déploiement sur Hugging Face Spaces
* [ ] Partage sur GitHub, LinkedIn, etc.

---

## 🧘 Bonus hebdomadaire

Chaque fin de semaine :

* [ ] Auto-évaluation de l’avancement
* [ ] Célébration des réussites 🎉
* [ ] Ajustements pour la suite
