import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Create first line of best fit (using all data)
    slope1, intercept1, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)
    sea_level_fit1 = [slope1 * year + intercept1 for year in years_extended]
    plt.plot(years_extended, sea_level_fit1, label='Best Fit (1880-2050)', color='blue')

    # Create second line of best fit (using data from 2000 onwards)
    data_recent = data[data['Year'] >= 2000]
    slope2, intercept2, r_value, p_value, std_err = linregress(data_recent['Year'], data_recent['CSIRO Adjusted Sea Level'])
    years_extended = range(2000, 2051)  # Adjusted to start at 2000 for the second line
    sea_level_fit2 = [slope2 * year + intercept2 for year in years_extended]
    plt.plot(years_extended, sea_level_fit2, label='Best Fit (2000-2050)', color='red')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
