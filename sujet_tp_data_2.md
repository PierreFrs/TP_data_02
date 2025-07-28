# TP : Automatisation d'un Pipeline de Traitement de Fichiers de Données

## **Contexte**

Vous travaillez pour une entreprise qui reçoit quotidiennement des fichiers de données de ventes au format CSV depuis différents magasins. Ces fichiers arrivent dans un répertoire d'entrée et doivent être traités automatiquement.

## **Objectifs**

Créer un système automatisé qui :

- Surveille l'arrivée de nouveaux fichiers
- Traite et transforme les données
- Génère des rapports de synthèse
- Archive les fichiers traités
- Gère les erreurs et logging

## **Structure du Projet**

```mardown
projet_pipeline/
├── data/
│   ├── input/           # Fichiers d'entrée
│   ├── processing/      # Traitement en cours
│   ├── output/          # Fichiers traités
│   └── archive/         # Archive
├── scripts/
│   ├── pipeline.sh      # Script principal
│   ├── process_data.py  # Traitement Python
│   └── generate_report.py
├── logs/               # Journaux
└── config/            # Configuration
```

## **Tâches à Réaliser**

### **Phase 1 : Surveillance automatique des fichiers (Bash)**

- Script qui surveille le répertoire `data/input/`
- Détection des nouveaux fichiers CSV
- Validation du format et de la structure
- Déplacement vers `data/processing/`

### **Phase 2 : Traitement des données (Python + Bash)**

- Script Python utilisant pandas pour :
  - Lire les fichiers CSV
  - Nettoyer les données (suppression doublons, valeurs aberrantes)
  - Calculer des statistiques (total ventes, moyennes par magasin)
  - Convertir en différents formats (JSON, Excel)
- Orchestration avec Bash

### **Phase 3 : Génération de rapports (Python)**

- Création automatique de rapports HTML avec :
  - Résumé des ventes par période
  - Top 10 des produits
  - Graphiques simples (matplotlib/seaborn)
  - Statistiques de qualité des données

### **Phase 4 : Gestion des fichiers et archivage (Bash)**

- Renommage avec horodatage
- Déplacement vers `data/output/` et `data/archive/`
- Compression des anciens fichiers
- Nettoyage automatique (suppression fichiers > 30 jours)

### **Phase 5 : Logging et gestion d'erreurs**

- Journalisation de toutes les opérations
- Rotation des logs
- Notifications par email/fichier en cas d'erreur
- Système de retry pour les fichiers en échec

## **Scripts à Développer**

### **1. Script Principal (pipeline.sh)**

```bash
#!/bin/bash
# Orchestrateur principal
# - Surveillance répertoire
# - Lancement traitement Python
# - Gestion erreurs et logging
```

### **2. Traitement Données (process_data.py)**

```python
# Script Python avec pandas
# - Lecture/validation CSV
# - Nettoyage et transformation
# - Calculs statistiques
# - Export formats multiples
```

### **3. Générateur de Rapports (generate_report.py)**

```python
# Génération rapports automatiques
# - Templates HTML
# - Graphiques matplotlib
# - Envoi par email (optionnel)
```

### **4. Utilitaires (utils.sh)**

```bash
# Fonctions réutilisables
# - Gestion logs
# - Validation fichiers
# - Archivage
```

## **Exemples de Fichiers de Données**

```csv
date,magasin,produit,quantite,prix_unitaire
2024-01-15,Store_001,Produit_A,10,25.50
2024-01-15,Store_001,Produit_B,5,15.00
...
```

## **Fonctionnalités à Implémenter**

### **Automatisation Bash :**

- Boucle de surveillance continue ou via cron
- Gestion des verrous pour éviter les exécutions simultanées
- Variables de configuration centralisées
- Gestion des signaux (SIGTERM, SIGINT)

### **Traitement Python :**

- Validation de schéma des données
- Gestion des encodages différents
- Calculs d'agrégations complexes
- Export vers multiples formats

### **Gestion des Erreurs :**

- Quarantaine pour fichiers corrompus
- Logs détaillés avec niveaux (INFO, WARNING, ERROR)
- Rapports d'erreurs automatiques
- Reprise après incident

## **Extensions Possibles**

- Traitement de fichiers Excel en plus des CSV
- Calculs de tendances sur plusieurs périodes
- Système de notifications par webhook
