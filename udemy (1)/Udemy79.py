#Sara, Kate and John are playing a board game. The three of them decided to come up with a new scoring system. 
#A player's first initial ("A", "B" or "C") denotes that player scoring a single point. 
#Given a string of capital letters, return a list of the players' scores.


puntuacion="ABCBBCAACBCACB"

def score(puntuacion):
    Sara=0
    Kate=0
    John=0
    for caracter in puntuacion:
        if caracter =="A":
            Sara+=1
        elif caracter == "B":
            Kate+=1
        elif caracter == "C":
            John+=1
    
    lista=["Sara:",Sara," kate:",Kate, " John:",John]
    return lista

print(score(puntuacion))