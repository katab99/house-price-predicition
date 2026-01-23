import numpy as np
from ml.house_price_regressor import HousePriceRegressor
from config import PRICE_PRED_MODEL


def test_predict():
    model = HousePriceRegressor(model_path=PRICE_PRED_MODEL)
    assert model is not None, "Model failed to load from disk"

    features = np.array([[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]])

    price_pred = model.predict(features)

    assert isinstance(price_pred, (np.ndarray))
    assert len(price_pred) == 1
