import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

datos = pd.read_csv('datos04.csv')

# Variables independientes (X) y dependiente (Y)
x = datos[['Horas_de_estudio', 'Horas_de_sueno', 'Participacion']].values
y = datos['Calificacion'].values

# Entrenar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(x, y)


# Datos de entrada
horas_estudio = [3, 5, 7]
horas_sueño = [4, 6, 8]
participacion = [5, 7, 9]

# Predicciones para horas de estudio
predicciones_estudio = []
for h in horas_estudio:
    prediccion = modelo.predict([[h, 0, 0]])[0]
    print(f"Para {h} horas de estudio la predicción es: {prediccion}")
    predicciones_estudio.append(prediccion)

# Predicciones para horas de sueño
predicciones_sueño = []
for h in horas_sueño:
    prediccion = modelo.predict([[0, h, 0]])[0]
    print(f"Para {h} horas de sueño la predicción es: {prediccion}")
    predicciones_sueño.append(prediccion)

# Predicciones para participación
predicciones_participacion = []
for p in participacion:
    prediccion = modelo.predict([[0, 0, p]])[0]
    print(f"Para {p} de participación la predicción es: {prediccion}")
    predicciones_participacion.append(prediccion)

# Crear gráfica
plt.figure(figsize=(10, 6))

# Graficar datos reales
plt.scatter(datos['Horas_de_estudio'], y, color='gray', label='Datos reales')

# Graficar predicciones como líneas
linea_estudio, = plt.plot(horas_estudio, predicciones_estudio, color='blue', label='Calificación vs. Horas de estudio')
linea_sueno, = plt.plot(horas_sueño, predicciones_sueño, color='orange', label='Calificación vs. Horas de sueño')
linea_participacion, = plt.plot(participacion, predicciones_participacion, color='green', label='Calificación vs. Participación')

# Graficar puntos de predicción
punto_estudio, = plt.plot(horas_estudio, predicciones_estudio, 'x', color='red', label='Predicciones (Horas de estudio)', markersize=10)
punto_sueño, = plt.plot(horas_sueño, predicciones_sueño, 'x', color='purple', label='Predicciones (Horas de sueño)', markersize=10)
punto_participacion, = plt.plot(participacion, predicciones_participacion, 'x', color='yellow', label='Predicciones (Participación)', markersize=10)

# Leyenda
plt.legend(handles=[linea_estudio, punto_estudio, 
                    linea_sueno, punto_sueño, 
                    linea_participacion, punto_participacion])
plt.xlabel('Variables Independientes')
plt.ylabel('Calificación')
plt.title('Calificación en función de Horas de Estudio, Horas de Sueño y Participación')


plt.grid(True)
plt.show()
