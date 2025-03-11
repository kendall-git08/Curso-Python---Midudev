def detect_bombs(grid):
    grid_result = []
    for idx_row, row in enumerate(grid):
        new_row = []
        for idx_cell_focus, cell_focus in enumerate(row):
            count = 0
            for idx_row_comparate, row_comparate in enumerate(grid):
                for idx_cell_comparate, cell_comparate in enumerate(row_comparate):
                    if cell_comparate:
                        if idx_cell_focus - idx_cell_comparate in [
                            0,
                            1,
                            -1,
                        ] and idx_row - idx_row_comparate in [0, 1, -1]:
                            if (
                                idx_row - idx_row_comparate == 0
                                and idx_cell_focus - idx_cell_comparate == 0
                            ):
                                pass
                            else:
                                count += 1

            new_row.append(count)
        grid_result.append(new_row)
    else:
        return grid_result


# detect_bombs([[True, True], [False, False], [True, True]])
print(detect_bombs([[True, False, False], [False, True, False], [False, False, False]]))
