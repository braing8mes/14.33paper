import pandas as pd
import numpy as np
import locale
from locale import atof
from math import log
from statistics import median
locale.setlocale(locale.LC_NUMERIC, '')
data = pd.read_csv('avo_clean.csv')

# drop munucipios with not all years of data
data = data.groupby('municipality').filter(lambda x: len(x) >= 7)
#data.to_csv('avo_final.csv', index=False)

always_produce = {}
treatment = {}
data.drop(data[(data['municipality'] == 'villa guerrero')&(data.state=='jalisco')].index, inplace=True)
data.drop(data[(data['municipality'] == 'santa maria del oro')&(data.state=='jalisco')].index, inplace=True)
#print(data['municipality'].value_counts())
data.to_csv('avo_final.csv', index=False)
data['value'] = data['value'].apply(atof)
data['value'] = data['value'].astype(float)
total = []
for mun in data['municipality'].unique():
    #always_produce[mun] = 0
    #treatment[mun] = 0
    old = data.loc[(data['municipality'] == mun)&(data['year'] < 2016)]
    new = data.loc[(data['municipality'] == mun)&(data['year'] >= 2016)]
    if old['value'].mean()*2.5 < new['value'].mean():
        treatment[mun] = new['value'].mean()
        if old['value'].mean() > 0:
            total.append(new['value'].mean()/old['value'].mean())
    else:
        always_produce[mun] = new['value'].mean()
        total.append(new['value'].mean()/old['value'].mean())
#print('# of municipalities:', len(data['municipality'].unique()))
#print('always produce:', len(always_produce))
#print('treatment:', len(treatment))
#print(treatment)
crime = pd.read_csv('crime_demo.csv')
homicides = pd.read_csv('homicides_demo.csv')
crime['treat'] = 0
homicides['treat'] = 0
crime['treat'] = crime.apply(lambda row: log(treatment[row['municipio']]) if (row['municipio'] in treatment.keys() and row['xmonth'] >= 67) else 0, axis=1)
homicides['treat'] = homicides.apply(lambda row: log(treatment[row['municipio']]) if (row['municipio'] in treatment.keys() and row['xmonth'] >= 67) else 0, axis=1)
crime['treat'] = crime.apply(lambda row: log(always_produce[row['municipio']]) if row['municipio'] in always_produce.keys() else row['treat'], axis=1)
homicides['treat'] = homicides.apply(lambda row: log(always_produce[row['municipio']]) if row['municipio'] in always_produce.keys() else row['treat'], axis=1)
crime.to_csv('crime_final.csv', index=False)
homicides.to_csv('homicides_final.csv', index=False)
#print('# municipalities: ', len(crime['municipio'].unique()))
#print('# treated: ', len(set(crime['municipio'].unique()).intersection(treatment.keys())))
#print('# always produce: ', len(set(crime['municipio'].unique()).intersection(always_produce.keys())))
#print('treated: ', set(crime['municipio'].unique()).intersection(treatment.keys()))
#print('always produce: ', set(crime['municipio'].unique()).intersection(always_produce.keys()))
test_crime = crime[crime['xmonth'] <= 60]
test_homicides = homicides[homicides['xmonth'] <= 60]
#test_crime.to_csv('crime_final_test.csv', index=False)
#test_homicides.to_csv('homicides_final_test.csv', index=False)
#print(sum(list(treatment.values()))/len(treatment))
#print(median(total))
tot = []
tot2 = []
tot3 = []
tot4 = []
for mun in crime['municipio'].unique():
    if mun not in treatment.keys() and mun not in always_produce.keys():
        tot.append(crime[(crime['municipio'] == mun)&(crime['año']<2016)]['crime_pc'].mean())
        tot2.append(crime[(crime['municipio'] == mun)&(crime['año']>=2016)]['crime_pc'].mean())
    else:
        tot3.append(crime[(crime['municipio'] == mun)&(crime['año']<2016)]['crime_pc'].mean())
        tot4.append(crime[(crime['municipio'] == mun)&(crime['año']>=2016)]['crime_pc'].mean())
print(sum(tot)/len(tot))
print(sum(tot2)/len(tot2))
print(sum(tot3)/len(tot3))
print(sum(tot4)/len(tot4))