from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
MODELS_DIR = DATA_DIR / "models"

REAL_ESTATE_DATA = DATA_DIR / "real_estate.csv"
PRICE_PRED_MODEL = MODELS_DIR / "model.joblib"