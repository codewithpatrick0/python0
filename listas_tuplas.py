
#todo Python Reaprendizaje (Listas y Tuplas)

#¡Ejercicio 1
#Dada una lista de números, elimina los duplicados y muestra la lista resultante ordenada.

lista_numeros = [5, 10, 15, 20, 5, 10, 2]

lista_limpia = []

for numero in lista_numeros:
    if numero not in lista_limpia:
        lista_limpia.append(numero)
        lista_limpia.sort()

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
    
    lista_resultante = [e for e in lista1 if e in lista2]

    return lista_resultante
    

lista1_num = [2, 5, 10, 12, 20, 99]
lista2_num = [10, 2, 99, 20,0, 0, 0, 5]

lista1_str = ["hola", "chau", "gemini"]
lista2_str = ["gemini", "chau", "hola", "CACAS"]

resultado = retornar_lista_resultante(lista1_num, lista2_num)
print(resultado)

resultado = retornar_lista_resultante(lista1_str, lista2_str)
print(resultado)

#¡Ejercicio 4 
#Dada una lista de números, sepáralos en dos listas: pares e impares.

lista_num = [2, 5, 10, 12, 7, 9]

lista_pares = []
lista_impares = []

for n in lista_num :
    if n % 2 == 0 :
        lista_pares.append(n)
    else :
        lista_impares.append(n)
        
print(lista_impares)
print(lista_pares)

#¡Ejercicio 5
#Crea una función que reciba una lista y retorne la lista al revés sin usar .reverse() ni slicing [::-1]

def devolver_lista_al_reves(lista):
    
    lista_reverse = []
    
    i = len(lista) -                1
    while i >= 0 :
            lista_reverse.append(lista[i])
            i -= 1
            
    return lista_reverse

lista = [1, 2, "hola", 4, 5]

resultado = devolver_lista_al_reves(lista)
print(resultado)

#¡Ejercicio 6
#Dada una lista de tuplas (nombre, edad), ordénalas por edad de menor a mayor e imprímelas.

lista_tuplas = [
    ("Patrick", 19),
    ("Luis", 52),
    ("Jorge", 5)
    ]

lista_ordenada = sorted(lista_tuplas, key=lambda x : x[1], reverse=False)

for i, elementos in enumerate(lista_ordenada):
    print(f"{i+1}. {lista_ordenada[i]}")