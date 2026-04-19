
#todo Python Reaprendizaje (Funciones)

#¡Ejercicio 1
#Crea una función que reciba un número y retorne si es par o impar.

def par_o_impar(numero) :
    if numero % 2 == 0 :
        return "par"
    else :
        return "impar"
    
numero = int(input("Ingresa un número : "))

resultado = par_o_impar(numero)
print(f"El número {numero} es {resultado}")

#¡Ejercicio 2
#Crea una función que reciba un string y retorne el string al revés.

def invertir_string(string) :
    
    return string[::-1]

string = input("Ingresa un string : ")
invertido = invertir_string(string)

print(f"El string '{string}' de manera invertida es '{invertido}'")

#¡Ejercicio 3
#Crea una función que reciba una lista de números y retorne el mayor, el menor y el promedio.

def analizar_num_lista(lista) :
    mayor = lista[0]
    menor = lista[0]
    suma = 0
    cantidad = 0
    for num in lista :
        if num > mayor :
            mayor = num
        
        if num < menor :
            menor = num
            
        suma += num
        cantidad += 1
        
    promedio = suma / cantidad
        
    return mayor, menor, promedio

numeros = [5, 2, 4, 10, 12, 1]

mayor, menor, promedio = analizar_num_lista(numeros)

print(f"El mayor de la lista es {mayor}, el menor es {menor} y el promedio es {promedio}")

#¡Ejercicio 4
"""Crea una función que reciba un número n 
y retorne una lista con los primeros n números de la secuencia Fibonacci."""

def n_secuencia_fibonacci(numero) :
    
    lista = [0, 1]
    
    for i in range(2, numero) :
        lista.append(lista[-1] + lista[-2])
        
    return lista[:numero]

numero = int(input("Ingresa un número : "))
resultado = n_secuencia_fibonacci(numero) 

print(f"Los primeros {numero} números de la secuencia Fibonacci son {resultado} ")

#¡Ejercicio 5
"""Crea una función que reciba un string y retorne cuántas vocales tiene 
— reutiliza la lógica del tema anterior."""
def vocales_string(string) :
    vocales = 0
    
    string = string.lower()
    for letra in string :
        if letra in "aeiou" :
            vocales += 1
        
    return vocales


string = input("Ingresa un string : ")
cantidad_vocales = vocales_string(string)

print(f"El string ingresado tiene {cantidad_vocales} vocales")

#¡Ejercicio 6
"""Crea un programa con funciones separadas para: pedir un número al usuario,
verificar si es primo, e imprimir el resultado. Cada cosa en su propia función."""

def solicitar_num() :
    numero = int(input("Ingresa un número : "))
    
    return numero

def verificar_primo(numero) :
    if numero <= 1 :
        return False
    
    for i in range(2, numero) :
        if numero % i == 0 :
            return False
        
    return True

numero = solicitar_num()
resultado = verificar_primo(numero)

if resultado :
    print(f"El número {numero} es primo")
else :
    print(f"El número {numero} no es primo")