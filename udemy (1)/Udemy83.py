#Write a function "notbut" that prints the integers from 1 to 1000.
#But for multiples of three print "not" instead of the number, and for the multiples of five print "but".
#For numbers which are multiples of both three and five print "notbut".
def numeros():
    num=[]
    for i in range(1,1001,1):
        num.append(i)
    return num

lista=numeros()

def notbut (lista):
    
    for n in lista:
        if n%3==0 and n%5==0:
            print("notbut")
        elif n%5==0:
            print("but")
        elif n%3==0 :
            print("not")
        else:
            print(n)

    

print(notbut(lista))

