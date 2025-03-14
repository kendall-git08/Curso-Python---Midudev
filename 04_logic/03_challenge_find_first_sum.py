"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

"""


# def goal_finder(nums: list, goal: int):
#     for candidate_idx, candidate in enumerate(nums):
#         for addens_idx, addens in enumerate(nums):
#             if addens_idx <= candidate_idx:
#                 continue
#             if candidate + addens == goal:
#                 return [candidate_idx, addens_idx]
#             return None

from os import system
if system("clear") != 0: system("cls")

# def find_first_sum(nums, goal):
#   # early return, una validación rápida
#   if len(nums) == 0: return None



# print(goal_finder(nums, goal))

# for i in [10, 2, 3, 4, 5, 6]:
#     print(i)

# Otra forma

nums = [4, 5, 6, 2]
goal = 11


def goal_finder(nums, goal):
    """
    Recibe una lista de numeros, y devuelve los indices que forman la combinacion que suman el valor 'goal'
    """
    seen = {}
    for idx_candidate, candidate in enumerate(nums):
        if goal - candidate in seen:
            return [seen[goal - candidate], idx_candidate]

        seen[candidate] = idx_candidate


print(goal_finder(nums, goal))
