print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
       _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 ''')

print("Welcome to Treasure Island.\n Your mission is to find the treasure\n")
print("Your mission is to find the treasure")
choice1=input('You have reached a road \n Where do you wanna go?\n Type "left" or "right".')
if choice1 == 'left' :
    choice2=input('You have reached a lake,\n Do you want to "swim" or "wait".\n')
    if choice2 == 'wait' :
        choice3=input('You have reached a hall, \n Choose a door to go in? \n "Red" or "Yellow" or "Blue ".\n')
        if choice3 == 'Yellow' :
            print("Yay!!! You have won the game Here is your treasure \n")
        elif input == 'Red' :
            print("Oh No You are Burned by Fire \n GAME OVER \n")
        elif input== 'Blue':
            print("Sorry You are Eaten by beasts, \nGAME OVER \n")
        else:
            print("GAME OVER \n")
    else:
        print("You are attacked by a Trout \n GAME OVER \n")
else:
    print("You fell into a hole \n GAME OVER \n")