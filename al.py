# the holy and pure and innocent variable block
# booleans
doorbroken = False
plydead = False
brokenhand = False
dinodead = False
dinoseen = False
plydefending = False
plycharge = False
dinodefense = False
dinocharge = False
ventopen = False
tookstool = False
tookSplinter = False
pretendLMAO = False
plywallBroken = False
stoolExplode = False

# strings
ply = ""
plysecondary = ""
miscfight = ""
equippeditem = "None"
weapon = "Nothing"
armor = "Nothing"

# lists
inventory = ['Nothing']

# integers
plypos = 0
plychoke = 5
ouch = 1
plyhealthDEFAULT = 10
plyhealth = 10
plyatckDEFAULT = 5
plyatck = 5
plydefenseDEFAULT = 0
plydefense = 0
dinohealth = 30
dinoatck = 2
dinoaction = 0
glassTicker = 2
ventpos = 0
ventDirection = 0

# dictionaries
#   'item name' : 'item description'
items = {
    'Nothing' : 'Empty air. Why is this here? Perhaps you can do something with it before it\'s gone forever.',
    'Stool' : 'An old wooden stool. It doesn\'t look like it\'ll last very long.',
    'Splinters' : 'A collection of broken little bits of wood.',
    'Pretend Splinters' : 'A fake collection of little broken bits of wood.',
    'Crowbar' : 'A sturdy piece of curved aluminium made for prying things open.',
    'Tooth' : 'A fake tooth from a plastic prehistoric predator.'
}

roomhints = {
    1 : 'You tried to think. You observe that there is a unbroken door in front of you.',
    2 : 'You tried to think. You observe that the brick wall in the doorframe looks unnatural.',
    3 : 'You tried to think. You observe a strange feeling of being watched.',
    4 : 'You tried to think. You observe a suspicious looking dinosaur.',
    5 : 'You tried to think. You observe a sense of satisfaction from killing a dinosaur.',
    6 : 'You tried to think. You observe a dangling crowbar from the Plastic Dinosaur that is too high to reach.',
    7 : 'You tried to think. You thought about the destruction of buildings.'
}

selfcheckroom = {
    1 : 'Trying to investigate this strange door they found',
    2 : 'Certified Destroyer of Doors',
    3 : '...',
    4 : 'Feels broken',
    5 : 'Plastic Dinosaur exterminator',
    6 : 'Ready to climb their newly obtained stool',
    7 : 'Already broke their newly obtained stool'
}

# the truly neutral functions
def glasscheck():
    global glassTicker
    global plypos
    if glassTicker == 2:
        print('For some reason, there is an absurd amount of condensation on the glass. You try to wipe it off, but the water refuses to part from the window. The image in the glass looks a bit clearer.')
        glassTicker -= 1
    elif glassTicker == 1:
        print('You inspect the glass even further. When you look closer, you see that the condensation isn\'t condensation. There is a sort of film covering the entirety of the surface of the glass.')
        glassTicker -=1
    elif glassTicker == 0:
        print("""You look even closer. Then, you realize, the glass isn\'t foggy, the museum is.
You blink. when your eyes flutter open, the glass is clear again. In fact, everything is clear.
Strangely, you feel healthier than usual.
You aren\'t where you were before.""")
        glassTicker = 2
        plypos = 11
        plyhealthDEFAULT += 2
        plyhealth = plyhealthDEFAULT

def dinomove():
    import random
    global plyhealth, dinoatck, dinocharge, dinodefense, plydefending
    dinoaction = random.randint(1, 9)
    if dinoaction > 6 and plydefending == True:
        print(f"PLASTIC DINO bit you! But you defended!")
        dinoatck = 2
        dinocharge = False
        dinodefense = False
        plydefending = False
    elif dinoaction > 6 and plydefending == False:
        print(f"PLASTIC DINO bit you for {dinoatck}!")
        plyhealth = plyhealth - dinoatck
        dinoatck = 2
        dinocharge = False
        dinodefense = False
    elif dinoaction < 4:
        print("PLASTIC DINO defended! It won't take damage next turn!")
        dinodefense = True
        plydefending = False
    elif dinoaction > 3 and dinoaction < 7 and dinocharge == False:
        print("PLASTIC DINO charged! Its next attack will do double damage!")
        dinocharge = True
        dinoatck = 4
        dinodefense = False
        plydefending = False
    elif dinoaction > 3 and dinoaction < 7 and dinocharge == True:
        print("PLASTIC DINO tried to charge! But it already did.")
        plydefending = False
    else:
        print("This will only print if something went horribly wrong.")

