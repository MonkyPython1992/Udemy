#Write a Python program that sorts the positive numbers in ascending order, and keeps the negative numbers untouched.
lista=[2,5,3,12,-9,11,-4,-6]
lista_positivos=[]
lista_negativos=[]

def sorts (lista):
    for numero in lista:
        if numero > 0:
            lista_positivos.append(numero)
        elif numero < 0:
            lista_negativos.append(numero)
    
    return (sorted(lista_positivos) + (lista_negativos))


print(sorts(lista))
            
    