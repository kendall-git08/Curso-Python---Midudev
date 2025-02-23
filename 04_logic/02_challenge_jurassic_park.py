"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

# Para ver si un número es par
#  siempre usamos el módulo %
#  nos da el resto de la división: eggs % 2 == 2


# con el => decimos que va a devoler un entero
def t_reggs_counter(list_of_eggs: list) -> int:
    t_reggs_count = 0
    for eggs in list_of_eggs:
        if eggs % 2 == 0:
            t_reggs_count += eggs
    return t_reggs_count


number_of_t_reggs = t_reggs_counter([1, 2, 3, 4, 5, 6, 7, 8])
print(number_of_t_reggs)
