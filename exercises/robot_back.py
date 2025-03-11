possible_movements = {"U": [0, 1], "L": [-1, 0], "R": [1, 0], "D": [0, -1]}

history = {0: [0, 0]}


def step_inverter(step):
    if step == "U":
        return "D"
    if step == "D":
        return "U"
    if step == "L":
        return "R"
    if step == "R":
        return "L"


def symbol_cleaner(sequence):
    cleaned_sequence = ""
    for idx_step, step in enumerate(sequence):
        if step == "*":
            new_step = sequence[idx_step + 1] * 2
            cleaned_sequence += new_step

        elif step == "!":
            new_step = step_inverter(sequence[idx_step + 1])
            cleaned_sequence += new_step

        elif step == "?":
            if sequence[idx_step + 1] in cleaned_sequence:
                continue
            else:
                cleaned_sequence += sequence[idx_step + 1]

        else:
            if sequence[idx_step - 1] not in ["*", "!", "?"]:
                cleaned_sequence += step
    return cleaned_sequence


def robot_back_detector(sequence):
    cleaned_sequence = symbol_cleaner(sequence)

    for order_step, step in enumerate(cleaned_sequence):
        current_movement = possible_movements[step]
        prev_movement = history[order_step]
        history[order_step + 1] = [
            current_movement[0] + prev_movement[0],
            current_movement[1] + prev_movement[1],
        ]
    last_position = list(history.values())[-1]

    if last_position == history[0]:
        return True
    else:
        return last_position


example = f"{'U?UD'}"
print(robot_back_detector(example))
