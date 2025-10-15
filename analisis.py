# analisis.py

# Abrimos el archivo en modo de lectura ('r')
with open('ventas_pizzeria.csv', 'r') as f:
    # Usamos f.readline() para leer la primera línea (el encabezado) y descartarla
    f.readline()
    
    # Ahora, el resto de las líneas son solo datos
    lineas = f.readlines()

print(f"Se leyeron {len(lineas)} registros de ventas.")

# Inicializamos nuestras variables para los cálculos
ingreso_total = 0.0
pizzas_totales = 0

# Iteramos sobre cada línea que leímos del archivo
for linea in lineas:
    # Quitamos espacios en blanco y saltos de línea, y separamos por la coma
    datos = linea.strip().split(',')
    
    # Extraemos la cantidad y el precio. ¡Recuerda convertirlos a números!
    cantidad = int(datos[3])
    precio = float(datos[4])
    
    # Calculamos el ingreso de esta venta y lo sumamos al total
    ingreso_venta = cantidad * precio
    ingreso_total = ingreso_total + ingreso_venta
    
    # Sumamos la cantidad de pizzas de esta venta al total
    pizzas_totales = pizzas_totales + cantidad

# Mostramos los resultados finales
print("--- Resultados del Análisis ---")
print(f"Ingreso Total: ${ingreso_total}")
print(f"Cantidad Total de Pizzas Vendidas: {pizzas_totales}")