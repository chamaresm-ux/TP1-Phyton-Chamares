#El Traductor de P: Crea un programa que transforme una palabra añadiendo
#una P; y repitiendo la vocal después de cada vocal encontrada (Ejemplo: hola-
#hopolapa).

palabra=input("Ingrese una palabra para convertirla: ")
resultado = ""

for letra in palabra:
    if letra.lower() in "aeiou":
        resultado += letra + "p" + letra
    else:
        resultado += letra
print("El resultado es:", resultado)