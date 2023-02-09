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
replace_values = ['nan', '2015', 'Madrid 28004', '2802\n28012', '28002\n28002', '-', '28', '2805', '2804', '28051\n28051', '2815']
df['Final_Zipcode'] = df.apply(lambda x: np.nan if x['Zipcode'] in replace_values else x['Zipcode'], axis=1)
df = df.drop('Zipcode', axis=1)

# Limpio los nombres de los barrios: me quedo con los valores de 'Neighbourhood' excepto en el caso de los nulls que los sustituyo por el valor de 'Neighbourhood Cleansed'
df['Final_Neighbourhood'] = df.apply(lambda x: x['Neighbourhood Cleansed'] if pd.isnull(x['Neighbourhood']) else x['Neighbourhood'], axis=1)
df = df.drop(['Neighbourhood', 'Neighbourhood Cleansed'], axis=1)

# Conversión del ID de la entrada en numérico en vez de string
df['ID'].astype(int)

# Conversión de las fechas de 'Host Since' en date
df['Host Since'] = pd.to_datetime(df['Host Since'])

# Normalización columna Amenities
# Reseteo de los índices para poder iterar por ellos
df = df.reset_index(drop=True)

# Conversión de la columna Amenities en tipo string y división de los strings en listas 
df['Amenities'] = df['Amenities'].astype(str).apply(lambda x: x.split(','))

# Variable con todos los elementos que aparecen en 'Amenities'
amenities = ['TV', 'Internet', 'Wireless Internet', 'Kitchen', 'Doorman','Elevator in building', 'Buzzer/wireless intercom', 'Heating', 'Washer','Essentials', 'Shampoo', 'Lock on bedroom door', 'Hangers','Air conditioning', 'Breakfast', 'Family/kid friendly', 'Dryer','Hair dryer', 'Iron', 'Laptop friendly workspace', 'Pets allowed','Gym', 'Smoke detector', 'Carbon monoxide detector', 'First aid kit','Fire extinguisher', '24-hour check-in', 'Smoking allowed','translation missing: en.hosting_amenity_49','translation missing: en.hosting_amenity_50', 'Bathtub','Pets live on this property', 'Dog(s)', 'Wheelchair accessible','Self Check-In', 'Lockbox', 'Private entrance', 'Safety card','Cable TV', 'nan', 'Suitable for events', 'Cat(s)', 'Indoor fireplace','Pool', 'Hot tub', 'Free parking on premises', 'Room-darkening shades','Doorman Entry', 'Game console', 'Private living room', 'Smartlock','Other pet(s)', 'High chair', 'Children’s books and toys','Pack ’n Play/travel crib', 'Children’s dinnerware','Babysitter recommendations', 'Outlet covers', 'Baby bath','Changing table', 'Crib', 'Window guards', 'Stair gates','Free parking on street', 'Keypad', 'Table corner guards','Paid parking off premises', 'Washer / Dryer']

# Bucle para iterar por todas las filas de la columna Amenities
for i, row in enumerate(df['Amenities']):
    # Bucle para iterar por todos los elementos de la variable amenities
    for el in amenities:
        # Si el elemento está en la lista de la columna Amenities, añado una nueva columna con el nombre del elemento y valor 1 para esa fila (o actualizo el valor si ya existe la columna) 
        if el in df.loc[i, 'Amenities']:
            df.loc[i, el] = 1
        # Si no está, le doy valor 0
        else:
            df.loc[i, el] = 0

# Tras analizar las columnas de amenities para valorar cuáles son más importantes, elimino el resto de columnas del dataframe
amenities_to_keep = ['Wireless Internet', 'Kitchen', 'Heating', 'Essentials', 'Washer', 'TV', 'Hangers', 'Shampoo', 'Elevator in building', 'Family/kid friendly']
amenities_to_drop = [amenity for amenity in amenities if amenity not in amenities_to_keep]
df = df.drop(columns=amenities_to_drop)

# Elimino también la columna original Amenities
df = df.drop(columns='Amenities')

# Guardo el nuevo dataframe en un csv para trabajar a partir de este
df.to_csv('airbnb-listings_cleaned.csv', sep = ';', index = False)
