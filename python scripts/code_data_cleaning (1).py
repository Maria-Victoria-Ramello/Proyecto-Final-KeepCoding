import pandas as pd
import numpy as np

uncleansed_df = pd.read_csv('../airbnb-listings.csv', delimiter=";", low_memory=False) 
# El df original está separado por ; para que pueda leerlo bien especifico con delimiter=';' 
 
# Carga del df
df = uncleansed_df[uncleansed_df['State'].astype(str).str.contains('Madrid')]

# Primera selección de columnas con las que vamos a trabajar:
columns_to_keep = ['ID', 'Host ID', 'Host Since', 'Street', 'Neighbourhood', 'Neighbourhood Cleansed', 'City', 'State', 'Zipcode', 'Latitude', 'Longitude', 'Amenities', 'Property Type', \
                   'Room Type', 'Bathrooms', 'Bedrooms', 'Beds', 'Bed Type', 'Square Feet', 'Price', 'Cleaning Fee', 'Availability 365', 'Review Scores Location', 'Cancellation Policy', 'Accommodates']
df = df.loc[:, columns_to_keep]

# Normalización del código postal
replace_values = {'nan': np.nan, '-': np.nan, '28': np.nan, '-' : np.nan, '2802\n28012' : '28012', '28002\n28002': '28002', '28051\n28051' : '28051', 'Madrid 28004': '28004', '2815' : '28015', '2805' : '28005'}
df = df.replace({'Zipcode': replace_values})

# Limpio los nombres de los barrios: me quedo con los valores de 'Neighbourhood' excepto en el caso de los nulls que los sustituyo por el valor de 'Neighbourhood Cleansed'
df['Final_Neighbourhood'] = df.apply(lambda x: x['Neighbourhood Cleansed'] if pd.isnull(x['Neighbourhood']) else x['Neighbourhood'], axis=1)
df = df.drop(['Neighbourhood', 'Neighbourhood Cleansed'], axis=1)

# Conversión del ID de la entrada en numérico en vez de string
df['ID'].astype(int)

# Conversión de las fechas de 'Host Since' en date
df['Host Since'] = pd.to_datetime(df['Host Since'])

df.to_csv('airbnb-listings_cleaned.csv', sep = ';', index = False)