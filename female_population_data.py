import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

df = pd.read_csv("/Users/davidvv/Documents/Datathon/code/sc-est2019-agesex-civ.csv")

xx_df = df[df['SEX'] == 2]
# xx_df.to_csv('female_data.csv')

def growth_calc(df):
    # set growths as an Default Dictionary
    growths = defaultdict(int)
    # for each item at each position in a list of all rows
    for index, row in df.iterrows():
        # if the value for age is 999 (which is what State ages are)
        if row['AGE'] == 999:
            # calculate the growth ratio between 2010 and 2019
            est_growth = ((row['POPEST2019_CIV'] - row['ESTBASE2010_CIV']) /row['ESTBASE2010_CIV'])*100 
            # set the ratio as the value in growths with the State name as the key
            growths[row['NAME']] = est_growth
    data = []
    for region, growth in growths.items():
        data.append([region,growth])
    return data


data = growth_calc(xx_df)

growth_df = pd.DataFrame(data, columns=['Estimated Growth (%)', 'Region'])
bargraph = growth_df.plot.barh(x = 'Estimated Growth (%)', y = 'Region', fontsize='5.5', 
    color ="#A3C585", title="Estimated Percentage Growth In Female Population Since 2010", label='Growth', 
    grid=True, yticks=(-5, -2.5, 0, 5, 10, 15, 20))


# plt.show()

def fifty_plus(df, data):
    older_pop = defaultdict(int)
    for index, row in df.iterrows():
        if row['AGE'] >= 50 and row['AGE'] != 999 and row['NAME'] != 'United States':
            older_pop[row['NAME']] += row[data]
    data_array = []
    for region, population in older_pop.items():
        data_array.append([region, population])
    return data_array

data2 = fifty_plus(xx_df, 'ESTBASE2010_CIV')
fifty_df1 = pd.DataFrame(data2, columns=['Region', 'Population above 50'])

def growth_calc2(df):
    fifty_growths = defaultdict(int)
    for index, row in df.iterrows():
        if row['AGE'] >= 50 and row['AGE'] != 999:
            est_growth = ((row['POPEST2019_CIV'] - row['ESTBASE2010_CIV']) /row['ESTBASE2010_CIV'])*100 
            fifty_growths[row['NAME']] = est_growth
    data3 = []
    for region, population in fifty_growths.items():
        data3.append([region, population])
    return data3

data3 = growth_calc2(xx_df)

fifty_growth_df = pd.DataFrame(data3, columns=['Population Growth % (Above 50)', 'Region'])

# bargraph2 = fifty_df1.plot.bar(x= 'Region', y='Population above 50', fontsize='5.5', 
#     color ="purple", title="50+ Female Population",label='Population', 
#     grid=True, yticks=(1500000, 3000000, 4500000, 6000000))

# bargraph3 = fifty_growth_df.plot.barh(x = 'Population Growth % (Above 50)', y = 'Region', fontsize='5.5', 
#     color ="#A3C585", title="Estimated Percentage Growth In 50+ Females Since 2010",label='Growth', 
#     grid=True, yticks=(-5, -2.5, 0, 5, 10, 15, 20))

plt.show()
# percentage_growth.to_csv('percentage_growth.csv')
fifty_df1.to_csv('fifty_df1.csv')
