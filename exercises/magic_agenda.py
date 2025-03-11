agendita = "+34-600-123-456 Calle Gran Via 12 <Juan Perez> Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654 <Carlos Ruiz> +1-800-555-0199 Fifth Ave New York"
# pattern = r"\+\d{1,3}[\d-]+"  # resumido y menos preciso, porque aparte del +34 o +31, buscara que tengan 1 o mas numerales o guiones, por lo que no estas estableciendo de manera precisa la estructura del numero telefonico
# number_pattern = r"\+\d{1,3}-\d{3,4}-\d{3,4}-\d{3,4}"  # mas largo, pero muchisimo mas preciso, ahora tendra que tener 3 o 4 numeros separados por guiones
# # pattern_2 = r"\w"
# # pattern_3 = r"^\+"
# name_pattern = r"<([\w\s]+)>"
# numbers = re.findall(number_pattern, agenda)
# print(numbers)

# names = re.findall(name_pattern, agenda)
# print(names)

import re


def find_in_agenda(agenda, phone):
    pattern = r"\+\d{1,3}[\d-]+"
    name_pattern = r"<([\w\s]+)>"
    direction_pattern = r"[A-Z][\w\s]+"
    count = 0
    to_find_direction = re.sub(name_pattern, "|", agenda)
    to_find_direction = re.sub(pattern, "|", to_find_direction)

    numbers = re.findall(pattern, agenda)
    names = re.findall(name_pattern, agenda)
    directions = re.findall(direction_pattern, to_find_direction)
    contact = None

    for idx_number, number in enumerate(numbers):
        if phone in number:
            contact = {
                "name": names[idx_number],
                "address": directions[idx_number].strip(),
            }

            count += 1
            if count > 1:
                return None
    return contact


print(find_in_agenda(agendita, "111111"))


# def find_in_agenda(agenda, phone):
#     # Patrones
#     pattern = r"\+\d{1,3}[\d-]+"
#     name_pattern = r"<([\w\s]+)>"
#     direction_pattern = r"[A-Z][\w\s]+"
#     to_find_direction = re.sub(name_pattern, "|", agenda)
#     to_find_direction = re.sub(pattern, "|", to_find_direction)

#     numbers = re.findall(pattern, agenda)
#     names = re.findall(name_pattern, agenda)
#     directions = re.findall(direction_pattern, to_find_direction)

#     # Validar coincidencias y buscar el contacto
#     contact = None
#     for idx_number, number in enumerate(numbers):
#         if phone in number:
#             if idx_number < len(names) and idx_number < len(
#                 directions
#             ):  # Validación de índices
#                 contact = {
#                     "name": names[idx_number],
#                     "address": directions[idx_number].strip(),
#                 }
#             else:
#                 return None
#             break  # Salir del bucle después de encontrar el contacto

#     return contact
