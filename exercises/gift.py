def in_box(box):

    for index, row in enumerate(box):
        if "*" in row:
            if index == 0 or index + 1 == len(box):
                return False
            else:
                gift_index = row.find("*")
                return gift_index != 0 and gift_index + 1 != len(row)

    return False


box = ["#####", "#   #", "# * #", "#   #", "#####"]
print(in_box(box))
