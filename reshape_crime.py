import pandas as pd
import numpy as np
df = pd.read_csv('combined_crime.csv')
homicide = df[df['tipo'] == 'homicidio'].drop(['tipo'], axis=1)
crime = df.groupby(['entidad', 'inegi', 'año', 'municipio'], as_index=False).agg({'enero': 'sum', 'febrero': 'sum', 'marzo': 'sum', 'abril': 'sum',
                                                                                      'mayo': 'sum', 'junio': 'sum', 'julio': 'sum', 'agosto': 'sum', 
                                                                          'septiembre': 'sum', 'octubre': 'sum', 'noviembre': 'sum', 'diciembre': 'sum'})
#homicide.to_csv('homicide.csv', index=False)
#crime.to_csv('crime.csv', index=False)
homicide_out = homicide.melt(id_vars = ['entidad', 'inegi', 'año', 'municipio'], value_vars= ['enero', 'febrero', 'marzo', 'abril',
                                                                                  'mayo', 'junio', 'julio', 'agosto', 'septiembre', 
                                                                                  'octubre', 'noviembre', 'diciembre'], var_name='month', 
                                                                                  value_name='homicides')
crime_out = crime.melt(id_vars = ['entidad', 'inegi', 'año', 'municipio'], value_vars= ['enero', 'febrero', 'marzo', 'abril',
                                                                                  'mayo', 'junio', 'julio', 'agosto', 'septiembre', 
                                                                                  'octubre', 'noviembre', 'diciembre'], var_name='month', 
                                                                                  value_name='crimes')

months = {'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6, 
          'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12}
homicide_out['xmonth'] = homicide_out.apply(lambda row: 12*(int(row.año)-2011)+months[row.month], axis=1)
crime_out['xmonth'] = crime_out.apply(lambda row: 12*(int(row.año)-2011)+months[row.month], axis=1)
#crime_out['xmonth'] = int(crime_out['año'])-2011 + months[crime_out['month']]

homicide_out.to_csv('homicide_reshaped.csv', index=False)
crime_out.to_csv('crime_reshaped.csv', index=False)
#df.to_csv('reshaped_crime.csv', index=False)