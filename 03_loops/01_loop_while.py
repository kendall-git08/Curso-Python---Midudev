
# ###
# # 01 - Bucles (while)
# # Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
# ###

# print("\n Bucle while:")

# # Bucle con una simple condición
# contador = 0

# while contador <= 5:
#   print(contador)
#   contador += 1 # es super importante para evitar un bucle infinito

# # utilizando la palabra break, para romper el bucle
# print("\n Bucle while con break:")
# contador = 0

# while True:
#   print(contador)
#   contador += 1
#   if contador == 5:
#     break # sale del bucle

# # continue, que lo hace es saltar esa iteración en concreto
# # y continuar con el bucle
# print("\n Bucle con continue")
# contador = 0
# while contador < 10:
#   contador += 1

#   if contador % 2 == 0:
#     continue

#   print(contador)

# # else, esta condición cuando se ejecuta?
# print("\n Bucle while con else:")
# contador = 0
# while contador < 5:
#   print(contador)
#   contador += 1
# else:
#   print("El bucle ha terminado")

# # else, esta condición cuando se ejecuta?
# print("\n Bucle while con else:")
# contador = 0
# while contador < 5:
#   print(contador)
#   contador += 1
# else:
#   print("El bucle ha terminado")

# # pedirle al usuario un número que tiene
# # que ser positivo si no, no le dejamos en paz
# numero = -1
# while numero < 0:
#   numero = int(input("Escribe un número positivo: "))
#   if numero < 0:
#     print("El número debe ser positivo. Intenta otra vez, majo o maja.")

# print(f"El número que has introducido es {numero}")

# numero = -1
# while numero < 0:
#   try:
#     numero = int(input("Escribe un número positivo: "))
#     if numero < 0:
#       print("El número debe ser positivo. Intenta otra vez, majo o maja.")
#   except:
#     print("Lo que introduces debe ser un número, que si no peta!")

# print(f"El número que has introducido es {numero}")

###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

from os import system
if system("clear") != 0: system("cls")

print("\n Bucle while:")

# Bucle con una simple condición
contador = 0

while contador <= 5:
  print(contador)
  contador += 1 # es super importante para evitar un bucle infinito

# utilizando la palabra break, para romper el bucle
print("\n Bucle while con break:")
contador = 0

while True:
  print(contador)
  contador += 1
  if contador == 5:
    break # sale del bucle

# continue, que lo hace es saltar esa iteración en concreto
# y continuar con el bucle
print("\n Bucle con continue")
contador = 0
while contador < 10:
  contador += 1

  if contador % 2 == 0:
    continue

  print(contador)

# else, esta condición cuando se ejecuta?
print("\n Bucle while con else:")
contador = 0
while contador < 5:
  print(contador)
  contador += 1
else:
  print("El bucle ha terminado")

# else, esta condición cuando se ejecuta?
print("\n Bucle while con else:")
contador = 0
while contador < 5:
  print(contador)
  contador += 1
else:
  print("El bucle ha terminado")

# pedirle al usuario un número que tiene
# que ser positivo si no, no le dejamos en paz
numero = -1
while numero < 0:
  numero = int(input("Escribe un número positivo: "))
  if numero < 0:
    print("El número debe ser positivo. Intenta otra vez, majo o maja.")

print(f"El número que has introducido es {numero}")

numero = -1
while numero < 0:
  try:
    numero = int(input("Escribe un número positivo: "))
    if numero < 0:
      print("El número debe ser positivo. Intenta otra vez, majo o maja.")
  except:
    print("Lo que introduces debe ser un número, que si no peta!")

print(f"El número que has introducido es {numero}")


###
# EJERCICIOS (while)
###
import os

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

number = 10
while number > 0:
    print(number)
    number -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.

os.system("cls")

print("\nEjercicio 2:")
number = 1
suma = 0

while 1 <= number <= 20:
    if number % 2 != 0:
        number += 1
        continue

    suma += number
    number += 1
print(suma)


# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

# os.system('cls')
# print("\nEjercicio 3:")
# mult = 1
# number = int(input('Introduce un numero para calcular su factorial: '))
# while number > 0:
#     mult *= number
#     number -= 1
# print(mult)


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".

os.system("cls")
print("\nEjercicio 4:")


# while True:
#     password = input("Introduce tu contrase;a: ")
#     print(len(password))
#     if len(password) < 8:
#         print('debe tener 8 caracteres')
#         continue
#     break


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
os.system("cls")
print("\nEjercicio 5:")

# multiplicator = 1
# number = int(input('introduce un numero: '))
# while multiplicator <= 10:
#     print(f'{number}x{multiplicator} = {number*multiplicator}')
#     multiplicator += 1


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

prime_number = int(input("introduce un numero: "))


while prime_number > 1:
    is_prime = True
    divisor = prime_number - 1

    while divisor > 1:
        if prime_number % divisor == 0:
            is_prime = False
            break

        divisor -= 1

    if is_prime:
        print(prime_number)

    prime_number -= 1
