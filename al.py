doorbroken = False
plypos = 0
plydead = False
plychoke = 5
ouch = 1
brokenhand = False
inventory = ['Nothing']

dinodead = False
dinoseen = False

plyhealth = 10
plyatck = 5
plydefense = False
plycharge = False
dinohealth = 30
dinoatck = 2
dinodefense = False
dinocharge = False
dinoaction = 0

ventopen = False
tookstool = False

print("There is a door here. You are facing north.")
while doorbroken == False and plydead == False:
    
    ply = input("").lower()

    if ply == "look north":
        print("The same thing as usual.")

    elif ply == "look west":
        print("Nothing. A blank void.")

    elif ply == 'look around':
        print("Perhaps you should try to specify what direction you want to look in.")

    elif ply == 'look east' and 'Stool' not in inventory:
        print("There is a small golden key lying on a stool.")

    elif ply == 'look east' and "Stool" in inventory:
        print("There is a small golden key lying on the floor.")

    elif ply == 'take key' or ply == "equip key" or ply == "get key" or ply == "pick up key":
        print("Your hand passes through the key like it wasn't even there.")

    elif ply == 'eat key':
        print("You heard a loud crunch sound. You didn't bite down yet.")

    elif ply == 'check key' or ply == 'inspect key':
        print("The key is the same color as the floor.")

    elif ply == 'check inventory' or ply == 'inventory':
        for x in inventory:
            print(x)

    elif ply == 'take stool' and 'Stool' not in inventory:
        print('You took the stool.')
        inventory.append('Stool')
        tookstool = True

    elif ply == 'look south':
        print("You aren't an owl, are you?")

    elif ply == 'open door':
        print("You jiggle the handle. The door is locked.")

    elif ply == 'check door':
        print("It's just a simple door. It looks fragile, though.")

    elif ply == 'eat door':
        print("You put your mouth on the door. The door is too big to be eaten in one sitting.")
    
    elif ply == 'break door':
        print("You broke down the door. There is nothing beyond the frame but a brick wall. \nThere is no longer a door here")
        doorbroken = True

    elif ply == 'fight door':
        print("""You prepare for battle against a true door.
Your actions are:
ATTACK
DEFEND
CHARGE""")
        doorfight = input("What will you do? \n").lower()
        if doorfight == 'attack' or doorfight == 'kill' or doorfight == 'punch' or doorfight == 'fight door':
            print("You attack the door with brute force. It instantly breaks down. \n There is only a brick wall beyond the frame.\nThere is no longer a door here")
            doorbroken = True
        elif doorfight == 'defend':
            print("You defended. The door doesn't do anything. You stop fighting it.")
        elif doorfight == 'charge':
            print("You charged. The door doesn't do anything. Perhaps it's best you save your energy for something else.")
        else:
            print("You can't think of how to perform that on a door. You disengage in combat.")

    elif ply == 'kill door':
        print("You brutally attack the door until it's nothing but rubble. \nYour hand hurts, but there is now a brick wall where the door was.\nThere is no longer a door here")
        doorbroken = True
        ouch += 1

    elif ply == 'go north':
        print('You bang your head against the door.')

    elif ply == 'go east':
        print('Your feet don\'t seem to move no matter how much you will them to go.')

    elif ply == 'go west':
        print('Your feet don\'t seem to move no matter how much you will them to go.')

    elif ply == 'go south':
        print('You attempt to go backwards. You trip over your own feet. When you get back up, you haven\'t moved at all.')

    elif ply == 'think' or ply == 'check' or ply == 'hint':
        print('You tried to think. You observe that there is a unbroken door in front of you.')
    
    elif ply == 'quit':
        print('Game over. ')
        plydead = True
        
    else:
        print("Your thoughts seem incomprehensible.")

while plypos == 0 and plydead == False:
    ply = input().lower()

    if ply == "check door":
        print("Nothing but splinters.")

    elif ply == 'check wall' or ply == 'check brick wall':
        print('A red brick wall. The surface ripples when you touch it.')

    elif ply == 'eat wall' or ply == 'eat brick wall':
        print('You sink your teeth into the wall. Suprisingly, your teeth glide through it. Tastes like water.')

    elif ply == 'check inventory' or ply == 'inventory':
        for x in inventory:
            print(x)

    elif ply == 'break wall' or ply == 'break brick wall' and ouch != 3 and brokenhand == False:
        print('You violently punch the wall. Your hand hurts.')
        ouch += 1

    elif ply == 'break wall' or ply == 'break brick wall' and ouch == 3 and brokenhand == False:
        print('You violently punch the wall. Your hand is now broken. You can\'t break anymore.')
        brokenhand = True

    elif ply == 'break wall' or ply == 'break brick wall' and brokenhand == True:
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
        tookstool = True

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
        print('You pass through brick like water. You choked to death. This is the end.\nGame Over\n\n\n\n  or is it?\nThere is no here.')
        plypos = 1

    elif ply == 'go east':
        print('You trip over your own feet. When you get back up, you haven\'t moved at all.')

    elif ply == 'go west':
        print('You trip over your own feet. When you get back up, you haven\'t moved at all.')

    elif ply == 'go south':
        print('You trip over your own feet. When you get back up, you haven\'t moved at all.')

    elif ply == 'think' or ply == 'check' or ply == 'hint':
        print('You tried to think. You observe that the Brick Wall looks unnatural.')
    
    else:
        print("Your thoughts seem incomprehensible.")

