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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome Suzanna to this game of Treasure Island.")
print("Your mission is to find the way to get ur ticket to argentina to see ur lover.")

option = input("Wich path will you follow left or right? ")
if option != "left":
    print("Fall into a hole. Game over")
else:
    print("u found a forest, and there is a river, what would you do? ")
    option = input("Swim or wait? ")
    if option != "swim":
        print("u get eaten by a wolf. Game over")
    else:
        print("you end up on an island, there u find a house with 3 doors each one from a different color")
        option = input("Which door?")
        if option == "blue":
            print("Eaten by beasts. Game over")
        elif option == "red":
            print("Burned by fire. Game over")
        elif option == "yellow":
            print("You Win!")
        else:
            print("game over")
