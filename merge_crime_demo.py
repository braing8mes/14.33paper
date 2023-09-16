import pandas as pd
import numpy as np

avo = pd.read_csv('avo_clean.csv')
crime = pd.read_csv('crime_reshaped.csv')
homicides = pd.read_csv('homicide_reshaped.csv')
demo = pd.read_csv('demographics\clean_demo.csv')
demo.rename({'nom_mun': 'municipio'}, axis=1, inplace=True)
demo['inegi'] = demo.apply(lambda row: 1000*row['entidad']+row['mun'], axis=1)
demo['inegi'] = demo['inegi'].astype('int64')

#crime.merge(demo, on='inegi', how='left')

pop_dict = dict(zip(demo['inegi'], demo['pobtot']))
crime['pop'] = crime['inegi'].map(pop_dict)
homicides['pop'] = homicides['inegi'].map(pop_dict)
graproe_dict = dict(zip(demo['inegi'], demo['graproes']))
crime['educ'] = crime['inegi'].map(graproe_dict)
homicides['educ'] = homicides['inegi'].map(graproe_dict)

# calculate per capita crime
crime['crime_pc'] = crime.apply(lambda row: row['crimes']/row['pop']*100000, axis=1)
homicides['homicides_pc'] = homicides.apply(lambda row: row['homicides']/row['pop']*100000, axis=1)

crime.to_csv('crime_demo.csv', index=False)
homicides.to_csv('homicides_demo.csv', index=False)
