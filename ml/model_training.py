import pandas as pd
from .house_price_regressor import HousePriceRegressor
from sklearn.model_selection import train_test_split
from config import REAL_ESTATE_DATA, PRICE_PRED_MODEL

house_data = pd.read_csv(REAL_ESTATE_DATA)

# featuring columns from `data_exploration.ipynb`
features = [
    "X1 transaction date",
    "X2 house age",
    "X3 distance to the nearest MRT station",
    "X4 number of convenience stores",
    "X5 latitude",
    "X6 longitude",
]

# create training and validation data
X = house_data[features]
y = house_data["Y house price of unit area"]
X_train, X_val, y_train, y_val = train_test_split(X, y, random_state=0)

# training model
model = HousePriceRegressor()
model.fit(X_train.values, y_train.values)

# export trained model
model.save_model(PRICE_PRED_MODEL)
