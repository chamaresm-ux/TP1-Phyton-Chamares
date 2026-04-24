#Compresión de Datos Básica: Escribe una función que reciba una lista de
#caracteres repetidos y devuelva una lista de sublistas con el carácter y su frecuencia

datos = ['a', 'a', 'b', 'c', 'c', 'c']
resultado = []
procesados = []

for caracter in datos:
    if caracter not in procesados:
        cantidad = datos.count(caracter)
        resultado.append([caracter, cantidad])
        procesados.append(caracter)
        
print(resultado)