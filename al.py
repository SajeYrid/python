doorlocked = True
doorclosed = True
doorbroken = False
playerpos = 0
while playerpos != 1:
    player = input("There is a door here. \n")

    if player == "look north":
        print()

    if player == 'open door' and doorlocked == True:
        print("You jiggle the handle. the door is locked.")
    
    elif player == 'open door' and doorlocked == False and doorclosed == True:
        print("You open the door. There is nothing here but a brick wall.")
        doorclosed = False
    
    elif player == 'open door' and doorclosed == False:
        print('the door is already open.')
    
    elif player == 'break door':
        print("you broke down the door. There is nothing beyond the frame but a brick wall.")
        doorbroken = True
        doorclosed = False
    
    elif player == 'break door' and doorbroken == True:
        print("It's already broken.")
    
    elif player == 'unlock door':
        print("you unlocked the door.")
        doorlocked = False
    
    elif player == 'unlock door' and doorlocked == False:
        print("the door is already unlocked.")

    elif player == 'move forward' and doorclosed == True:
        print('You bang your head against the door.')

    elif player == 'move forward' and doorclosed == False:
        print('You pass through brick like water.')
        playerpos = 1
    
    else:
        print("invalid command")
    
