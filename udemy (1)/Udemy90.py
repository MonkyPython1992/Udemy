#A number added with its additive inverse equals zero. Create a function that returns a list of additive inverses.

numbers=[1,21,-34,123,-30]
def inverse_additive(lista):
    inverses=[]
    for numero in lista:
        x= 0 - numero
        inverses.append(x)
    return inverses

print(inverse_additive(numbers))