print("Ejercicio 41")
# ejercicio 41
#Crea una función que calcule el área de un triángulo.
def area_triangulo(base, height):
    return base * height / 2
print(area_triangulo(10,20))


print("Ejercicio 42")
# ejercicio 42
#Escribe una función que devuelva la longitud de una lista
def longuitud(lista):
    return len(lista)
lista = input("Ingrese los numeros por favor: ")
element = lista.split(",")
length = longuitud(element)
print(f"La longitud de la lista es: {length}")


print("Ejercicio 43")
# ejercicio 43
#Crea una función que convierta grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius es {fahrenheit} grados Fahrenheit.")


print("Ejercicio 44")
# ejercicio 44
#Escribe una función que genere una lista de números primos.
def lista_de_primos(limit):
    cousin = []
    for num in range(2, limit + 1):
        is_cousin = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_cousin = False
                break
        if is_cousin:
            cousin.append(num)
    return cousin
limit1 = int(input("Ingresa el límite superior para la lista de primos: "))
cousin1 = lista_de_primos(limit1)
print("Lista de números primos hasta", limit1, ":", cousin1)


print("Ejercicio 45")
# ejercicio 45
#Crea una función que calcule el factorial de un número
def factorial(num):
    if num < 0:
        return "El factorial no exise para numeros menores a cero"
    elif num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result
num =int(input("Ingrese un numero: "))
result = factorial(num)
print(f"El factorial de {num} es {result}")


print("Ejercicio 46")
# ejercicio 46
#Escribe una función que verifique si una cadena de texto es un pangrama (contiene todas las letras del alfabeto).
def es_pangrama(chair):
    chair = chair.lower()
    string_letters = set(chair)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(string_letters)
text = input("Ingresa una cadena de texto: ")

if es_pangrama(text):
    print("Es un pangrama.")
else:
    print("No es un pangrama.")


print("Ejercicio 47")
# ejercicio 47
#Crea una función que devuelva el número de vocales en una cadena de texto.
def contar_vocales(chair):
    chair = chair.lower()
    vowels = "aeiou"
    counter = 0
    for letter in chair:
        if letter in vowels:
            counter += 1
    return counter

text = input("Ingrese un texto: ")
num_vowels = contar_vocales(text)
print(f"El número de vocales en la cadena es: {num_vowels}")

print("Ejercicio 48")
# ejercicio 48
#Escribe una función que calcule el mínimo común múltiplo (MCM) de dos números.
def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a
def calcular_mcm(a, b):
    if a == 0 or b == 0:
        return 0
    return (a * b) // calcular_mcd(a, b)
num1 = 12
num2 = 18

mcm = calcular_mcm(num1, num2)
print(f"El MCM de {num1} y {num2} es: {mcm}")


print("Ejercicio 49")
# ejercicio 49
#Crea una función que verifique si una cadena de texto es un palíndromo.
def palidromo(chair):
    chair = chair.replace(" ", "").lower()
    return chair == chair[::-1]

text = input("Ingresa una cadena de texto: ")
if palidromo(text):
        print("Es un palíndromo.")
else:
        print("No es un palíndromo.")


print("Ejercicio 50")
# ejercicio 50
#Escribe una función que determine si un número es par o impar
def par_impar(num):
    if num % 2 == 0:
        return  "Es par"
    else:
        return "Es impar"
num = int(input("Ingrese un numero"))
result = par_impar(num)
print(f"El número {num} es {result}.")


print("Ejercicio 51")
# ejercicio 51
#Crea una clase llamada "Persona" con atributos nombre y edad.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person("Frank", 20)
person2 = Person("Arianna", 18)

print(f"{person1.name} tiene {person1.age} años.")
print(f"{person2.name} tiene {person2.age} años.")


print("Ejercicio 52")
# ejercicio 52
#Crea un objeto de la clase "Persona" e imprime sus atributos.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person("Frank", 20)
print(f"Nombre: {person1.name} ")
print(f"Edad: {person1.age} años.")


print("Ejercicio 53")
# ejercicio 53
#Agrega un método a la clase "Persona" para saludar.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def saludos(self):
        print(f"Hola, soy {self.name}  y tengo {self.age} años")
