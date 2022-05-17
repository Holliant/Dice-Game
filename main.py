#Welcomes user to the game
print("Welcome da dice game")

import random
result = 0

#roles the 2 dice pregame
st = random.randint(1,6)
nd = random.randint(1,6)

#roles and displays the first role
print("|-------------------|")
print("| Rolling your dice |")
print("|-------------------|")
print("The value of the first dice is " + str(st) +"")

#roles and displays the second role
print("|-------------------|")
print("| Rolling your dice |")
print("|-------------------|")
print("The value of the second dice is " + str(nd) +"")  

#add the scores if any of the var = 1 or 6  
if st in [1,6]:
   result = result + 50
   
if nd in [1,6]:
   result = result + 50

#end txt for the game
if result == int(100):
    print("Congrdulations your score is " + str(result) + " you win!!!")
else:
    print("game repating is wip")
    print(" Your score is " + str(result) + " though")

