import logging

from src.pipeline import load_and_transform_data

logging.basicConfig(level=logging.INFO) # Set up logging to display INFO level messages


dataframe = load_and_transform_data(
    "data/King_County_House_prices_dataset.csv"
)

print(dataframe.head())
print(dataframe.shape)
print(dataframe.columns.tolist())