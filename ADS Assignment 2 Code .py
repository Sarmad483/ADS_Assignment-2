import pdb

import matplotlib.pyplot
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plot
import os
#Reading csv file
input_csv = os.getcwd() + "\\ClimateChange.csv"
#Filtering countries due to large amount of data
countries_1 = ['Andorra', 'Austria','Barbados' , 'Germany']
countries_2 = ['United States', 'Central African Republic', 'Germany', 'Chile', 'Bolivia', 'Congo, Dem. Rep.', 'Libya']
countries_3 = ['Cuba', 'United Kingdom', 'Djibouti', 'Belgium', 'Ecuador']

#Function to make dataframe
def read_file(input_csv):
    first_df_filter = pd.read_csv(input_csv, skiprows=4)
    first_df_filter = first_df_filter.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])
    first_df_filter = first_df_filter.dropna(how='all')
    first_df_filter = first_df_filter.set_index('Country Name')
    second_df_filter = first_df_filter.T

    return first_df_filter, second_df_filter


# two dataframes
first_df_filter, second_df_filter = read_file(input_csv)
print(first_df_filter.loc[countries_1, '2014'].describe())

plot.figure(facecolor='lightblue')
sns.boxplot(x='Country Name', y='2011', data=first_df_filter.loc[countries_1].reset_index(), color="red")
plot.ylabel('CO2 emissions (kt)')
mng = plot.get_current_fig_manager()
# mng.window.state('zoomed')
plot.show()
# pdb.set_trace()
def bar_chart():
    bar_data = os.getcwd() + "\\ClimateChange.csv"
    bar_data = pd.read_csv(bar_data, skiprows=4)
    bar_data = bar_data.drop_duplicates(subset=["Country Name"], keep='first').tail(6)
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
#Plotting bar chart
    plt.bar(bar_data["Country Name"], bar_data["2021"], width=0.8, color=bar_colors)
    plt.ylabel('Urban population data of 2021')
    plt.xlabel('Countries')
    plt.show()
    #Calling function
bar_chart()
#plotting another graph
first_df_filter.loc[countries_2, '2009':].plot(color="blue")
plot.ylabel('Community health workers (per 1,000 people)')
mng = plot.get_current_fig_manager()
# mng.window.state('zoomed')
plot.show()

#Plotting graph
sns.boxplot(x='Country Name', y='2005', data=first_df_filter.loc[countries_3].reset_index(), color="blue")
first_df_filter.loc[countries_3, '2005':].plot()
plot.ylabel('Methane emissions (kt of CO2 equivalent)')
mng = plot.get_current_fig_manager()
# mng.window.state('zoomed')
plot.show()