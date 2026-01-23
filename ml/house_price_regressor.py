from sklearn.base import BaseEstimator
from sklearn.tree import DecisionTreeRegressor
import joblib


class HousePriceRegressor(BaseEstimator):
    def __init__(self, model_path=None):
        if model_path is not None:
            self.model = joblib.load(model_path)
        else:
            self.model = DecisionTreeRegressor()

    def fit(self, X, y):
        self.model.fit(X,y)
        return self

    def predict(self, X):
        return self.model.predict(X)
    
    def save_model(self, filename):
        joblib.dump(self.model, filename, compress=3)
