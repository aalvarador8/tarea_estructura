#Ejercicio 1
#Crea una lista de números enteros y calcula su suma.
numbers = input("Ingresa una lista de números enteros separados por comas: ")
elements = numbers.split(",")
suma = 0
for element in elements:
    try:
        numero = int(element)
        suma += numero
    except ValueError:
        print(f"'{element}' no es un número entero válido y será omitido.")
print("La suma de los números enteros es:", suma)


print("Ejercicio 2")
#ejercicio 2
# Encuentra el número más grande en una lista de números.
# Crear una lista de números
numbers = [5, 12, 9, 3, 7, 45, 15]
maximo = numbers[0]
for number in numbers:
    if number > maximo:
        maximo = number

print("El número más grande es:", maximo)


print("Ejercicio 3")
#ejercicio 3
#Encuentra el número más pequeño en una lista de números.
nums = [1, 4, 67, 8, 10, 0]
minimo = nums[0]
for num in nums:
    if num < minimo:
        minimo = num
print("El numero mas pequeño es:", minimo)


print("Ejercicio 4")
#ejercicio 4
#Elimina los elementos duplicados de una lista.
lista = [1, 2, 2, 3, 4, 4, 5]
sets = set(lista)
list_without_duplicates = list(sets)

print(list_without_duplicates)



print("Ejercicio 5")
#ejercicio 5
#Dada una lista, invierte su orden.
num = [1, 2, 3, 4, 5]
inverted_list = []
for elemento in reversed(num):
    inverted_list.append(elemento)

print(inverted_list)


print("Ejercicio 6")
#ejercicio 6
#Escribe un programa que cuente cuántas veces aparece un elemento en una lista
numbers = [1, 2, 2, 3, 4, 2, 5, 2, 5, 6, 9, 0]

element_to_count =int(input("Ingrese el elemento a contar: "))
counter = 0
for element in numbers:
    if element == element_to_count:
        counter += 1
print(f"El elemento {element_to_count} aparece {counter} veces en la lista.")


print("Ejercicio 7")
#ejercicio 7
#Crea una lista de números pares del 1 al 20.
pair_numbers = []
for nums in range(2, 21, 2):
    pair_numbers.append(nums)

print(pair_numbers)

print("Ejercicio 8")
#ejercicio 8
#Dada una lista de nombres, ordénalos alfabéticamente.
names = ["Ana", "Carlos", "David", "Berta", "Elena"]
for i in names:
    names.sort()
print(names)

print("Ejercicio 9")
#ejercicio 9
#Crea una lista de los cuadrados de los números del 1 al 10.
square_numbers = []
for num in range(1, 11):
    square_number = num ** 2
    square_numbers.append(square_number)

print(square_numbers)

print("Ejercicio 10")
#ejercicio 10
#Dada una lista de números, encuentra el segundo número más grande.
nums = [7, 12, 5, 2, 9, 10, 15, 3]
maximo = max(nums)
second_number = float('-inf') #representa el infinito negativo de cualquier numero finito
for num in nums:
    if num != maximo and num > second_number:
        second_number = num
print("El segundo número más grande es:", second_number)

print("Ejercicio 11")

#ejercicio 11
#Crea un diccionario con nombres de personas como claves y sus edades como valores.
information = {}
condiction = True
while condiction:
    name = input("Que informacion desea introducir:")
    age = input(name + ":")
    information[name]= age
    print(information)
    condiction = input("Quieres añadir mas informacion (si/no)") == "si"

print("Ejercicio 12")
#ejercicio 12
#Agrega un nuevo elemento a un diccionario
dictionary = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Mexico"
}
condiction = True
while condiction:
    key = input("Que informacion desea introducir:")
    value = input(key + ":")
    dictionary[key]= value
    print(dictionary)
    condiction = input("Quieres añadir mas informacion (si/no): ") == "si"

print("Diccionario actualizado:")
for key, value in dictionary.items():
    print(f"{key}: {value}")


print("Ejercicio 13")
#ejercicio 13
#Elimina un elemento de un diccionario por clave.
dictionary1 = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Mexico"
}
key_to_delete = input("Que clave desea eliminar: ")
if key_to_delete in dictionary1:
    del dictionary1[key_to_delete]
    print(f"Se ha eliminado el elemento con la clave '{key_to_delete}'.")
else:
    print(f"La clave '{key_to_delete}' no existe en el diccionario.")

print("Diccionario actualizado:")
print(dictionary1)

print("Ejercicio 14")
#ejercicio 14
# Itera a través de las claves de un diccionario e imprime sus valores
dictionary = {"name": "Arianna", "age": 18, "city": "Milagro"}
print(dictionary)

for key, value in dictionary.items():
    print(f"llave:{key }, valor: {value}")


