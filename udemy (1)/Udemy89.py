#Write a Python  program to convert adjectives into adverbs of the following:
# 'nice,strong, cute'
lista=["nice","strong","cute"]
def convert (lista,agregado):
    adverbs=[]
    for palabra in lista:
        adverbio=palabra + agregado
        adverbs.append(adverbio)
    return adverbs

print(convert(lista,"ly"))
    
    