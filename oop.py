
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
        return self.edad >= 18
    
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
        return 2 * (self.ancho + self.alto)
    
rectangulo1 = Rectangulo(20, 12)

print(F"Área: {rectangulo1.calcular_area()}")
print(f"Perímetro: {rectangulo1.calcular_perimetro()}")

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
            return 
        print("No tienes saldo suficiente para retirar el monto indicado")
        return
            
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

#¡Ejercicio 5
"""
Crea una clase Producto con nombre, precio y stock. 
Agrega métodos para aplicar descuento y vender unidades — con validaciones de stock.
"""

class Producto :
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio
        self.__stock =  stock
        
    #Aplicaré un descuento del 20% a partir de la compra de un producto mayor a S/1000.00
    def vender(self, unidades):
        if unidades > self.__stock:
            print("No hay stock suficiente del producto.")
            return 
        
        self.__stock = self.__stock - unidades
        print(f"Cantidad vendida: {unidades} unidad(es) | Nuevo stock: {self.__stock}")
        
    def aplicar_descuento(self):
        if self.__precio > 1000 :
            self.__precio = self.__precio - (0.2 * self.__precio)
            return True
        return False
    
    def obtener_precio(self):
        return self.__precio
    
producto1 = Producto('Iphone 17', 1299.99, 20)
producto2 = Producto('Mouse', 549.99, 10)

#Aplicamos descuento para comprobar si tienen:
print(f"¿{producto1.nombre} tiene descuento? {producto1.aplicar_descuento()} | Precio con descuento: S/{producto1.obtener_precio():,.2f}")
print(f"¿{producto2.nombre} tiene descuento? {producto2.aplicar_descuento()} | Precio con descuento: S/{producto2.obtener_precio():,.2f}") #Es el mismo ya que no hay

#Vender
producto1.vender(21)
producto2.vender(2)

#¡Ejercicio 6
"""
Crea una clase Calculadora que guarde el historial de operaciones realizadas. 
Implementa suma, resta, multiplicación y división, y un método para imprimir el historial completo.
"""
class Calculadora :
    def __init__(self, historial=None):
        if historial is None:
            self.__historial = []
            
    def sumar(self, a, b):
        resultado = a + b
        self.__historial.append(f"{a} + {b} = {a+b}")
        return resultado
    
    def restar(self, a, b):
        resultado = a - b
        self.__historial.append(f"{a} - {b} = {a-b}")
        return resultado
    
    def multiplicar(self, a, b):
        resultado = a * b
        self.__historial.append(f"{a} x {b} = {a*b}")
        return resultado
    
    def dividir(self, a, b):
        if b == 0 :
            print("No se puede dividir entre 0, prueba otro número")
            return None
        resultado = a / b
        self.__historial.append(f"{a} / {b} = {a/b}")
        return resultado
    
    def mostrar_historial(self):
        if not self.__historial:
            print("El historial se encuentra vacío")
            return
        for i, operacion in enumerate(self.__historial, start=1):
            print(f"Operación {i}. {operacion}")
            
calculadora = Calculadora()

calculadora.sumar(2, 3)
calculadora.restar(10, 3)
calculadora.multiplicar(2, 3)
calculadora.dividir(10, 2)
calculadora.dividir(5, 0)

calculadora.mostrar_historial()
