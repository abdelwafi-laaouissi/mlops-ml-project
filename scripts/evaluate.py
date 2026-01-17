# scripts/evaluate.py
import json
from pathlib import Path
import joblib
import yaml
from sklearn.metrics import classification_report

from src.data import load_dataset


def load_cfg(path="config/train.yaml"):
    return yaml.safe_load(open(path, "r", encoding="utf-8"))


def main():
    cfg = load_cfg()
    art_dir = Path(cfg.get("artifacts_dir", "artifacts"))
    
    # Charger modèle
    model = joblib.load(art_dir / "model.joblib")
    
    # Charger données complètes
    X, y = load_dataset(cfg)
    
    # Prédire
    pred = model.predict(X)
    
    # Générer rapport
    report = classification_report(y, pred, output_dict=True)
    json.dump(report, open(art_dir / "report.json", "w"), indent=2)
    
    print(" Evaluate OK: artifacts/report.json créé")


if __name__ == "__main__":
    main()