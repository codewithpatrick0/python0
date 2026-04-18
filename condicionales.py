
#todo Python Reaprendizaje (Condicionales)

#¡Ejercicio 1
#Dado un número del 1 al 7, imprime el día de la semana correspondiente.

dia = int(input("Ingresa el número de un día de la semana : "))
    
if dia == 1 :
    print("Lunes")
elif dia == 2 :
    print("Martes")
elif dia == 3 :
    print("Miércoles")
elif dia == 4 :
    print("Jueves")
elif dia == 5 :
    print("Viernes")
elif dia == 6 :
    print("Sábado")
elif dia == 7 :
    print("Domingo")
else :
    print("Número de día inválido")
    
#¡Ejercicio 2
#Dados tres números, imprime cuál es el mayor.

num_1 = 5
num_2 = 2
num_3 = 3

if num_1 >= num_2 and num_1 >= num_3 :
    print(num_1)
elif num_2 >= num_1 and num_2 >= num_3 :
    print(num_2)
else :
    print(num_3)
    
#¡Ejercicio 3
#Dado un año, determina si es bisiesto.

año = int(input("Ingresa el año : "))

#! Regla de años centenarios
if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0 :
    print(f"El año {año} si es bisiesto")
else :
    print(f"El año {año} no es bisiesto")
    
#¡Ejercicio 4
#Dado un salario, calcula el impuesto: menos de 1000 paga 0%, entre 1000 y 3000 paga 10%, más de 3000 paga 20%.

salario = float(input("Ingresa tu salario : "))
impuesto = 0

if 0 < salario < 1000 :
    print("No pagas impuestos")
elif 1000 <= salario <= 3000 :
    impuesto = salario * 0.1
    print(f"Tu impuesto a pagar es {impuesto}")
elif salario > 3000 :
    impuesto = salario * 0.2
    print(f"Tu impuesto a pagar es {impuesto}")
else :
    print("Salario inválido")
    
#¡Ejercicio 5
#Dado un número del 0 al 100, imprime la letra de calificación: A (90-100), B (80-89), C (70-79), D (60-69), F (menos de 60).

numero = int(input("Ingresa un número : "))
if numero < 0 or numero > 100 :
    print("Número inválido")
elif 90 <= numero <= 100 :
    print("A")
elif 80 <= numero <= 89 :
    print("B")
elif 70 <= numero <= 79 :
    print("C")
elif 60 <= numero <= 69 :
    print("D")
else :
    print("F")
    
#¡Ejercicio 6
"""Simula un login: define un usuario y contraseña correctos, pide los datos al usuario
e imprime si el acceso fue exitoso o no, con mensajes diferentes para usuario incorrecto,
contraseña incorrecta, o ambos incorrectos."""

usuario = "codewithpatrick0"
contraseña = "cacas2323"

usuario_ingreso = input("Ingresa tu usuario : ")
contraseña_ingreso = input("Ingresa tu contraseña : ")

if usuario_ingreso == usuario and contraseña_ingreso == contraseña:
    print("Datos correctos, iniciaste sesión...")
elif usuario_ingreso != usuario and contraseña_ingreso != contraseña:
    print("Ambos datos incorrectos, vuelve a intentarlo")
elif usuario_ingreso != usuario:
    print("Usuario incorrecto, vuelve a intentarlo")
else:
    print("Contraseña incorrecta, vuelve a intentarlo")