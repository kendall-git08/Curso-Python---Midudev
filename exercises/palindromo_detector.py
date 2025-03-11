# Palindromo detector


def detector(word):
    if word == word[::-1]:
        print("es un palindromo")

    else:
        print("no es un palindromo")


input_word = input("escriba una palabra, para verificar si es un palindromo: \n")
detector(input_word)
