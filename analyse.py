from src.analysis import (
    plot_correlation_heatmap,
    plot_histograms,
    plot_houses_map,
    plot_pairplot,
    plot_price_boxplot,
    plot_price_vs_center_distance,
    plot_price_vs_water_distance,
    plot_sqft_price_vs_center_distance,
    plot_sqft_price_vs_water_distance,
    plot_water_distance_map,
)
from src.pipeline import load_and_transform_data


DATA_FILE = "data/King_County_House_prices_dataset.csv"


def main():
    dataframe = load_and_transform_data(DATA_FILE)

    plot_histograms(dataframe)
    plot_price_boxplot(dataframe)
    plot_pairplot(dataframe)
    plot_correlation_heatmap(dataframe)
    plot_price_vs_center_distance(dataframe)
    plot_sqft_price_vs_center_distance(dataframe)
    plot_price_vs_water_distance(dataframe)
    plot_sqft_price_vs_water_distance(dataframe)
    plot_houses_map(dataframe)
    plot_water_distance_map(dataframe)


if __name__ == "__main__":
    main()