doorbroken = False
playerpos = 0
while doorbroken == False:
    player = input("There is a door here. \n")

    if player == "look north":
        print("The same thing as usual.")

    elif player == "check door":
        print("Just a door. Nothing special.")

    elif player == "look west":
        print("nothing.")

    elif player == "look east":
        print("nothing.")

    elif player == "look south":
        print("You aren't an owl, are you?")

    elif player == 'open door':
        print("You jiggle the handle. the door is locked.")
    
    elif player == 'break door':
        print("You broke down the door. There is nothing beyond the frame but a brick wall.")
        doorbroken = True

    elif player == 'move forward' and doorclosed == True:
        print('You bang your head against the door.')
    
    else:
        print("Invalid command.")

while playerpos == 0:
    player = input("There is no longer a door here. \n")

    if player == "check door":
        print("Nothing but splinters.")

    elif player == "look north":
        print("A brick wall standing in a doorframe.")

    elif player == "look west":
        print("Nothing.")

    elif player == "look east":
        print("Nothing.")

    elif player == "look south":
        print("You aren't an owl, are you?")
    
    elif player == 'open door':
        print("You can't open splinters.")
    
    elif player == 'open door' and doorclosed == False:
        print('The door is already open.')

    elif player == 'break door' and doorbroken == True:
        print("It's already broken.")

    elif player == 'move forward' and doorclosed == False:
        print('You pass through brick like water.')
        playerpos = 1
    
    else:
        print("Invalid command.")