while plypos == 1 and plydead == False:

    ply = input().lower().split()

    if plychoke == 0:
        print("You somehow managed to choke to death for a second time. There aren't third chances in this world. \n\nGame over.")
        plydead = True

    elif 'break' in ply and brokenhand == False:
        print('You broke. You lost Nothing.\n\n\n\n\n\n\n\nYou wake up to find yourself in a massive glass case in what appears to be a museum.')
        plypos = 2
        plychoke = 5
        inventory.remove('Nothing')

    elif 'eat' in ply:
        print('As soon as you open your mouth, you feel the air rush out. Bad idea.')
        plychoke -= 2
        if plychoke >= 3:
            print(f'You have {plychoke} actions left.')
        
    elif 'inventory' in ply:
        for x in inventory:
            print(x)

    elif 'kill' in ply and 'myself' in ply:
        print('You broke. You lost Nothing.\n\n\n\n\n\n\n\nYou wake up to find yourself in a massive glass case in what appears to be a museum.')
        plypos = 2
        plychoke = 5
        inventory.remove('Nothing')

    elif 'break' in ply and brokenhand == True:
        print('You wish you could.')
        plychoke -= 1
        if plychoke >= 3:
            print(f'You have {plychoke} actions left.')

    elif 'think' in ply or 'check' in ply or 'hint' in ply:
        print('You tried to think. You thought about breaking.')

    elif 'open' in ply:
        print('You opened. You felt a change. \n\n\n\n\n\n\n\nYou wake up to find yourself in a massive glass case in what appears to be a museum.')
        plypos = 2
        plychoke = 5

    else:
        plychoke -= 1
        print('There isn\'t a way to do that. You feel your lungs lose air.')
        if plychoke >= 3:
            print(f'You have {plychoke} actions left.')


while plypos == 2 and tookstool == False and plydead == False:
    ply = input('What now? \n').lower()

    if ply == "look north":
        print("Through the glass case, you see a museum. The glass is too foggy to make out any details.")

    elif ply == 'break glass' and brokenhand == False or ply == 'break window' and brokenhand == False:
        print('You bash your fist against the glass. It rebounds into your own face. Now your hand AND face hurt. Good job.')

    elif ply == 'break glass' and brokenhand == True or ply == 'break window' and brokenhand == True:
        print('If you were to try, your hand would hurt even more than it already does.')

    elif ply == 'check inventory' or ply == 'inventory':
        for x in inventory:
            print(x)

    elif ply == "check dinosaur" and dinoseen == False:
        print("What dinosaur?")

    elif ply == 'fight dinosaur' and dinoseen == False:
        print("Your prehistoric rage goes unquenched, as you haven't seen any dinosaurs.")

    elif ply == 'fight dinosaur' and dinoseen == True:
        print("You initiate a battle with the dinosaur. \nBATTLE START!")
        print("""
Your actions are:
ATTACK
DEFEND
CHARGE""")
        plypos = 3

    elif ply == "check dinosaur" and dinoseen == True:
        print("You go to check the dinosaur. It reacts. \nBATTLE START!")
        print("""
Your actions are:
ATTACK
DEFEND
CHARGE""")
        plypos = 3
        
    elif ply == 'look west':
        print("Big plastic dinosaur. It looks suprisingly life-like.")
        dinoseen = True

    elif ply == 'look south':
        print("Fake grass.")

    elif ply == 'look east':
        print('A basic beige wall.')

    elif ply == 'go north':
        print("You smack your face into the glass.")

    elif ply == 'go south':
        print('This room is too small to meaningfully move in any direction.')

    elif ply == 'go east':
        print('This room is too small to meaningfully move in any direction.')

    elif ply == 'go west' and dinoseen == False:
        print('Without looking first, you casually walk staight into the jaws of a prehistoric predator. \nGame over.')
        plydead == True

    elif ply == 'go west' and dinoseen == True:
        print('Wanting to investigate the dinosaur, you walk west. The dinosaur reacts. \nBATTLE START!')
        print("""
Your actions are:
ATTACK
DEFEND
CHARGE""")
        plypos = 3

    elif ply == 'think' and dinoseen == False or ply == 'check' and dinoseen == False or ply == 'hint' and dinoseen == False:
        print('You tried to think. You observe a strange feeling of being watched.')

    elif ply == 'think' and dinoseen == True or ply == 'check' and dinoseen == True or ply == 'hint' and dinoseen == True:
        print('You tried to think. You observe a suspicous looking dinosaur')

    else:
        print("Your thoughts seem incomprehensible.")

