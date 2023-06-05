#Write a function 'remove_indices' which removes one or more indices from a list.


lista=["John", "Bob", "Charles", "Trev"]

def remove_indices(lista,indices):
    for n in indices:
        del lista[n]
    return lista
        
    
print(remove_indices(lista,[1,2]))