# ###
# # 02 - Bucles (for)
# # Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable o una lista
# ###

# print("\nBucle for:")

# # Iterar una lista
# frutas = ["manzana", "pera", "mandarina"]
# for fruta in frutas:
#     print(fruta)

# # Iterar sobre cualquier cosa que sea iterable
# cadena = "midudev"
# for caracter in cadena:
#     print(caracter)

# # enumerate()
# frutas = ["manzana", "pera", "mandarina"]
# for idx, value in enumerate(frutas):
#     print(f"El índice es {idx} y la fruta es {value}")

# # bucles anidados
# letras = ["A", "B", "C"]
# numeros = [1, 2, 3]

# for letra in letras:
#     for numero in numeros:
#         print(f"{letra}{numero}")


# # break
# print("\nbreak:")
# animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
# for idx, animal in enumerate(animales):
#     print(animal)
#     if animal == "loro":
#         print(f"El loro está escondido en el índice {idx}")
#         break

# # continue
# print("\ncontinue:")
# animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
# for idx, animal in enumerate(animales):
#     if animal == "loro":
#         continue

#     print(animal)

# # Comprensión de listas (list comprehension)
# animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
# animales_mayus = [animal.upper() for animal in animales]
# print(animales_mayus)

# # Muestra los números pares de una lista
# pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
# print(pares)

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

print("una forma")
numeros = [num for num in [1, 2, 3, 4, 5, 6, 7, 8, 9] if num % 2 == 0]
print(numeros)

print("otra forma")
for num in range(2, 20):
    if num % 2 == 0:
        print(num)

print("otra forma")
nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for num in nums:
    if num % 2 == 0:
        print(num)


# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")

numeros = [10, 20, 30, 40, 50]

suma = 0

for num in numeros:
    suma += num

print(suma // len(numeros))

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
numero_mayor = 0
numeros = [15, 5, 25, 10, 20, 200]
for num in numeros:
    if num > numero_mayor:
        numero_mayor = num
print(f"el numero mayor de la lista {numeros} es {numero_mayor}")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
palabras = ["casa", "arbol", "sol", "elefante", "luna", "alicanto"]

# una forma
palabras_mas_cinco_letras = [palabra for palabra in palabras if len(palabra) > 5]
print(palabras_mas_cinco_letras)

# otra forma
palabras_mas_cinco_letras = []
for palabra in palabras:
    if len(palabra) > 5:
        palabras_mas_cinco_letras.append(palabra)
print(palabras_mas_cinco_letras)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).

palabras = ["casa", "arbol", "sol", "Elefante", "luna", "coche", "exactitud"]
count = 0
print("\nEjercicio 5:")
try:
    input_letter = input("introduce una letra: ").lower()
    for palabra in palabras:
        if palabra.lower().startswith(input_letter):
            count += 1
    print(f"hay un total de {count} palabras que empiezan por {input_letter}")

except:
    print("introduza un caracter valido")

print("otra forma")

count = 0
for palabra in palabras:
    if palabra[0].lower() == input_letter:
        count += 1
print(f"hay un total de {count} palabras que empiezan por {input_letter}")
