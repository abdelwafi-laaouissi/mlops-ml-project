# src/model.py
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


def build_model(cfg: dict):
    name = cfg["model"].get("name", "logistic_regression")

    if name == "logistic_regression":
        return LogisticRegression(
            max_iter=int(cfg["model"].get("max_iter", 2000))
        )
    elif name == "random_forest":
        return RandomForestClassifier(
            n_estimators=int(cfg["model"].get("n_estimators", 100)),
            random_state=42
        )
    else:
        raise ValueError(f"Model not supported: {name}")