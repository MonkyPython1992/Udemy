#Write a Python program that cotain a function which take a string of numbers separated by a comma and space and, 
# return the total of all the numbers.
texto="1 ,2 ,3 , 4 ,5 , 6"
numeros=["1","2","3","4","5","6","7","8","9","0"]
def total_num(string,numeros):
    contador=0
    for caracter in string:
        for numero in numeros:
            if caracter==numero:
                contador+=1
        
   
    return contador

print("Total de números en el string: ",total_num(texto,numeros))