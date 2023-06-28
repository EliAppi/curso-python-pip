#Juego piedra papel o tijera por rounds con funciones
import random    #libreria opciones aleatorias


def choose_option():
  option=("piedra","papel","tijera") #creo tupla ya que las opciones no se pueden modificar en el juego
  user_option = input("piedra, papel o tijera= ")
  user_option = user_option.lower() # Convierto entrada de usuario a minusculas
  pc_option =random.choice(option)
  return(user_option,pc_option,option)
  
def check_rules(user_option,pc_option,user_point,
  pc_point):
  
  template=(f"La maquina puso= {pc_option}")
  if user_option =="piedra" and pc_option=="papel":
    print(template,"\nPerdiste")
    pc_point+=1
  elif user_option =="piedra" and pc_option=="tijera":
    print(template,"\nGanaste!")
    user_point+=1
  elif user_option =="papel" and pc_option=="piedra":
    print(template,"\nGanaste!")
    user_point+=1
  elif user_option =="papel" and pc_option=="tijera":
    print(template,"\nPerdiste")
    pc_point+=1
  elif user_option =="tijera" and pc_option=="piedra":
    print(template,"\nPerdiste")
    pc_point+=1
  elif user_option =="tijera" and pc_option=="papel":
    print(template,"\nGanaste!")
    user_point+=1
  else:
    print(template,"\nEmpate")
      
  return (user_point,pc_point)

def run_game():
  round=1
  user_point=0
  pc_point=0
  total_round=input("Cuantos round seran? ")
  
  while(round<=int(total_round)):
    print("*"*10) # Separador manual de operaciones
    print("Round ",round)
    
    user_option,pc_option,option=choose_option() #Llamara aca funcion de choose
    
    if user_option in option:
          
      user_point,pc_point=check_rules(user_option,pc_option,user_point,
  pc_point)#Llamar aca funcion de rules
      print(f"Puntaje: Tú: {user_point}, Maquina: {pc_point}")
      round+=1
    
    else:
        print("*"*10,"\nElige una opcion valida")
  
  check_results(user_point,pc_point)#Llamar aca funcion de resultados
  
def check_results(user_point,pc_point):
  if user_point<pc_point:
    print("*"*10,"\nPerdiste el juego!")
  elif user_point>pc_point:
    print("*"*10,"\nGanaste el juego!")
  else:
    print("*"*10,"\nEmpataron el juego!")

run_game()