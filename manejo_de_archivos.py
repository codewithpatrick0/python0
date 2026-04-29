
#todo Python Reaprendizaje (Manejo de archivos)

#¡Ejercicio 1
#Crea un archivo notas.txt, escribe 5 líneas de texto y luego léelo e imprímelo.

with open('notas.txt', 'r') as archivo:
    for linea in archivo:
        print(linea.rstrip())
        
#¡Ejercicio 2
#Abre el archivo anterior y agrega 3 líneas más sin borrar las anteriores.

with open('notas.txt', 'a') as archivo:
    archivo.write('\ny\nlos\nadoro')

print("Contenido agregado:\n ")
with open('notas.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
    

#¡Ejercicio 3
"""
Lee un archivo línea por línea y cuenta cuántas líneas tiene,
cuántas palabras en total y cuántos caracteres.
"""
lineas_total = 0
caracteres_total = 0
palabras_total = 0
with open('notas.txt', 'r') as archivo:
    for linea in archivo:
        lineas_total += 1
        caracteres_total += len(linea)
        palabras_total += len(linea.split())
        
print(f"El archivo leído tiene {lineas_total} líneas, {caracteres_total} caracteres y {palabras_total} palabras en total.")

#¡Ejercicio 4
"""
Crea un programa que guarde nombres en un archivo —
el usuario ingresa nombres hasta escribir "salir",
y cada nombre se guarda en una línea nueva.
"""
with open('nombres.txt', 'a') as archivo:
    while True:
        
        nombre = input("Ingresa un nombre para añadir al archivo: ").strip().lower()
        
        if nombre == "salir":
            break
        
        archivo.write(nombre.capitalize()+"\n")

#¡Ejercicio 5
"""
Lee el archivo del ejercicio anterior 
y elimina los duplicados, luego guarda la lista limpia en un archivo nuevo.
"""

with open('nombres.txt', 'r') as archivo:
    #Eliminar duplicados
    lista_nombres = archivo.readlines()
    lista_limpia = list(set(lista_nombres))
    
with open('nombres_sin_duplicados.txt', 'w') as archivo:
    
    for nombre in lista_limpia:
        archivo.write(nombre)
        
#¡Ejercicio 6
"""
Crea un CSV con columnas nombre, edad, ciudad con al menos 5 filas, 
luego léelo e imprime solo las personas mayores de 18 años.
"""

import csv

with open('archivo.csv', 'r', encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    
    print("Personas mayores de edad:")
    for fila in lector :
        nombre = fila['nombre']
        edad = int(fila['edad'])
        ciudad = fila['ciudad']
        if edad >= 18 :
            print(nombre)
