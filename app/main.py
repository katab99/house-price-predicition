import os
import logging
from fastapi import FastAPI
from .models import Features, Prediction
from .utils import convert_data_to_array
from ml.house_price_regressor import HousePriceRegressor
from config import PRICE_PRED_MODEL


app = FastAPI()


LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logger = logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


# routes
@app.post("/predict")
async def post_predict(features: Features):
    logger.debug(f"Predicting with features: {features}")

    data = convert_data_to_array(features)
    model = HousePriceRegressor(model_path=PRICE_PRED_MODEL)
    price_pred = model.predict(data)

    response = Prediction(price=price_pred[0])

    logger.debug(f"Prediction result: {response}")

    return response


@app.get("/health")
async def get_health():
    return {"status": "OK"}
