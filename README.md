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

## 📊 Artefacts générés

Après exécution de `train.py`, le dossier `artifacts/` contient :

- `model.joblib` - Modèle entraîné (pipeline complet)
- `metrics.json` - Métriques de performance (accuracy, F1-macro)
- `confusion_matrix.png` - Visualisation de la matrice de confusion
- `report.json` - Rapport de classification détaillé (par classe)

## ⚙️ Configuration

Modifiez `config/train.yaml` pour ajuster :
```yaml
data:
  kind: "iris"  # ou "csv" pour données custom
  
model:
  name: "random_forest"  # ou "logistic_regression"
  n_estimators: 100      # pour random_forest
  
split:
  test_size: 0.2
  random_state: 42
```

## 📈 Performance

**Random Forest (v0.1.0):**
- Accuracy: 0.97
- F1-macro: 0.97

## 🔧 Développement
```bash
# Créer une branche feature
git checkout -b feature/ma-feature

# Faire vos modifications...
python scripts/train.py  # Tester

# Commit et push
git add .
git commit -m "feat: description"
git push origin feature/ma-feature

# Créer une Pull Request sur GitHub
```

## 🧪 Tests
```bash
pytest tests/
```


## 👥 Auteurs

LAAOUISSI ABDELWAFI - Projet MLOps M2