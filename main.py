#Welcomes user to the game
print("Welcome da dice game")

import random

def start_game():
   life = 3

   while life > 0:

      result = 0

      #roles the 2 dice pregame
      st = random.randint(1,6)
      nd = random.randint(1,6)

      #roles and displays the first role
      # print("|-------------------|")
      # print("| Rolling your dice |")
      # print("|-------------------|")
      print("The value of the first dice is " + str(st) +"")

      #roles and displays the second role
      # print("|-------------------|")
      # print("| Rolling your dice |")
      # print("|-------------------|")
      print("The value of the second dice is " + str(nd) +"")  

      print("")

      #add the scores if any of the var = 1 or 6  
      if st in [1,6]:
         result = result + 50
         
      if nd in [1,6]:
         result = result + 50

      life = life - 1

   #end txt for the game
   if result == int(100):
      print("Congratulations your score is " + str(result) + " you win!!!")
   else:
      print("You lost...")

while True:
   start_game()
   if input("Do you want to play again? (Y/N)") == "N":
      exit()