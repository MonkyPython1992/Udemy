# Write a Python program that takes a word and give true if the word has two identical letters


def double_letters(word):
    return any(letter*2 in word for letter in word)

print(double_letters("moon"))


#La función ,any, devuelve el booleano True si alguno de los elementos del iterable que se cede como argumento es True, 
# y devuelve el booleano False en caso contrario (o si el iterable está vacío).