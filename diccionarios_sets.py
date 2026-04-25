
#todo Python Reaprendizaje (Diccionarios y sets)
#Dado un string, cuenta la frecuencia de cada letra usando un diccionario.

string = "Mi tatatatara"
string = string.replace(" ", "")
diccionario = {}

for letra in string :
    if letra not in diccionario :
        diccionario[letra] = 1
    else :
        diccionario[letra] = diccionario[letra] + 1
        
print(diccionario)

#¡Ejercicio 2
#Dado un diccionario de productos y precios, imprime solo los productos que cuestan más de 50.

productos = {
        "laptop" : 2000,
        "juguete" : 35,
        "chupete" : 5,
        "celular" : 500
    }

for producto in productos :
    if productos[producto] > 50 :
        print(producto.capitalize())
        
#¡Ejercicio 3
#Crea una función que reciba una lista y retorne un diccionario con cuántas veces aparece cada elemento.

def lista_a_diccionario(lista) :
    diccionario = {}
    for elemento in lista :
        if elemento not in diccionario :
            diccionario[elemento] = 1
        else :
            diccionario[elemento] = diccionario[elemento] + 1
            
    return diccionario

lista = [1, 1, 2, 3, 3, 3, "hola", "chau", "hola", 2]

print(lista_a_diccionario(lista))

#¡Ejercicio 4
"""
Dados dos sets, imprime los elementos en común,
los que están en el primero pero no en el segundo, y la unión de ambos.
"""

set_1 = {"hola", 1, 2, 5, "chau"}
set_2 = {"chau", 2, 7, 8, "python", 10}

print("\nElementos en común:\n")
for elemento in (set_1 & set_2):
    print(f"- {elemento}")
    
print("\nElementos del set  1 que no están en el set 2:\n")
for elemento in (set_1 - set_2):
    print(f"- {elemento}")
    
print("\nUnión de set 1 y set 2:\n")
for elemento in (set_1 | set_2):
    print(f"- {elemento}")
    
#¡Ejercicio 5
#Dado un diccionario de estudiantes y sus notas, imprime el nombre del estudiante con la nota más alta.

notas = {
    "Patrick" : 20,
    "Luis" : 10,
    "Mari" : 15,
    "Fabian" : 12
    }

nota_maxima = max(notas, key=notas.get)

print(f"El estudiante con la nota máxima es {nota_maxima}")

#¡Ejercicio 6
"""
Crea un sistema simple de inventario — permite agregar productos,
actualizar stock y consultar si un producto existe, todo usando un diccionario.
"""

inventario = {}
while True:
    print("1. Agregar productos")
    print("2. Actualizar stock")
    print("3. Consultar producto")
    print("4. Cerrar sistema")

    opcion = int(input("Selecciona una opción : "))

    if opcion == 1 :
        producto = input("Ingresa el producto a agregar: ")
        stock = int(input("Ingresa el stock del producto: "))
        
        inventario[producto] = stock
        
    elif opcion == 2 :
        producto = input("Ingresa el producto a añadir stock: ")
        stock = int(input("Ingresa el nuevo stock del producto: "))
        if producto in inventario:
            inventario[producto] = stock
        else:
            print("Producto inexistente, no se puede agregar stock")
        
    elif opcion == 3 :
        producto = input("Ingresa el producto que deseas consultar: ")
        
        if producto in inventario :
            print(f"Producto: {producto} | Stock: {inventario[producto]}")
        else :
            print(inventario.get(producto, "El producto ingresado no existe"))

    elif opcion == 4:
        print("Hasta luego")
        break
    
    else: 
        print("OPCION INVÁLIDA")