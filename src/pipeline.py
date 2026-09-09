import pandas as pd

from .cleaning import clean_data, remove_invalid_bedroom_records
from .features import (add_center_distance, add_price_per_square_foot, add_water_distance,)


PIPELINE_STEPS = [
    remove_invalid_bedroom_records,
    clean_data,
    add_price_per_square_foot,
    add_center_distance,
    add_water_distance,
]


def load_and_transform_data(path):
    dataframe = pd.read_csv(path)

    for step in PIPELINE_STEPS:
        dataframe = step(dataframe)

    return dataframe