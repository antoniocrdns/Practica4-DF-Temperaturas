import pandas as pd
import matplotlib.pyplot as plt

# Datos de las ventas para 6 productos durante 7 días
ventaSemana = pd.DataFrame({
    'Producto 1': [101, 55, 95, 78, 232, 125, 145],
    'Producto 2': [45, 75, 55, 65, 85, 120, 130],
    'Producto 3': [90, 85, 70, 65, 95, 110, 105],
    'Producto 4': [120, 60, 80, 70, 150, 160, 180],
    'Producto 5': [60, 40, 55, 70, 60, 50, 45],
    'Producto 6': [30, 35, 40, 50, 45, 30, 40]
}, index=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'])

# Total ventas semana
totalSemana = ventaSemana.sum().sum()

# Promedio diario de ventas para cada producto
promedioDiario = ventaSemana.mean()

# Día con ventas más altas y más bajas para cada producto
diaVentasAltas = ventaSemana.idxmax()
diaVentasBajas = ventaSemana.idxmin()

# Filtrar productos con promedio diario superior a 100 unidades
productosPromedioAlto = promedioDiario[promedioDiario > 100]

# Encontrar productos con ventas menores a 70 unidades en algún día
productosVentasMenores70 = ventaSemana[ventaSemana < 70].dropna(how='all')

# Incrementar ventas un 10% si el total es menor a 500 unidades en la semana
for col in ventaSemana.columns:
    if ventaSemana[col].sum() < 500:
        ventaSemana[col] = ventaSemana[col] * 1.1

# Sumar ventas de todos los productos para cada día y encontrar el día con más ventas totales
ventasTotalesPorDia = ventaSemana.sum(axis=1)
diaMasVentasTotales = ventasTotalesPorDia.idxmax()

# Verificar si algún producto tuvo ventas altas durante 3 días seguidos
productosCrecientes = []
for col in ventaSemana.columns:
    if (ventaSemana[col].diff().dropna() > 0).rolling(3).sum().max() >= 3:
        productosCrecientes.append(col)

# Verificar si al menos 2 productos disminuyeron sus ventas en comparación al día anterior
productosDisminucion = (ventaSemana.diff() < 0).sum(axis=1)
diasDisminucion = productosDisminucion[productosDisminucion >= 2]

# Calcular porcentaje de ventas diarias de cada producto en comparación de sus ventas totales
porcentajeVentasDiarias = ventaSemana.div(ventaSemana.sum(axis=0), axis=1) * 100

# Crear serie para producto 'pepinillos' y realizar los mismos análisis
pepinillos = pd.Series([55, 60, 65, 70, 75, 80, 85], index=ventaSemana.index)
ventaSemana['Pepinillos'] = pepinillos


print(f"Total de ventas semanal: {totalSemana}")
print(f"Promedio diario de ventas por producto:\n{promedioDiario}")
print(f"Día de ventas más altas por producto:\n{diaVentasAltas}")
print(f"Día de ventas más bajas por producto:\n{diaVentasBajas}")
print(f"Productos con promedio diario mayor a 100 unidades:\n{productosPromedioAlto}")
print(f"Productos con ventas menores a 70 unidades:\n{productosVentasMenores70}")
print(f"Día con más ventas totales: {diaMasVentasTotales}")
print(f"Productos con ventas mayores durante 3 días seguidos: {productosCrecientes}")
print(f"Días con al menos 2 productos con ventas bajas:\n{diasDisminucion}")
print(f"Porcentaje de ventas diarias:\n{porcentajeVentasDiarias}")


plt.figure(figsize=(10, 6))
ventaSemana.plot(kind='line', marker='o')
plt.title('Ventas diarias de productos')
plt.xlabel('Día')
plt.ylabel('Unidades Vendidas')
plt.grid(True)
plt.show()
