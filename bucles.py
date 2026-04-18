
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

print(f"La suma de los números ingresados es {suma} y el promedio es {suma/intentos}")       

        