def globalcommands():
    # skip the void for this one, it parses commands differently
    global ply, inventory, plyhealth, plydefense, doorbroken, plydead, plypos, tookstool, dinodead, dinoseen, equippeditem
    if ply == 'look around' or ply == 'look':
        print("Perhaps you should try to specify what direction you want to look in.")
        return True
    elif ply == "kill me" or ply == "kill myself":
        print("You punched yourself multiple times. You're too weak to deal any damage.")
        return True
    elif ply == 'check inventory' or ply == 'inventory' or ply == 'open inventory':
        for x in inventory:
            print(x)
        return True
    elif ply == 'quit':
        quit()
    elif ply == 'think' or ply == 'check' or ply == 'hint':
        if plypos == 1 and doorbroken == False and plydead == False:
            print(roomhints[1])
        elif plypos == 1 and doorbroken == True and plydead == False:
            print(roomhints[2])
        elif plypos == 3 and tookstool == False and plydead == False and dinodead == False and dinoseen == False:
            print(roomhints[3])
        elif plypos == 3 and tookstool == False and plydead == False and dinodead == False and dinoseen == True:
            print(roomhints[4])
        elif plypos == 3 and tookstool == False and plydead == False and dinodead == True:
            print(roomhints[5])
        elif plypos == 3 and tookstool == True and plydead == False and 'Stool' in inventory:
            print(roomhints[6])
        elif plypos == 3 and tookstool == True and plydead == False and 'Stool' not in inventory:
            print(roomhints[7])
        return True
    elif ply == "check me" or ply == "check myself" or ply == "check self":
        global plyatck
        global weapon
        global plydefense
        global armor
        print("YOU \nCURRENT HP: " + str(plyhealth) + "\nATTACK: " + str(plyatck) + " (" + weapon + ")\nDEFENSE: " + str(plydefense) + " (" + armor + ")")
        if plypos == 1 and doorbroken == False and plydead == False:
            print(selfcheckroom[1])
        elif plypos == 1 and doorbroken == True and plydead == False:
            print(selfcheckroom[2])
        elif plypos == 3 and tookstool == False and plydead == False and dinodead == False and dinoseen == False:
            print(selfcheckroom[3])
        elif plypos == 3 and tookstool == False and plydead == False and dinodead == False and dinoseen == True:
            print(selfcheckroom[4])
        elif plypos == 3 and tookstool == False and plydead == False and dinodead == True:
            print(selfcheckroom[5])
        elif plypos == 3 and tookstool == True and plydead == False and 'Stool' in inventory:
            print(selfcheckroom[6])
        elif plypos == 3 and tookstool == True and plydead == False and 'Stool' not in inventory:
            print(selfcheckroom[7])
        return True
    elif ply.startswith("equip "):
        item_to_equip = ply[6:].strip().title()
        if item_to_equip in inventory:
            equippeditem = item_to_equip
            if equippeditem == 'Nothing':
                print(f"You equipped {equippeditem}.")
                print("Your Attack and Defense went back to default")
                weapon = "Nothing"
                plyatck = plyatckDEFAULT
                armor = "Nothing"
                plydefense = plydefenseDEFAULT
            else:
                if equippeditem == weapon or equippeditem == armor:
                    print(f"You already have the {equippeditem} equipped.")
                else:
                    print(f"You equipped the {equippeditem}.")
                    if equippeditem == 'Stool':
                        print("You gained +1 Defense")
                        armor = 'Stool'
                        plydefense = plydefenseDEFAULT + 1
                    elif equippeditem == 'Splinters':
                        if stoolExplode == True:
                            print("In remembrance of the stool, you equipped the Splinters as armor.\nYou gained +1 Defense")
                            armor = 'Splinters'
                            plydefense = plydefenseDEFAULT + 1
                        else:
                            print("You gained +1 Attack")
                            weapon = 'Splinters'
                            plyatck = plyatckDEFAULT + 1
                    elif equippeditem == 'Pretend Splinters':
                        print("You act like you are holding splinters.\nYou gained -1 Attack")
                        weapon = "Pretend Splinters"
                        plyatck = plyatckDEFAULT - 1
                    elif equippeditem == 'Crowbar':
                        print("You gained +2 Attack")
                        weapon = "Crowbar"
                        plyatck = plyatckDEFAULT + 2
                    elif equippeditem == 'Brick':
                        print("You gained +1 Attack")
                        weapon = "Brick"
                        plyatck = plyatckDEFAULT + 1
                    elif equippeditem == 'Tooth':
                        print("You wear it as a badge of honor.\nYou gained +1 Defense")
                        armor = 'Tooth'
                        plydefense = plydefenseDEFAULT + 1
        else:
            print(f"You don't have a {item_to_equip} in your inventory.")
        return True
    else:
        return False

# the unholy and devilish and evil while loops
# Title screen

print("""
           88 88                         
           88 \"\"                         
           88                            
,adPPYYba, 88 88  ,adPPYba, 8b,dPPYba,   
\"\"     `Y8 88 88 a8P_____88 88P'   `"8a  
,adPPPPP88 88 88 8PP\"\"\"\"\"\"\" 88       88  
88,    ,88 88 88 "8b,   ,aa 88       88  
`\"8bbdP\"Y8 88 88  `\"Ybbd8\"\' 88       88  \n\n\n\n\n\n\n\nStart Game? Y/N""")

