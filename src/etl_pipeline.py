import pandas as pd
from sqlalchemy import create_engine

# 1️⃣ EXTRACT
print("Extrayendo datos...")
df = pd.read_csv("../data/raw_data.csv")

# 2️⃣ TRANSFORM
print("Limpiando datos...")
df['name'] = df['name'].fillna("Sin nombre")
df['city'] = df['city'].fillna("Desconocido")
df['price'] = df['price'].fillna(df['price'].mean())
df['price'] = df['price'].astype(float)

# Mostrar los primeros registros
print(df.head())

# 3️⃣ LOAD
print("Cargando datos limpios en base de datos SQLite...")
engine = create_engine('sqlite:///../output/airbnb_data.db')
df.to_sql('listings', con=engine, if_exists='replace', index=False)

print("✅ Proceso ETL completado con éxito.")