while plypos == 3 and plydead == False:

    ply = input(f"Your health is: {plyhealth}. PLASTIC DINO's health is {dinohealth}. What do you do?\n").lower()

    def dinomove():
        
        global plyhealth
        global dinoatck
        global dinocharge
        global dinodefense
        
        import random
        dinoaction = random.randint(0, 10)
            
        if dinoaction > 5:
            print(f"PLASTIC DINO bit you for {dinoatck}!")
            plyhealth = plyhealth - dinoatck
            dinoatck = 2
            dinocharge = False
            dinodefense = False
                
        elif dinoaction < 5:
            print("PLASTIC DINO defended! It won't take damage next turn!")
            dinodefense = True
    
        elif dinoaction == 5 and dinocharge == False:
            print("PLASTIC DINO charged! Its next attack will do double damage!")
            dinocharge = True
            dinoatck = 4
            dinodefense = False
    
        elif dinoaction == 5 and dinocharge == True:
            print("PLASTIC DINO tried to charge! But it already did.")
    
        else:
            print("This will only print if something went horribly wrong.")

    if ply == ('attack') and dinodefense == False:
        print(f'You attacked PLASTIC DINO for {plyatck} damage!')
        dinohealth = dinohealth - plyatck
        plyatck = 5
        plycharge = False
        dinomove()

    elif ply == ('attack') and dinodefense == True:
        print('You attacked PLASTIC DINO! But it defended.')
        plyatck = 5
        plycharge = False
        dinodefense = False
        dinomove()

    elif ply == ('defend'):
        print('You defended! You won\'t take damage this turn.')
        plyatck = 5
        dinodefense = False
        dinomove()

    elif ply == ('charge') and plycharge == False:
        print('You charged! You will do double damage on your next attack!')
        plyatck = 10
        plycharge = True
        dinodefense = False
        dinomove()

    elif ply == ('charge') and plycharge == True:
        print('You tried to charge again! But nothing happened...')
        plyatck = 10
        plycharge = True
        dinodefense = False
        dinomove()

    elif ply == 'think' or ply == 'check' or ply == 'hint':
        print(f"""ATTACK: Deals {plyatck} Damage to the Dinosaur if it isn't defending.
        DEFEND: Allows you to take 0 Damage this turn.
        CHARGE: Powers up attack to deal double damage next attack.""")

    else:
        print("That isn't an action you can do.")
    
    if plyhealth <= 0:
        print("You died! Loser!")
        plydead = True
    
    if dinohealth <= 0:
        dinodead = True
        print("You won!")
        plypos = 2

            
while plypos == 2 and tookstool == True and plydead == False:

    ply = input('What now? \n').lower()

    if ply == "look north":
        print("Through the glass case, you see a museum. The glass is too foggy to make out any details.")

    elif ply == 'check inventory' or ply == 'inventory':
        for x in inventory:
            print(x)

    elif ply == 'look west' and 'Crowbar' not in inventory:
        print("Big plastic dinosaur. A crowbar dangles from its mouth.")
        dinoseen = True

    elif ply == 'look east':
        print('A basic beige wall.')
    
    elif ply == 'break glass':
        print('You bash your fist against the glass. It rebounds into your own face. Now your hand AND face hurt. Good job.')

    elif ply == "check dinosaur" and dinoseen == True:
        print("A large chunk of plastic in the shape of a dinosaur.")

    elif ply == "check dinosaur" and dinoseen == False:
        print("What dinosaur?")

    elif ply == 'look west' and 'Crowbar' in inventory:
        print("Big plastic dinosaur. It looks fake.")

    elif ply == 'take crowbar':
        print("You placed the stool down in front of the dinosaur and took the crowbar from its mouth. Crowbar was added to inventory. When you step off the stool, it dissovles into dust.")
        inventory.append('Crowbar')
        inventory.remove('Stool')

    elif ply == 'look south':
        print("Fake grass. There is an air vent embedded in the ground")

    elif ply == 'go north':
        print("You smack your face into the glass.")

    elif ply == 'go south':
        print('This room is too small to meaningfully move in any direction.')

    elif ply == 'go east':
        print('This room is too small to meaningfully move in any direction.')

    elif ply == 'go west':
        print('It appears there is a giant plastic dinosaur in the way.')
        dinoseen = True

    elif ply == 'think' or ply == 'check' or ply == 'hint':
        print('You tried to think. You thought about using the stool to get the crowbar.')

    elif ply == 'open vent' and 'Crowbar' in inventory and ventopen == False:
        print("You pry open the vent with the crowbar. It's too small to climb inside, but there is a red brick inside.")
        ventopen = True

    elif ply == 'open vent' and 'Crowbar' in inventory and ventopen == True:
        print("You close the vent just so you can open it. Again.")

    elif ply == 'open vent' and 'Crowbar' not in inventory:
        print('You try to pull open the vent with your bare hands. It dosen\'t work.')

    else:
        print("Your thoughts seem incomprehensible.")