while plypos == 0:
    ply = input().lower()
    if ply == 'y':
        plypos = 1
        print("Instructions:\nComplete the game using any method necessary. Use cardinal directions. type 'Think' or 'Hint' for a hint. \nGood luck. \n")
        print("There is a door here. You are facing north.")
    elif ply == 'n':
        quit()
    else:
        print('That isn\'t an option. type \'Y\' for Yes and \'N\' for No')

# area 1 (unbroken door)

while plypos == 1 and doorbroken == False and plydead == False:
    
    ply = input("").lower()

    if globalcommands():
        pass

    elif ply == "look north" or ply == 'look forward':
        print("The same thing as usual.")

    elif ply == "look west" or ply == 'look left':
        print("Nothing. A blank void.")

    elif (ply == 'look east' or ply == 'look right') and 'Stool' not in inventory:
        print("There is a small golden key lying on a stool.")

    elif ply == 'look east' and "Stool" in inventory:
        print("There is a small golden key lying on the floor.")

    elif ply == 'eat key':
        print("You heard a loud crunch sound. You didn't bite down yet.")

    elif ply == 'check key' or ply == 'inspect key':
        print("The key is the same color as the floor.")

    elif ply.endswith(" key") or ply.endswith(" key on stool"):
        print("Your hand passes through the key like it wasn't even there.")

    elif ply == 'take stool' and 'Stool' not in inventory:
        print('You took the stool.\nSTOOL added into your INVENTORY.')
        inventory.append('Stool')
        tookstool = True

    elif ply == 'take stool' and 'Stool' in inventory:
        print('Amazingly, you already took the stool.')

    elif ply == 'look south' or ply == 'look back':
        print("You aren't an owl, are you?")

    elif ply == 'open door':
        print("You jiggle the handle. The door is locked.")

    elif ply == 'check door':
        print("It's just a simple door. It looks fragile, though.")

    elif ply == 'eat door':
        print("You put your mouth on the door. The door is too big to be eaten in one sitting.")

    elif ply == 'close door':
        print("You close the closed door.")

    elif ply == 'unlock door':
        print("You try to unlock the door. Your finger does not fit through the lock.")
    
    elif ply == 'take door':
        print("You attempt to take the door. It's lodged into the door frame")
    
    elif ply == 'break door':
        print("You broke down the door. There is nothing beyond the frame but a brick wall. \nThere is no longer a door here")
        doorbroken = True

    elif ply == 'fight door':
        print(f"""You prepare for battle against a true door. Your health is: {plyhealth}. DOOR's health is ???
Your actions are:
ATTACK
DEFEND
CHARGE""")
        miscfight = input("What will you do? \n").lower()
        if miscfight == 'attack' or miscfight == 'kill' or miscfight == 'punch' or miscfight == 'fight door':
            print("You attack the door with brute force. It instantly breaks down. \nThere is only a brick wall beyond the frame.\nThere is no longer a door here")
            doorbroken = True
        elif miscfight == 'defend':
            print("You defended. The door doesn't do anything. You stop fighting it.")
        elif miscfight == 'charge':
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
        
    else:
        print("Your thoughts seem incomprehensible.")
        
# area 1 (broken door)

