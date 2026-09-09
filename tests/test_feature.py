import pandas as pd

from src.features import (
    add_center_distance,
    add_price_per_square_foot,
)


def test_add_price_per_square_foot():
    dataframe = pd.DataFrame(
        {
            "price": [300000, 400000],
            "sqft_living": [1000, 2000],
        }
    )

    result = add_price_per_square_foot(dataframe)

    assert "sqft_price" in result.columns
    assert result["sqft_price"].tolist() == [300, 200]


def test_add_price_per_square_foot_does_not_modify_original_dataframe():
    dataframe = pd.DataFrame(
        {
            "price": [300000],
            "sqft_living": [1000],
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