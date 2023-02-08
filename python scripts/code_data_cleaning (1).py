# Importar librerías
import pandas as pd
import numpy as np


uncleansed_df = pd.read_csv('./raw/airbnb-listings.csv', delimiter=";", low_memory=False) 
# El df original está separado por ; para que pueda leerlo bien especifico con delimiter=';' 

# Carga del df
uncleansed_df = uncleansed_df[uncleansed_df['State'].astype(str).str.contains('Madrid')]

# Limpieza de columnas 1º:
columns_to_keep = ['ID', 'Host ID', 'Host Since', 'Street', 'Neighbourhood', 'Neighbourhood Cleansed', 'City', 'State', 'Zipcode', 'Latitude', 'Longitude', \
                   'Amenities', 'Property Type', 'Room Type', 'Bathrooms', 'Bedrooms', 'Beds', 'Bed Type', 'Square Feet', 'Price', 'Cleaning Fee', \
                   'Availability 365', 'Review Scores Location', 'Cancellation Policy', 'Accommodates']

df = uncleansed_df.loc[:, columns_to_keep]

# Normalización del código postal
replace_values = {'nan': np.nan, '-': np.nan, '28': np.nan, '-' : np.nan, '2802\n28012' : '28012', '28002\n28002': '28002', '28051\n28051' : '28051', \
                  'Madrid 28004': '28004', '2815' : '28015', '2805' : '28005'}

df = df.replace({'Zipcode': replace_values})

# Conversión del ID de la entrada en numérico en vez de string
df['ID'].astype(int)

# Conversión de las fechas de 'Host Since' en date
df['Host Since']
df['Host Since'] = pd.to_datetime(df['Host Since'])

# Limpio bien los nombres de los barrios: me quedo con los valores de 'Neighbourhood' excepto en el caso de los nulls que los sustituyo por el valor de 'Neighbourhood Cleansed'
# La columna con estos valores se denomina 'Final_Neighbourhood'
df.loc[df['Neighbourhood'].isnull(), 'Final_Neighbourhood'] = df['Neighbourhood Cleansed']
df.loc[df['Neighbourhood'].notnull(), 'Final_Neighbourhood'] = df['Neighbourhood']

# Limpieza de columnas 2º:
df = df.drop(['Neighbourhood', 'Neighbourhood Cleansed'], axis = 1)

df.to_csv('airbnb-listings_cleaned.csv', sep = ';', index = False)