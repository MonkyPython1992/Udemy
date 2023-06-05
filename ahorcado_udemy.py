import random

palabras_animales= 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()

imagenes_vidas= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   | 
  O   |
 /|\  |
 / \  |
      |
=========''']

def obtenerPalabraAlAzar(listaDePalabras):
  índiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
  return listaDePalabras[índiceDePalabras]

palabra_elegida=obtenerPalabraAlAzar(palabras_animales).lower()
letras_de_palabra= len(palabra_elegida)

game_over= False

intentos = 6
print("A H O R C A D O")

resultado=[]

for _ in range(letras_de_palabra):
  resultado += '_'

#iterador para que el juego continue en funcionamiento
while not game_over:
  player_input=input(" \n Elija una letra:   \r")
  if player_input in resultado:
    print(f'Letra adivinada:{player_input} ')
  
  for posicion in range(letras_de_palabra):
    letra= palabra_elegida[posicion]
    if letra == player_input:
      resultado[posicion] = letra

  if player_input not in resultado:
    print(f' {player_input} no se encuentra en la palabra  \n')
    intentos -=1
    if intentos == 0:
      game_over= True
      print(" \n Game Over  \n")
      print(f" \n La plabra era: {palabra_elegida}")

  
  print(f"{''.join(resultado)}")

  if '_' not in resultado:
    game_over= True
    print("Has ganado!")

  print(imagenes_vidas[6-intentos])
  