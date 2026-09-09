import numpy as np
from .decorators import log_step

# Calculate price per square foot feature
@log_step
def add_price_per_square_foot(dataframe):
    result = dataframe.copy()
    result["sqft_price"] = result["price"] / result["sqft_living"]
    return result

# add the center distance feature
@log_step
def add_center_distance(dataframe):
    result = dataframe.copy()
    center_lat = 47.62774
    center_long = -122.24194

    # Absolute difference in latitude between the center and the property.
    delta_lat = np.absolute(center_lat - result["lat"])

    # Absolute difference in longitude between the center and the property.
    delta_long = np.absolute(center_long - result["long"])

    # Distance between the center and the property.
    result["center_distance"] = (
        (delta_long * np.cos(np.radians(center_lat))) ** 2 + delta_lat ** 2
    ) ** (1/2) * 2 * np.pi * 6378 /360
    
    return result
