# Importar librerías
import pandas as pd
import numpy as np
import re
from sqlalchemy import create_engine

# Lectura de los ficheros
raw_file = '../airbnb-listings.csv'
df = pd.read_csv(raw_file, delimiter=";", low_memory=False)

# Seleccionar comunidad de Madrid
madrid_condition = df['State'].astype(str).str.contains('Madrid')
df = df[madrid_condition]

# Selección de columnas con las que se va a trabajar
columns_to_keep = ['ID', 'Host ID', 'Host Since', 'Neighbourhood', 'Neighbourhood Cleansed', 'City', 'State', 'Zipcode', 'Latitude', 'Longitude', \
                   'Amenities', 'Property Type', 'Room Type', 'Bathrooms', 'Bedrooms', 'Beds', 'Bed Type', 'Square Feet', 'Cleaning Fee', \
                   'Availability 365', 'Review Scores Location', 'Cancellation Policy', 'Accommodates', 'Reviews per Month', 'Minimum Nights', 'Price', 'Monthly Price', 'Weekly Price']
df = df[columns_to_keep]

# Normalizar códigos postales
replace_values = {'nan': np.nan, '-': np.nan, '28': np.nan, '-' : np.nan, '2802\n28012' : '28012', '28002\n28002': '28002', '28051\n28051' : '28051', 'Madrid 28004': '28004', '2815' : '28015', '2805' : '28005'}
df = df.replace({'Zipcode': replace_values})

# Conversión de las fechas de 'Host Since' en date
df['Host Since'] = pd.to_datetime(df['Host Since'])

# Analizamos qué columnas necesitan normalización textual
str_columns = ['Neighbourhood', 'City', 'State', 'Property Type', 'Room Type', 'Bed Type', 'Cancellation Policy']

# Función para eliminar los caracteres no alfa-numéricos y los dobles espacios
def no_alfa_num(text):
    characters = '-|_|\(|\)|  '
    for character in text:
        match = re.search(characters, text)
        if match:
            text = text.replace(match.group(0), ' ')
    return text

# Función para normalizar tildes y eñes
def normalize(text):
    characters = (('á', 'a'), ('é', 'e'), ('í', 'i'), ('ó', 'o'), ('ú', 'u'), ('ñ', 'n'))
    for a, b in characters:
        text = text.replace(a, b).replace(a.upper(), b.upper())
    return text

# Normalización de las columnas de texto
for column in df.columns:
    if column in str_columns:
        column_normalized = list(map(normalize, list(map(no_alfa_num, df[column].astype(str)))))
        df[column] = column_normalized

# Limpio los nombres de los barrios: me quedo con los valores de 'Neighbourhood' excepto en el caso de los nulls que los sustituyo por el valor de 'Neighbourhood Cleansed'
df['Neighbourhood'] = df['Neighbourhood'].fillna(df['Neighbourhood Cleansed'])
df = df.drop('Neighbourhood Cleansed', axis = 1)

# Se crea una nueva columna con la tasa de ocupación calculada según la fórmula
def calculate_ocupacy(reviews_month, min_nights, availability):
    return reviews_month * min_nights * 12 / availability

reviews = df['Reviews per Month'].fillna(0)
nights = df['Minimum Nights'].fillna(0)
availability = df['Availability 365'].fillna(0).map(lambda value: value if value != 0 else 9999999)

df['Ocupacy'] = calculate_ocupacy(reviews, nights, availability)

# Agrupar los 'Property Type' por los que interesan u otros
valid_property_types = ['House', 'Apartment', 'Bed & Breakfast', 'Condominium', 'Loft', 'Chalet', 'Hostal']
df['Property Type'] = df['Property Type'].map(lambda value: value if value in valid_property_types else 'Other')

# A partir de la columna 'Amenities' creo una columna por cada uno de los elementos. Además estas columnas pasan a ser un nuevo df.
df_amenities = df.Amenities.str.get_dummies(sep=',').astype(bool).join(df[['ID', 'Price']])
amenities_to_keep = ['ID', 'Price', 'Self Check-In', 'Smartlock', 'Air conditioning', 'Elevator in building', 'Essentials', 'Internet', 'Heating', 'Pets allowed', 'Smoking allowed', 'Pool', 'TV', 'Kitchen', 'Gym']
df_amenities = df_amenities[amenities_to_keep]

df = df.drop('Amenities', axis=1) # borro la columna 'Amenities' del df original