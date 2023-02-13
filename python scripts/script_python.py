# Librerías y funciones que vamos a utilizar
import pandas as pd
import numpy as np
import re

# Elimina los caracteres no alfa-numéricos y los dobles espacios
def no_alfa_num(text):
    characters = '-|_|\(|\)|  '
    for character in text:
        match = re.search(characters, text)
        if match:
            text = text.replace(match.group(0), ' ')
    return text

# Normaliza tildes y eñes
def normalize(text):
    characters = (('á', 'a'), ('é', 'e'), ('í', 'i'), ('ó', 'o'), ('ú', 'u'), ('ü', 'u'), ('ñ', 'n'))
    for a, b in characters:
        text = text.replace(a, b).replace(a.upper(), b.upper())
    return text

# Calcula la tasa de ocupación
def calculate_occupancy(reviews_month, min_nights, availability):
    return reviews_month * min_nights * 12 / availability

# Cargamos el fichero original
raw_file = '../subject/airbnb-listings.csv'
df = pd.read_csv(raw_file, delimiter=";", low_memory=False)

# Seleccionamos las filas correspondientes a la Comunidad de Madrid y las columnas con las que vamos a trabajar
rows_to_keep = df['State'].astype(str).str.contains('Madrid')
columns_to_keep = ['ID', 'Host ID', 'Host Since', 'Neighbourhood', 'Neighbourhood Cleansed', 'City', 'State', 'Zipcode', 'Latitude', 'Longitude', 'Amenities', 'Property Type', 'Room Type', 'Bathrooms', 'Bedrooms', 'Beds', 'Bed Type', 'Square Feet', 'Cleaning Fee', 'Availability 365', 'Review Scores Location', 'Cancellation Policy', 'Accommodates', 'Reviews per Month', 'Minimum Nights', 'Price', 'Monthly Price', 'Weekly Price']
df = df.loc[rows_to_keep, columns_to_keep]

# Normalizamos los valores de la columna 'Zipcode'
zp_normalization = {'nan':np.nan, '-':np.nan, '28':np.nan, '2802\n28012':'28012', '28002\n28002':'28002', '28051\n28051':'28051', 'Madrid 28004':'28004', '2815':'28015', '2805':'28005', '20126':np.nan, '2804':'28004', '27013':'28013', '2015':'28015', '27004':'28004', '25008':'28008', '20013':'28013', '280013':'28013'}
df = df.replace({'Zipcode': zp_normalization})

# Convertimos los datos de la columna 'Host Since' en tipo fecha
df['Host Since'] = pd.to_datetime(df['Host Since'])

# Cambiamos los valores nulos de la columna 'Neighbourhood' por el valor correspondiente de la columna 'Neighbourhood Cleansed', eliminamos esta última
df['Neighbourhood'] = df['Neighbourhood'].fillna(df['Neighbourhood Cleansed'])
df = df.drop('Neighbourhood Cleansed', axis = 1)

# Normalizamos las columnas de texto
str_columns = ['Neighbourhood', 'City', 'State', 'Property Type', 'Room Type', 'Bed Type', 'Cancellation Policy']
for column in df.columns:
    if column in str_columns:
        column_normalized = list(map(normalize, list(map(no_alfa_num, df[column].astype(str)))))
        df[column] = column_normalized

# Creamos una nueva columna con la tasa de ocupación calculada según la fórmula
reviews = df['Reviews per Month'].fillna(0)
nights = df['Minimum Nights'].fillna(0)
availability = df['Availability 365'].fillna(0).map(lambda value: value if value != 0 else 9999999)
df['Occupancy'] = calculate_occupancy(reviews, nights, availability)

# Agrupamos los valores de la columna 'Property Type' por los más comunes y almacenamos el resto en el valor 'Other'
valid_property_types = ['House', 'Apartment', 'Bed & Breakfast', 'Condominium', 'Loft', 'Chalet', 'Hostal']
df['Property Type'] = df['Property Type'].map(lambda value: value if value in valid_property_types else 'Other')

# Creamos un nuevo dataframe con la columna 'ID' y una columna por cada uno de los elementos de la columna 'Amenities', eliminamos esta última del dataframe original
df_amenities = df.Amenities.str.get_dummies(sep=',').astype(bool).join(df['ID'])
df = df.drop('Amenities', axis=1) 

# Nos quedamos con las columnas de 'Amenities' que consideramos relevantes
amenities_to_keep = ['ID', 'Self Check-In', 'Smartlock', 'Air conditioning', 'Elevator in building', 'Essentials', 'Internet', 'Heating', 'Pets allowed', 'Smoking allowed', 'Pool', 'TV', 'Kitchen', 'Gym']
df_amenities = df_amenities[amenities_to_keep]

# Guardamos ambos dataframes en dos nuevos ficheros
df.to_csv('../clean/airbnb-listings_cleaned.csv', sep=';', index=False)
df_amenities.to_csv('../clean/amenities.csv', sep=';', index=False)
 