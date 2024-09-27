import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('temperaturas.csv')
print("Primeras 10 filas del DataFrame:")
print(df.head(10))

print("----------------------------------------")
nullValues = df['Temperatura'].isnull().sum()
print(f"Valores nulos por columna: {nullValues}")

print("----------------------------------------")
dfClean = df.dropna()
print(f"Filas despues de eliminar valores nulos: \n{dfClean}")

print("----------------------------------------")
temp_promedio = dfClean['Temperatura'].mean()
print(f"Temperatura promedio de todas las ciudades: {temp_promedio}")

print("----------------------------------------")
tempMax = dfClean.groupby('Ciudad')['Temperatura'].max()
tempMin = dfClean.groupby('Ciudad')['Temperatura'].min()
print(f"Temperatura maxima por ciudad: \n{tempMax}")
print("----------------------------------------")
print(f"Temperatura minima por ciudad: \n{tempMin}")

print("----------------------------------------")
ciudadTempMax = dfClean.loc[dfClean['Temperatura'].idxmax(), 'Ciudad']
print(f"Ciudad con la temperatura mas alta: {ciudadTempMax}")

print("----------------------------------------")
ciudadesTempMayor30 = dfClean[dfClean['Temperatura'] > 30]
print(f"Ciudades con la temperatura mayor a 30: \n{ciudadesTempMayor30}")

# Mostrar grafica de barras con la temperatura promedio por ciudad
plt.figure(figsize=(10, 5))
dfAvgTemp = dfClean.groupby('Ciudad')['Temperatura'].mean()
dfAvgTemp.plot(kind='bar', color='skyblue')
plt.title('Temperatura Promedio por Ciudad')
plt.xlabel('Ciudad')
plt.ylabel('Temperatura Promedio (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Mostrar grafico de linea por variacion de temperatura por ciudad
plt.figure(figsize=(12, 6))

colores = ['red', 'green', 'blue', 'orange', 'purple', 'brown', 'pink']
estilos = ['-', '--', '-.', ':', '-', '--', '-.']

for i, (ciudad, datos) in enumerate(dfClean.groupby('Ciudad')):
    plt.plot(datos.index, datos['Temperatura'], marker='o', linestyle=estilos[i % len(estilos)], color=colores[i % len(colores)], label=ciudad)

plt.title('Variación de Temperatura por Ciudad')
plt.xlabel('Índice de Medición')
plt.ylabel('Temperatura (°C)')
plt.legend(title='Ciudad')
plt.grid(True)
plt.tight_layout()
plt.show()

print("----------------------------------------")
ciudadesTempMayor30.to_csv('ciudadesTempMayor30.csv', index=False)
print("Archivo 'ciudadesTempMayor30.csv' guardado con éxito.")