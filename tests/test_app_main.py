def test_get_health(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_post_predict(client):
    request = {
        "transaction_date": 1.0,
        "house_age": 2.0,
        "dist_to_nearest_mrt_station": 3.0,
        "num_of_convenience_store": 4,
        "latitude": 5.0,
        "longitude": 6.0,
    }

    response = client.post("/predict", json=request)

    assert response.status_code == 200
    assert isinstance(response.json()["price"], float)


def test_post_predict_invalid(client):
    invalid_request = {
        "transaction_date": 1.0,
        "house_age": -2.0,
        "dist_to_nearest_mrt_station": 3.0,
        "num_of_convenience_store": 4,
        "latitude": 5.0,
        "longitude": 6.0,
    }

    response = client.post("/predict", json=invalid_request)

    assert response.status_code == 422


def test_post_predict_missing_field(client):
    missing_field_request = {"house_age": 2.0}
    response = client.post("/predict", json=missing_field_request)
    assert response.status_code == 422
