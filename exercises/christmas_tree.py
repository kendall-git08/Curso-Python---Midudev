def tree_crafter(height, skin):
    tree = ""
    base = height - 1 + height
    log = (base - 1) // 2

    for asterike in range(1, base + 1, 2):
        aside = (base - asterike) // 2

        tree += f'{"_"*aside}{skin*asterike}{"_"*aside}\n'

    tree += f'{"_"*log}#{"_"*log}\n'
    tree += f'{"_"*log}#{"_"*log}'
    return tree


print(tree_crafter(3, "*"))
