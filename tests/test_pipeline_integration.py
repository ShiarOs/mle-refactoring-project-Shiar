from pathlib import Path

import pandas as pd

from src.pipeline import load_and_transform_data


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_ROOT / "data" / "King_County_House_prices_dataset.csv"


def test_pipeline_processes_real_dataset():
    result = load_and_transform_data(str(DATA_FILE))

    assert isinstance(result, pd.DataFrame)
    assert len(result) > 0


def test_pipeline_creates_expected_features_in_real_dataset():
    result = load_and_transform_data(str(DATA_FILE))

    expected_columns = {
        "sqft_basement",
        "last_known_change",
        "sqft_price",
        "center_distance",
        "water_distance",
    }

    assert expected_columns.issubset(result.columns)


def test_pipeline_removes_columns_that_should_not_remain():
    result = load_and_transform_data(str(DATA_FILE))

    assert "yr_built" not in result.columns
    assert "yr_renovated" not in result.columns

def test_pipeline_removes_invalid_bedroom_record():
    result = load_and_transform_data(str(DATA_FILE))

    assert 33 not in result["bedrooms"].values

def test_pipeline_does_not_leave_missing_values_in_cleaned_columns():
    result = load_and_transform_data(str(DATA_FILE))

    assert result["view"].isna().sum() == 0
    assert result["waterfront"].isna().sum() == 0
    assert result["last_known_change"].isna().sum() == 0