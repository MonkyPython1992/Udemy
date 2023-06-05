#Create a function that takes three number arguments — one number as an input and two additional numbers 
# representing the endpoints of a closed range and return the number limited to this range.

#If the number falls within the range, the number should be returned.

#If the number is less than the lower limit of the range, the lower limit should be returned.

#If the number is greater than the upper limit of the range, the upper limit should be returned.

def endpoints(num,range1,range2):
    
    if num > range1 and num < range2:
        return num
    elif num < range1:
        return range1
    else:
        return range2
        
num=int(input("Ingrese un numero: "))
print(endpoints(num,100,349))
