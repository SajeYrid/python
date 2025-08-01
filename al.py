doorbroken = False
playerpos = 0

while doorbroken == False:
    player = input("There is a door here. \n").lower()

    if player == 'look north':
        print("The same thing as usual.")

    elif player == 'look west':
        print("nothing.")

    elif player == 'look east':
        print("There is a small golden key lying on a stool.")

    elif player == 'take key':
        print('your hand passes through the key like it wasn\'t even there.')

    elif player == 'look south':
        print("You aren't an owl, are you?")

    elif player == 'open door':
        print("You jiggle the handle. the door is locked.")

    elif player == 'check door':
        print("It's just a simple door. it looks fragile, though.")
    
    elif player == 'break door':
        print("You broke down the door. There is nothing beyond the frame but a brick wall.")
        doorbroken = True

    elif player == 'go north':
        print('You bang your head against the door.')

    elif player == 'go east':
        print('Your feet don\'t seem to move no matter how much you will them to go.')

    elif player == 'go west':
        print('Your feet don\'t seem to move no matter how much you will them to go.')

    elif player == 'go south':
        print('You attempt to go backwards. You trip over your own feet. When you get back up, you haven\'t moved at all.')
    
    elif player == 'quit':
        print('Game over.')
        playerpos = 1
        doorbroken = True
        
    else:
        print("Your thoughts seem incomprehensible.")

while playerpos == 0:
    player = input("There is no longer a door here. \n").lower()

    if player == "check door":
        print("Nothing but splinters.")

    elif player == "look north":
        print("A brick wall standing in a doorframe. The surface ripples when you touch it.")

    elif player == "look west":
        print("Nothing.")

    elif player == "look east":
        print("There is a stool with nothing on it whatsoever.")

    elif player == "look south":
        print("You aren't an owl, are you?")
    
    elif player == 'open door':
        print("You can't open splinters.")

    elif player == 'break door':
        print("It's already broken.")

    elif player == 'quit':
        print('Game over.')
        playerpos = 1

    elif player == 'go north':
        print('You pass through brick like water. You choked to death. This is the end. \n Game Over')
        playerpos = 1

    elif player == 'go east':
        print('Your feet don\'t seem to move no matter how much you will them to go.')

    elif player == 'go west':
        print('Your feet don\'t seem to move no matter how much you will them to go.')

    elif player == 'go south':
        print('You attempt to go backwards. You trip over your own feet. When you get back up, you haven\'t moved at all.')
    
    else:
        print("Your thoughts seem incomprehensible.")
