import pandas as pd

from src.features import (
    add_center_distance,
    add_price_per_square_foot,
    add_water_distance,
)


def test_add_price_per_square_foot():
    dataframe = pd.DataFrame(
        {
            "price": [300000, 400000],
            "sqft_living": [1000, 2000],
            "sqft_lot": [1000, 2000],
        }
    )

    result = add_price_per_square_foot(dataframe)

    assert "sqft_price" in result.columns
    assert result["sqft_price"].tolist() == [150.0, 100.0]


def test_add_price_per_square_foot_does_not_modify_original_dataframe():
    dataframe = pd.DataFrame(
        {
            "price": [300000],
            "sqft_living": [1000],
            "sqft_lot": [1000],
        }
    )

    add_price_per_square_foot(dataframe)

    assert "sqft_price" not in dataframe.columns


def test_add_center_distance():
    dataframe = pd.DataFrame(
        {
            "lat": [47.62774],
            "long": [-122.24194],
        }
    )

    result = add_center_distance(dataframe)

    assert "center_distance" in result.columns
    assert result["center_distance"].iloc[0] == 0


def test_add_water_distance():
    dataframe = pd.DataFrame(
        {
            "lat": [47.62774, 47.63774],
            "long": [-122.24194, -122.24194],
            "waterfront": [1, 0],
        }
    )

    result = add_water_distance(dataframe)

    assert "water_distance" in result.columns
    assert result["water_distance"].iloc[0] == 0
    assert result["water_distance"].iloc[1] > 0