import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # First line of best fit (1880–latest year)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years_extended = np.arange(df['Year'].min(), 2051)
    sea_levels = res.slope * years_extended + res.intercept

    plt.plot(years_extended, sea_levels, 'r')

    # Second line of best fit (from year 2000)
    df_recent = df[df['Year'] >= 2000]

    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    years_recent = np.arange(2000, 2051)
    sea_levels_recent = res_recent.slope * years_recent + res_recent.intercept

    plt.plot(years_recent, sea_levels_recent, 'g')

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save and return plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()
