from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
from ml.house_price_regressor import HousePriceRegressor
from .utils import convert_data_to_array
from config import PRICE_PRED_MODEL

# import logging


# models
class Features(BaseModel):
    transaction_date: float
    house_age: float = Field(ge=0)
    dist_to_nearest_mrt_station: float = Field(ge=0)
    num_of_convenience_store: int = Field(ge=0)
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)


class Prediction(BaseModel):
    price: float


app = FastAPI()

# logger = logging.basicConfig()


# routes
@app.post("/predict")
async def post_predict(features: Features):

    data = convert_data_to_array(features)
    model = HousePriceRegressor(model_path=PRICE_PRED_MODEL)
    price_pred = model.predict(data)

    response = Prediction(price=price_pred[0])

    return response


@app.get("/health")
async def get_health():
    return {"status": "OK"}
