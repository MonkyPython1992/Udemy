#Write a function that takes a list and determines whether it's strictly increasing, strictly decreasing, or neither.

lista1=[1,2,3,4,5]
lista2=[5,4,3,2,1]
lista3=[2,5,3,8,9]

def lista_mode(lista):
    if lista == sorted(lista):
        return("The list is strictly increasing")
    elif lista == (sorted(lista,reverse=True)):
        return("The list is strictly decreasing")
    else:
        return("The list has no order")

print(lista_mode(lista2))


