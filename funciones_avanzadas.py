
#todo Python Reaprendizaje (Funciones Avanzadas)

#¡Ejercicio 1
#Dada una lista de números, usa map para obtener el cuadrado de cada uno.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numeros_cuadrados = list(map(lambda x : x**2, numeros))
print(numeros_cuadrados)

#¡Ejercicio 2
#Dada una lista de palabras, usa filter para quedarte solo con las que empiezan con vocal.

palabras = ['android', 'elefante', 'moto', 'arroz', 'pato']

palabras_vocal = list(filter(lambda x : x[0] in 'aeiouáéíóú', palabras))
print(palabras_vocal)

