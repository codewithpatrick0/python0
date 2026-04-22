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