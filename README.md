# Proyecto-Final-KeepCoding
Proyecto final para el Bootcamp: Mujeres en Tech con KeepCoding, en la especialización de Big Data.

Este proyecto *se hace en grupo*: Somos las Data Witches 🧙‍♀️🔮

- Carmen Rey González.
- María Berraquero García.
- Laura Daniela Morales Gutiérrez.
- María Victoria Ramello.

La finalidad era explorar este [dataset](https://public.opendatasoft.com/explore/dataset/airbnb-listings/export/?disjunctive.host_verifications&disjunctive.amenities&disjunctive.features&q=Madrid&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQ09VTlQiLCJ5QXhpcyI6Imhvc3RfbGlzdGluZ3NfY291bnQiLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiJyYW5nZS1jdXN0b20ifV0sInhBeGlzIjoiY2l0eSIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6IiIsInNvcnQiOiIiLCJzZXJpZXNCcmVha2Rvd24iOiJyb29tX3R5cGUiLCJjb25maWciOnsiZGF0YXNldCI6ImFpcmJuYi1saXN0aW5ncyIsIm9wdGlvbnMiOnsiZGlzanVuY3RpdmUuaG9zdF92ZXJpZmljYXRpb25zIjp0cnVlLCJkaXNqdW5jdGl2ZS5hbWVuaXRpZXMiOnRydWUsImRpc2p1bmN0aXZlLmZlYXR1cmVzIjp0cnVlfX19XSwidGltZXNjYWxlIjoiIiwiZGlzcGxheUxlZ2VuZCI6dHJ1ZSwiYWxpZ25Nb250aCI6dHJ1ZX0%3D&location=16,41.38377,2.15774&basemap=jawg.streets) y realizar las preguntas planteadas por el grupo para finalmente proponer un algoritmo de regresión lineal que prediga el precio de un inmueble en función de las características elegidas. 

Los pasos que seguimos fueron los siguientes:

1. Arquitectura, validación de datos y análisis exploratorio:

[Lenguajes utilizados: Python, SQL]

[Librerías utilizadas: pandas, numpy, matplotlib, seaborn]

Decidimos realizar un [*Jupyter Notebook*](https://github.com/LauraDanielamg/Proyecto-Final-KeepCoding/blob/main/python%20scripts/Data_cleaning_and_exploring.ipynb) que recoge la memoria del proceso de limpieza y exploración de datos. Asi mismo genera un [csv limpio](https://github.com/LauraDanielamg/Proyecto-Final-KeepCoding/blob/main/clean/airbnb-listings_cleaned.csv) a partir del [csv original](https://github.com/LauraDanielamg/Proyecto-Final-KeepCoding/blob/main/subject/airbnb-listings.zip) y un [amenities.csv](https://github.com/LauraDanielamg/Proyecto-Final-KeepCoding/blob/main/clean/amenities.csv) con los datos de las amenidades por cada alojamiento.

En el directorio [SQL scripts](https://github.com/LauraDanielamg/Proyecto-Final-KeepCoding/tree/main/SQL%20scripts) de este repo pueden encontrar los scripts necesarios para la ingesta de datos en una base de datos, asi como el [modelo Entidad-Relación](https://github.com/LauraDanielamg/Proyecto-Final-KeepCoding/blob/main/SQL%20scripts/diagrama-ER.drawio)

2.La visualicación de las métricas:

Se ha realizado con Tableau. 

3. Realización del modelo predictivo de regresion lineal

Se encuentra recogido en la carpeta [R](https://github.com/LauraDanielamg/Proyecto-Final-KeepCoding/tree/main/R). Proponemos dos modelos y analizamos cual es el mejor entre ambos. 

4. Realizamos un informe final con todas las conclusiones y puntos destacables del proceso:

Puede ser revisado [aqui](https://github.com/LauraDanielamg/Proyecto-Final-KeepCoding/blob/main/Informe%20Proyecto%20Final%20Data%20Witches.docx)