print("Ejercicio 15")
#ejercicio 15
# Verifica si una clave existe en un diccionario.
dictionary2 = {
    "nombre": "Juan",
    "apellido": "Perez",
    "telefono": "09934567",
    "edad": 30,
    "ciudad": "Mexico"
}
key_to_verify = input("Que clave desea buscar: ")

if key_to_verify in dictionary2:
    print(f"La clave '{key_to_verify}' existe en el diccionario.")
else:
    print(f"La clave '{key_to_verify}' no existe en el diccionario.")



print("Ejercicio 16")
#ejrcicio 16
#·Dada una lista de diccionarios (personas), encuentra la persona más joven.
persons = [
    {"nombre": "Pedro", "edad": 30},
    {"nombre": "María", "edad": 25},
    {"nombre": "Carlos", "edad": 35},
    {"nombre": "Ana", "edad": 28},
    {"nombre": "Luis", "edad": 40}
]
younger_people = persons[0]
for person in persons:
    if person["edad"] < younger_people["edad"]:
        younger_people = person
print("La persona más joven es:", younger_people["nombre"], "con", younger_people["edad"], "años.")

print("Ejercicio 17")
#ejercicio 17
# Dada una lista de diccionarios (libros), busca un libro por título.
Books = [
    {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año": 1967
    },
    {
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "año": 1605
    },
    {
        "titulo": "Harry Potter y la piedra filosofal",
        "autor": "J.K. Rowling",
        "año": 1997
    }
]
searched_title = input("Ingrese el título del libro que desea buscar: ").capitalize()
for book in Books:
    if book["titulo"] == searched_title:
        print("Libro encontrado:")
        print("Título:", book["titulo"])
        print("Autor:", book["autor"])
        print("Año:", book["año"])
        break
else:
    print("Libro no encontrado")

print("Ejercicio 18")
#ejercicio 18
#Crea un diccionario que cuente cuántas veces aparece cada palabra en una cadena de texto.
phrase = input("Ingrese una frase: ")
words = phrase.split()
word_count = {}
for word in words:
    word = word.strip(".,!?")
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f'"{word}": {count}')


print("Ejercicio 19")
#ejercicio 19
#. Dado un diccionario de productos y sus precios, calcula el precio total de una lista de compras.
products = {
    "manzanas": 1.0,
    "plátanos": 0.50,
    "naranjas": 0.75,
    "uvas": 3.0,
    "peras": 4.25
}
lista_de_compras = ["peras", "naranjas", "uvas"]

def calcular_precio_total(products, lista_de_compras):
    total_price = 0
    for product in lista_de_compras:
        if product in products:
            total_price += products[product]
        else:
            print(f"El producto '{product}' no está en el diccionario de productos.")
    return total_price

total_price = calcular_precio_total(products, lista_de_compras)
print(f"El precio total de la lista de compras es: ${total_price:.2f}")


print("Ejercicio 20")
#ejercicio 20
#Combina dos diccionarios en uno solo.
dictionary_1 = {"a": 1, "b": 2, "c": 10, "d": 22}
dictionary_2 = {"e": 1, "f": 90, "g": 34, "h": 30}
for key, value in dictionary_1.items():
    print(f"Diccionario 1  Clave: {key}, Valor: {value}")
for key, value in dictionary_2.items():
    print(f"Diccionario 2  Clave: {key}, Valor: {value}")

combined_dictionary = {**dictionary_1, **dictionary_2}
print(combined_dictionary)


print("Ejercicio 21")
#ejercicio 21
#Usa un bucle while para contar del 1 al 10.
counter = 1
while counter <= 10:
    print(counter)
    counter += 1

print("Ejercicio 22")
#ejercicio 22
#Usa un bucle for para imprimir los números pares del 1 al 20.
for i in range(1,21):
    if i % 2 == 0:
        print(i)


print("Ejercicio 23")
#ejercicio 23
#Escribe un programa que imprima los elementos de una lista utilizando un bucle for.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for element in numbers:
    print(element)


print("Ejercicio 24")
#ejercicio 24
#Usa un bucle while para sumar los números del 1 al 100.
counter = 1
suma = 0
while counter <= 100:
    suma += counter
    counter += 1

print(f"La suma de los numeros del 1 al 100 es: {suma}")


print("Ejercicio 25")
#ejercicio 25
#Escribe un programa que cuente cuántas veces aparece una letra en una cadena de texto utilizando un bucle for

chain = input("Ingrese una frase por favor: ")
letter_count = input("Que letra desea contar: ")
counter = 0
for letter in chain:
    if letter == letter_count:
        counter += 1
print(f"La letra '{letter_count}' aparece {counter} veces en la cadena.")