while plypos == 1 and doorbroken == True and plydead == False:
    ply = input().lower()

    if globalcommands():
        pass

    elif ply == "check door":
        print("Nothing but splinters.")

    elif ply == 'take door' and tookSplinter == False:
        print("You cannot take the door as it is broken. You take splinters in remembrance of the broken door.\nSPLINTERS added into your INVENTORY")
        inventory.append('Splinters')
        tookSplinter = True

    elif ply == 'take door' and tookSplinter == True and pretendLMAO == False:
        print("You already took the splinters. You pretended to take more splinters.\nPRETEND SPLINTERS added into your INVENTORY")
        inventory.append('Pretend Splinters')
        pretendLMAO = True

    elif ply == 'take door' and tookSplinter == True and pretendLMAO == True:
        print("You already took the pretend splinters. You cannot fathom about what comes after pretend splinters.")

    elif ply == 'check wall' or ply == 'check brick wall':
        print('A red brick wall. The surface ripples when you touch it.')

    elif (ply == 'take wall' or ply == 'take brick wall') and ouch != 3 and brokenhand == False:
        print('You attempt to take the wall. Your hand passes right through the wall.\nOnce you took out your hand, it felt injured.')
        ouch += 1

    elif (ply == 'take wall' or ply == 'take brick wall') and ouch == 3 and brokenhand == False:
        print('You attempt to take the wall. Your hand passes right through the wall.\nOnce you took out your hand, if felt broken.\nYou can\'t use your hand anymore.')
        brokenhand = True
        plyatckDEFAULT -= 1

    elif (ply == 'take wall' or ply == 'take brick wall') and brokenhand == True:
        print("You attempt to take the wall. You have a bad reaction. You stop your attempt to take the wall.")

    elif ply == 'eat wall' or ply == 'eat brick wall':
        print('You sink your teeth into the wall. Suprisingly, your teeth glide through it. Tastes like water.')

    elif (ply == 'break wall' or ply == 'break brick wall') and ouch != 3 and brokenhand == False:
        print('You violently punch the wall. Your hand passes right through the wall.\nOnce you took out your hand, it felt injured.')
        ouch += 1

    elif (ply == 'break wall' or ply == 'break brick wall') and ouch == 3 and brokenhand == False:
        print('You violently punch the wall. Your hand passes right through the wall.\nOnce you took out your hand, if felt broken.\nYou can\'t use your hand anymore.')
        brokenhand = True
        plyatckDEFAULT -= 1

    elif (ply == 'break wall' or ply == 'break brick wall') and brokenhand == True:
        print("You unfortunately don't have the strength to do that.")

    elif ply == "look north":
        print("A brick wall standing in a doorframe. The surface ripples when you touch it.")

    elif ply == "look west":
        print("Nothing.")

    elif ply == "look east" and 'Stool' in inventory:
        print("There was a stool here.")

    elif ply == "look east" and 'Stool' not in inventory:
        print("There is a stool with nothing on it whatsoever.")

    elif ply == 'take stool' and 'Stool' not in inventory:
        print('You took the stool.\nSTOOL added into your INVENTORY.')
        inventory.append('Stool')
        tookstool = True

    elif ply == 'take stool' and 'Stool' in inventory:
        print('Amazingly, you already took the stool.')

    elif ply == "look south":
        print("You aren't an owl, are you?")
    
    elif ply == 'open door':
        print("You can't open splinters.")

    elif ply == 'break door':
        print("It's already broken.")

    elif ply == 'go north':
        print('You pass through brick like water. You choked to death. This is the end.\nGame Over\n\n\n\n  or is it?\nThere is no here.')
        plypos = 2

    elif ply == 'go east':
        print('You trip over your own feet. When you get back up, you haven\'t moved at all.')

    elif ply == 'go west':
        print('You trip over your own feet. When you get back up, you haven\'t moved at all.')

    elif ply == 'go south':
        print('You trip over your own feet. When you get back up, you haven\'t moved at all.')

    elif ply == "close door":
        print("You try to figure out how to inact this outrageous thought. You come up with nothing.")

    elif ply == 'fight wall':
        print(f"""You prepare for battle against a brick wall. Your health is: {plyhealth}. WALL's health is 0
Your actions are:
ATTACK
DEFEND
CHARGE""")
        miscfight = input("What will you do? \n").lower()
        if (miscfight == 'attack' or miscfight == 'kill' or miscfight == 'punch' or miscfight == 'fight wall' or miscfight == 'fight brick wall') and brokenhand == False:
            print("You attempt to attack the wall. Your hand passes right through the wall.")
            if ouch != 3:
                print("Once you pulled out your hand, it felt injured.")
                ouch += 1
            elif ouch == 3:
                print("Once you pulled out your hand, if felt broken.\nYou cannot use your hand anymore.")
                brokenhand = True
                plyatckDEFAULT -= 1
        elif (miscfight == 'attack' or miscfight == 'kill' or miscfight == 'punch' or miscfight == 'fight wall' or miscfight == 'fight brick wall') and brokenhand == True:
            print("You try to attack the wall. Your hand doesn't move. You cannot fight it in this state.")
        elif miscfight == 'defend':
            print("You defended. The wall slightly ripples. You stop fighting it.")
        elif miscfight == 'charge':
            print("You charged. The wall violently ripples. You look confused and stop fighting.")
        elif ply == 'quit':
            quit()
        else:
            print("You can't think of how to perform that on a wall. You disengage in combat.")
    
    else:
        print("Your thoughts seem incomprehensible.")

# area 2 (void)

while plypos == 2 and plydead == False:

    ply = input().lower().split()

    if plychoke <= 0:
        print("You somehow managed to choke to death for a second time. There aren't third chances in this world.\n\nGame over.")
        plydead = True

    elif ('break' in ply and brokenhand == False) or ('kill' in ply and 'myself' in ply):
        print('You broke. You lost Nothing.\n\n\n\n\n\n\n\nYou wake up to find yourself in a massive glass case in what appears to be a museum.\nWhat now?')
        plypos = 3
        plychoke = 5
        inventory.remove('Nothing')

    elif 'check' in ply:
        print('You checked... something. It gave the impression of broken glass.')

    elif 'eat' in ply or 'breath' in ply:
        print('As soon as you open your mouth, you feel the air rush out. Bad idea.')
        plychoke -= 2
        if plychoke <= 3 and plychoke != 0:
            print(f'You have {plychoke} actions left.')
        
    elif 'inventory' in ply:
        for x in inventory:
            print(x)

    elif 'break' in ply and brokenhand == True:
        print('You wish you could.')
        plychoke -= 1
        if plychoke <= 3 and plychoke != 0:
            print(f'You have {plychoke} actions left.')

    elif ('think' in ply or 'check' in ply or 'hint' in ply) and brokenhand == False:
        print('You tried to think. You thought about breaking.')

    elif ('think' in ply or 'check' in ply or 'hint' in ply) and brokenhand == True:
        print('You tried to think. You thought about doors.')

    elif ply == 'quit':
        quit()

    elif 'open' in ply:
        print('You opened. You felt a change.\n\n\n\n\n\n\n\nYou wake up to find yourself in a massive glass case in what appears to be a museum.\nWhat now?')
        plypos = 3
        plychoke = 5

    else:
        plychoke -= 1
        print('There isn\'t a way to do that. You feel your lungs lose air.')
        if plychoke <= 3 and plychoke != 0:
            print(f'You have {plychoke} actions left.')

