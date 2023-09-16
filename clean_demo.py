import pandas as pd
import numpy as np
jalisco = pd.read_csv('demographics\ITER2020 - 14 Jalisco.csv')
mexico = pd.read_csv('demographics\ITER2020 - 15 Mexico.csv')
michoacan = pd.read_csv('demographics\ITER2020 - 16 Michoacan de Ocampo.csv')
morelos = pd.read_csv('demographics\ITER2020 - 17 Morelos.csv')
nayarit = pd.read_csv('demographics\ITER2020 - 18 Nayarit.csv')

data = [jalisco, mexico, michoacan, morelos, nayarit]
for each in data:
    each.columns = each.columns.str.lower()
    each['nom_ent'] = each['nom_ent'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8').str.lower()
    each['nom_mun'] = each['nom_mun'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8').str.lower()
    each['nom_loc'] = each['nom_loc'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8').str.lower()
    each['graproes'].replace('*', np.nan, inplace=True)
    each['graproes'].replace('N/D', np.nan, inplace=True)
    each['graproes'] = each.graproes.astype(float)
    each['graproes'].fillna(each['graproes'].mean(), inplace=True)
    each = each[each['nom_loc']=='total del municipio']
for each in data:
    each.to_csv('demographics\clean_'+each['nom_ent'][0]+'.csv', index=False)
out = pd.concat(data)
out = out[out['nom_loc'] == 'total del municipio']
out.to_csv('demographics\clean_demo.csv', index=False)