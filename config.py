import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = Path(os.getenv("DATA_DIR", BASE_DIR / "data"))
MODELS_DIR = Path(os.getenv("MODELS_DIR", DATA_DIR / "models"))
REAL_ESTATE_DATA = Path(os.getenv("REAL_ESTATE_DATA", DATA_DIR / "real_estate.csv"))
PRICE_PRED_MODEL = Path(os.getenv("PRICE_PRED_MODEL", MODELS_DIR / "model.joblib"))
