# mlops-ml-project (baseline)

Projet ML baseline utilisant scikit-learn et le dataset Iris pour démontrer les bonnes pratiques MLOps.

## Installation
```bash
# Créer environnement virtuel
python -m venv .venv

# Activer (Windows)
.venv\Scripts\activate

# Activer (Linux/Mac)
source .venv/bin/activate

# Installer dépendances
pip install -r requirements.txt
```

## Entraînement
```bash
python scripts/train.py
```

Génère les artefacts dans `artifacts/`:
- `model.joblib` - Modèle entraîné
- `metrics.json` - Métriques de performance
- `confusion_matrix.png` - Matrice de confusion

## Évaluation
```bash
python scripts/evaluate.py
```

Génère `artifacts/report.json` avec le rapport de classification complet.

## Structure du projet
```
mlops-ml-project/
├── config/
│   └── train.yaml          # Configuration entraînement
├── src/
│   ├── __init__.py
│   ├── data.py             # Chargement données
│   ├── features.py         # Prétraitement
│   └── model.py            # Définition modèle
├── scripts/
│   ├── train.py            # Script entraînement
│   └── evaluate.py         # Script évaluation
├── tests/
│   └── test_config.py      # Tests unitaires
├── artifacts/              # Artefacts générés (non versionné)
├── data/                   # Données (non versionné)
├── README.md
└── requirements.txt
```

## Configuration

Modifiez `config/train.yaml` pour ajuster:
- Dataset (iris ou CSV custom)
- Paramètres de split
- Hyperparamètres du modèle