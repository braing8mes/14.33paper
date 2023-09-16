import numpy as np
import pandas as pd
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
avo = pd.read_csv('avo_final.csv')
new = avo[avo['year'] >= 2016]
new['production'] = new['production'].apply(str.replace, args=(',', '')).astype(float)
new['value'] = new['value'].apply(str.replace, args=(',', '')).astype(float)
new = new.groupby(['municipality','state']).agg({'production': 'mean', 'value': 'mean'}).reset_index()
a = np.array(new['production'])
print(a.mean())
print(a.std())
print(a.min())
print(a.max())
#new.to_csv('avo_stats.csv', index=False)
