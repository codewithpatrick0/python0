
#todo Python Reaprendizaje (OOP - Programación Orientada a Objetos)

#¡Ejercicio 1
"""
Crea una clase Persona con nombre, edad y ciudad. 
Agrega un método que retorne una presentación y otro que diga si es mayor de edad.
"""

class Persona :
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
        
    def presentacion(self):
        print(f"Mi nombre es {self.nombre}, mi edad es {self.edad} y soy de {self.ciudad}")
        
    def mayor_de_edad(self):
        return self.edad > 18
    
persona1 = Persona('Patrick', 19, 'Lima')

persona1.presentacion()
print(persona1.mayor_de_edad())

#¡Ejercicio 2
"""
Crea una clase Rectangulo con ancho y alto. Agrega métodos para calcular área y perímetro.
"""

class Rectangulo :
    def __init__(self, ancho, alto) :
        self.ancho = ancho
        self.alto = alto
        
    def calcular_area(self):
        return self.ancho * self.alto
    
    def calcular_perimetro(self):
        return 2 * (self.ancho * self.alto)
    
rectangulo1 = Rectangulo(20, 12)

print(rectangulo1.calcular_area())
print(rectangulo1.calcular_perimetro())

#¡Ejercicio 3
"""
Crea una clase CuentaBancaria con saldo privado. 
Implementa métodos para depositar, retirar y consultar saldo — con validaciones.
"""

class CuentaBancaria :
    def __init__(self, saldo):
        self.__saldo = saldo
    
    def depositar(self, monto):
        if monto > 0 :
            self.__saldo += monto
            print(f"El monto de S/{monto:,.2f} fue depositado correctamente | Nuevo saldo : S/{self.__saldo:,.2f}")
        else :
            print('Monto inválido a depositar')
    
    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            print(f"El monto de S/{monto:,.2f} fue retirado correctamente | Nuevo saldo : S/{self.__saldo:,.2f}")
            
    def consultar_saldo(self):
        return f"S/{self.__saldo}"
    
cuenta1 = CuentaBancaria(1800.50)
cuenta1.depositar(210.2)
print(cuenta1.consultar_saldo())

cuenta1.retirar(1550.7)
print(cuenta1.consultar_saldo())

#¡Ejercicio 4
"""
Crea una clase Estudiante con nombre, notas como lista, y métodos para agregar nota,
calcular promedio y retornar si aprobó o no.
"""

class Estudiante :
    def __init__(self, nombre, notas=None):
        self.nombre = nombre
        if notas is None:
            self.__notas = []

    def set_notas(self, nota):
        if nota >= 0 and nota <= 20 :
            self.__notas.append(nota)
        else:  
            print("Nota inválida, tiene que estar en el rango de 0 y 20")
            
    def calcular_promedio(self):
        if not self.__notas :
            print("No tienes notas para calcular el promedio")
            return 0
        
        return (sum(self.__notas) / len(self.__notas))
    
    def aprobacion(self):
        if self.calcular_promedio() > 11.5:
            return True
        
        return False

estudiante1 = Estudiante('Patrick')

estudiante1.set_notas(13)
estudiante1.set_notas(16)
estudiante1.set_notas(20)

print(f"El promedio del estudiante es {estudiante1.calcular_promedio():,.2f}")
print(f"¿Aprobó?: {estudiante1.aprobacion()}")