import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

mammography = pd.read_csv("/Users/davidvv/Documents/Datathon/code/facility_count_by_state.csv")

df = pd.read_csv("/Users/davidvv/Documents/Datathon/code/fifty_df1.csv")
states = {
'AK': 'Alaska',
'AL': 'Alabama',
'AR': 'Arkansas',
'AZ': 'Arizona',
'CA': 'California',
'CO': 'Colorado',
'CT': 'Connecticut',
'DC': 'District of Columbia',
'DE': 'Delaware',
'FL': 'Florida',
'GA': 'Georgia',
'HI': 'Hawaii',
'IA': 'Iowa',
'ID': 'Idaho',
'IL': 'Illinois',
'IN': 'Indiana',
'KS': 'Kansas',
'KY': 'Kentucky',
'LA': 'Louisiana',
'MA': 'Massachusetts',
'MD': 'Maryland',
'ME': 'Maine',
'MI': 'Michigan',
'MN': 'Minnesota',
'MO': 'Missouri',
'MS': 'Mississippi',
'MT': 'Montana',
'NC': 'North Carolina',
'ND': 'North Dakota',
'NE': 'Nebraska',
'NH': 'New Hampshire',
'NJ': 'New Jersey',
'NM': 'New Mexico',
'NV': 'Nevada',
'NY': 'New York',
'OH': 'Ohio',
'OK': 'Oklahoma',
'OR': 'Oregon',
'PA': 'Pennsylvania',
'RI': 'Rhode Island',
'SC': 'South Carolina',
'SD': 'South Dakota',
'TN': 'Tennessee',
'TX': 'Texas',
'UT': 'Utah',
'VA': 'Virginia',
'VT': 'Vermont',
'WA': 'Washington',
'WI': 'Wisconsin',
'WV': 'West Virginia',
'WY': 'Wyoming'
}

for index, row in mammography.iterrows():
    for abr, state in states.items():
        if row['state'] == abr:
            mammography.loc[index,'state'] = state
   


def ratio_calc(df1, df2):
    ratio_dict = defaultdict(int)
    for index, row in df1.iterrows():
        for index2, row2 in df2.iterrows():
            if row['Region'] == row2['state']:
                ratio_dict[row['Region']] = row['Population above 50'] / row2['facility_count']
    data = []
    for region, ratio in ratio_dict.items():
        data.append([region, ratio])
    return data

data = ratio_calc(df, mammography)
ratio_df = pd.DataFrame(data, columns=['State', 'Ratio'])

bargraph2 = ratio_df.plot.bar(x= 'State', y='Ratio', fontsize='5.5', 
color ="#F28E46", title="Ratio of 50+ Population per Facility", grid=True)
    
plt.show()

# ratio_df.to_csv('ratio_df.csv')