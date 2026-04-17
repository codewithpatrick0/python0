#todo Python Reaprendizaje (Strings)

#¡Ejercicio 1
#Dado un string, imprime cuántas letras tiene, en mayúsculas, en minúsculas y con la primera letra en mayúscula.

string = "mi mamá es bella"

print(f"El string dado tiene :{len(string.replace(" ", ""))} letras")
print(string.upper())
print(string.lower())
print(string.capitalize())

#¡Ejercicio 2
#Verifica si una palabra es palíndromo (igual al revés). Ej: "reconocer".

palabra = "reconocer" 

print(f"¿La palabra {palabra} es palídromo? :  {palabra[::-1] == palabra}")

#¡Ejercicio 3
#Dado un texto con espacios extra al inicio y al final, límpialo y reemplaza todas las letras "a" por "@".

texto = " Hagamos la tarea de matemática "

texto_nuevo = texto.strip().replace("a","@").replace("á","@")

print(texto_nuevo)

#¡Ejercicio 4
#Dado un nombre completo como "juan pablo garcia", formatealo como "Garcia, Juan Pablo"

nombre_completo = "juan pablo garcia"
nombre_completo = nombre_completo.title()

partes = nombre_completo.split()

print(f"{partes[-1]}, {' '.join(partes[:-1])}")

#¡Ejercicio 5
#Cuenta cuántas veces aparece una vocal específica en un texto dado.

texto = "Mi hermano come huevo con carne"

print(f"¿Cuantas veces tiene la vocal 'e' el texto dado?:  {texto.count("e")}")

#¡Ejercicio 6
#Dado un string, invierte el orden de las palabras. Ej: "hola mundo cruel" → "cruel mundo hola"

oracion = "hola mundo cruel"

list_oracion = (oracion.split())
list_oracion = list_oracion[::-1]

oracion_nueva = ' '.join(list_oracion)
print(oracion_nueva)

