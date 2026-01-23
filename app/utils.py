from pydantic import BaseModel 
import numpy as np

def convert_data_to_array(data_model : BaseModel):
    data_dict = data_model.model_dump()
    data_list = list(data_dict.values())
    np_array = np.array(data_list).reshape(1, -1)
    return np_array
    