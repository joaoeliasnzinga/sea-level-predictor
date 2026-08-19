import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    fig, ax = plt.subplots(figsize=(12,6))
    ax.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
    #Regressão Linear
    #Primeira Regressão Linear (1880 - 2050)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope = res.slope
    intercept = res.intercept
    x_pred1 = pd.Series([i for i in range(1880,2051)])
    y_pred1 = slope * x_pred1 + intercept
    ax.plot(x_pred1, y_pred1, color='red')
    #
    #
    df_recent = df[df['Year'] >= 2000]
    res_cent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series([i for i in range(2000, 2051)])
    y_pred2 = res_cent.slope * x_pred2 + res_cent.intercept
    ax.plot(x_pred2, y_pred2,color='green')
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('CSIRO Adjusted Sea Level')

    fig.savefig('sea_level.png')
    return ax



draw_plot()