print("Ejercicio 26")
#ejercicio 26
#Utiliza un bucle for para imprimir los números del 10 al 1 en orden decreciente
for i in range(10, 0, -1):
    print(i)


print("Ejercicio 27")
#ejercicio 27
#Escribe un programa que imprima los números impares del 1 al 30 usando un bucle for
for num in range(1, 31):
    if num % 2 != 0:
        print(num)

print("Ejercicio 28")
# ejercicio 28
#Usa un bucle while para encontrar el primer número divisible por 7 y 11.
number = 1
while True:
    if number % 7 == 0 and number % 11 == 0:
        print(f"El primer número divisible por 7 y 11 es: {number}")
        break
    number += 1


print("Ejercicio 29")
# ejercicio 29
#Escribe un programa que genere los primeros 10 números de la secuencia Fibonacci.
fibonacci = [0, 1]
for i in range(2, 10):
    next_number = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(next_number)

for num in fibonacci:
    print(num)


print("Ejercicio 30")
# ejercicio 30
#Utiliza un bucle for para imprimir los elementos de una lista en reversa.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for element in reversed(numbers):
    print(element)

print("Ejercicio 31")
# ejercicio 31
#Escribe un programa que determine si un número es positivo, negativo o cero.
# Pedir al usuario que ingrese un número
num = int(input("Ingresa un número: "))
if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")


print("Ejercicio 32")
# ejercicio 32
#Dado un número, verifica si es par o impar.
num =int(input("Ingrese un numero: "))
if num % 2 == 0:
    print(f"El numero {num} es par")
else:
    print(f"El numero {num} es impar")


print("Ejercicio 33")
# ejercicio 33
#Escribe un programa que determine si un año es bisiesto
year = int(input("Ingresa un año: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} es un año bisiesto.")
else:
    print(f"{year} no es un año bisiesto.")


print("Ejercicio 34")
# ejercicio 34
#Dada la edad de una persona, clasifícala como niño, adolescente, adulto o anciano.
age = int(input("Ingrese una edad: "))
if age < 18:
    if age < 13:
        print("Eres un niño.")
    else:
        print("Eres un adolescente.")
elif age < 64:
    print("Eres un adulto.")
else:
    print("Eres un anciano.")


print("Ejercicio 35")
# ejercicio 35
#Escribe un programa que determine si un triángulo es equilátero, isósceles o escaleno.
side_1 = float(input("Ingresa la longitud del primer lado: "))
side_2 = float(input("Ingresa la longitud del segundo lado: "))
side_3 = float(input("Ingresa la longitud del tercer lado: "))

if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
    if side_1 == side_2 == side_3:
        print("Es un triángulo equilátero.")
    elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
        print("Es un triángulo isósceles.")
    else:
        print("Es un triángulo escaleno.")
else:
    print("No es un triángulo válido.")


print("Ejercicio 36")
# ejercicio 36
#Dado un número, verifica si es primo o no
nums = int(input("Ingresa un número: "))
if nums > 1:
    is_cousin = True
    for i in range(2, nums):
        if (nums % i) == 0:
            is_cousin = False
            break
    if is_cousin:
        print(f"{nums} es un número primo.")
    else:
        print(f"{nums} no es un número primo.")
else:
    print("El número debe ser mayor que 1 para ser considerado primo.")


print("Ejercicio 37")
# ejercicio 37
#Escribe un programa que clasifique a un estudiante según su calificación (A, B, C, D, F).
qualification = float(input("Ingresa la calificación del estudiante: "))
if qualification >= 95:
    print("Calificación: A (Excelente)")
elif qualification >= 85:
    print("Calificación: B (Muy bien)")
elif qualification >= 75:
    print("Calificación: C (Satisfactorio)")
elif qualification >= 65:
    print("Calificación: D (Puede mejorar)")
else:
    print("Calificación: F (Reprobado)")

print("Ejercicio 38")
# ejercicio 38
#Dada una cadena de texto, verifica si es un palíndromo.
text = input("Ingresa una cadena de texto: ")
text = text.replace(" ", "").lower()
if text == text[::-1]:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")


print("Ejercicio 39")
# ejercicio 39
#Escribe un programa que determine si un número es divisible por 3 y 5.
number = int(input("Ingresa un número: "))
if number % 3 == 0 and number % 5 == 0:
    print(f"{number} es divisible por 3 y 5.")
else:
    print(f"{number} no es divisible por 3 y 5 al mismo tiempo.")


print("Ejercicio 40")
# ejercicio 40
#Dado un número, verifica si es positivo y múltiplo de 4.
nums = int(input("Ingresa un número: "))
if nums > 0 and nums % 4 == 0:
    print(f"{nums} es positivo y múltiplo de 4.")
else:
    print(f"{nums} no cumple con ambas condiciones (positivo y múltiplo de 4).")



