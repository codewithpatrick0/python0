
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




