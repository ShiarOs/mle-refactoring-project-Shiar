import pandas as pd

from .cleaning import clean_data
from .features import add_center_distance, add_price_per_square_foot

PIPELINE_STEPS = [
    clean_data,
    add_price_per_square_foot,
    add_center_distance
]

def load_and_transform_data(path):
    dataframe = pd.read_csv(path)
    for step in PIPELINE_STEPS:
        dataframe = step(dataframe)
    return dataframe