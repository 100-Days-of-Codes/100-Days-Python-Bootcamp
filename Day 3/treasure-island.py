print('''
         _..._
       .'     '.
      /'-.---.-'\
      |/`     `\|
     ( \  0 0  / )
      |/   V   \|
       \ '-:-' /
      .'`-----'`.
    /`           `\
   /  /         \  \
  /._/|         |\_.\
  |  )\._     _./(  |
  \_)_/_   Y   _\_(_/
    / ` ) / \ / ` \
    \   \/   \|   /
     '._/     \_.'
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right". ').lower()



if choice1 == "left":
    choice2 = input('You\'re come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed. There is a house 3 doors. One red, one yellow and one blue. Which colur do you choose? ').lower()
        if choice3 == "red":
            print('It\'s a room full of fire, Game Over.')
        elif choice3 == "yellow":
            print('You found the treasure! You Win!')
        elif choice3 == "blue":
            print('You enter a room of beasts, Game Over.')
        else:
            print("You chose a door that dosen't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")
