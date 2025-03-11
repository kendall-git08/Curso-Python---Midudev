global_instructions = ["MOV 3 C", "DEC C", "DEC C", "DEC C", "JMP C 3", "MOV C A"]


def manual_creator(instructions):
    manual = {}
    for idx, instruction in enumerate(instructions):
        manual[idx] = instruction.split(" ")
    return manual


def compile(instructions):
    machine_operations = {}
    manual = manual_creator(instructions)
    number_of_loops = 0

    for instruction in instructions:
        if instruction.startswith("JMP"):
            number_of_loops += 1

    for _ in range(number_of_loops + 1):
        for instructions in manual.values():
            if instructions[0] == "MOV":
                try:
                    machine_operations[instructions[2]] = int(instructions[1])
                except:
                    try:
                        machine_operations[instructions[2]] = machine_operations[
                            instructions[1]
                        ]
                    except:
                        machine_operations[instructions[1]] = 0
                        machine_operations[instructions[2]] = 0

            if instructions[0] == "INC":
                try:
                    machine_operations[instructions[1]] += 1
                except:
                    machine_operations[instructions[1]] = 1

            if instructions[0] == "DEC":
                try:
                    machine_operations[instructions[1]] -= 1
                except:
                    machine_operations[instructions[1]] = 1

            if instructions[0] == "JMP":
                if machine_operations[instructions[1]] == 0:
                    manual = manual_creator(global_instructions[int(instructions[2]) :])

                    break
                else:
                    continue
        else:
            break

    return machine_operations.get("A", None)


print(compile(global_instructions))
