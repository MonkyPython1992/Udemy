list_1=[3, 5, 8, 9, 2, 2, 4]
list_2=[2,4,5,6,2,2,4]

list_3=[1,2,3,4,5,6]
list_4=[1,2,3,4,5,6]

list_5=[1,2,3,4,5,6]
list_6=[6,5,4,3,2,1]

def zipped(lista1,lista2):
    if lista1==lista2:
        return True
    elif lista1[-1] != lista2[-1]:
        return False
    for i in range(2, len(lista1)+1):
        if lista1[-i]!= lista2[-i]:
            return [len(lista1)-i, len(lista2)-i]
                
print(zipped(list_1,list_2))
print("segunda prueba")
print(zipped(list_3,list_4))
print("tercera prueba")
print(zipped(list_5,list_6))

#Two lists are part of the same zipper if the ending is identical. 
#The identical section can be thought of as being "zipped-up"
#Create a Python program that takes in two lists. Return False if none of the list is "zipped."
#Return True if the lists are identical. 
#Otherwise, return a list with the first index in each list where the zipper diverges.
            