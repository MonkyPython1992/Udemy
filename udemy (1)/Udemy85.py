#Create a function that returns a sorted string with no duplicate characters
def sorted(string):
    new_string=[]
    for i in string:
        if i not in new_string:
            new_string.append(i)
    
    return new_string
        
new=sorted("asaadff")
new1= "".join(new)
print(new1)

#Create a function that returns the words in reverse order:
Example=['circus', 'flying', 'pythons', 'monty']

def reverse_order(lista):
    return lista[::-1]

print(reverse_order(Example))


