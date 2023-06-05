#Create a function that takes a list of numbers and returns the sum of its cubes

numbers=[1,2,4,12,3]

def sum_cubes(lista):
    cubes=[]
    for numero in lista:
        cubes.append(numero**3)
    
    return sum(cubes)

print("Sum of cubes of list:",sum_cubes(numbers))
        