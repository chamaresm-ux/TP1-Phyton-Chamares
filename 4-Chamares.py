#Buscador de Duplicados: Dada una lista con elementos repetidos, genera una
#nueva lista que contenga únicamente los elementos que aparecían más de una vez,
#pero sin repetirlos en el resultado final.

Lista=[2, 24, 32, 2, 40, 356, 7, "mocos", 36, 77, 80, "mati", "mati", 59, 30, 66, 40, 32]
ListaFinal=[]

for i in Lista:
    if Lista.count(i) > 1 and i not in ListaFinal:
        ListaFinal.append(i)

print("Elementos repetidos en la lista: ", ListaFinal)
