# src/features.py
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, FunctionTransformer
from sklearn.impute import SimpleImputer


def _clip(X):
    """Clipper les valeurs extrêmes"""
    return X.clip(-3, 3)


def build_numeric_preprocess():
    """
    Prétraitement amélioré :
    - imputation médiane
    - standardisation
    - clipping des outliers
    """
    return Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("clip", FunctionTransformer(_clip)),
    ])