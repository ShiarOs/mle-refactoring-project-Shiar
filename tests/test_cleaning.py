import pandas as pd

from src.cleaning import clean_data


def create_cleaning_dataframe():
    return pd.DataFrame(
        {
            "id": [1, 2],
            "price": [300000, 400000],
            "sqft_living": [1000, 2000],
            "sqft_above": [800, 1500],
            "view": [None, 2],
            "waterfront": [None, 1],
            "yr_built": [1990, 2000],
            "yr_renovated": [None, 2010],
            "lat": [47.5, 47.6],
            "long": [-122.2, -122.3],
        }
    )


def test_clean_data_creates_basement_area():
    dataframe = create_cleaning_dataframe()

    result = clean_data(dataframe)

    assert "sqft_basement" in result.columns
    assert result["sqft_basement"].tolist() == [200, 500]


def test_clean_data_fills_view_and_waterfront():
    dataframe = create_cleaning_dataframe()

    result = clean_data(dataframe)

    assert result["view"].isna().sum() == 0
    assert result["waterfront"].isna().sum() == 0


def test_clean_data_creates_last_known_change():
    dataframe = create_cleaning_dataframe()

    result = clean_data(dataframe)

    assert "last_known_change" in result.columns
    assert result["last_known_change"].tolist() == [1990, 2010]


def test_clean_data_removes_original_year_columns():
    dataframe = create_cleaning_dataframe()

    result = clean_data(dataframe)

    assert "yr_built" not in result.columns
    assert "yr_renovated" not in result.columns


def test_clean_data_does_not_modify_original_dataframe():
    dataframe = create_cleaning_dataframe()
    original_columns = dataframe.columns.tolist()

    clean_data(dataframe)

    assert dataframe.columns.tolist() == original_columns
    assert "sqft_basement" not in dataframe.columns