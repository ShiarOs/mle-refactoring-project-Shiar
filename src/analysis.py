import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns


HISTOGRAM_COLUMNS = [
    "price",
    "bathrooms",
    "bedrooms",
    "floors",
    "grade",
    "last_known_change",
    "sqft_living",
    "sqft_lot",
]


def plot_histograms(dataframe):
    dataframe[HISTOGRAM_COLUMNS].hist(bins=50, figsize=(20, 15))
    plt.tight_layout()
    plt.show()


def plot_price_boxplot(dataframe):
    figure = px.box(
        dataframe,
        y="price",
        labels={"price": "House Price in $"},
    )
    figure.show()


def plot_pairplot(dataframe):
    sns.pairplot(dataframe[HISTOGRAM_COLUMNS])
    plt.show()


def plot_correlation_heatmap(dataframe):
    numeric_dataframe = dataframe.select_dtypes(include=["number"])
    mask = np.triu(numeric_dataframe.corr())

    plt.figure(figsize=(20, 15))
    sns.heatmap(
        numeric_dataframe.corr().round(2),
        annot=True,
        mask=mask,
        cmap="RdBu_r",
    )
    plt.tight_layout()
    plt.show()


def plot_price_vs_center_distance(dataframe):
    sns.relplot(
        data=dataframe,
        x="center_distance",
        y="price",
    )
    plt.show()


def plot_sqft_price_vs_center_distance(dataframe):
    sns.relplot(
        data=dataframe,
        x="center_distance",
        y="sqft_price",
    )
    plt.show()


def plot_price_vs_water_distance(dataframe):
    sns.relplot(
        data=dataframe,
        x="water_distance",
        y="price",
    )
    plt.show()


def plot_sqft_price_vs_water_distance(dataframe):
    sns.relplot(
        data=dataframe,
        x="water_distance",
        y="sqft_price",
    )
    plt.show()


def plot_houses_map(dataframe):
    figure = px.scatter_map(
        dataframe,
        lat="lat",
        lon="long",
        hover_name="id",
        hover_data=["sqft_price", "sqft_living", "zipcode", "floors"],
        size="sqft_price",
        color="center_distance",
        color_continuous_scale=["green", "yellow", "red"],
        zoom=7.7,
        center={"lat": 47.5, "lon": -122.2},
        height=400,
    )

    figure.update_layout(map_style="open-street-map")
    figure.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    figure.show()


def plot_water_distance_map(dataframe):
    close_to_water = dataframe.query("water_distance <= 5")

    figure = px.scatter_map(
        close_to_water,
        lat="lat",
        lon="long",
        hover_name="id",
        hover_data=["sqft_price", "sqft_living", "zipcode", "floors"],
        size="sqft_price",
        color="water_distance",
        color_continuous_scale=["green", "yellow", "red"],
        zoom=8.4,
        height=400,
    )

    figure.update_layout(map_style="open-street-map")
    figure.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    figure.show()