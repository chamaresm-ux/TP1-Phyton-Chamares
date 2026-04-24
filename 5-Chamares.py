#Simulador de Carrito de Compras: Crea un programa que permita al usuario
#ingresar nombres de productos y sus precios hasta que escriba "fin". Al terminar,
#debe mostrar el total gastado y el producto más caro.

Carrito = []

while True:
    Producto = input("Ingrese el producto adquirido (o fin para terminar): ")

    if Producto.lower() == "fin":
        if len(Carrito) == 0:
            print("Tenés que ingresar al menos un producto antes de finalizar.")
            continue
        else:
            break

    Precio = float(input("Ingrese el precio: "))
    Carrito.append([Producto, Precio])

# Cálculos
Total = 0
ProductoMasCaro = Carrito[0][0]
PrecioMasCaro = Carrito[0][1]

for i in Carrito:
    Total += i[1]

    if i[1] > PrecioMasCaro:
        PrecioMasCaro = i[1]
        ProductoMasCaro = i[0]

print("Total gastado:", Total)
print("Producto mas caro:", ProductoMasCaro)