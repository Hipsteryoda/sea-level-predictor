import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    year_adds = pd.Series([n for n in range(df.Year.max()+1, 2051)])
    fig, ax = plt.subplots()
    ax0 = plt.scatter(x=df.Year, y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    x = df.Year.append(year_adds)
    res = linregress(x=df.Year, y=df['CSIRO Adjusted Sea Level'])
    ax1 = plt.plot(x, res.intercept+res.slope*x, 'r', label='LOBF')

    # Create second line of best fit
    x = pd.Series([n for n in range(2000, 2050+1)])
    second_res = linregress(x=df.loc[df.Year >= 2000, 'Year'], y=df.loc[df.Year >= 2000, 'CSIRO Adjusted Sea Level'])
    ax2 = plt.plot(x, second_res.intercept+second_res.slope*x, 'g', label='LOBF')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
  
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()