# area 3 (museum without stool)

while plypos == 3 and tookstool == False and plydead == False and dinodead == False:
    ply = input().lower()

    if globalcommands():
        pass

    elif ply == "look north":
        print("Through the glass case, you see a museum. The glass is too foggy to make out any details.")

    elif (ply == 'break glass' or ply == 'break window' or ply == 'break case') and brokenhand == False:
        print('You bash your fist against the glass. It rebounds into your own face. You take 1 Damage.')
        ouch += 1
        plyhealth -= 1
        if ouch == 3:
            print('Your hand has given up on you.\nYou can\'t use your hand anymore.')
        else:
            print('Your hand hurts more than usual.')

    elif (ply == 'break glass' or ply == 'break window' or ply == 'break case') and brokenhand == True:
        print('If you were to try, your hand would hurt even more than it already does.')

    elif ply == 'eat glass':
        print("You press your mouth against the glass and attempt to take a bite. Unfortunately, the surface is too smooth and your teeth harmlessly slide against it. Drats.")

    elif ply == 'check glass':
        glasscheck()

    elif ply == "check dinosaur" and dinoseen == False:
        print("What dinosaur?")

    elif ply == 'fight dinosaur' and dinoseen == False:
        print("Your prehistoric rage goes unquenched, as you haven't seen any dinosaurs so far.")

    elif ply == 'fight dinosaur' and dinoseen == True:
        print("You initiate a battle with the dinosaur. \nBATTLE START!")
        print("""
Your actions are:
ATTACK
DEFEND
CHARGE""")
        plypos = 4

    elif ply == "check dinosaur" and dinoseen == True:
        print("You go to check the dinosaur. It reacts. \nBATTLE START!")
        print("""
Your actions are:
ATTACK
DEFEND
CHARGE""")
        plypos = 4
        
    elif ply == 'look west':
        print("Big plastic dinosaur. It looks surprisingly life-like.")
        dinoseen = True

    elif ply == 'look south':
        print("Fake grass. There is a metal vent embedded in the ground.")

    elif ply == 'look east':
        print('A basic beige wall.')

    elif ply == 'go north':
        print("You smack your face into the glass.")

    elif ply == 'go south':
        print('This room is too small to meaningfully move in any direction.')

    elif ply == 'go east':
        print('This room is too small to meaningfully move in any direction.')

    elif ply == 'go west' and dinoseen == False:
        print('Without looking first, you casually walk straight into the jaws of a prehistoric predator. \nGame over.')
        plydead = True

    elif ply == 'go west' and dinoseen == True:
        print('Wanting to investigate the dinosaur, you walk west. The dinosaur reacts. \nBATTLE START!')
        print("""
Your actions are:
ATTACK
DEFEND
CHARGE""")
        plypos = 4

    else:
        print("Your thoughts seem incomprehensible.")

# area 4 (battle against a true dino)

while plypos == 4 and plydead == False:

    ply = input(f"Your health is: {plyhealth}. PLASTIC DINO's health is {dinohealth}. What do you do?\n").lower()

    if ply == 'attack' and dinodefense == False:
        print(f'You attacked PLASTIC DINO for {plyatck} damage!')
        dinohealth = dinohealth - plyatck
        if plycharge == True:
            import math
            plyatck = math.floor(plyatck / 2)
            plycharge = False
        dinomove()

    elif ply == 'attack' and dinodefense == True:
        print('You attacked PLASTIC DINO! But it defended.')
        if plycharge == True:
            plyatck = math.floor(plyatck / 2)
            plycharge = False
        dinodefense = False
        dinomove()

    elif ply == 'defend':
        print('You defended! You won\'t take damage this turn.')
        dinodefense = False
        plydefending = True
        dinomove()

    elif ply == 'charge' and plycharge == False:
        print('You charged! You will do double damage on your next attack!')
        plyatck *= 2
        plycharge = True
        dinodefense = False
        dinomove()

    elif ply == 'charge' and plycharge == True:
        print('You tried to charge again! But nothing happened...')
        dinodefense = False
        dinomove()

    elif ply == 'think' or ply == 'check' or ply == 'hint':
        print(f"""ATTACK: Deals {plyatck} Damage to the Dinosaur if it isn't defending.
        DEFEND: Allows you to take 0 Damage this turn.
        CHARGE: Powers up attack to deal double damage next attack.""")

    elif ply == 'quit':
        quit()

    else:
        print("That isn't an action you can do.")
    
    if plyhealth <= 0 and dinohealth > 0:
        print("You died! Loser!")
        plydead = True
    
    elif dinohealth <= 0 and plyhealth > 0:
        dinodead = True
        print("You won! \nThe dinosaur disappears into dust. It leaves a very large tooth behind.\nWhat now?")
        plypos = 3

    elif dinohealth <= 0 and plyhealth <= 0:
        print('As you see the dinosaur collapse, you slowly lose consciousness and fall over.\nGame over.')
        plydead = True

