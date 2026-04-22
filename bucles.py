
#todo Python Reaprendizaje (Bucles)

#¡Ejercicio 1
#Imprime todos los números del 1 al 100 que sean divisibles por 3 o por 5.

for i in range(1, 101) :

    if  i % 3 == 0 or i % 5 == 0 :
        print(i)

#¡Ejercicio 2
#Dado un número, calcula su factorial. Ej: 5! = 5 × 4 × 3 × 2 × 1 = 120.

numero = int(input("Ingresa un número : "))
resultado = 1
for i in range(1, numero + 1) :
    resultado *= i 

print(resultado)

#¡Ejercicio 3
#Pide números al usuario hasta que ingrese 0. Al final imprime la suma total y el promedio.
intentos = 0
suma = 0
while True :
    numero = int(input("Ingresa un número : "))

    if numero == 0 :
       break
    elif numero < 0 :
        print("Número inválido, vuelve a intentar otro")
        continue
    else :
         intentos += 1
         suma += numero

if intentos == 0 :
    promedio = 0
else :
    promedio = suma / intentos

print(f"La suma de los números ingresados es {suma} y el promedio es {promedio}")       

        
#¡Ejercicio 4
#Imprime la tabla de multiplicar de un número ingresado por el usuario.

numero = int(input("Ingresa un número : "))
for i in range(1, 13) :
    resultado = numero * i
    print(f"{i} x {numero} = {resultado}")

#¡Ejercicio 5
#Dado un string, cuenta cuántas vocales tiene sin usar .count().

string = input("Ingresa un string : ")

vocales = 0

for letra in string :
    if letra in "aeiou":
        vocales +=1

print(f"El string ingresado tiene {vocales} vocales")

#¡Ejercicio 6
#Imprime un triángulo de asteriscos de altura n. Ej con n = 4:
n = int(input("Ingresa altura : "))
for i in range(n+1) :
    print("*" * i)
