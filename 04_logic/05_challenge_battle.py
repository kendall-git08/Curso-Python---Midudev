"""
Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud. 

Cada número en lista_a se "enfrenta" al número en la misma posición en lista_b.

- Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
- Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
- Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.

Debes simular estos enfrentamientos y devolver el resultado final:
- Si al final queda un número en lista_a, devuelve ese número seguido de la letra "a" (por ejemplo, "3a").
- Si al final queda un número en lista_b, devuelve ese número seguido de la letra "b" (por ejemplo, "2b").
- En caso de empate, devuelve la letra "x".

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

# resultado = battle(lista_a, lista_b)  # -> "2b"

# Explicación:
# - 2 vs 3: gana 3 (+1)
# - 4 vs 3+1: empate
# - 2 vs 4: gana 4 (+2)
# Resultado: "2b"

lista_a = [4, 4, 4]
lista_b = [2, 8, 2]

resultado = battle(lista_a, lista_b)  # -> "x"

# Explicación:
# - 4 vs 2: gana 4 (+2)
# - 4+2 vs 8: gana 8 (+2)
# - 4 vs 2+2: empate
# Resultado: "x"
"""

# Fuerza bruta: buscar la solución A SACO.
#  Algoritmos ocultos o cálculos o fórmulas
# Programación dinámica: buscar una solución mas eficiente


def battle(lista_a, lista_b):
    battles_matchmaking = {}
    difference = 0
    round_winner = None

    print(len(lista_a))

    for players in range(len(lista_a)):
        battles_matchmaking[lista_a[players]] = lista_b[players]

    for player_a, player_b in battles_matchmaking.items():
        if player_a > player_b:
            difference = player_a + difference - player_b
            round_winner = f"{difference}a"

        if player_b > player_a:
            difference = (player_a - player_b) * -1 + difference
            round_winner = f"{difference}b"

        else:
            difference = 0

    return round_winner


# resultado = battle(lista_a, lista_b)  # -> "2b"
lista_a = [6, 4, 4]
lista_b = [2, 8, 2]


def battle_list(lista_a, lista_b):
    difference = 0
    for index in range(len(lista_a)):
        difference = lista_a[index] + (-lista_b[index]) + difference

    if difference < 0:
        return f"{difference*-1}b"
    if difference == 0:
        return "x"
    else:
        return f"{difference}a"


print(battle_list(lista_a, lista_b))
