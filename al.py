doorbroken = False
plypos = 0
plydead = False
plychoke = 3
ouch = 1
brokenhand = False
inventory = ['Nothing']
dinodead = False
plyhealth = 10
plyatck = 5
dinohealth = 30
dinoatck = 2
dinoaction = 0

while doorbroken == False and plydead == False:
    
    ply = input("There is a door here. \n").lower()

    if ply == "look north" or ply == "check north":
        print("The same thing as usual.")

    elif ply == "look west" or ply == "check north":
        print("Nothing. A blank void.")

    elif ply == 'look east' and 'Stool' not in inventory:
        print("There is a small golden key lying on a stool.")

    elif ply == 'look east' and "Stool" in inventory:
        print("There is a small golden key lying on the floor.")

    elif ply == 'take key':
        print("your hand passes through the key like it wasn't even there.")

    elif ply == 'check inventory':
        for x in inventory:
            print(x)

    elif ply == 'inventory':
        for x in inventory:
            print(x)

    elif ply == 'take stool' and 'Stool' not in inventory:
        print('You took the stool.')
        inventory.append('Stool')

    elif ply == 'look south':
        print("You aren't an owl, are you?")

    elif ply == 'open door':
        print("You jiggle the handle. The door is locked.")

    elif ply == 'check door':
        print("It's just a simple door. It looks fragile, though.")
    
    elif ply == 'break door':
        print("You broke down the door. There is nothing beyond the frame but a brick wall.")
        doorbroken = True

    elif ply == 'go north':
        print('You bang your head against the door.')

    elif ply == 'go east':
        print('Your feet don\'t seem to move no matter how much you will them to go.')

    elif ply == 'go west':
        print('Your feet don\'t seem to move no matter how much you will them to go.')

    elif ply == 'go south':
        print('You attempt to go backwards. You trip over your own feet. When you get back up, you haven\'t moved at all.')
    
    elif ply == 'quit':
        print('Game over. ')
        plydead = True
        
    else:
        print("Your thoughts seem incomprehensible.")

while plypos == 0 and plydead == False:
    ply = input("There is no longer a door here. \n").lower()

    if ply == "check door":
        print("Nothing but splinters.")

    elif ply == 'check wall':
        print('A red brick wall. The surface ripples when you touch it.')

    elif ply == 'check inventory':
        for x in inventory:
            print(x)

    elif ply == 'inventory':
        for x in inventory:
            print(x)

    elif ply == 'break wall' and ouch != 3 and brokenhand == False:
        print('You violently punch the wall. Your hand hurts.')
        ouch = ouch + 1

    elif ply == 'break wall' and ouch == 3 and brokenhand == False:
        print('You violently punch the wall. Your hand is now broken. You can\'t break anymore.')
        brokenhand = True

    elif ply == 'break wall' and brokenhand == True:
        print("You wish you could do that, moron.")

    elif ply == "look north":
        print("A brick wall standing in a doorframe. The surface ripples when you touch it.")

    elif ply == "look west":
        print("Nothing.")

    elif ply == "look east" and 'Stool' in inventory:
        print("There was a stool here.")

    elif ply == "look east" and 'Stool' not in inventory:
        print("There is a stool with nothing on it whatsoever.")

    elif ply == 'take stool' and 'Stool' not in inventory:
        print('You took the stool.')
        inventory.append('Stool')

    elif ply == "look south":
        print("You aren't an owl, are you?")
    
    elif ply == 'open door':
        print("You can't open splinters.")

    elif ply == 'break door':
        print("It's already broken.")

    elif ply == 'quit':
        print('Game over.')
        plydead = True

    elif ply == 'go north':
        print('You pass through brick like water. You choked to death. This is the end.\nGame Over\n\n\n\n  or is it?')
        plypos = 1

    elif ply == 'go east':
        print('You trip over your own feet. When you get back up, you haven\'t moved at all.')

    elif ply == 'go west':
        print('You trip over your own feet. When you get back up, you haven\'t moved at all.')

    elif ply == 'go south':
        print('You trip over your own feet. When you get back up, you haven\'t moved at all.')
    
    else:
        print("Your thoughts seem incomprehensible.")

while plypos == 1 and plydead == False:
    ply = input("There is no               here. \n").lower().split()

    if plychoke == 0:
        print("You choked to death. Again. I will not give you another chance. \n\nGame over.")
        plydead = True

    if 'break' in ply and brokenhand == False:
        print('you broke. you lost Nothing.\n\n\n\n\n\n\n\nYou wake up to find yourself in a massive glass case in what appears to be a museum.')
        plypos = 2
        plychoke = 3
        inventory.remove('Nothing')
    
    elif ply == 'check inventory':
        for x in inventory:
            print(x)

    elif ply == 'inventory':
        for x in inventory:
            print(x)

    elif 'break' in ply and brokenhand == True:
        print('you wish you could.')
        plychoke -= 1

    else:
        plychoke -= 1
        print('Wrong answer. You feel your lungs lose air.')


while plypos ==2 and plydead == False and "Stool" not in inventory:
    ply = input('What now? \n').lower()

    if ply == "look north":
        print("Through the glass case, you see a museum. The glass is too foggy to make out any details.")

    elif ply == 'check inventory':
        for x in inventory:
            print(x)

    elif ply == 'inventory':
        for x in inventory:
            print(x)

    elif ply == "check dinosaur":
        print("You go to check the dinosaur. It reacts. \nBATTLE START!")
        plypos = 3
        

    elif ply == 'look west':
        print("Big plastic dinosaur. It looks suprisingly life-like.")

    elif ply == 'look south':
        print("Fake grass. There is an air vent embedded in the ground")

    else:
        print("Your thoughts seem incomprehensible.")

while plypos == 3 and 

                
while plypos == 2 and plydead == False and "Stool" in inventory:
    ply = input('What now? \n').lower()

    if ply == "look north":
        print("Through the glass case, you see a museum. The glass is too foggy to make out any details.")

    elif ply == 'check inventory':
        for x in inventory:
            print(x)

    elif ply == 'inventory':
        for x in inventory:
            print(x)

    elif ply == 'look west' and 'Crowbar' not in inventory:
        print("Big plastic dinosaur. A crowbar dangles from its mouth.")

    elif ply == 'look east':
        print('A basic beige wall.')

    elif ply == "check dinosaur":
        print("A large chunk of plastic in the shape of a dinosaur.")

    elif ply == 'look west' and 'Crowbar' in inventory:
        print("Big plastic dinosaur. It looks fake.")

    elif ply == 'take crowbar':
        print("You placed the stool down in front of the dinosaur and took the crowbar from its mouth. Crowbar was added to inventory.")
        inventory.append('Crowbar')
        inventory.remove('Stool')

    elif ply == 'look south':
        print("Fake grass. There is an air vent embedded in the ground")

    else:
        print("Your thoughts seem incomprehensible.")
