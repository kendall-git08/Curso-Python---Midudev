def package_sorter(packages):
    iterations = packages.count("(")
    unordered_list = packages

    for _ in range(iterations):
        for character_idx, character in enumerate(unordered_list):
            if character == "(":
                start = character_idx

            if character == ")":
                final = character_idx

                unordered_list = (
                    unordered_list[:start]
                    + unordered_list[final - 1 : start : -1]
                    + unordered_list[final + 1 :]
                )

                break
    return unordered_list


print(package_sorter("(abc(def(ghi)))"))
