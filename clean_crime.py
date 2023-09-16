import pandas as pd
import numpy as np
old = pd.read_csv('crime_municipal_2011-17.csv', encoding='latin-1')
new = pd.read_csv('crime_municipal_2015-23.csv', encoding='latin-1')

# Change column names to lower case
old.columns=old.columns.str.lower()
new.columns=new.columns.str.lower()
for col in old.columns:
    if old[col].dtype == object:
        old[col] = old[col].astype(str).str.lower()
for col in new.columns:
    if new[col].dtype == object or new[col].dtype == str:
        new[col] = new[col].astype(str).str.lower()
new['entidad']=new['entidad'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
# Keep states of interest
states = ['michoacan', 'nayarit', 'mexico', 'morelos', 'jalisco']
old = old[old['entidad'].isin(states)]
new = new[new['entidad'].isin(states)]
print('# of municipalities in old: ',old['municipio'].nunique())
print('# of municipalities in new: ',new['municipio'].nunique())
# Keep crimes of interest
old = old[(old['tipo'] == 'dolosos') | (old['tipo'] == 'extorsion')]
new = new[(new['subtipo de delito'] == 'homicidio doloso') | (new['subtipo de delito'] == 'extorsión')]





# Keep years of interest
old = old[(old['año'] >= 2011) & (old['año'] <= 2014)]
new = new[(new['año'] >= 2015) & (new['año'] <= 2019)]

#old.to_csv('clean_crime_2011-14.csv', index=False)
#new.to_csv('clean_crime_2015-19.csv', index=False)