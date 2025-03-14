###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

from os import system
if system("clear") != 0: system("cls")

# """ Definición de una función

# def nombre_de_la_funcion(parametro1, parametro2, ...):
#   # docstring
#   # cuerpo de la función
#   return valor_de_retorno # opcional

# """

# # Ejemplo de una función para imprimir algo en consola
# def saludar():
#   print("¡Hola!")

# # Ejemplo de una función con parámetro
# def saludar_a(nombre):
#   print(f"¡Hola {nombre}!")

# saludar_a("midudev")
# saludar_a("madeval")
# saludar_a("pheralb")
# saludar_a("felixicaza")
# saludar_a("Carmen Ansio")

# # Funciones con más parámetros
# def sumar(a, b):
#   suma = a + b
#   return suma

# result = sumar(2, 3)
# print(result)

# # Documentar las funciones con docstring
# def restar(a, b):
#   """Resta dos números y devuelve el resultado"""
#   return a - b

# parámetros por defecto
# def multiplicar(a, b = 2):
#   return a * b

# print(multiplicar(2))
# print(multiplicar(2, 3))


# Argumentos por posición
def describir_persona(nombre: str, edad: int, sexo: str):
    print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")


# parámetros son posicionales
describir_persona(1, 25, "gato")
describir_persona("midudev", 25, "gato")
describir_persona("hombre", "madeval", 39)

# Argumentos por clave
# parámetros nombrados
describir_persona(sexo="gato", nombre="midudev", edad=25)
describir_persona(sexo="hombre", nombre="madeval", edad=21)


# Argumentos de longitud de variable (*args):
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma


print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# Argumentos de clave-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


mostrar_informacion_de(nombre="midudev", edad=25, sexo="gato")
print("\n")
mostrar_informacion_de(name="madeval", edad=21, country="Uruguay")
print("\n")
mostrar_informacion_de(nick="pheralb", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(super_name="felixicaza", es_modo=True, gatos=40)

#  Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
import os


def calculator(operator: str, num1: int, num2: int):
    if operator == "1":
        return num1 + num2
    if operator == "2":
        return num1 - num2
    if operator == "3":
        return num1 * num2
    if operator == "4":
        if num2 == 0:
            return "La division entre 0 es indefinida"
        else:
            return num1 % num2


# while True:
#     operator = input(
#         "Que operacion matematica quiere realizar? \n1.- Suma\n2.- Resta\n3.- multiplicacion\n4.- Division\n"
#     )

#     try:
#         num1, num2 = input("introduce los 2 numeros que quieres")
#         resultado = calculator(operator, int(num1), int(num2))

#         print(f"el resultado es: {resultado}")

#         decision = input("desea hacer otra operacion? y/n")

#         if decision == "y":
#             continue
#         break

#     except:
#         print("introduce los 2 numeros seguidos")

os.system("cls")
# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".


def codifier(message: list):
    aux_list = message[7:]
    secret_message = ""
    for letter in aux_list:
        secret_message += letter
    print(secret_message)


codifier(mensaje)


# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
os.system("cls")
numbers = [1, 2, 3, 4, 5, 6]


def elements_inverter(to_reverse: list):
    new_list = to_reverse[:3][::-1] + to_reverse[3:]
    print(new_list)


elements_inverter(numbers)

os.system("cls")
# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
# Un número es primo si es divisible por sólo uno de los números enteros entre 1 y él mismo, incluido.


def prime_detector(number: int):
    prime_numbers = []
    is_prime = True
    for candidate in range(2, number + 1):
        for divisor in range(candidate - 1, 1, -1):
            if candidate % divisor == 0:
                is_prime = False
                break
            else:
                is_prime = True

        if is_prime:
            prime_numbers.append(candidate)

        """ Determina los números primos menores o iguales que el valor que sea enviada como argumento"""
    return prime_numbers


number = int(input("introduce un numero"))
prime_numbers = prime_detector(number)

for i in prime_numbers:
    print(i)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).


def firstLetterDetector(letter: str):
    palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
    count = 0

    for palabra in palabras:
        if letter.lower() == palabra[0].lower():
            count += 1
    return count


letter = input("introduce una letra: ")
words = firstLetterDetector(letter)
print(words)
