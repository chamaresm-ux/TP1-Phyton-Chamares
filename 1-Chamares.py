#Calculadora de Promedio Móvil: Escribe un programa que reciba una lista de
#números y devuelva una nueva lista donde cada elemento sea el promedio entre el
#úmero actual y el anterior (el primero se queda igual).

numeroslista=[10, 20, 30, 40, 50, 60]
promedioslista= []

promedioslista.append(numeroslista[0])

for i in range (1,len(numeroslista)):
    promedio= (numeroslista [i] + numeroslista [i-1]) / 2
    promedioslista.append(promedio)

print("Lista de promedios: ", promedioslista) 
