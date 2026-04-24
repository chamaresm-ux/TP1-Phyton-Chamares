#Conversor de Binario a Decimal: Solicita al usuario una lista de ceros y unos
#(un número binario) y calcula su equivalente decimal manualmente usando ciclos.

binario = input("Ingrese unos y ceros para formar un número binario: ")

valido = True

for i in binario:
    if i != "0" and i != "1":
        print("Error, solo debe ingresar ceros y unos.")
        valido = False
        break

if valido:
    decimal = 0
    exponente = 0

    for i in range(len(binario) - 1, -1, -1):
        bit = int(binario[i])
        decimal += bit * (2 ** exponente)
        exponente += 1

    print("El numero binario ingresado es igual a", decimal)