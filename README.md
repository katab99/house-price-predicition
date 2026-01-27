# House Price Prediction Service

## About

This project implements a house price prediction service, which consists of 2 main parts;
a house price predictor model and a REST API to predict values through with the model.

- `/ml` : contains anything machine learning related, the interface to the predictor model, and also the training script of the model. The model is a decision tree regressor by default.
- `/app` : implements the API using FastAPI. The API consists 2 endpoints:
  - `GET /health` : returns an OK status as response
  - `POST /predict` : to a request with features responds with a price prediction

Example request body to `POST /predict`.

```
{
    "transaction_date": 1.0,
    "house_age": 2.0,
    "dist_to_nearest_mrt_station": 3.0,
    "num_of_convenience_store": 4,
    "latitude": 5.0,
    "longitude": 6.0,
}
```

`config.py` consists resource paths that can be defined through environment variables:

- `DATA_DIR` : points to the data folder of the repository (default: `./data`)
- `MODELS_DIR` : the folder that contains the trained models (`./data/models`)
- `REAL_ESTATE_DATA` : the data that the model is trained on (`./data/real_estate.csv`)
- `PRICE_PRED_MODEL` : the trained model used by the API (`./data/models/model.joblib`)

The Docker image does not contain anything from folders `/data` and `/tests`. The model file(s) are mounted through volumes to the docker image.

## Development

1. Clone the repository and install dependencies.

```
git clone https://github.com/katab99/house-price-predicition.git
cd house-price-prediction
pip install -r requirements.txt
```

2. To run the training of a model

```
python -m ml.model_training
```

3. To run the API

```
fastapi dev app/main.py
```

## Testing

Install the testing dependencies

```
pip install pytest httpx
```

To run the tests, run the command below.

```
python -m pytest
```

## Building Docker

```
docker build -t house-price-api:latest .
```

## Running Docker with Prod

```
docker compose up
```
