#Write a Python program that choose only integers from a mixed list like the Following:

x = [1, 'so', 2, 'too', 3, 'but', 4, 'soon', 5, 'every', 6, 'non', 7, 'right']

def only_int(list):
    integers=[]
    for x in list:
        if type(x)==int:
            integers.append(x)
    
    return integers
            
print(only_int(x))