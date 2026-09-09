import numpy as np
from sklearn.neighbors import NearestNeighbors

from .decorators import log_step


@log_step
def add_price_per_square_foot(dataframe):
    result = dataframe.copy()

    result["sqft_price"] = (
        result["price"] / (result["sqft_living"] + result["sqft_lot"])
    ).round(2)

    return result


@log_step
def add_center_distance(dataframe):
    result = dataframe.copy()

    center_latitude = 47.62774
    center_longitude = -122.24194

    delta_latitude = np.absolute(center_latitude - result["lat"])
    delta_longitude = np.absolute(center_longitude - result["long"])

    result["center_distance"] = (
        (
            (delta_longitude * np.cos(np.radians(47.6219))) ** 2
            + delta_latitude**2
        )
        ** 0.5
        * 2
        * np.pi
        * 6378
        / 360
    )

    return result


@log_step
def add_water_distance(dataframe):
    result = dataframe.copy()

    waterfront_houses = result.loc[
        result["waterfront"] == 1,
        ["lat", "long"],
    ]

    if waterfront_houses.empty:
        raise ValueError("Cannot calculate water_distance without waterfront houses.")

    reference_latitude = waterfront_houses["lat"].to_numpy()
    reference_longitude = waterfront_houses["long"].to_numpy()

    house_latitude = result["lat"].to_numpy()
    house_longitude = result["long"].to_numpy()

    waterfront_coordinates = np.column_stack(
        (
            reference_latitude,
            reference_longitude * np.cos(np.radians(reference_latitude)),
        )
    )

    house_coordinates = np.column_stack(
        (
            house_latitude,
            house_longitude * np.cos(np.radians(house_latitude)),
        )
    )

    nearest_neighbors = NearestNeighbors(n_neighbors=1)
    nearest_neighbors.fit(waterfront_coordinates)

    distances_in_degrees, _ = nearest_neighbors.kneighbors(house_coordinates)

    result["water_distance"] = (
        distances_in_degrees[:, 0] * 2 * np.pi * 6378 / 360
    )

    return result