doorlocked = True
player = input("There is a door here. \n")
if player == 'open door' and doorlocked == True:
    print("You jiggle the handle. the door is locked.")
elif player == 'open door' and doorlocked == False:
    print("You open the door. There is nothing here but a brick wall.")
elif player == 'break door':
    print("""you broke down the door. There is nothing beyond the frame but a brick wall.""")
else:
    print("invalid command")
