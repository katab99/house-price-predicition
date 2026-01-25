from pydantic import BaseModel, Field


class Features(BaseModel):
    transaction_date: float
    house_age: float = Field(ge=0)
    dist_to_nearest_mrt_station: float = Field(ge=0)
    num_of_convenience_store: int = Field(ge=0)
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)


class Prediction(BaseModel):
    price: float