person1 = Person("Arianna", 18)
person1.saludos()


print("Ejercicio 54")
# ejercicio 54
#Crea una clase llamada "Rectángulo" con atributos largo y ancho.
class Rectangle:
    def __init__(self, large, width):
        self.large = large
        self.width = width
rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(8, 4)
print(f"Rectángulo 1: Largo = {rectangle1.large}, Ancho = {rectangle1.width}")
print(f"Rectángulo 2: Largo = {rectangle2.large}, Ancho = {rectangle2.width}")


print("Ejercicio 55")
# ejercicio 55
#Agrega un método a la clase "Rectángulo" para calcular el área.
class Rectangle:
    def __init__(self, large, width):
        self.large = large
        self.width = width
    def area_rectangulo(self):
        return self.large * self.width

rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(8, 4)

area1 = rectangle1.area_rectangulo()
area2 = rectangle2.area_rectangulo()
print(f"Área del Rectángulo 1: {area1} ")
print(f"Área del Rectángulo 2: {area2} ")


print("Ejercicio 56")
# ejercicio 56
#Crea una clase llamada "CuentaBancaria" con atributos saldo y titular
class cuenta_bancaria():
    def __init__(self, balance, headline):
        self.balance = balance
        self.headline = headline

usuario1 = cuenta_bancaria(1000, "Arianna")
print(f"El usuario {usuario1.headline} tiene de saldo ${usuario1.balance}")


print("Ejercicio 57")
# ejercicio 57
#Agrega métodos para depositar y retirar dinero de la cuenta bancaria.
class cuenta_bancaria:
    def __init__(self, balance, headline):
        self.balance = balance
        self.headline = headline
    def depositar(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Depósito de ${amount} realizado. Saldo actual: ${self.balance}"
        else:
            return "La cantidad de depósito debe ser mayor que cero."
    def retirar(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Retiro de ${amount} realizado. Saldo actual: ${self.balance}"
        elif amount > self.balance:
            return "Saldo insuficiente para el retiro."
        else:
            return "La cantidad de retiro debe ser mayor que cero."

usuario1 = cuenta_bancaria(1000, "Arianna")

print(f"El usuario {usuario1.headline} tiene un saldo de ${usuario1.balance}")
print(usuario1.depositar(500))
print(usuario1.retirar(200))
print(usuario1.retirar(1500))


print("Ejercicio 58")
# ejercicio 58
#Crea una clase llamada "Coche" con atributos marca, modelo y año.
class Coche:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
coche1 = Coche("Toyota", "Camry", 2021)
coche2 = Coche("Ford", "Mustang", 2019)

print(f"El coche 1 es de marca {coche1.brand}, Modelo {coche1.model}, Año {coche1.year}")
print(f"El coche 2 es de marca {coche2.brand}, Modelo {coche2.model}, Año {coche2.year}")


print("Ejercicio 59")
# ejercicio 59
#Agrega un método para acelerar el coche.
class Coche:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    def acelerar(self, increase):
        if increase > 0:
            self.speed += increase
            return f"El coche aceleró a {self.speed} km/h"
        else:
            return "El incremento de velocidad debe ser mayor que cero."
coche1 = Coche("Toyota", "Camry", 2021)
print(f"El coche 1 es de marca {coche1.brand}, Modelo {coche1.model}, Año {coche1.year}")
print(coche1.acelerar(20))
print(coche1.acelerar(10))


print("Ejercicio 60")
#ejercicio 60
#Escribe un programa que cree una lista de objetos "Coche" y acelere cada uno de ellos.
class Coche:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    def acelerar(self, increase):
        if increase > 0:
            self.speed += increase
            return f"El coche aceleró a {self.speed} km/h"
        else:
            return "El incremento de velocidad debe ser mayor que cero."
cars = [Coche("Toyota", "Camry", 2022), Coche("Ford", "Mustang", 2020), Coche("Honda", "Civic", 2021)]

# Acelerar cada coche en la lista
for car in cars:
    print(f"El coche 1 es de marca {coche1.brand}, Modelo {coche1.model}, Año {coche1.year}")
    print(car.acelerar(20))
    print(car.acelerar(10))
    print()


