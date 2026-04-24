#Análisis de Rango: Dada una lista de 10 números aleatorios, encuentra el valor
#máximo, el mínimo y calcula la diferencia entre ellos.

lista=[5, 8, 79, 10, 2, 56, 60, 70, 1, 42]
valormax=0
valormin=1000

for i in lista:
    if i > valormax:
        valormax=i
    else:
        if i < valormin:
            valormin=i

diferencia= (valormax - valormin)

print("El valor maximo es:", valormax)
print("El valor minimo es:", valormin)
print("La diferencia entre ambos valores es de", diferencia)