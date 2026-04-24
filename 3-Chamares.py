#Inversión de Frases: Pide al usuario una frase y devuelve las palabras en orden
#inverso utilizando listas (Ejemplo: "Hola mundo";...;"mundo Hola").

Frase=input("por favor, ingrese una frase de al menos dos palabras: ")
PalabraSeparacion=Frase.split()
PalabraInvertida=PalabraSeparacion[::-1]
FraseInvertida= " ".join(PalabraInvertida) #esto es para que no quede la frase con coma

print("Frase invertida: ", FraseInvertida.lower()) #esto es para que no quede una mayuscula en el final de la frase 
