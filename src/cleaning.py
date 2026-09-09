
import numpy as np
from .decorators import log_step

@log_step
def clean_data(dataframe):
    result = dataframe.copy() # create a copy of the original dataframe to avoid modifying it directly
    result["sqft_basement"] = result["sqft_living"] - result["sqft_above"]
    result["view"] = result["view"].fillna(0) # fill missing values in the "view" column with 0]
    result["waterfront"] = result["waterfront"].fillna(0) # fill missing values in the "waterfront" column with 0

    result["last_known_change"] = np.where(
        (result["yr_renovated"].isna()) | (result["yr_renovated"] == 0),
        result["yr_built"],
        result["yr_renovated"]
    )
    result = result.drop(columns=["yr_built", "yr_renovated"])
    
    # print(result.head()) # print the first few rows of the cleaned dataframe for debugging
    return result