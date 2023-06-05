class GameBoard():
  #creamos instancias de gameboard

  def __init__(self):
    self.game_board={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' ' }

  #creamos los setters de los items
  def set_items(self,user,position,game_board):
    game_board[position]=user
    return game_board

  #creamos un decorador @property para la funcion del tablero ,para poder crear diferentes instancias
  @property
  #Se usa para asignarle una funcionalidad "especial" a ciertos métodos para que actúen como getters, setters o deleters al momento de definir y usar propiedades en una clase.
  def gameBoard(self):
    return self.game_board

  def ClearBoard(self):
    self.game_board={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' ' }

  def is_place_taken(self,game_board,index):
    if game_board[index] != ' ':
      return True

  def is_board_full(self,game_board):
    for index in range(1,10):
      if game_board[index] == ' ':
        return False

    return True

  def is_game_won(self,game_board):
    win_condition=((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
    for win in win_condition:
      if game_board[win[0]] == game_board[win[1]] and game_board[win[1]] == game_board[win[2]] and game_board[win[0]] != ' ':
        return True
    
  #funcion para imprimir el tablero
  def printBoard(self,game_board):
    index=0
    for fila in range(1,4):
      for columna in range(1,4):
        index+=1
        if columna != 3:
          print(game_board[index],end='')
          print("|",end='')
        else:
          print(game_board[index])

class Game():
  #comienzo de juego
  def game_start(self):

    self.controlboard=GameBoard()
    self.game_board= self.controlboard.gameBoard
    
    print("Bienvenidos al juego X-O o Ta-Te-Ti")
    print("Ingrese el nombre del jugador 1")
    self.player_1_name=input(" : ")
    print("Ingrese el nombre del jugador 2 ")
    self.player_2_name=input(" : ")
    print("El tablero esta representado por indices del 1 al 9 que determinan la posicion de tu X o de tu O")
    print(" \n \n")
    self.player_1='X'
    self.player_2='O'
    self.controlboard.printBoard(self.game_board)
    print(" \n \n")
    self.turno=1
    
  #final del juego y posibilidad de volver a jugar
  def game_end(self):
    if self.game_running== False:
      replay =input("Ingresa 0 para salir, o 1 para volver a jugar:")
      try:
        if int(replay):
          self.game_running = True
          self.game_start()
      except:
        print("Por favor ingrese un numero")

  #administracion de turnos
  def take_turns(self,user,item):
    print(" \n ")
    print("Elegi un numero del 1 al 9 para ubicar tu jugada.")
    try:
      position=int(input(": "))
      print(" \n")
      if position > 9 or position < 1:
        raise Exception

    except:
      print("Elegi un numero del 1 al 9.")
      return self.take_turns(user,item)

    if self.controlboard.is_place_taken(self.game_board,position):
      print("Esa posicion ya esta ocupada.")
      self.take_turns(user,item)
    else:
      self.controlboard.set_items(user,position,self.game_board)
      self.controlboard.printBoard(self.game_board)
      if self.controlboard.is_game_won(self.game_board):
        if user == "X":
          print("\n" + self.player_1_name + " has ganado! \n")
          self.game_running=False
        else:
          print( "\n"+ self.player_2_name + " has ganado! \n")
          self.game_running=False

  
      
  #manejo del juego
  def main(self,):
    self.game_running=True
    self.game_start()
    while self.game_running:
      if self.turno%2 !=0:
        self.take_turns(self.player_1,"X")
      else:
        self.take_turns(self.player_2,"O")

      if self.controlboard.is_board_full(self.game_board):
        print("Empate.")
        self.game_running= False

      self.turno +=1

      if not self.game_running:
        self.game_end()

#game launcher
if __name__=='__main__':
  Game().main()
      
    
      
          
        
  

    
        
      