def distribute_weight(weight: int) -> str:

    boxes = {
        1: [" _ ", "|_|"],
        2: [" ___ ", "|___|"],
        5: [" _____ ", "|     |", "|_____|"],
        10: [" _________ ", "|         |", "|_________|"],
    }
    stacked_boxes = []
    result_box = ""
    goal = weight
    repetitions = 0

    while goal > 0:
        for idx, box in reversed(boxes.items()):
            if goal >= idx:

                stacked_boxes.append(box)
                goal = goal - idx
                break

    reversed_stacked_boxes = list(reversed(stacked_boxes))

    for idx_box, box in enumerate(reversed(stacked_boxes)):

        for idx_part, part_of_box in enumerate(box):
            if len(stacked_boxes) == 1:

                result_box += f"{part_of_box}\n"
            else:
                if idx_box == 0:  # La caja de arriba del todo

                    pass
                elif (
                    idx_box == 1
                ):  # la segunda caja, aqui armamos la caja de arriba del todo tambien

                    if idx_part == 0:  # 0 es el techo
                        # recuerda que la lista stacked_boxes debes tratarla del reves

                        repetitions = reversed_stacked_boxes[idx_box - 1][0].count("_")
                        if len(box) < 3 or len(reversed_stacked_boxes[idx_box - 1]) < 3:
                            result_box += f"{reversed_stacked_boxes[idx_box-1][0]}\n{reversed_stacked_boxes[idx_box-1][1]}{part_of_box.replace("_", "", repetitions+1).strip()}\n"
                        else:
                            result_box += f"{reversed_stacked_boxes[idx_box-1][0]}\n{reversed_stacked_boxes[idx_box-1][1]}\n{reversed_stacked_boxes[idx_box-1][2]}{part_of_box.replace("_", "", repetitions+1).strip()}\n"

                    elif (
                        idx_part > 0
                        and idx_part == len(box) - 1
                        and idx_box == len(reversed_stacked_boxes) - 1
                    ):
                        result_box += f"{part_of_box}"

                    else:
                        if (
                            len(stacked_boxes) > 2
                            and reversed_stacked_boxes[idx_box + 1][0].count("_")
                            > reversed_stacked_boxes[idx_box][0].count("_")
                            and idx_part
                            == len(box) - 1  # si es la ultima parte de la box
                        ):

                            down = reversed_stacked_boxes[idx_box + 1][0].count("_")
                            top = reversed_stacked_boxes[idx_box][0].count("_")
                            repetitions = down - top - 1

                            # result_box += f"{part_of_box.replace("_", "", repetitions+1).strip()}\n"

                            result_box += f"{part_of_box}{"_"*repetitions}\n"

                        else:

                            result_box += f"{part_of_box}\n"  # al ser la part_box mayor a 0, coloca la parte sin el techo

                elif (
                    idx_box > 1 and idx_box <= len(reversed_stacked_boxes) - 2
                ):  # resto de cajas, menos la ultima y las 2 primeras (0 y 1)

                    if idx_part == 0:
                        pass
                    elif idx_part == len(box) - 1:

                        down = reversed_stacked_boxes[idx_box + 1][0].count("_")
                        top = reversed_stacked_boxes[idx_box][0].count("_")
                        repetitions = down - top - 1
                        result_box += f"{part_of_box}{"_"*repetitions}\n"
                    else:
                        result_box += f"{part_of_box}\n"

                else:  # ultima caja

                    if idx_part == 0:
                        pass
                    elif idx_part > 0 and idx_part <= len(box) - 2:
                        result_box += f"{part_of_box}\n"
                    else:
                        result_box += f"{part_of_box}"
                        # a la finalisima parte le quitamos el salto de linea

    return result_box


print(distribute_weight(1))
