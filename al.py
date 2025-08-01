doorbroken = False
playerpos = 0
playerdead = False
playerchoke = 2
ouch = 1
brokenhand = False

while doorbroken == False and playerdead == False:
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
        playerdead = True
        
    else:
        print("Your thoughts seem incomprehensible.")

while playerpos == 0 and playerdead == False:
    player = input("There is no longer a door here. \n").lower()

    if player == "check door":
        print("Nothing but splinters.")

    elif player == 'check wall':
        print('A red brick wall. The surface ripples when you touch it.')

    elif player == 'break wall' and ouch != 3 and brokenhand == False:
        print('You violently punch the wall. Your hand hurts.')
        ouch = ouch + 1

    elif player == 'break wall' and ouch == 3 and brokenhand == False:
        print('You violently punch the wall. Your hand is now broken. You can\'t break anymore.')
        brokenhand = True

    elif player == 'break wall' and brokenhand == True:
        print("You wish you could do that, moron.")

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
        playerdead = True

    elif player == 'go north':
        print('You pass through brick like water. You choked to death. This is the end.\nGame Over\n\n\n\n  or is it?')
        playerpos = 1

    elif player == 'go east':
        print('Your feet don\'t seem to move no matter how much you will them to go.')

    elif player == 'go west':
        print('Your feet don\'t seem to move no matter how much you will them to go.')

    elif player == 'go south':
        print('You attempt to go backwards. You trip over your own feet. When you get back up, you haven\'t moved at all.')
    
    else:
        print("Your thoughts seem incomprehensible.")

while playerpos == 1 and playerdead == False:
    player = input("There is no               here. \n").lower().split()

    if playerchoke == 0:
        print("You choked to death. Again. I will not give you another chance. \n\nGame over.")
        playerdead = True

    if player[0] == 'break' and brokenhand == False:
        print('you broke \n\n\n\n\n\n\n\nYou wake up to find yourself in a massive glass case in what appears to be a museum.')
        playerpos = 2

    elif player[0] == 'break' and brokenhand == True:
        print('you wish you could.')
        playerchoke = playerchoke - 1

    else:
        print('Wrong answer. You feel your lungs lose air.')
        playerchoke = playerchoke - 1
            
                
while playerpos == 2 and playerdead == False:
    player = input('What now?')
