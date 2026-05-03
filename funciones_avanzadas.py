
#todo Python Reaprendizaje (Funciones Avanzadas)

#¡Ejercicio 1
#Dada una lista de números, usa map para obtener el cuadrado de cada uno.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numeros_cuadrados = list(map(lambda x : x**2, numeros))
print(numeros_cuadrados)

#¡Ejercicio 2
#Dada una lista de palabras, usa filter para quedarte solo con las que empiezan con vocal.

palabras = ['árbol', 'android', 'elefante', 'moto', 'arroz', 'pato']

palabras_vocal = list(filter(lambda x : x[0] in 'aeiouáéíóú', palabras))
print(palabras_vocal)

#¡Ejercicio 3
#Dada una lista de tuplas (nombre, nota), ordénalas de mayor a menor nota usando sorted y lambda.

notas = [
        ('Luis', 20),
        ('Luisa', 15),
        ('Fabian', 12),
        ('Patrick', 16),
        ('Juan', 10),
        ('Kathy', 5)
    ]

notas_ordenadas = sorted(notas, key= lambda x : x[1], reverse=True)
print(notas_ordenadas)

#¡Ejercicio 4
#Usa map y lambda para convertir una lista de strings a enteros.

strings = ['1', '2', '3', '4', '5']
enteros = list(map(int, strings))
print(enteros)

#¡Ejercicio 5
#Combina map y filter — dada una lista de números, filtra los pares y luego eleva cada uno al cubo.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]

numeros_pares_al_cubo = list(map(lambda x : x ** 3, filter(lambda x : x % 2 == 0, numeros)))
print(numeros_pares_al_cubo)

#¡Ejercicio 6
"""
Dada una lista de diccionarios con nombre y salario,
ordénalos por salario de mayor a menor y filtra solo los que ganan más de 2000.
"""

empleados = [
    {'nombre': 'Ana', 'salario': 1800},
    {'nombre': 'Pedro', 'salario': 2500},
    {'nombre': 'Luis', 'salario': 3000},
    {'nombre': 'Marta', 'salario': 2100},
    {'nombre': 'Juan', 'salario': 1500}
]

empleados_sueldo_superior = list(filter(lambda x : x['salario'] > 2000 , empleados))
empleados_sueldo_superior = sorted(empleados_sueldo_superior, key=lambda x :  x['salario'], reverse=True)
print(empleados_sueldo_superior)