# area 3 (haha that dino is dead)

while plypos == 3 and tookstool == False and plydead == False and dinodead == True:

    ply = input().lower()

    if globalcommands():
        pass

    elif ply == "look north":
        print("Through the glass case, you see a museum. The glass is too foggy to make out any details.")

    elif (ply == 'break glass' or ply == 'break window' or ply == 'break case') and brokenhand == False:
        print('You bash your fist against the glass. It rebounds into your own face. You take 1 Damage.')
        ouch += 1
        plyhealth -= 1
        if ouch == 3:
            print('Your hand has given up on you.\nYou can\'t use your hand anymore.')
        else:
            print('Your hand hurts more than usual.')
        if plyhealth == 0:
            print('You hit yourself hard enough to accidentaly deal the final blow to yourself.\nYou fall to the ground with a loud thud. There is no way to get back up.\n\nGame over.')
            plydead = True

    elif (ply == 'break glass' or ply == 'break window' or ply == 'break case') and brokenhand == True:
        print('If you were to try, your hand would hurt even more than it already does.')

    elif ply == 'eat glass':
        print("You press your mouth against the glass and attempt to take a bite. Unfortunately, the surface is too smooth and your teeth harmlessly slide against it.")

    elif ply == 'check glass':
        print('When you look closer, you see the glass is entirely clear. However, you still cannot see anything through it.')

    elif ply == "check dinosaur":
        print("You witness a whole lot of dust.")
        if plyhealth <= 2:
            print("You felt as if you acted in self defense.")
        else:
            print("You felt like you did a better job than that meteor.")

    elif ply == 'fight dinosaur':
        print("You square up against the dinosaur's ashes.\nUnfortuantly, it doesn't engage in combat with you.\nYou stop fighting.")

    elif (ply == 'take tooth' or ply == 'take large tooth') and 'Tooth' not in inventory:
        print("You take the particularly large tooth.\nTOOTH added to your INVENTORY")
        inventory.append('Tooth')

    elif (ply == 'take tooth' or ply == 'take large tooth') and 'Tooth' in inventory:
        print("You put the tooth back in order to feel the satisfaction of obtaining it again.\nTOOTH removed from your inventory.")
        inventory.remove('Tooth')
        if armor == 'Tooth':
            armor = 'Nothing'
            plydefense = 0
        
    elif ply == 'look west' and 'Tooth' not in inventory:
        print("There is a large pile of dust. A particularly large tooth lays at the top.")

    elif ply == 'look west' and 'Tooth' in inventory:
        print("Just some simple dust.")

    elif ply == 'look south':
        print("Fake grass. There is a metal vent embedded in the ground.")

    elif ply == 'look east':
        print('A basic beige wall.')

    elif ply == 'go north':
        print("You smack your face into the glass.")

    elif ply == 'go south':
        print('This room is too small to meaningfully move in any direction.')

    elif ply == 'go east':
        print('This room is too small to meaningfully move in any direction.')

    elif ply == 'go west':
        print('There is a giant pile of presumably microplastics in your way.')

    elif ply == 'think' or ply == 'check' or ply == 'hint':
        print('You tried to think. You observe a sense of satisfaction from killing a dinosaur.')

    elif ply == 'check vent' and ventopen == False:
        print("You check the vent. You notice a slight crack that can be budged.")

    elif ply == 'check vent' and ventopen == True:
        print('You observe the opened vent.')

    elif ply == 'open vent' and 'Tooth' not in inventory:
        print('You attempt to open the vent. You cannot achieve this as your fingers are not thin and strong enough for this task.')

    elif ply == 'open vent' and 'Tooth' in inventory and ventopen == False:
        ventopen = True
        print('You open the vent using the tooth. There looks to be a way through the vent.')

    elif ply == 'open vent' and 'Tooth' in inventory and ventopen == True:
        print('You luckily have already opened the vent.')

    elif (ply == 'enter vent' or ply == 'go in vent') and ventopen == True:
        print('You climb into the vent.\nYou are at an intersection.\nTo your left, there is a path ending in several turns.\nTo your right, there is a path ending in a right turn.\nDirectly ahead of you is a wall.\nWhere do you go?')
        plypos = 5

    elif (ply == 'enter vent' or ply == 'go in vent') and ventopen == False:
        print('You attempt to climb into the vent. Unfortunatly, you lack the ability to fit through small holes.')

    else:
        print("Your thoughts seem incomprehensible.")

# area 3 (museum with stool)

