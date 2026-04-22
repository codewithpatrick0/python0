#todo Python Reaprendizaje (Listas y Tuplas)

#¡Ejercicio 1
#Dada una lista de números, elimina los duplicados y muestra la lista resultante ordenada.

lista_numeros = [5, 10, 15, 20, 5, 10, 2]

lista_limpia = []

for numero in lista_numeros:
    if numero not in lista_limpia:
        lista_limpia.append(numero)

print(lista_limpia)

#¡Ejercicio 2
#Dada una lista de strings, retorna una nueva lista solo con los strings que tengan más de 4 letras.

lista_strings = ["ho la", "ro  l", "mundos", "pythonico", "ey", "mi mamá me mima"]
lista_strings_largos = []

for string in lista_strings :
    
    if len(string.replace(" ","")) > 4 :
        lista_strings_largos.append(string)

print(lista_strings_largos)

#¡Ejercicio 3
#Crea una función que reciba dos listas y retorne los elementos que tienen en común.

def retornar_lista_resultante(lista1, lista2):
    lista_resultante = []

    for i in min(len((lista1, lista2))):
        if lista1[i] == lista2[i] :
            lista_resultante.append(lista1[i])

    return lista_resultante

lista1 = [2, 5, 10, 12, 20]
lista2 = [10, 2, 99, 20]

resultado = retornar_lista_resultante(lista1, lista2)
print(resultado)
