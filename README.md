# 🌿 Détection Automatisée des Maladies des Plantes par Deep Learning

## 📌 Description du Projet

Ce projet de Deep Learning a pour objectif la détection automatique des maladies des plantes à partir d’images de feuilles.

Grâce aux techniques de Vision par Ordinateur et aux Réseaux de Neurones Convolutifs (CNN), le modèle est capable d’identifier différentes maladies végétales avec une excellente précision. Cette solution permet une détection précoce des maladies et peut contribuer à améliorer la surveillance des cultures agricoles.

Le projet comprend l’entraînement du modèle, l’évaluation de ses performances, la visualisation des résultats ainsi qu’une application permettant d’utiliser le modèle entraîné.

---

## 🎯 Objectifs

* Détecter automatiquement les maladies des plantes.
* Classifier les images de feuilles selon leur catégorie.
* Évaluer les performances d’un modèle de Deep Learning.
* Produire des visualisations pour l’analyse des résultats.
* Fournir un outil d’aide à la décision pour le domaine agricole.

---

## 🛠️ Technologies Utilisées

* Python
* TensorFlow
* Keras
* NumPy
* Pandas
* Matplotlib
* Scikit-Learn
* Jupyter Notebook

---

## 📂 Structure du Projet

```text
D-tection-Automatis-e-des-Maladies-des-Plantes/
│
├── plant_disease_model.keras
├── plant_disease_model.tflite
├── entrainement_modele.ipynb
├── app.py
├── requirements.txt
├── README.md
├── presentation_projet.pptx
│
└── Reports/
    ├── matrice_confusion_finale.png
    ├── courbe_accuracy_poster_style.png
    ├── courbe_loss_poster_style.png
    ├── courbe_ROC_professionnelle.png
    ├── historique_entrainement_poster.png
    ├── rapport_performances_visuel.png
    ├── dashboard_metriques_globales.png
    ├── poster_accuracy_seule.png
    ├── poster_loss_seule.png
    ├── treemap_cultures_maladies.png
    └── treemap_performance_ia.png
```

---

## 🧠 Modèle de Deep Learning

Le modèle principal est enregistré dans :

```text
plant_disease_model.keras
```

Une version optimisée pour les environnements mobiles est également disponible :

```text
plant_disease_model.tflite
```

Le modèle atteint une précision d’environ **96 %**, ce qui démontre son efficacité dans la classification des maladies des plantes.

---

## 📊 Évaluation des Performances

Les performances du modèle ont été évaluées à l’aide de plusieurs métriques :

* Accuracy
* Precision
* Recall
* F1-Score
* Courbe ROC
* Matrice de confusion

Les résultats obtenus sont regroupés dans le dossier **Reports/**.

### Visualisations disponibles

* Matrice de confusion finale
* Courbe Accuracy
* Courbe Loss
* Courbe ROC
* Historique d'entraînement
* Dashboard global des métriques
* Rapport visuel des performances
* Treemap des cultures et maladies
* Treemap des performances du modèle

---

## 🚀 Installation et Exécution

### 1. Cloner le projet

```bash
git clone https://github.com/noraidouaouzal-etu-lab/D-tection-Automatis-e-des-Maladies-des-Plantes.git
```

### 2. Accéder au projet

```bash
cd D-tection-Automatis-e-des-Maladies-des-Plantes
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer l'application

```bash
python app.py
```

---

## 📓 Notebook d'Entraînement

Le notebook principal utilisé pour l’entraînement du modèle est :

```text
entrainement_modele.ipynb
```

Ce notebook contient :

* Le chargement des données
* Le prétraitement des images
* La construction du modèle CNN
* L’entraînement du modèle
* L’évaluation des performances
* La sauvegarde du modèle final

---

## 📄 Présentation

La présentation PowerPoint du projet est disponible dans :

```text
presentation_projet.pptx
```

---

## 🌱 Applications

Ce projet peut être utilisé dans :

* L’agriculture intelligente
* La surveillance des cultures
* La détection précoce des maladies végétales
* Les systèmes d’aide à la décision agricole

---

## 👩‍🎓 Réalisé par

* **Nora Idouaouzal**
* **Malak Bousseta**

Master Data Science & Big Data

Faculté des Sciences Ben M'Sik – Casablanca

Année Universitaire 2025-2026

---

## 👨‍🏫 Encadrement

Projet réalisé dans le cadre du Master Data Science & Big Data.

---

## 📜 Licence

Projet académique réalisé à des fins pédagogiques et éducatives.
