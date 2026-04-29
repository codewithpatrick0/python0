
#todo Python Reaprendizaje (List Comprehensions)

#¡Ejercicio 1
#Dado un rango del 1 al 20, crea una lista con los números impares usando list comprehension.

numeros_impares = [i for i in range(21) if i % 2 != 0]
print(numeros_impares)

#¡Ejercicio 2
"""
Dada una lista de palabras, crea una nueva lista con cada palabra en mayúsculas
y solo si tiene más de 3 letras.
"""

palabras = ["sol", "mar", "hola", "python", "dia", "mundo", "paz", "programacion", "luz", "backend"]

palabras_formateadas = [p.upper() for p in palabras if len(p) > 3]
print(palabras_formateadas)

#¡Ejercicio 3
"""
Dado un diccionario de productos y precios,
crea un nuevo diccionario solo con los productos que cuestan menos de 100 usando dict comprehension.
"""

productos = {
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 150,
    "Cable HDMI": 15,
    "Audífonos": 85,
    "Laptop": 800,
    "Escritorio": 120,
    "Soporte": 35
}

productos_baratos = {k : v for k, v in productos.items() if v < 100}
print(productos_baratos)

#¡Ejercicio 4
#Dada una lista de números, crea un diccionario donde la clave sea el número y el valor sea su cuadrado.

numeros = [1, 2, 3, 4, 5, -2, 10, 0]

dict_cuadrados = {n:n**2 for n in numeros}
print(dict_cuadrados)

#¡Ejercicio 5
#Dada una lista de strings, usa set comprehension para obtener las longitudes únicas de los strings

palabras = ["java", "python", "php", "go", "c++", "rust", "html", "css", "javascript"]

longitudes_unicas = {len(p) for p in palabras}
print(longitudes_unicas)

#¡Ejercicio 6
"""
Tienes una lista de temperaturas en Celsius — 
conviértelas todas a Fahrenheit usando list comprehension 
y filtra solo las que sean mayores a 100°F.
"""

celsius = [0, 20, 37, 38, 40, 45, 100]

farenheit = [(c * 9/5) + 32 for c in celsius if (c * 9/5) + 32 > 100]
print(farenheit)