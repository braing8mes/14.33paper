import pandas as pd
import numpy as np
df = pd.read_csv('mun_avo_prod.txt', sep = "\t", encoding= 'latin-1')
df.columns = ['municipality', 'harvested_area', 'production', 'value', 'year']
df['state'] = np.nan
for i in range(2011,2020):
    #print(df[df['municipality'] == str(i)])
    pass
df.loc[0,'year'] = 2011
df.loc[170, 'year'] = 2012
df.loc[345, 'year'] = 2013
df.loc[525, 'year'] = 2014
df.loc[706, 'year'] = 2015
df.loc[888, 'year'] = 2016
df.loc[1079, 'year'] = 2017
df.loc[1274, 'year'] = 2018
df.loc[1470, 'year'] = 2019
states = ['michoacan', 'nayarit', 'mexico', 'morelos', 'jalisco']
df['municipality'] = df['municipality'].str.lower()
df['municipality'] = df['municipality'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
for i in range(0, len(df)):
    if df.loc[i, 'municipality'] in states:
        df.loc[i, 'state'] = df.loc[i, 'municipality']

df['year'].fillna(method='ffill', inplace=True)
df['state'].fillna(method='ffill', inplace=True)
df = df.drop(df[df['municipality'].isin(states)].index)
years = [str(i) for i in range(2011,2020)]
df = df.drop(df[df['municipality'].isin(years)].index)
cutoff = df.index[df['municipality'] == "2020"].tolist()[0]
df = df.loc[:cutoff-1]
df.to_csv('avo_clean.csv', index=False)
