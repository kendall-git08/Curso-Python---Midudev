movements_options = {
    "select_u": {"letter": "U", "to_row": -1, "to_space": 0},
    "select_l": {"letter": "L", "to_row": 0, "to_space": -1},
    "select_r": {"letter": "R", "to_row": 0, "to_space": 1},
    "select_d": {"letter": "D", "to_row": 1, "to_space": 0},
}


def magic_train(board, mov):
    for option in movements_options.values():
        if option["letter"] == mov:
            letter = option
            break

    for idx_row, row in enumerate(board):
        if "@" in row:
            idx_head = row.find("@")

            try:
                if (
                    board[idx_row + letter["to_row"]][idx_head + letter["to_space"]]
                    == "*"
                    and idx_head + letter != -1
                ):
                    return "eat"
                if (
                    board[idx_row + letter["to_row"]][idx_head + letter["to_space"]]
                    == "·"
                    and idx_head + letter != -1
                ):
                    print("entre aqui")
                    return "none"
                if (
                    board[idx_row + letter["to_row"]][idx_head + letter["to_space"]]
                    == "o"
                    and idx_head + letter != -1
                ):
                    return "crash"
            except:
                return "crash"


board = ["@····", "o····", "o····"]
mov = input(
    "introduce tu movimiento [U/L/R/D] para el siguiente tablero\n·····\n*····\n@····\no····\no····\n"
).upper()

print(magic_train(board, mov))
