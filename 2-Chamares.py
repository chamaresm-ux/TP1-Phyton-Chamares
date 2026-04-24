#El Filtro de Nombres: Crea una función que reciba una lista de nombres y
#devuelva solo aquellos que comiencen con una vocal y tengan más de 5
#caracteres.

NombresLista= ["Matias", "Eros", "Cristian", "Ulises", "Nicolas", "Antonio", "Diego", "Fabian"]
NombresFiltro=[]

for Nombre in NombresLista:
    if len(Nombre) >5 and Nombre[0].lower() in "aeiou":
        NombresFiltro.append(Nombre)

print("Los nombres que cumplen los requisitos son: ", NombresFiltro)
