#k_means clustering algorithm

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

df = pd.read_csv("/Users/davidvv/Documents/Datathon/code/beginner.csv")

df = df.drop(columns = ['Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12'])
colnames = list(df.columns)


# shifts columns over if address 3 exists
def cleaner(df):
    # iterates through the file by position in row
    for index, row in df.iterrows():
        # if the data in Address 3 is a string
        if type(row['Address 3']) is str:
            # if the the data in State is a string
            if type(row['State']) is str:
                # if the data in State is 2 characters long
                if len(row['State']) == 2:
                    continue
                else:
                    # moves the data 1 column to the left
                    df.loc[index,'City'] = df.loc[index,'State']
                    df.loc[index, 'State'] = df.loc[index,'Zip Code']
                    df.loc[index,'Zip Code'] = df.loc[index,'Phone']
                    df.loc[index, 'Phone'] = df.loc[index, 'Fax']

        # while the data in City is a float
        while type(row['City']) is float: 
            # moves the data 1 column to the left
            df.loc[index,'City'] = df.loc[index,'State']
            df.loc[index, 'State'] = df.loc[index,'Zip Code']
            df.loc[index,'Zip Code'] = df.loc[index,'Phone']
            df.loc[index, 'Phone'] = df.loc[index, 'Fax']
    return df

# removes all non states
def cleansing(df):
    # iterate over file by position in row
    for index, row in df.iterrows():
        # if the item at that position in State is a float
        if type(row['State']) is float:
            # remove it from the data set
            df = df.drop(index)
        # if the item at that position is a strong
        elif type(row['State']) is str:
            # if the item is not 2 characters long or if it is a US territory
            if len(row['State']) != 2 or row['State'] in ['GU','AS','AP','VU', 'PR','GI','MP','VI','AE']:
                # drop it from the data set
                df = df.drop(index)
    
        
    return df

df1 = cleaner(df)
cleandf = cleansing(df1)


states = cleandf['State'].value_counts(ascending=False)
zip_codes = cleandf['Zip Code'].value_counts(ascending=False)

bargraph = states.plot.bar(x = 'State', y = 'Number', fontsize='6', 
    color ="Pink", title="Mammography Facilities per State", 
    grid=True, yticks=(0,100,200,300, 400, 500, 600, 700, 800))

plt.show()

print(states)

cleandf.to_csv('export.csv')