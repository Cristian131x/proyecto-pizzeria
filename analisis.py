class Venta:
    def __init__(self, linea_csv):
        # Separamos los datos de la línea
        datos = linea_csv.strip().split(',')
       
        # Asignamos cada dato a un atributo, convirtiéndolo al tipo correcto
        self.fecha = datos[0]
        self.dia_semana = datos[1]
        self.nombre_pizza = datos[2]
        self.cantidad = int(datos[3])
        self.precio = float(datos[4])

# 1. Leemos todas las líneas del archivo
with open('ventas_pizzeria.csv', 'r') as f:
    f.readline() # Descartamos el encabezado
    lineas = f.readlines()


# 2. Creamos una lista para guardar nuestros objetos de venta
lista_ventas = []
for linea in lineas:
    # Por cada línea, creamos un objeto Venta y lo añadimos a nuestra lista
    venta = Venta(linea)
    lista_ventas.append(venta)


# 3. Recalculamos los totales, pero ahora usando nuestra lista de objetos
ingreso_total = 0.0
pizzas_totales = 0
for venta in lista_ventas:
    ingreso_venta = venta.cantidad * venta.precio
    ingreso_total += ingreso_venta # Usamos += como una forma más corta de sumar
    pizzas_totales += venta.cantidad

# 4. Calculamos la pizza más vendida
ventas_por_pizza = {} # Un diccionario para contar las ventas por nombre de pizza


for venta in lista_ventas:
    nombre = venta.nombre_pizza
    cantidad = venta.cantidad
   
    if nombre in ventas_por_pizza:
        ventas_por_pizza[nombre] += cantidad
    else:
        ventas_por_pizza[nombre] = cantidad


# Buscamos la pizza con la mayor cantidad en nuestro diccionario
pizza_mas_vendida_nombre = max(ventas_por_pizza, key=ventas_por_pizza.get)
pizza_mas_vendida_cantidad = ventas_por_pizza[pizza_mas_vendida_nombre]


# 5. Mostramos todos los resultados
print("--- Resultados del Análisis ---")
print(f"Ingreso Total: ${ingreso_total}")
print(f"Cantidad Total de Pizzas Vendidas: {pizzas_totales}")
print("--- Análisis Adicional ---")
print(f"La pizza más vendida fue: '{pizza_mas_vendida_nombre}' con {pizza_mas_vendida_cantidad} unidades.")