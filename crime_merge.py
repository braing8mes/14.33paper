import pandas as pd
import numpy as np
old = pd.read_csv('clean_crime_2011-14.csv')
new = pd.read_csv('clean_crime_2015-19.csv')

# group homicide counts together by month and municipality
old['tipo'] = old['tipo'].map({'dolosos': 'homicidio', 'extorsion': 'extorsion'})
old = old.groupby(['entidad', 'inegi', 'año', 'municipio', 'tipo']).agg({'enero': 'sum', 'febrero': 'sum', 'marzo': 'sum', 'abril': 'sum',
                                                                          'mayo': 'sum', 'junio': 'sum', 'julio': 'sum', 'agosto': 'sum', 
                                                                          'septiembre': 'sum', 'octubre': 'sum', 'noviembre': 'sum', 'diciembre': 'sum'})
old = old.reset_index()
new.rename({'cve. municipio': 'inegi'}, axis=1, inplace=True)
new.rename({'tipo de delito': 'tipo'}, axis=1, inplace=True)
#new['tipo'] = new['tipo'].map({'extorsión': 'extorsion', 'homocidio': 'homicidio'})
new['municipio']=new['municipio'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
old['municipio']=old['municipio'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
new['tipo']=new['tipo'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

new = new.groupby(['entidad', 'inegi', 'año', 'municipio', 'tipo']).agg({'enero': 'sum', 'febrero': 'sum', 'marzo': 'sum', 'abril': 'sum',
                                                                                      'mayo': 'sum', 'junio': 'sum', 'julio': 'sum', 'agosto': 'sum', 
                                                                          'septiembre': 'sum', 'octubre': 'sum', 'noviembre': 'sum', 'diciembre': 'sum'}) 
new = new.reset_index()
print('number of municipalities in both: ',len(set(old['inegi']).intersection(set(new['inegi']))))

print('old # of municipalities after groupby: ',old['inegi'].nunique())
print('new # of municipalities after groupby: ',new['inegi'].nunique())
combined = pd.concat([old, new], ignore_index=True)
print('combined # of municipalities: ',combined['inegi'].nunique())
print("year breakdown: ", combined['año'].value_counts())
combined.replace({'municipio':{'acambay de ruiz castaneda': 'acambay', 
                               'tlaltizapan de zapata': 'tlaltizapan',
                               'zacualpan de amilpas': 'zacualpan',
                               'san pedro tlaquepaque': 'tlaquepaque',
                               'jonacatepec de leandro valle': 'jonacatepec',
                               }},inplace=True)

#a = combined['inegi'].value_counts(sort=True, ascending=True)
#a.to_csv('municipality_counts.csv')
v = combined.inegi.value_counts()
out = combined[combined.inegi.isin(v.index[v.gt(13)])]
print("year breakdown: ", out['año'].value_counts())
out.to_csv('combined_crime.csv', index=False)
#combined.to_csv('combined_crime.csv', index=False)