while plypos == 3 and tookstool == True and plydead == False:

    ply = input().lower()

    if globalcommands():
        pass

    elif ply == "look north":
        print("Through the glass case, you see a museum. The glass is too foggy to make out any details.")

    elif ply == 'check glass':
        glasscheck()

    elif ply == 'look west' and 'Crowbar' not in inventory:
        print("Big plastic dinosaur. A crowbar dangles from its mouth.")
        dinoseen = True

    elif ply == 'look east':
        print('A basic beige wall.')
    
    elif ply == 'break glass' or ply == 'break window' or ply == 'break case':
        if brokenhand == False:
            print('You bash your fist against the glass. It rebounds into your own face. Now your hand AND face hurt. Good job.')
        else:
            print('If you were to try, your hand would hurt even more than it already does.')

    elif ply == 'eat glass':
        print("You press your mouth against the glass and attempt to take a bite. Unfortunately, the surface is too smooth and your teeth harmlessly slide against it. Drats.")

    elif ply == "check dinosaur" and dinoseen == True:
        print("A large chunk of plastic in the shape of a dinosaur.")

    elif ply == 'fight dinosaur' and dinoseen == True:
        print("You wished that the dinosaur was alive so you could be responsible for their extinction.")

    elif ply == 'climb dinosaur' and dinoseen == True and 'Stool' in inventory:
        print("You used the stool the climb up onto the plastic dinosaur. You notice a hatch to exit to glass case.")
        plysecondary = input("Exit out? Y/N\n").lower()
        if plysecondary == 'y' or plysecondary == 'yes':
            print("""You climb out of the glass case. You find yourself on top of the glass case you were in.
Suddenly, the glass case dissapears from under your feet as you fall to the ground.
You land in a new location that is surrounded by glass.
You feel a little bit healthier than before.
You no longer have access to the stool.
You are not where you were before.""")
            plypos = 11
            plyhealthDEFAULT += 2
            plyhealth = plyhealthDEFAULT
            inventory.remove('Stool')
        elif plysecondary == 'n' or plysecondary == 'no':
            print("You decide to not climb out yet.\nYou jump back down to the ground.")
        else:
            print("You counldn't comprehend what you meant. You decide to jump back down to the ground.")

    elif ply == 'take dinosaur' and dinoseen == True:
        print('You attempt to take the whole dinosaur. If unfourtnatly is too big to be put in your inventory. You punch it in frustration.')

    elif (ply == "check dinosaur" or ply == "fight dinosaur" or ply == "climb dinosaur" or ply == "take dinosaur") and dinoseen == False:
        print("What dinosaur?")

    elif ply == 'look west' and 'Crowbar' in inventory:
        print("Big plastic dinosaur. It looks fake.")

    elif ply == 'take crowbar':
        if tookSplinter == True and 'Crowbar' not in inventory:
            print("You placed the stool down in front of the dinosaur and took the crowbar from its mouth. When you step off the stool, it dissovles into dust. CROWBAR added into your INVENTORY. ")
            inventory.append('Crowbar')
            inventory.remove('Stool')
            if armor == 'Stool':
                armor = 'Nothing'
                plydefense = 0
        elif tookSplinter == False and 'Crowbar' not in inventory:
            print("You placed the stool down in front of the dinosaur and took the crowbar from its mouth. When you step off the stool, it spontaneously explodes into a pile of splinters. CROWBAR added into your INVENTORY. ")
            inventory.append('Crowbar')
            inventory.remove('Stool')
            stoolExplode = True
            if armor == 'Stool':
                armor = 'Nothing'
                plydefense = 0
        elif 'Crowbar' in inventory:
            print('You already have it.')

    elif ply == 'take stool' and stoolExplode == True and tookSplinter == False:
        print('The stool is sadly dead. You grab a handful of splinters to honor the late stool. SPLINTERS added into your INVENTORY')
        inventory.append('Splinters')
        tookSplinter = True

    elif ply == 'take stool' and stoolExplode == True and tookSplinter == True:
        print('You already took the splinters. You can\'t really think of anything else to do.')
        inventory.append('Splinters')
        tookSplinter = True

    elif ply == 'look south':
        print("Fake grass. There is an air vent embedded in the ground")

    elif ply == 'go north':
        print("You smack your face into the glass.")

    elif ply == 'go south':
        print('This room is too small to meaningfully move in any direction.')

    elif ply == 'go east' and plywallBroken == False:
        print('This room is too small to meaningfully move in any direction.')

    elif ply == 'go east' and plywallBroken == True:
        print('Behind the wall, you find a house. It\'s reminiscent of your old childhood home, but you\'ve definitely never been here before.\nThe museum fades from your peripheral as you walk in. \nYou are facing north towards the front door.')
        plypos == 19

    elif ply == 'go west':
        print('It appears there is a giant plastic dinosaur in the way.')
        dinoseen = True

    elif ply == 'open vent' and 'Crowbar' in inventory and ventopen == False:
        print("You pry open the vent with the crowbar. It's too small to climb inside, but there is a red brick inside.")
        ventopen = True

    elif ply == 'take brick' or ply == 'take red brick':
        if ventopen == True and 'Brick' not in inventory:
            print('You took the brick. As you hold it in your hand, it feels more liquid than solid. Yet, it\'s still solid enough to break something. BRICK added into your INVENTORY')
            inventory.append('Brick')
        elif ventopen == True and 'Brick' in inventory:
            print('You already took it.')
        else:
            print('What brick?')

    elif ply == 'open vent' and 'Crowbar' in inventory and ventopen == True:
        print("You close the vent just so you can open it. Again.")

    elif ply == 'open vent' and 'Crowbar' not in inventory:
        print('You try to pull open the vent with your bare hands. It dosen\'t work.')

    elif ply == 'check wall':
        print('A thin plywood wall painted beige. You could probably break it with something heavy enough.')

    elif ply == 'break wall':
        plysecondary = input('With what?').lower()
        if plysecondary == 'brick' and 'Brick' in inventory:
            print('You throw the brick at the wall. After the brick impacts, the wall is seemingly completely decimated.')
            plywallBroken = True
        elif plysecondary == 'brick' and 'Brick' not in inventory:
            print('You don\'t have one of those')
        elif plysecondary != 'brick' and plysecondary in inventory:
            print('You take out ' + plysecondary + '. You don\'t know what to do with it. You put it away.')
        elif plysecondary == 'hand' or plysecondary == 'head' or plysecondary == 'me' or plysecondary == 'foot':
            print('You would prefer not to risk breaking any bones. Maybe try using an item instead.')
        elif plysecondary == 'think' and 'Brick' not in inventory or plysecondary == 'check' and 'Brick' not in inventory or plysecondary == 'hint' and 'Brick' not in inventory:
            print('You tried to think. You feel as if what you need to break the wall is somewhere around here.')
        elif plysecondary == 'think' and 'Brick' in inventory or plysecondary == 'check' and 'Brick' in inventory or plysecondary == 'hint' and 'Brick' in inventory:
            print('You tried to think. You feel as if what you need to break the wall is somewhere in your INVENTORY.')
        elif plysecondary == 'crowbar' and 'Crowbar' not in inventory:
            print('You currently don\'t have a crowbar. Perhaps you can find one nearby?')
        elif plysecondary == 'crowbar' and 'Crowbar' in inventory:
            print('You thought about breaking the wall with the crowbar. You\'d perfer to not damage it just yet.')
        else:
            print('You know already that that wouldn\'t work.')

    else:
        print("Your thoughts seem incomprehensible.")

