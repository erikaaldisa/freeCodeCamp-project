import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    fig = plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    bestfitx1 = np.arange(df["Year"].min(), 2051, 1)
    bestfity1 = bestfitx1*res.slope + res.intercept
    fig = plt.plot(bestfitx1, bestfity1, 'r')

    # Create second line of best fit
    df_2000 = df[df["Year"]>=2000]
    res2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    bestfitx2 = np.arange(2000, 2051, 1)
    bestfity2 = bestfitx2*res2000.slope + res2000.intercept
    fig = plt.plot(bestfitx2, bestfity2, 'g')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()