
#todo Python Reaprenddizaje (Manejo de errores)

#¡Ejercicio 1
#Pide un número al usuario y maneja el error si ingresa texto en vez de número.

try:
    numero = int(input("Ingresa un número"))
    print("Numero ingresado correctamente")
except ValueError:
    print("Debes ingresar solo números")
finally:
    print("\nSaliendo...\n")
    
#¡Ejercicio 2
#Crea una función que divida dos números y maneje la división entre cero.

def dividir_entre_cero():
    while True:
        try:
            numero1 = int(input("Ingresa un número entero: "))
            numero2 = int(input("Ingresa otro número: "))
            resultado = numero1 / numero2
            return resultado
        
        except ValueError:
            print("Solo puedes ingresar números enteros")
        except ZeroDivisionError:
            print("No se puede dividir entre 0, prueba otro número")
            
            
resultado = dividir_entre_cero()
print(resultado)

#¡Ejercicio 3
"""
Dado un diccionario, intenta acceder a una clave que no existe 
y maneja el error sin usar .get().
"""

libro = {
        "nombre" : "Misery",
        "autor" : "Stephen King",
        "codigo" : "U24305392",
        "precio" : 59.99,
        "isbn" : "34987542312"
        }

try :
    print(libro["ventas"])
except KeyError:
    print("No se encontró la clave")

#¡Ejercicio 4
"""
Crea una función que reciba una lista y un índice,
 y maneje el error si el índice no existe.
"""

def lista_indice(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return None
    
lista = [1, 2, 3, 4, 5, "hola", "chau"]

print(lista_indice(lista, 2))
print(lista_indice(lista, 99))

#¡Ejercicio 5
"""
Crea una función que valide una edad — debe ser número entero y estar entre 0 y 120.
 Lanza un ValueError con mensaje claro si no cumple.
"""

def validar_edad(edad):
    if not 0 <= edad <= 120 :
        raise ValueError("La edad tiene que estar en el rango entre 0 y 120 años")
    return True
    
try:
    resultado = validar_edad(122)
    print(resultado)
except ValueError as e:
    print(f"Error detectado: {e}")


#¡Ejercicio 6
"""
Combina todo — crea un programa que pida al usuario dos números y una operación 
(suma, resta, multiplicación, división), maneje todos los errores posibles
 y use finally para imprimir "Operación finalizada" siempre.
"""

while True:
    try :
        numero1 = int(input("Ingresa un número"))
        numero2 = int(input("Ingresa otro número"))

        print(f"La suma de los números es {numero1 + numero2}")
        print(f"La resta de los números es {numero1 - numero2}")
        print(f"La multiplicación de los números es {numero1 * numero2}")
        print(f"La división de los números es {numero1 / numero2}")
        break
    
    except ValueError as e:
        print(f"{e} : Solo puede ingresar números enteros")
    except ZeroDivisionError as e :
        print(f"{e} : No se puede dividir entre 0")
    finally:
            print("Operación finalizada...")