# Area 5 (gregory, have you heard of a)

while plypos == 3 and plydead == False:

    ply = input().lower()

    if globalcommands():
        pass

    elif ply == 'left' or ply == 'go left':
        
        if ventpos == 0:
            
            if ventDirection == 0:
                print('You go left.\nTo your left, there is a wall.\nTo your right, there is a path that ends in a right turn.\nDirectly ahead of you is a path leading to an intersection.\nWhere do you go?')
                ventpos = 1
                ventDirection = 3
                
            elif ventDirection == 1:
                print('You ram your shoulder into the wall on your left. The galvanized steel sheet doesn\'t budge.')

            elif ventDirection == 3:
                print('You ram your shoulder into the wall on your left. The galvanized steel sheet doesn\'t budge.')
            

        elif ventpos == 1:
            
            if ventDirection == 1:
                print('You go left.\nTo your left, there is a wall.\nTo your right, there is a very long stretch with several turns.\nDirectly ahead of you is a wall.')
                ventpos = 2
                ventDirection = 0

            elif ventDirection == 2:
                print('You go left.\nTo your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a path ending in another left turn.')
                ventpos = 0
                ventDirection = 1

            elif ventDirection == 3:
                print('You ram your shoulder into the wall on your left. The galvanized steel sheet doesn\'t budge.')
            
        elif ventpos == 2:
            
            if ventDirection == 0:
                print('You ram your shoulder into the wall on your left. The galvanized steel sheet doesn\'t budge.')
                
            elif ventDirection == 3:
                print('You go left.\nTo your left, there is a long path ending in another left turn.\nTo your right, there is a path leading to an intersection.\nDirectly ahead of you is a wall.')
                ventpos = 1
                ventDirection = 2
            
            
        elif ventpos == 3:
            
            if ventDirection == 1:
                print('You ram your shoulder into the wall on your left. The galvanized steel sheet doesn\'t budge.')

            elif ventDirection == 3:
                print('You ram your shoulder into the wall on your left. The galvanized steel sheet doesn\'t budge.')
            
            
        elif ventpos == 4:
            if ventDirection == 1:
                print('You go left.\nTo your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a path leading to an intersection.')
                ventpos = 28
            elif ventDirection == 2:
                print('You go left.\nTo your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a there is a very long stretch.')
            
            
        elif ventpos == 5:
            print('You ram your shoulder into the wall on your left. The galvanized steel sheet doesn\'t budge.')
            

        elif ventpos == 6:
            print('You ram your shoulder into the wall on your left. Suprinsingly, the galvanized steel sheet dissolves behind your force. As you .')
            
            
    
