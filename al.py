doorlocked = True
doorclosed = True
doorbroken = False
playerpos = 0
while playerpos == 0:
    player = input("There is a door here. \n")

    if player == "look north":
        print("The same thing as usual.")

    elif player == 'open door' and doorlocked == True:
        print("You jiggle the handle. the door is locked.")
    
    elif player == 'open door' and doorlocked == False and doorclosed == True:
        print("You open the door. There is nothing here but a brick wall.")
        doorclosed = False
    
    elif player == 'open door' and doorclosed == False:
        print('The door is already open.')
    
    elif player == 'break door':
        print("You broke down the door. There is nothing beyond the frame but a brick wall.")
        doorbroken = True
        doorclosed = False
    
    elif player == 'break door' and doorbroken == True:
        print("It's already broken.")

    elif player == 'move forward' and doorclosed == True:
        print('You bang your head against the door.')

    elif player == 'move forward' and doorclosed == False:
        print('You pass through brick like water.')
        playerpos = 1
    
    else:
        print("Invalid command.")
    
