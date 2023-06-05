#Write a function that takes two numbers and returns if they should be added, subtracted, multiplied or divided 
#to get 30.If none of the operations can give 30, return None.

def treinta (n1,n2):
    if n1 + n2== 30:
        return "Added "+ str(n1) + " and " + str(n2)
    elif n1 - n2 == 30 or n2 - n1 == 30:
        if n1 > n2:
            return "subtracted " + str(n1) +" and "+str(n2)
        else:
            return "subtracted " + str(n2) +" and "+ str(n1)
    elif n1 * n2 == 30:
        return "multiplied " + str(n1) + " and "+ str(n2)
    elif n1//n2 == 30 or n2//n1 == 30:
        if n1 > n2:
            return "Divided " +str(n1) +" and "+str(n2)
        else:
            return "Divided " + str(n2) +" and "+ str(n1) 
    else:
        return None
        
            
print(treinta(2,60))   