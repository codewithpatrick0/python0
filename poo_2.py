
#todo Python Reaprendizaje (OOP - 2 | Programación Orientada a Objetos)

#¡Ejercicio 1
"""
Crea una clase Animal con nombre y sonido.
Crea dos clases hijas Perro y Gato que sobreescriban el método hablar(). 
Crea una lista con varios animales e imprime lo que dice cada uno.
"""

class Animal :
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
        
    def hablar(self):
        return '...'
    
class Perro(Animal):
    def __init__(self, nombre, sonido='Guau'):
        super().__init__(nombre, sonido)
    
    def hablar(self):
        return self.sonido
    
class Gato(Animal):
    def __init__(self, nombre, sonido='Miau'):
        super().__init__(nombre, sonido)
    
    def hablar(self):
        return self.sonido

mi_perro = Perro('Coki')
mi_gato = Gato('Wilson')

animales = [mi_perro, mi_gato]

for animal in animales:
    print(f"{animal.nombre}: {animal.hablar()}")
    
#¡Ejercicio 2
"""
Crea una clase Figura con un método area() que retorne 0.
Crea clases hijas Circulo, Rectangulo y Triangulo que calculen su área correctamente.
"""
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        #Este método tendrá cada subclase de manera distinta
        pass
    
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        import math
        return math.pi * (self.radio**2)
    
class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    def area(self):
        return self.alto *self.ancho
    
class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return (self.base * self.altura) / 2

circulo1 = Circulo(22.5)
rectangulo1 = Rectangulo(20, 5)
triangulo1 = Triangulo(20, 33.5)
print(f"Area del círculo: {circulo1.area():,.2f}")
print(f"Área del rectángulo: {rectangulo1.area():,.2f}")
print(f"Área del triángulo: {triangulo1.area():,.2f}")

#¡Ejercicio 3
"""
Crea una clase Vehiculo con marca, modelo y velocidad máxima. 
Crea clases hijas Auto y Moto — cada una agrega atributos propios 
y sobreescribe un método descripcion().
"""

class Vehiculo :
    def __init__(self, marca, modelo, vel_max, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self._vel_max = vel_max
        
    @property
    def vel_max(self):
        return self._vel_max
    
    @vel_max.setter
    def vel_max(self, new_vel):
        if isinstance(new_vel, (int, float)) and new_vel > 0:
            self._vel_max = new_vel
        else:
            print("¡Error! La velocidad es inválida.")
        
    def descripcion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Velocidad máxima: {self._vel_max}")
        print(f"Color: {self.color}")
    
class Auto(Vehiculo):
    def __init__(self, marca, modelo, vel_max, color, puertas):
        super().__init__(marca, modelo, vel_max, color)
        self.puertas = puertas
        
    def descripcion(self):
        super().descripcion()
        print(f"Cantidad de puertas: {self.puertas}")
        
class Moto(Vehiculo):
    def __init__(self, marca, modelo, vel_max, estilo, color):
        super().__init__(marca, modelo, vel_max, color)
        self.estilo = estilo
        
    def descripcion(self):
        super().descripcion()
        print(f"Estilo: {self.estilo}")
        
moto1 = Moto('Yamaha', 'MT15', 135, 'hyper-naked', 'Azul')
auto1 = Auto('Toyota', 'Supra MK4', 250, 'Naranja', 2)

vehiculos = [moto1, auto1]

print('\n---Mis vehículos---')
for i, v in enumerate(vehiculos, start=1):
    print(f"\nVehículo {i}:\n")
    v.descripcion()
    
print('\n')
#¡Ejercicio 4
"""
Crea una clase Empleado que herede de la clase Persona del tema anterior. Agrega salario y cargo. 
Sobreescribe el método presentacion() para incluir los nuevos datos.
"""
from oop import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, ciudad, salario, cargo):
        super().__init__(nombre, edad, ciudad)
        self.__salario = salario
        self.cargo = cargo
        
    def get_salario(self):
        return self.__salario
        
    def presentacion(self):
        super().presentacion()
        print(f"Mi cargo es {self.cargo} y mi salario es de S/{self.get_salario():,.2f}")
        
empleado1 =  Empleado('Fabián', 22, 'Miraflores', 800, 'almacenero')

empleado1.presentacion()

