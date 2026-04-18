
#todo Python Reaprendizaje (Tipos de datos, Variables y Operadores)

#¡Ejercicio 1
#Guarda tu nombre, edad y altura en variables. Imprime una oración usando las tres.

nombre = "Patrick"
edad = "19"
altura = 1.7

print(f"Mi nombre es {nombre}, tengo {edad} años y mido {1.7} m")

#¡Ejercicio 2
#Dado un número, determina si es par o impar usando solo operadores.

num_1 = 6
num_2 = 9

print("¿Número 1 es par? :", (num_1 % 2 == 0))
print("¿Número 2 es par?", (num_2 % 2 == 0))

#¡Ejercicio 3
#Tienes a = 10 y b = 3. Calcula e imprime: suma, resta, multiplicación, división, división entera, módulo y potencia.

a = 10
b = 3

print("Suma :", a + b)
print("Resta :", a - b)
print("Multiplicación :", a * b)
print("División :", a / b)
print("División entera :", a // b)
print("Resto :", a % b)
print("Potencia :", a ** b)

#¡Ejercicio 4
#Convierte una temperatura en Celsius a Fahrenheit y a Kelvin.

temp_celsius = 987

a_fahrenheit = (temp_celsius * (9 / 5)) + 32
a_kelvin = (temp_celsius + 273.15)

print(f"La temperatura de {temp_celsius} C, convertida a Fahrenheit es : {a_fahrenheit:,.2f} F, y convertida a Kelvin : {a_kelvin} K")

#¡Ejercicio 5
#Intercambia el valor de dos variables sin usar una tercera variable.

a = 2
b = 3

print("Antes: a = ", a, "b = ", b)

a, b = b, a

print("Después: a = ", a, "b = ", b)



#*Otra forma

x = 4
y = 6
print("Antes: x = ", x, "y = ",y)
x = x + y
y = x - y
x = x - y

print("Después: x = ", x, "y = ", y)

#¡Ejercicio 6
#Dado un número de segundos (ej: 3725), conviértelo a horas, minutos y segundos.

num_s = 3725

horas = num_s // 3600
minutos = (num_s % 3600) // 60
segundos = (num_s % 3600) % 60


print(f"El número de {num_s} segundos en horas, minutos y segundos es {horas} hora {minutos} minutos {segundos} segundos ")