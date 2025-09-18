plydeaths = 0
def retry():
    # the holy and pure and innocent variable block
    # booleans
    global doorbroken, plydead, brokenhand, dinodead, dinoseen, enemythink, plydefending, plycharge, enemydefending, enemycharge, enemyspecial, ventopen, tookstool, tookSplinter, pretendLMAO, plywallBroken
    global stoolExplode, plyturn, plyerror, kys, insidehouse, firstitem, computer
    doorbroken = False
    plydead = False
    brokenhand = False
    dinodead = False
    dinoseen = False
    enemythink = False
    plydefending = False
    plycharge = False
    enemydefending = False
    enemycharge = False
    enemyspecial = False
    ventopen = False
    tookstool = False
    tookSplinter = False
    pretendLMAO = False
    plywallBroken = False
    stoolExplode = False
    plyturn = True
    plyerror = False
    kys = False
    insidehouse = False
    firstitem = False
    computer = False

    # strings
    global ply, plysecondary, miscfight, equippeditem, weapon, weaponspecial, armor, enemyname, enemyphrase, enemyspecialmove
    ply = ""
    plysecondary = ""
    miscfight = ""
    equippeditem = "None"
    weapon = "Nothing"
    weaponspecial = 'Nothing'
    armor = "Nothing"
    enemyname = ""
    enemyphrase = ""
    enemyspecialmove = ""

    # lists
    global inventory
    inventory = ['Nothing']

    # integers
    global plypos, plychoke, ouch, plyhealthDEFAULT, plyhealth, plyatckDEFAULT, plyatck, plyatckplus, plydefenseDEFAULT, plydefense, weaponability, weaponnumber, specialcharge
    plypos = 0
    plychoke = 5
    ouch = 1
    plyhealthDEFAULT = 10
    plyhealth = 10
    plyatckDEFAULT = 5
    plyatck = 5
    plyatckplus = 0
    plydefenseDEFAULT = 0
    plydefense = 0
    weaponability = 0
    weaponnumber = 0
    specialcharge = 3
    global enemyhealth, enemyatck, enemyatckplus, enemyatckDEFAULT, enemyspecialtype, enemyspecialnumber, enemyspecialcount, enemyaction
    enemyhealth = 0
    enemyatck = 0
    enemyatckplus = 0
    enemyatckDEFAULT = 0
    enemydefense = 0
    enemyspecialtype = 0
    enemyspecialnumber = 0
    enemyspecialcount = 0
    enemyaction = 0
    global swordstrength, glassTicker, ventpos, ventDirection, officepos
    swordstrength = 5
    glassTicker = 2
    ventpos = 0
    ventDirection = 0
    officepos = 0

# dictionaries
#   'item name' : 'item description'
items = {
    'Nothing' : 'NOTHING - Empty air. Why is this here? Perhaps you can do something with it before it\'s gone forever.',
    'Stool' : 'STOOL - An old wooden stool. It doesn\'t look like it\'ll last very long.',
    'Splinters' : 'SPLINTERS - A collection of broken little bits of wood.',
    'Pretend Splinters' : 'PRETEND SPLINTERS - A collection of little broken bits of wood made from your imagination.',
    'Crowbar' : 'CROWBAR - A sturdy piece of curved aluminium made for prying things open.',
    'Tooth' : 'TOOTH - A fake tooth from a plastic prehistoric predator.',
    'Brick' : 'BRICK - A brick that feels like a liquid for some reason. Still acts like a solid object.',
    'Shard' : 'SHARD - A mysterious shard that you obtained from the void in some way. You feel as if you shouldn\'t have been able to obtain this.',
    'Sword' : 'SWORD - A sword shaped object that formed from the shard. Perfect for slaying anything in your way.',
    'Key' : 'KEY - A key that you obtained from a skeleton. Looks to have the ability to unlock various locks.',
    'Lantern' : 'LANTERN - An ordinary lantern with no oddities whatsoever.',
    'Branch' : 'BRANCH - A part of the tree that was left to die.'  
}

roomhints = {
    1 : 'You tried to think. You observe that there is a unbroken door in front of you.',
    2 : 'You tried to think. You observe that the brick wall in the doorframe looks unnatural.',
    3 : 'You tried to think. You observe a strange feeling of being watched.',
    4 : 'You tried to think. You observe a suspicious looking dinosaur.',
    5 : 'You tried to think. You observe a sense of satisfaction from killing a dinosaur.',
    6 : 'You tried to think. You observe a dangling crowbar from the Plastic Dinosaur that is too high to reach.',
    7 : 'You tried to think. You thought about the destruction of buildings.',
    8 : 'You tried to think. You observe a puzzle you have already completed before.',
    9 : 'You tried to think. You thought about the minotaur in the labyrinth.',
    10 : 'You tried to think. You observe a strange message.'
}

selfcheckroom = {
    1 : 'Trying to investigate this strange door they found.',
    2 : 'Certified Destroyer of Doors.',
    3 : 'Feels broken.',
    4 : 'Feels a prehistoric rage overtaking them.',
    5 : 'Plastic Dinosaur exterminator.',
    6 : 'Ready to climb their newly obtained stool.',
    7 : 'Already broke their newly obtained stool.',
    8 : 'Still trying to investigate this unique door they found.'
}

# classes, but the cool kind
class Enemy:
    def __init__(self, name, health, attack, defense, atckphrase, special):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.atckphrase = atckphrase
        self.special = special

class Special:
    def __init__(self, name, ability, number):
        self.name = name
        self.ability = ability
        self.number = number

# Enemies
def plasticDino():
    global plasticDino, enemyname, enemyhealth, enemyatck, enemyatckDEFAULT, enemydefense, enemyphrase, enemydefending, enemycharge, enemyspecial, enemyspecialmove, enemyspecialtype, enemyspecialnumber
    plasticDino = Enemy("The Plastic Dinosaur", 30, 2, 0, "bit you", False)
    enemyname = plasticDino.name
    enemyhealth = plasticDino.health
    enemyatck = plasticDino.attack
    enemyatckDEFAULT = plasticDino.attack
    enemydefense = plasticDino.defense
    enemyphrase = plasticDino.atckphrase
    enemyspecial = plasticDino.special

    enemyspecialmove = ""
    enemyspecialtype = 0
    enemyspecialnumber = 0
    
    enemydefending = False
    enemycharge = False

def voidenemy():
    global voidenemy, enemyname, enemyhealth, enemyatck, enemyatckDEFAULT, enemydefense, enemyphrase, enemydefending, enemycharge, voidspecial
    global enemyspecial, enemyspecialmove, enemyspecialtype, enemyspecialnumber, enemyspecialcount
    voidenemy = Enemy("The VOID", 50, 3, 1, "suffocated you", True)
    enemyname = voidenemy.name
    enemyhealth = voidenemy.health
    enemyatck = voidenemy.attack
    enemyatckDEFAULT = voidenemy.attack
    enemydefense = voidenemy.defense
    enemyphrase = voidenemy.atckphrase
    enemyspecial = voidenemy.special

    voidspecial = Special("Life Drain", 1, 4)
    enemyspecialmove = voidspecial.name
    enemyspecialtype = voidspecial.ability
    enemyspecialnumber = voidspecial.number

    enemydefending = False
    enemycharge = False
    enemyspecialcount = 0


# For easier enemy formatting, here's the template (Using the Plastic Dinosaur as a base.)
    #enemyname = plasticDino.name
    #enemyhealth = plasticDino.health
    #enemyatck = plasticDino.attack
    #enemyatckDEFAULT = plasticDino.attack
    #enemydefense = plasticDino.defense
    #enemyphrase = plasticDino.atckphrase
    #enemyspecial = plasticDino.special

    #enemydefending = False
    #enemycharge = False

# Weapon Specials
    # NOTE THIS: The Special follows this class:
        #Name - What the special move is called
        #Ability - What type of ability it has (1 = Deals Damage, 2 = Increases Attack, 3 = Heals HP, 4 = Increases Defense)
        #Number - What number is used for the ability

def plyspecial():
    global specialweapon, weapon, weaponspecial, weaponability, weaponnumber, specialcharge
    if weapon == 'Nothing':
        specialweapon = Special("Nothing", 0, 0)
    elif weapon == 'Splinters':
        specialweapon = Special("Splinter Knuckles", 2, 2)
    elif weapon == 'Pretend Splinters':
        specialweapon = Special("Nothing", 0, 0)
    elif weapon == 'Crowbar':
        specialweapon = Special("Spinning Crowbar", 1, 10)
    elif weapon == 'Brick':
        specialweapon = Special("Solid Drink", 3, 5)
    elif weapon == 'Shard':
        specialweapon = Special("Kill", 1, 20)
    elif weapon == 'Sword':
        specialweapon = Special("Eliminate", 1, 40)
    elif weapon == 'Key':
        specialweapon = Special("Nothing", 0, 0)
    elif weapon == 'Lantern':
        specialweapon = Special("Light it up", 2, 1)

    weaponspecial = specialweapon.name
    weaponability = specialweapon.ability
    weaponnumber = specialweapon.number
    specialcharge = 3


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
        plypos = 12
        plyhealthDEFAULT += 2
        plyhealth = plyhealthDEFAULT

def battlestart():
    global weaponspecial
    if weaponspecial != 'Nothing':
        print(f"""
Your actions are:
\033[1;31mATTACK
\033[1;34mDEFEND
\033[1;32mCHARGE
\033[1;30mSPECIAL: {weaponspecial} (Ready in 3 Turns)\033[0m""")
    else:
        print("""
Your actions are:
\033[1;31mATTACK
\033[1;34mDEFEND
\033[1;32mCHARGE\033[0m""")

def plymove():
    global ply, plyhealth, enemydefending, enemyhealth, plyatck, enemydefense, plycharge, enemythink, enemyname, plydefending, plyerror, enemyatck, plydefense, specialcharge, weaponspecial, weaponability, weaponnumber, plyatckplus

    if plyerror == True:
        plyerror = False
    else:
        if specialcharge == 0:
            print(f"Your special move, \033[1;3{weaponability}m{weaponspecial}\033[0m is now ready. Type SPECIAL to use it.")
        else:
            if weaponspecial != "Nothing":
                specialcharge -= 1

    ply = input(f"\033[1;32mYour health is: {plyhealth}. \033[1;35m{enemyname}'s health is {enemyhealth}. \033[0mWhat do you do?\n> ").lower()

    import math

    if ply == 'attack' and enemydefending == False:
        print(f"\033[1;31mYou attacked {enemyname} for {plyatck - enemydefense} damage!\033[0m")
        enemyhealth = enemyhealth - (plyatck - enemydefense)
        if plyatckplus != 0:
            plyatck -= plyatckplus
            plyatckplus = 0
        if plycharge == True:
            plyatck = math.floor(plyatck / 2)
            plycharge = False
        return True

    elif ply == 'attack' and enemydefending == True:
        print(f"\033[1;31mYou attacked {enemyname}! \033[1;35mBut {enemyname} defended.\033[0m")
        if plyatckplus != 0:
            plyatck -= plyatckplus
            plyatckplus = 0
        if plycharge == True:
            plyatck = math.floor(plyatck / 2)
            plycharge = False
        enemydefending = False
        return True

    elif ply == 'defend':
        print('\033[1;34mYou defended! You won\'t take damage this turn.\033[0m')
        enemydefending = False
        plydefending = True
        return True

    elif ply == 'charge' and plycharge == False:
        print('\033[1;32mYou charged! You will do double damage on your next attack!\033[0m')
        if plyatckplus != 0:
            plyatck -= plyatckplus
            plyatck *= 2
            plyatck += plyatckplus
        else:
            plyatck *= 2
        plycharge = True
        enemydefending = False
        return True

    elif ply == 'charge' and plycharge == True:
        print('\033[1;32mYou tried to charge again!\033[0m But nothing happened...')
        enemydefending = False
        return True

    elif ply == 'special':
        if specialcharge == 0 and weaponability == 1:
            print(f"\033[1;31mYou use {weaponspecial}! You deal {weaponnumber + plyatck} damage to {enemyname}!\033[0m")
            enemyhealth -= (plyatck + weaponnumber)
            if plycharge == True:
                plyatck = math.floor(plyatck / 2)
                plycharge = False
            enemydefending = False
            specialcharge = 3
            return True
        elif specialcharge == 0 and weaponability == 2:
            print(f"\033[1;32mYou use {weaponspecial}! You gain +{weaponnumber} attack for your next attack.\033[0m")
            plyatck += weaponnumber
            plyatckplus += weaponnumber
            specialcharge = 3
            enemydefending = False
            return True
        elif specialcharge == 0 and weaponability == 3:
            print(f"\033[1;33mYou use {weaponspecial}! You healed +{weaponnumber} health.\033[0m")
            plyhealth += weaponnumber
            specialcharge = 3
            return True
        elif specialcharge == 0 and weaponability == 4:
            print(f"\033[1;34mYou use {weaponspecial}! You gain +{weaponnumber} defense for the rest of the fight.\033[0m")
            plydefense += weaponnumber
            specialcharge = 3
            return True
        elif specialcharge != 0 and weaponspecial != 'Nothing':
            print(f"\033[1;30mYou cannot use {weaponspecial} yet. You still have to wait {specialcharge} turns.\033[0m")
            plyerror = True
            return False
        else:
            plyerror = True
            return False

    elif ply == 'check':
        print(f"""\033[1;32mYOU:
    CURRENT HP - {plyhealth}
    CURRENT ATTACK - {plyatck} ({weapon})
    CURRENT DEFENSE - {plydefense}
\033[1;35m{enemyname}:
    CURRENT HP - {enemyhealth}
    CURRENT ATTACK - {enemyatck}
    CURRENT DEFENSE - {enemydefense}\033[0m""")

    elif ply == 'check self' or ply == 'check me':
        print(f"""\033[1;32mYOU:
    CURRENT HP - {plyhealth}
    CURRENT ATTACK - {plyatck} ({weapon})
    CURRENT DEFENSE - {plydefense}\033[0m""")

    elif ply == 'check enemy' or enemyname in ply:
        print(f"""\033[1;35m{enemyname}:
    CURRENT HP - {enemyhealth}
    CURRENT ATTACK - {enemyatck}
    CURRENT DEFENSE - {enemydefense}\033[0m""")

    elif ply == 'think' or ply == 'hint':
        print(f"""You ended up thinking. You remembered how to fight.
\033[1;31mATTACK: Deals {plyatck - enemydefense} Damage to {enemyname} if {enemyname} isn't defending.
\033[1;34mDEFEND: Allows you to take 0 Damage this turn.
\033[1;32mCHARGE: Powers up attack to deal double damage next attack.\033[0m""")
        if weaponspecial != 'Nothing':
            if weaponability == 1:
                print(f"\033[1;31mSPECIAL: {weaponspecial} - Deals {weaponnumber + plyatck} damage to {enemyname}, ignoring defense.\033[0m")
            elif weaponability == 2:
                print(f"\033[1;32mSPECIAL: {weaponspecial} - Adds +{weaponnumber} damage to your next attack.\033[0m")
            elif weaponability == 3:
                print(f"\033[1;33mSPECIAL: {weaponspecial} - Heals self {weaponnumber} health. Can go over your max HP.\033[0m")
            elif weaponability == 4:
                print(f"\033[1;34mSPECIAL: {weaponspecial} - Gains +{weaponnumber} defense for the rest of the battle.\033[0m")
            if specialcharge != 0:
                print(f"You can use {weaponspecial} in {specialcharge} turns.")
        if enemythink == False:
            enemythink = True
        elif enemythink == True:
            print(f"{enemyname} notices you thinking for an aditional time and \033[1;31m{enemyphrase} for {enemyatck - plydefense} damage\033[0m as you weren't defending.")
            plyhealth -= (enemyatck - plydefense)
            enemyatck = enemyatckDEFAULT
        return True

    elif ply == 'quit':
        quit()
        return True

    else:
        plyerror = True
        return True

def enemymove():
    import random
    global plydefense, plyhealth, enemyatck, enemydefense, enemyhealth, enemycharge, enemydefense, enemydefending, plydefending
    global enemyspecial, enemyspecialcount, enemyspecialmove, enemyspecialtype, enemyspecialnumber, enemyatckplus

    enemyaction = random.randint(1, 9)
    if enemyspecial == True:
        if enemyspecialcount == 5:
            print(f"\033[1;3{enemyspecialtype}m{enemyname} used their speical move, {enemyspecialmove}!\033[0m")
            if enemyspecialtype == 1:
                if plydefending == True:
                    print(f"\033[1;3{enemyspecialtype}m{enemyname} deals {(enemyspecialnumber / 2) - plydefense} damage to you.")
                    plyhealth -= int((enemyspecialnumber / 2) - plydefense)
                else:
                    print(f"\033[1;3{enemyspecialtype}m{enemyname} deals {enemyspecialnumber} damage to you.")
                    plyhealth -= enemyspecialnumber
                plydefending = False
            elif enemyspecialtype == 2:
                print(f"\033[1;3{enemyspecialtype}m{enemyname} gains +{enemyspecialnumber} attack for their next attack.")
                enemyatck += enemyspecialnumber
                enemyatckplus += enemyspecialnumber
                plydefending = False
            elif enemyspecialtype == 3:
                print(f"\033[1;3{enemyspecialtype}m{enemyname} heals {enemyspecialnumber} health.")
                enemyhealth += enemyspecialnumber
                plydefending = False
            elif enemyspecialtype == 4:
                print("\033[1;3{enemyspecialtype}m{enemyname} gains +{enemyspecialnumber} defense for the rest of the fight.")
                enemydefense += enemyspecialnumber
                plydefending = False
            else:
                print("But it didn't do anything because they don't have a valid command.")
            enemyspecialcount = 0
        else:
            enemyspecialcount += 1
            if enemyaction > 6 and plydefending == True:
                print(f"\033[1;31m {enemyname} {enemyphrase}. \033[1;34mBut you defended!\033[0m")
                enemyatck = enemyatckDEFAULT
                enemycharge = False
                enemydefending = False
                plydefending = False
            elif enemyaction > 6 and plydefending == False:
                print(f"\033[1;31m {enemyname} {enemyphrase} for {enemyatck - plydefense}!\033[0m")
                plyhealth = plyhealth - (enemyatck - plydefense)
                enemyatck = enemyatckDEFAULT
                enemycharge = False
                enemydefending = False
            elif enemyaction < 4:
                print(f"\033[1;34m {enemyname} defended! {enemyname} won't take damage next turn!\033[0m")
                enemydefending = True
                plydefending = False
            elif enemyaction > 3 and enemyaction < 7 and enemycharge == False:
                print(f"\033[1;32m {enemyname} charged! {enemyname}'s next attack will do double damage!\033[0m")
                enemycharge = True
                if enemyatckplus != 0:
                    enemyatck -= enemyatckplus
                    enemyatck *= 2
                    enemyatck += enemyatckplus
                enemydefending = False
                plydefending = False
            elif enemyaction > 3 and enemyaction < 7 and enemycharge == True:
                print(f"\033[1;32m {enemyname} tried to charge! \033[0mBut {enemyname} already did.")
                plydefending = False
            else:
                print("This will only print if something went horribly wrong.")
            if enemyspecialcount == 4:
                print(f"\033[1;3{enemyspecialtype}m {enemyname} looks to be readying something strong.\033[0m")
                enemyspecialcount = 5
    else:
        if enemyaction > 6 and plydefending == True:
            print(f"\033[1;31m {enemyname} {enemyphrase}. \033[1;34mBut you defended!\033[0m")
            enemyatck = enemyatckDEFAULT
            enemycharge = False
            enemydefending = False
            plydefending = False
        elif enemyaction > 6 and plydefending == False:
            print(f"\033[1;31m {enemyname} {enemyphrase} for {enemyatck - plydefense}!\033[0m")
            plyhealth = plyhealth - (enemyatck - plydefense)
            enemyatck = enemyatckDEFAULT
            enemycharge = False
            enemydefending = False
        elif enemyaction < 4:
            print(f"\033[1;34m {enemyname} defended! {enemyname} won't take damage next turn!\033[0m")
            enemydefending = True
            plydefending = False
        elif enemyaction > 3 and enemyaction < 7 and enemycharge == False:
            print(f"\033[1;32m {enemyname} charged! {enemyname}'s next attack will do double damage!\033[0m")
            enemycharge = True
            enemyatck *= 2
            enemydefending = False
            plydefending = False
        elif enemyaction > 3 and enemyaction < 7 and enemycharge == True:
            print(f"\033[1;32m {enemyname} tried to charge! \033[0mBut {enemyname} already did.")
            plydefending = False
        else:
            print("This will only print if something went horribly wrong.")

def globalcommands():
    # skip the void for this one, it parses commands differently
    global ply, inventory, plyhealth, plydefense, doorbroken, plydead, plypos, tookstool, dinodead, dinoseen, equippeditem, plyatck, weapon, armor, kys, swordstrength
    if ply == 'look around' or ply == 'look':
        print("Perhaps you should try to specify what direction you want to look in.")
        return True
    elif ply == "kill me" or ply == "kill myself":
        if kys == True:
            print("You decide to not attempt self-harm again.")
        if plyatck < 10 and kys == False:
            print("You punched yourself multiple times. You're too weak to deal any damage.")
            kys = True
        elif plyatck >= 10 and plyatck < 100 and kys == False:
            print("You punched yourself multiple times. You managed to make a dent on yourself. \033[1;31mYou take 1 Damage.\033[0m")
            plyhealth -= 1
            if plyhealth == 0:
                print("Amazingly, you managed to dispatch yourself using your own fists. Moron.\n\n\n\033[1;31mGame Over, I guess?")
            kys = True
        elif plyatck >= 100 and kys == False:
            print("You already have enough power, you cannot stop here.")
            kys = True
        return True
    elif ply == 'check inventory' or ply == 'inventory' or ply == 'open inventory':
        if len(inventory) == 0:
            print('\033[1;33mYou do not have any items in your inventory currently.\033[0m')
        else:
            for x in inventory:
                print('\033[1;33m' + x + '\033[0m')
        return True
    elif ply == 'quit':
        print("Ok, bye then.")
        quit()
    elif ply == 'alien':
        print("You sob due to the lack of aliens in your area.")
        return True

    elif ply == 'equip item':
        print("Please make sure to specify what item to equip. (EXAMPLE: Equip Hammer)")
        return True
    
    elif ply == 'idk' or ply == 'i dont know' or ply == 'i don\'t know' or ply == 'i dunno':
        print("Then figure \033[1;31mit\033[0m out.")
        return True
    elif ply == 'think' or ply == 'check' or ply == 'hint':
        if plypos == 1 and doorbroken == False and plydead == False and plydeaths == 0:
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
        elif plypos == 1 and doorbroken == False and plydead == False and plydeaths != 0:
            print(roomhints[8])
        elif plypos == 5 and plydead == False:
            print(roomhints[9])
        elif plypos == 6 and plydead == False:
            print(roomhints[10])
        return True
    elif ply == "check me" or ply == "check myself" or ply == "check self":
        print("YOU \nCURRENT HP: " + str(plyhealth) + "\n\033[1;31mATTACK: " + str(plyatck) + " \033[1;33m(" + weapon + ")\n\033[1;34mDEFENSE: " + str(plydefense) + " \033[1;33m(" + armor + ")\033[0m")
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
                print(f"\033[1;33mYou equipped {equippeditem}.")
                print("\033[1;35mYour Attack and Defense went back to default\033[0m")
                weapon = "Nothing"
                plyatck = plyatckDEFAULT
                armor = "Nothing"
                plydefense = plydefenseDEFAULT
            else:
                if equippeditem == weapon or equippeditem == armor:
                    print(f"\033[1;33mYou already have the {equippeditem} equipped.\033[0m")
                else:
                    print(f"\033[1;33mYou equipped the {equippeditem}.")
                    if equippeditem == 'Stool':
                        print("\033[1;34mYou gained +1 Defense\033[0m")
                        armor = 'Stool'
                        plydefense = plydefenseDEFAULT + 1
                    elif equippeditem == 'Splinters':
                        if stoolExplode == True:
                            print("In remembrance of the stool, you equipped the Splinters as armor.\n\033[1;34mYou gained +1 Defense\033[0m")
                            armor = 'Splinters'
                            plydefense = plydefenseDEFAULT + 1
                        else:
                            print("\033[1;31mYou gained +1 Attack\033[0m")
                            weapon = 'Splinters'
                            plyatck = plyatckDEFAULT + 1
                    elif equippeditem == 'Pretend Splinters':
                        print("You act like you are holding splinters.\n\033[1;31mYou gained -1 Attack\033[0m")
                        weapon = "Pretend Splinters"
                        plyatck = plyatckDEFAULT - 1
                    elif equippeditem == 'Crowbar':
                        print("\033[1;31mYou gained +2 Attack\033[0m")
                        weapon = "Crowbar"
                        plyatck = plyatckDEFAULT + 2
                    elif equippeditem == 'Brick':
                        print("\033[1;31mYou gained +1 Attack\033[0m")
                        weapon = "Brick"
                        plyatck = plyatckDEFAULT + 1
                    elif equippeditem == 'Shard':
                        print("You feel an overwhelming sense of power\033[1;31m\nYou gained +3 Attack\033[0m")
                        weapon = "Shard"
                        plyatck = plyatckDEFAULT + 3
                    elif equippeditem == 'Sword':
                        print(f"You feel an even greater overwhelming sense of power\033[1;31m\nYou gained +{swordstrength} Attack\033[0m")
                        weapon = "Sword"
                        plyatck = plyatckDEFAULT + swordstrength
                    elif equippeditem == 'Tooth':
                        print("You wear it as a badge of honor.\n\033[1;34mYou gained +1 Defense\033[0m")
                        armor = 'Tooth'
                        plydefense = plydefenseDEFAULT + 1
                    elif equippeditem == 'Key':
                        print("\033[1;31mYou gained +1 Attack\033[0m")
                        weapon = 'Key'
                        plyatck = plyatckDEFAULT + 1
                    elif equippeditem == 'Lantern':
                        print("\033[1;31mYou gained +1 Attack\033[0m")
                        weapon = 'Lantern'
                        plyatck = plyatckDEFAULT + 1
                    elif equippeditem == 'Branch':
                        print("\033[1;31mThere is no need. It would only hinder your abilities.\033[0m")
        else:
            print(f"\033[1;33mYou don't have a \"{item_to_equip}\" in your inventory.\033[0m")
        return True
    elif ply.startswith("check "):
        item_to_equip = ply[6:].strip().title()
        if item_to_equip in inventory:
            print("\033[1;33m" + items[item_to_equip] + "\033[0m")
        else:
            print("Your thoughts seem incomprehensible.")
        return True
    else:
        return False
        
def ventdesc():
    global vent_descriptions, ventpos, ventDirection
    print((vent_descriptions[ventpos])[ventDirection])

def ventmove_left():
    global vent_walls, ventdesc, ventpos, ventDirection
    if (vent_walls[ventpos])[(ventDirection -1) % 4] == True:
        print('You slam your shoulder into the galvanized steel sheet on your left. It doesn\'t budge.')
    elif (vent_walls[ventpos])[(ventDirection - 1) % 4] == False:
        if ventpos == 6 and ventDirection == 1:
            print('You slam your shoulder into the galvanized steel sheet on your left. Suprisingly, you pass right through it.')
            ventdesc()
            ventDirection = int((ventDirection - 1) % 4)
        elif ventpos == 27 and ventDirection == 3:
            print('You attempt to pass through the stopped fan. While you are halfway through, the fan starts up again. You are cleanly bisected in two. \nGame Over.')
            plydead = True
        elif ventpos == 8 and ventDirection == 0:
            print('You walk into the light. You... walk? Weren\'t you just crawling?\nYou appear to be in some sort of security office. Computer monitors line one wall just above a desk. You are facing east.')
            plypos = 6
        else:
            print("You go left.")
            if ventDirection == 0:
                ventDirection = 3
                if ventpos == 0:
                    ventpos = 1
                    ventdesc()
                elif ventpos == 1:
                    ventpos = 13
                    ventdesc()
                elif ventpos == 3:
                    ventpos = 2
                    ventdesc()
                elif ventpos == 4:
                    ventpos = 3
                    ventdesc()
                elif ventpos == 5:
                    ventpos = 4
                    ventdesc()
                elif ventpos == 6:
                    ventpos = 5
                    ventdesc()
                elif ventpos == 7:
                    ventpos = 6
                    ventdesc()
                elif ventpos == 9:
                    ventpos = 0
                    ventdesc()
                elif ventpos == 10:
                    ventpos = 11
                    ventdesc()
                elif ventpos == 11:
                    ventpos = 12
                    ventdesc()
                elif ventpos == 16:
                    ventpos = 15
                    ventdesc()
                elif ventpos == 17:
                    ventpos = 16
                    ventdesc()
                elif ventpos == 18:
                    ventpos = 17
                    ventdesc()
                elif ventpos == 20:
                    ventpos = 19
                    ventdesc()
                elif ventpos == 21:
                    ventpos = 20
                    ventdesc()
                elif ventpos == 22:
                    ventpos = 6
                    ventdesc()
                elif ventpos == 23:
                    ventpos = 22
                    ventdesc()
            elif ventDirection == 1:
                ventDirection = 0
                if ventpos == 1:
                    ventpos = 2
                    ventdesc()
                elif ventpos == 4:
                    ventpos = 28
                    ventdesc()
                elif ventpos == 9:
                    ventpos = 10
                    ventdesc()
                elif ventpos == 13:
                    ventpos = 14
                    ventdesc()
                elif ventpos == 14:
                    ventpos = 15
                    ventdesc()
                elif ventpos == 18:
                    ventpos = 19
                    ventdesc()
                elif ventpos == 22:
                    ventpos = 21
                    ventdesc()
                elif ventpos == 23:
                    ventpos = 24
                    ventdesc()
                elif ventpos == 25:
                    ventpos = 13
                    ventdesc()
                elif ventpos == 26:
                    ventpos = 22
                    ventdesc()
                elif ventpos == 27:
                    ventpos = 26
                    ventdesc()
                elif ventpos == 28:
                    ventpos = 17
                    ventdesc()
            elif ventDirection == 2:
                ventDirection = 1
                if ventpos == 0:
                    ventpos = 9
                    ventdesc()
                elif ventpos == 1:
                    ventpos = 0
                    ventdesc()
                elif ventpos == 2:
                    ventpos = 3
                    ventdesc()
                elif ventpos == 3:
                    ventpos = 4
                    ventdesc()
                elif ventpos == 4:
                    ventpos = 5
                    ventdesc()
                elif ventpos == 5:
                    ventpos = 6
                    ventdesc()
                elif ventpos == 6:
                    ventpos = 22
                    ventdesc()
                elif ventpos == 8:
                    ventpos = 7
                    ventdesc()
                elif ventpos == 11:
                    ventpos = 10
                    ventdesc()
                elif ventpos == 12:
                    ventpos = 11
                    ventdesc()
                elif ventpos == 13:
                    ventpos = 1
                    ventdesc()
                elif ventpos == 15:
                    ventpos = 16
                    ventdesc()
                elif ventpos == 16:
                    ventpos = 17
                    ventdesc()
                elif ventpos == 17:
                    ventpos = 18
                    ventdesc()
                elif ventpos == 19:
                    ventpos = 20
                    ventdesc()
                elif ventpos == 20:
                    ventpos = 21
                    ventdesc()
                elif ventpos == 22:
                    ventpos = 23
                    ventdesc()
            elif ventDirection == 3:
                ventDirection = 2
                if ventpos == 2:
                    ventpos = 1
                    ventdesc()
                elif ventpos == 10:
                    ventpos = 9
                    ventdesc()
                elif ventpos == 13:
                    ventpos = 25
                    ventdesc()
                elif ventpos == 14:
                    ventpos = 13
                    ventdesc()
                elif ventpos == 15:
                    ventpos = 14
                    ventdesc()
                elif ventpos == 17:
                    ventpos = 28
                    ventdesc()
                elif ventpos == 19:
                    ventpos = 18
                    ventdesc()
                elif ventpos == 21:
                    ventpos = 22
                    ventdesc()
                elif ventpos == 22:
                    ventpos = 26
                    ventdesc()
                elif ventpos == 24:
                    ventpos = 23
                    ventdesc()
                elif ventpos == 26:
                    ventpos = 27
                    ventdesc()
                elif ventpos == 28:
                    ventpos = 4
                    ventdesc()

def ventmove_forward():
    global vent_walls, ventdesc, ventpos, ventDirection
    if (vent_walls[ventpos])[ventDirection % 4] == True:
        print('You slam your face into the galvanized steel sheet in front of you. It doesn\'t budge.')
    elif (vent_walls[ventpos])[ventDirection % 4] == False:
        if ventpos == 6 and ventDirection == 0:
            print('You slam your face into the galvanized steel sheet in front of you. Suprisingly, you pass right through it.')
            ventdesc()
        elif ventpos == 27 and ventDirection == 2:
            print('You attempt to pass through the stopped fan. While you are halfway through, the fan starts up again. You are cleanly bisected across the waist. \nGame Over.')
            plydead = True
        elif ventpos == 8 and ventDirection == 3:
            print('You walk into the light. You... walk? Weren\'t you just crawling?\nYou appear to be in some sort of security office. Computer monitors line one wall just above a desk. You are facing east.')
            plypos = 6
        else:
            print('You crawl forward.')
            if ventDirection == 0:
                if ventpos == 1:
                    ventpos = 2
                    ventdesc()
                elif ventpos == 4:
                    ventpos = 28
                    ventdesc()
                elif ventpos == 9:
                    ventpos = 10
                    ventdesc()
                elif ventpos == 13:
                    ventpos = 14
                    ventdesc()
                elif ventpos == 14:
                    ventpos = 15
                    ventdesc()
                elif ventpos == 18:
                    ventpos = 19
                    ventdesc()
                elif ventpos == 22:
                    ventpos = 21
                    ventdesc()
                elif ventpos == 23:
                    ventpos = 24
                    ventdesc()
                elif ventpos == 25:
                    ventpos = 13
                    ventdesc()
                elif ventpos == 26:
                    ventpos = 22
                    ventdesc()
                elif ventpos == 27:
                    ventpos = 26
                    ventdesc()
                elif ventpos == 28:
                    ventpos = 17
                    ventdesc()
            elif ventDirection == 1:
                if ventpos == 0:
                    ventpos = 9
                    ventdesc()
                elif ventpos == 1:
                    ventpos = 0
                    ventdesc()
                elif ventpos == 2:
                    ventpos = 3
                    ventdesc()
                elif ventpos == 3:
                    ventpos = 4
                    ventdesc()
                elif ventpos == 4:
                    ventpos = 5
                    ventdesc()
                elif ventpos == 5:
                    ventpos = 6
                    ventdesc()
                elif ventpos == 6:
                    ventpos = 22
                    ventdesc()
                elif ventpos == 8:
                    ventpos = 7
                    ventdesc()
                elif ventpos == 11:
                    ventpos = 10
                    ventdesc()
                elif ventpos == 12:
                    ventpos = 11
                    ventdesc()
                elif ventpos == 13:
                    ventpos = 1
                    ventdesc()
                elif ventpos == 15:
                    ventpos = 16
                    ventdesc()
                elif ventpos == 16:
                    ventpos = 17
                    ventdesc()
                elif ventpos == 17:
                    ventpos = 18
                    ventdesc()
                elif ventpos == 19:
                    ventpos = 20
                    ventdesc()
                elif ventpos == 20:
                    ventpos = 21
                    ventdesc()
                elif ventpos == 22:
                    ventpos = 23
                    ventdesc()
            elif ventDirection == 2:
                if ventpos == 2:
                    ventpos = 1
                    ventdesc()
                elif ventpos == 10:
                    ventpos = 9
                    ventdesc()
                elif ventpos == 13:
                    ventpos = 25
                    ventdesc()
                elif ventpos == 14:
                    ventpos = 13
                    ventdesc()
                elif ventpos == 15:
                    ventpos = 14
                    ventdesc()
                elif ventpos == 17:
                    ventpos = 28
                    ventdesc()
                elif ventpos == 19:
                    ventpos = 18
                    ventdesc()
                elif ventpos == 21:
                    ventpos = 22
                    ventdesc()
                elif ventpos == 22:
                    ventpos = 26
                    ventdesc()
                elif ventpos == 24:
                    ventpos = 23
                    ventdesc()
                elif ventpos == 26:
                    ventpos = 27
                    ventdesc()
                elif ventpos == 28:
                    ventpos = 4
                    ventdesc()
            elif ventDirection == 3:
                if ventpos == 0:
                    ventpos = 1
                    ventdesc()
                elif ventpos == 1:
                    ventpos = 13
                    ventdesc()
                elif ventpos == 3:
                    ventpos = 2
                    ventdesc()
                elif ventpos == 4:
                    ventpos = 3
                    ventdesc()
                elif ventpos == 5:
                    ventpos = 4
                    ventdesc()
                elif ventpos == 6:
                    ventpos = 5
                    ventdesc()
                elif ventpos == 7:
                    ventpos = 6
                    ventdesc()
                elif ventpos == 9:
                    ventpos = 0
                    ventdesc()
                elif ventpos == 10:
                    ventpos = 11
                    ventdesc()
                elif ventpos == 11:
                    ventpos = 12
                    ventdesc()
                elif ventpos == 16:
                    ventpos = 15
                    ventdesc()
                elif ventpos == 17:
                    ventpos = 16
                    ventdesc()
                elif ventpos == 18:
                    ventpos = 17
                    ventdesc()
                elif ventpos == 20:
                    ventpos = 19
                    ventdesc()
                elif ventpos == 21:
                    ventpos = 20
                    ventdesc()
                elif ventpos == 22:
                    ventpos = 6
                    ventdesc()
                elif ventpos == 23:
                    ventpos = 22
                    ventdesc()

def ventmove_right():
    global vent_walls, ventdesc, ventpos, ventDirection
    if (vent_walls[ventpos])[(ventDirection + 1) % 4] == True:
        print('You slam your shoulder into the galvanized steel sheet in front of you. It doesn\'t budge.')
    elif (vent_walls[ventpos])[(ventDirection + 1) % 4] == False:
        if ventpos == 6 and ventDirection == 3:
            print('You slam your face into the galvanized steel sheet in front of you. Suprisingly, you pass right through it.')
            ventdesc()
        elif ventpos == 27 and ventDirection == 1:
            print('You attempt to pass through the stopped fan. While you are halfway through, the fan starts up again. You are cleanly bisected across the waist. \nGame Over.')
            plydead = True
        elif ventpos == 8 and ventDirection == 2:
            print('You walk into the light. You... walk? Weren\'t you just crawling?\nYou appear to be in some sort of security office. Computer monitors line one wall just above a desk. You are facing east.')
            plypos = 6
        else:
            print('You go right.')
            if ventDirection == 0:
                ventDirection = 1
                if ventpos == 0:
                    ventpos = 9
                    ventdesc()
                elif ventpos == 1:
                    ventpos = 0
                    ventdesc()
                elif ventpos == 2:
                    ventpos = 3
                    ventdesc()
                elif ventpos == 3:
                    ventpos = 4
                    ventdesc()
                elif ventpos == 4:
                    ventpos = 5
                    ventdesc()
                elif ventpos == 5:
                    ventpos = 6
                    ventdesc()
                elif ventpos == 6:
                    ventpos = 22
                    ventdesc()
                elif ventpos == 8:
                    ventpos = 7
                    ventdesc()
                elif ventpos == 11:
                    ventpos = 10
                    ventdesc()
                elif ventpos == 12:
                    ventpos = 11
                    ventdesc()
                elif ventpos == 13:
                    ventpos = 1
                    ventdesc()
                elif ventpos == 15:
                    ventpos = 16
                    ventdesc()
                elif ventpos == 16:
                    ventpos = 17
                    ventdesc()
                elif ventpos == 17:
                    ventpos = 18
                    ventdesc()
                elif ventpos == 19:
                    ventpos = 20
                    ventdesc()
                elif ventpos == 20:
                    ventpos = 21
                    ventdesc()
                elif ventpos == 22:
                    ventpos = 23
                    ventdesc()
            elif ventDirection == 1:
                ventDirection = 2
                if ventpos == 2:
                    ventpos = 1
                    ventdesc()
                elif ventpos == 10:
                    ventpos = 9
                    ventdesc()
                elif ventpos == 13:
                    ventpos = 25
                    ventdesc()
                elif ventpos == 14:
                    ventpos = 13
                    ventdesc()
                elif ventpos == 15:
                    ventpos = 14
                    ventdesc()
                elif ventpos == 17:
                    ventpos = 28
                    ventdesc()
                elif ventpos == 19:
                    ventpos = 18
                    ventdesc()
                elif ventpos == 21:
                    ventpos = 22
                    ventdesc()
                elif ventpos == 22:
                    ventpos = 26
                    ventdesc()
                elif ventpos == 24:
                    ventpos = 23
                    ventdesc()
                elif ventpos == 26:
                    ventpos = 27
                    ventdesc()
                elif ventpos == 28:
                    ventpos = 4
                    ventdesc()
            elif ventDirection == 2:
                ventDirection = 3
                if ventpos == 0:
                    ventpos = 1
                    ventdesc()
                elif ventpos == 1:
                    ventpos = 13
                    ventdesc()
                elif ventpos == 3:
                    ventpos = 2
                    ventdesc()
                elif ventpos == 4:
                    ventpos = 3
                    ventdesc()
                elif ventpos == 5:
                    ventpos = 4
                    ventdesc()
                elif ventpos == 6:
                    ventpos = 5
                    ventdesc()
                elif ventpos == 7:
                    ventpos = 6
                    ventdesc()
                elif ventpos == 9:
                    ventpos = 0
                    ventdesc()
                elif ventpos == 10:
                    ventpos = 11
                    ventdesc()
                elif ventpos == 11:
                    ventpos = 12
                    ventdesc()
                elif ventpos == 16:
                    ventpos = 15
                    ventdesc()
                elif ventpos == 17:
                    ventpos = 16
                    ventdesc()
                elif ventpos == 18:
                    ventpos = 17
                    ventdesc()
                elif ventpos == 20:
                    ventpos = 19
                    ventdesc()
                elif ventpos == 21:
                    ventpos = 20
                    ventdesc()
                elif ventpos == 22:
                    ventpos = 6
                    ventdesc()
                elif ventpos == 23:
                    ventpos = 22
                    ventdesc()
            elif ventDirection == 3:
                ventDirection = 0
                if ventpos == 1:
                    ventpos = 2
                    ventdesc()
                elif ventpos == 4:
                    ventpos = 28
                    ventdesc()
                elif ventpos == 9:
                    ventpos = 10
                    ventdesc()
                elif ventpos == 13:
                    ventpos = 14
                    ventdesc()
                elif ventpos == 14:
                    ventpos = 15
                    ventdesc()
                elif ventpos == 18:
                    ventpos = 19
                    ventdesc()
                elif ventpos == 22:
                    ventpos = 21
                    ventdesc()
                elif ventpos == 23:
                    ventpos = 24
                    ventdesc()
                elif ventpos == 25:
                    ventpos = 13
                    ventdesc()
                elif ventpos == 26:
                    ventpos = 22
                    ventdesc()
                elif ventpos == 27:
                    ventpos = 26
                    ventdesc()
                elif ventpos == 28:
                    ventpos = 17
                    ventdesc()

def ventmove_back():
    global vent_walls, ventdesc, ventpos, ventDirection
    if (vent_walls[ventpos])[(ventDirection - 2) % 4] == True:
        print('You crawl backwards into the galvanized steel sheet behind you. It doesn\'t budge.')
    elif (vent_walls[ventpos])[(ventDirection - 2) % 4] == False:
        if ventpos == 6 and ventDirection == 0:
            print('You crawl backwards into the galvanized steel sheet behind you. Suprisingly, you pass right through it.')
            ventdesc()
        elif ventpos == 27 and ventDirection == 2:
            print('You attempt to pass through the stopped fan. While you are halfway through, the fan starts up again. You are cleanly bisected across the waist. \nGame Over.')
            plydead = True
        elif ventpos == 8 and ventDirection == 3:
            print('You walk into the light. You... walk? Weren\'t you just crawling?\nYou appear to be in some sort of security office. Computer monitors line one wall just above a desk. You are facing east.')
            plypos = 6
        else:
            print('You crawl backward.')
            if ventDirection == 0:
                if ventpos == 2:
                    ventpos = 1
                    ventdesc()
                elif ventpos == 10:
                    ventpos = 9
                    ventdesc()
                elif ventpos == 13:
                    ventpos = 25
                    ventdesc()
                elif ventpos == 14:
                    ventpos = 13
                    ventdesc()
                elif ventpos == 15:
                    ventpos = 14
                    ventdesc()
                elif ventpos == 17:
                    ventpos = 28
                    ventdesc()
                elif ventpos == 19:
                    ventpos = 18
                    ventdesc()
                elif ventpos == 21:
                    ventpos = 22
                    ventdesc()
                elif ventpos == 22:
                    ventpos = 26
                    ventdesc()
                elif ventpos == 24:
                    ventpos = 23
                    ventdesc()
                elif ventpos == 26:
                    ventpos = 27
                    ventdesc()
                elif ventpos == 28:
                    ventpos = 4
                    ventdesc()
            elif ventDirection == 1:
                if ventpos == 0:
                    ventpos = 1
                    ventdesc()
                elif ventpos == 1:
                    ventpos = 13
                    ventdesc()
                elif ventpos == 3:
                    ventpos = 2
                    ventdesc()
                elif ventpos == 4:
                    ventpos = 3
                    ventdesc()
                elif ventpos == 5:
                    ventpos = 4
                    ventdesc()
                elif ventpos == 6:
                    ventpos = 5
                    ventdesc()
                elif ventpos == 7:
                    ventpos = 6
                    ventdesc()
                elif ventpos == 9:
                    ventpos = 0
                    ventdesc()
                elif ventpos == 10:
                    ventpos = 11
                    ventdesc()
                elif ventpos == 11:
                    ventpos = 12
                    ventdesc()
                elif ventpos == 16:
                    ventpos = 15
                    ventdesc()
                elif ventpos == 17:
                    ventpos = 16
                    ventdesc()
                elif ventpos == 18:
                    ventpos = 17
                    ventdesc()
                elif ventpos == 20:
                    ventpos = 19
                    ventdesc()
                elif ventpos == 21:
                    ventpos = 20
                    ventdesc()
                elif ventpos == 22:
                    ventpos = 6
                    ventdesc()
                elif ventpos == 23:
                    ventpos = 22
                    ventdesc()
            elif ventDirection == 2:
                if ventpos == 1:
                    ventpos = 2
                    ventdesc()
                elif ventpos == 4:
                    ventpos = 28
                    ventdesc()
                elif ventpos == 9:
                    ventpos = 10
                    ventdesc()
                elif ventpos == 13:
                    ventpos = 14
                    ventdesc()
                elif ventpos == 14:
                    ventpos = 15
                    ventdesc()
                elif ventpos == 18:
                    ventpos = 19
                    ventdesc()
                elif ventpos == 22:
                    ventpos = 21
                    ventdesc()
                elif ventpos == 23:
                    ventpos = 24
                    ventdesc()
                elif ventpos == 25:
                    ventpos = 13
                    ventdesc()
                elif ventpos == 26:
                    ventpos = 22
                    ventdesc()
                elif ventpos == 27:
                    ventpos = 26
                    ventdesc()
                elif ventpos == 28:
                    ventpos = 17
                    ventdesc()
            elif ventDirection == 3:
                if ventpos == 0:
                    ventpos = 9
                    ventdesc()
                elif ventpos == 1:
                    ventpos = 0
                    ventdesc()
                elif ventpos == 2:
                    ventpos = 3
                    ventdesc()
                elif ventpos == 3:
                    ventpos = 4
                    ventdesc()
                elif ventpos == 4:
                    ventpos = 5
                    ventdesc()
                elif ventpos == 5:
                    ventpos = 6
                    ventdesc()
                elif ventpos == 6:
                    ventpos = 22
                    ventdesc()
                elif ventpos == 8:
                    ventpos = 7
                    ventdesc()
                elif ventpos == 11:
                    ventpos = 10
                    ventdesc()
                elif ventpos == 12:
                    ventpos = 11
                    ventdesc()
                elif ventpos == 13:
                    ventpos = 1
                    ventdesc()
                elif ventpos == 15:
                    ventpos = 16
                    ventdesc()
                elif ventpos == 16:
                    ventpos = 17
                    ventdesc()
                elif ventpos == 17:
                    ventpos = 18
                    ventdesc()
                elif ventpos == 19:
                    ventpos = 20
                    ventdesc()
                elif ventpos == 20:
                    ventpos = 21
                    ventdesc()
                elif ventpos == 22:
                    ventpos = 23
                    ventdesc()
                
# the unholy and devilish and evil while loops
# Title screen
retry()
print("""\033[1;32m
           88 88                         
           88 \"\"                         
           88                            
,adPPYYba, 88 88  ,adPPYba, 8b,dPPYba,   
\"\"     `Y8 88 88 a8P_____88 88P'   `"8a  
,adPPPPP88 88 88 8PP\"\"\"\"\"\"\" 88       88  
88,    ,88 88 88 "8b,   ,aa 88       88  
`\"8bbdP\"Y8 88 88  `\"Ybbd8\"\' 88       88  \033[0m\n\n\n\n\n\n\n\nStart Game? Y/N""")

while plypos == 0:
    ply = input('> ').lower()
    if ply == 'y' or ply == 'yes':
        plypos = 1
        print("Instructions:\nComplete the game using any method necessary. Use cardinal directions. type 'Think' or 'Hint' for a hint.\nGood luck.\n")
        print("There is a door here. You are facing north.")
    elif ply == 'n' or ply == 'no':
        print("Ok? Dunno why you decided to show up then. I mean, like, we spent a long while programming this game. It's got tons of routes and options for you to do. It's a pretty good game if I say so myself. But I guess if you don't want to play that's... alright. Like yeah, who cares about alien? I surely, definitly, definitivly, absoulutly do not care about this wonderful creation that I made. You, on the other hand, absoulutly do care about this game considering you are either reading this via the source code or through Python idle and are taking your time to read all of this. But yeah, sure, leave. It's not like I wanted you to be here anyway.")
        quit()
    elif ply == 'break' or ply == 'attack' or ply == 'punch' or ply == 'fight':
        plypos = 1
        print("With a fiery mind, you start the game with the mindset of dealing more damage.")
        print("Instructions:\nComplete the game using any method necessary. Use cardinal directions. type 'Think' or 'Hint' for a hint.\nGood luck.\n")
        print("There is a door here. You are facing north.")
        plyatckDEFAULT += 1
        plyatck = plyatckDEFAULT
    elif ply == 'defend' or ply == 'block' or ply == 'coward':
        plypos = 1
        print("With a strategic mind, you decide to start the game with the mindset of taking as little damage as possible.")
        print("Instructions:\nComplete the game using any method necessary. Use cardinal directions. type 'Think' or 'Hint' for a hint.\nGood luck.\n")
        print("There is a door here. You are facing north.")
        plydefenseDEFAULT += 1
        plydefense = plydefenseDEFAULT
    elif ply == 'weak' or ply == 'hard' or ply == 'hard mode' or ply == 'challenge':
        plypos = 1
        print("You decide to activate hard mode. You only have 1 attack from now on.")
        print("Instructions:\nComplete the game using any method necessary. Use cardinal directions. type 'Think' or 'Hint' for a hint.\nGood luck.\n")
        print("There is a door here. You are facing north.")
        plyatckDEFAULT += -4
        plyatck = plyatckDEFAULT
    else:
        print('That isn\'t an option. type \'Y\' for Yes and \'N\' for No')

# area 1 (unbroken door)
while plypos == 1 and doorbroken == False and plydead == False:
    
    ply = input('> ').lower()

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
        print('You took the stool.\n\033[1;33mSTOOL added into your INVENTORY.\033[0m')
        inventory.append('Stool')
        tookstool = True
        if firstitem == False:
            print("You can equip items by typing EQUIP ITEM")
            firstitem = True

    elif ply == 'take stool' and 'Stool' in inventory:
        print('Amazingly, you already took the stool.')

    elif ply == 'look south' or ply == 'look back':
        print("You aren't an owl, are you?")

    elif ply == 'open door':
        print("You jiggle the handle. The door is locked.")

    elif ply == 'check door':
        print("It's just a simple, fragile door.")

    elif ply == 'eat door':
        print("You put your mouth on the door. The door is too big to be eaten in one sitting.")

    elif ply == 'close door':
        print("You close the closed door.")

    elif ply == 'unlock door':
        print("You try to unlock the door. Your finger does not fit through the lock.")
    
    elif ply == 'take door':
        print("You attempt to take the door. It's lodged into the door frame")
    
    elif ply == 'break door':
        print("\033[1;31mYou broke down the door.\033[0m There is nothing beyond the frame but a brick wall. \nThere is no longer a door here")
        doorbroken = True

    elif ply == 'fight door':
        print("You prepare for battle against a \033[1;35mtrue door.")
        plyspecial()
        battlestart()
        print(f"\033[1;32mYour health is: {plyhealth}. \033[1;35mDOOR's health is ???")
        miscfight = input("\033[0mWhat will you do? \n> ").lower()
        if miscfight == 'attack' or miscfight == 'kill' or miscfight == 'punch' or miscfight == 'fight door':
            print(f"\033[1;31mYou attack the door with brute force for {plyatck} damage. It instantly breaks down.\033[0m \nThere is only a brick wall beyond the frame.\nThere is no longer a door here")
            doorbroken = True
            if plyatck >= 6:
                plyatck += 1
                plyatckDEFAULT += 1
                print("You felt a tad bit stronger.")
        elif miscfight == 'defend':
            print("\033[1;34mYou defended.\033[0m The door doesn't do anything. You stop fighting it.")
        elif miscfight == 'charge':
            print("\033[1;32mYou charged.\033[0m The door doesn't do anything. Perhaps it's best you save your energy for something else.")
        else:
            print("You can't think of how to perform that on a door. You disengage in combat.")

    elif ply == 'kill door':
        print("\033[1;31mYou brutally attack the door until it's nothing but rubble. \nYour hand hurts, but there is now a brick wall where the door was.\n\033[0mThere is no longer a door here")
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

    elif ply == 'what':
        print("huh?")
        
    else:
        print("Your thoughts seem incomprehensible.")
        
# area 1 (broken door)
while plypos == 1 and doorbroken == True and plydead == False:
    ply = input('> ').lower()

    if globalcommands():
        pass

    elif ply == "check door":
        print("Nothing but splinters.")

    elif ply == 'take door' and tookSplinter == False:
        print("You cannot take the door as it is broken. You take splinters in remembrance of the broken door.\n\033[1;33mSPLINTERS added into your INVENTORY\033[0m")
        inventory.append('Splinters')
        tookSplinter = True
        if firstitem == False:
            print("You can equip items by typing EQUIP ITEM")
            firstitem = True
        #  ,̶'̶ ̶ ̶,̶ ̶|̶ ̶,̶'̶ ̶_̶'̶ 

    elif ply == 'take splinters' and tookSplinter == False:
        print("You take splinters in remembrance of the broken door.\n\033[1;33mSPLINTERS added into your INVENTORY\033[0m")
        inventory.append('Splinters')
        tookSplinter = True
        if firstitem == False:
            print("You can equip items by typing EQUIP ITEM")
            firstitem = True

    elif (ply == 'take door' or ply == 'take splinters' or ply == 'take pretend splinters') and tookSplinter == True and pretendLMAO == False:
        print("You already took the splinters. You pretended to take more splinters.\n\033[1;33mPRETEND SPLINTERS added into your INVENTORY\033[0m")
        inventory.append('Pretend Splinters')
        pretendLMAO = True

    elif (ply == 'take door' or ply == 'take splinters' or ply == 'take pretend splinters') and tookSplinter == True and pretendLMAO == True:
        print("You already took the pretend splinters. You cannot fathom about what comes after pretend splinters.")

    elif ply == 'check wall' or ply == 'check brick wall':
        print('A red brick wall. The surface ripples when you touch it.')

    elif (ply == 'take wall' or ply == 'take brick wall') and ouch != 3 and brokenhand == False:
        print('You attempt to take the wall. Your hand passes right through the wall.\nOnce you took out your hand, it felt injured.')
        ouch += 1

    elif (ply == 'take wall' or ply == 'take brick wall') and ouch == 3 and brokenhand == False:
        print('You attempt to take the wall. Your hand passes right through the wall.\nOnce you took out your hand, if felt broken.\n\033[1;31mYou can\'t use your hand anymore.\033[0m')
        brokenhand = True
        plyatck -= 1
        plyatckDEFAULT -= 1

    elif (ply == 'take wall' or ply == 'take brick wall') and brokenhand == True:
        print("You attempt to take the wall. You have a bad reaction. You stop your attempt to take the wall.")

    elif ply == 'eat wall' or ply == 'eat brick wall':
        print('You sink your teeth into the wall. Suprisingly, your teeth glide through it. Tastes like water.')

    elif (ply == 'break wall' or ply == 'break brick wall') and ouch != 3 and brokenhand == False:
        print('You violently punch the wall. Your hand passes right through the wall.\nOnce you took out your hand, it felt injured.')
        ouch += 1

    elif (ply == 'break wall' or ply == 'break brick wall') and ouch == 3 and brokenhand == False:
        print('You violently punch the wall. Your hand passes right through the wall.\nOnce you took out your hand, if felt broken.\n\033[1;31mYou can\'t use your hand anymore.\033[0m')
        brokenhand = True
        plyatck -= 1
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
        print('You took the stool.\n\033[1;33mSTOOL added into your INVENTORY.\033[0m')
        inventory.append('Stool')
        tookstool = True
        if firstitem == False:
            print("You can equip items by typing EQUIP ITEM")
            firstitem = True

    elif ply == 'take stool' and 'Stool' in inventory:
        print('Amazingly, you already took the stool.')

    elif ply == "look south":
        print("You aren't an owl, are you?")
    
    elif ply == 'open door':
        print("You can't open splinters.")

    elif ply == 'break door':
        print("It's already broken.")

    elif ply == 'go north':
        print('You pass through brick like water. You choked to death. This is the end.\n\033[1;31mGame Over\n\n\n\n  \033[0mor is it?\n\033[1;31mThere is no here.')
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
        print(f"You prepare for battle against a \033[1;35mbrick wall.")
        plyspecial()
        battlestart()
        print(f"\033[1;32mYour health is: {plyhealth}. \033[1;35mWALL's health is 0")
        miscfight = input("\033[0mWhat will you do? \n> ").lower()
        if (miscfight == 'attack' or miscfight == 'kill' or miscfight == 'punch' or miscfight == 'fight wall' or miscfight == 'fight brick wall') and brokenhand == False and plyatck < 7:
            print("\033[1;31mYou attempt to attack the wall.\033[0m Your hand passes right through the wall.")
            if ouch != 3:
                print("Once you pulled out your hand, it felt injured.")
                ouch += 1
            elif ouch == 3:
                print("Once you pulled out your hand, if felt broken.\n\033[1;31mYou cannot use your hand anymore.\033[0m")
                brokenhand = True
                plyatck -= 1
                plyatckDEFAULT -= 1
        elif (miscfight == 'attack' or miscfight == 'kill' or miscfight == 'punch' or miscfight == 'fight wall' or miscfight == 'fight brick wall') and brokenhand == False and plyatck >= 7:
            print(f"\033[1;31mWith full force, you manage to deal {plyatck * 2} damage to the wall.\033[0m\nYou end up passing straight through the wall and suffocating. \n\033[1;31mGame Over\n\n\n\n  \033[0mor is it?\n\033[1;31mThere is no here.")
            plypos = 2
            plyatck += 1
            plyatckDEFAULT += 1
        elif (miscfight == 'attack' or miscfight == 'kill' or miscfight == 'punch' or miscfight == 'fight wall' or miscfight == 'fight brick wall') and brokenhand == True:
            print("\033[1;31mYou try to attack the wall. \033[0mYour hand doesn't move. You cannot fight it in this state.")
        elif miscfight == 'defend':
            print("\033[1;34mYou defended.\033[0m The wall slightly ripples. You stop fighting it.")
        elif miscfight == 'charge':
            print("\033[1;32mYou charged.\033[0m The wall violently ripples. You look confused and stop fighting.")
        elif ply == 'quit':
            quit()
        else:
            print("You can't think of how to perform that on a wall. You disengage in combat.")
    
    else:
        print("Your thoughts seem incomprehensible.")

# area 2 (void)
while plypos == 2 and plydead == False:

    ply = input('> ').lower().split()

    if ('break' in ply and brokenhand == False) or ('kill' in ply and 'myself' in ply):
        print('You broke. \033[1;33mYou lost Nothing.\n\n\n\n\n\n\n\n\033[0mYou wake up to find yourself in a massive glass case in what appears to be a museum.\nWhat now?')
        plypos = 3
        plychoke = 5
        inventory.remove('Nothing')

    elif 'check' in ply:
        print('You checked... something. It gave the impression of broken glass.')

    elif 'eat' in ply or 'breath' in ply:
        print('As soon as you open your mouth, you feel the air rush out. Bad idea.')
        if plychoke > 1:
            plychoke -= 2
        else:
            plychoke -= 1
        if plychoke <= 3 and plychoke != 0:
            print(f'\033[1;35mYou have {plychoke} actions left.\033[1;31m')

    elif 'fight' in ply and plyatck >= 8:
        print("You decide to use all of your power to fight the void. You encounter VOID \nBATTLE START!")
        voidenemy()
        plyspecial()
        battlestart()
        
        plychoke = 8
        
    elif 'inventory' in ply:
        for x in inventory:
            print(x)

    elif 'break' in ply and brokenhand == True:
        print('You wish you could.')
        plychoke -= 1
        if plychoke <= 3 and plychoke != 0:
            print(f'\033[1;35mYou have {plychoke} actions left.\033[1;31m')

    elif ('think' in ply or 'check' in ply or 'hint' in ply) and brokenhand == False:
        print('You tried to think. You thought about breaking.')

    elif ('think' in ply or 'check' in ply or 'hint' in ply) and brokenhand == True:
        print('You tried to think. You thought about doors.')

    elif ply == 'quit':
        quit()

    elif 'open' in ply:
        print('You opened. You felt a change.\n\n\n\n\n\n\n\n\033[0mYou wake up to find yourself in a massive glass case in what appears to be a museum.\nWhat now?')
        plypos = 3
        plychoke = 5

    else:
        plychoke -= 1
        print('There isn\'t a way to do that. You feel your lungs lose air.')
        if plychoke <= 3 and plychoke != 0:
            print(f'\033[1;35mYou have {plychoke} actions left.\033[1;31m')

    if plychoke <= 0:
        print("You somehow managed to choke to death for a second time. There aren't third chances in this world.\n\nGame over.\033[0m")
        plydead = True

    if plychoke == 8:
        while plyhealth > 0 and enemyhealth > 0:
            if plyturn == True and plyhealth > 0:
                plymove()
                plyturn = False
                pass
                if plyerror == True:
                    if ply != 'special':
                        print("That is not a move that you have access to. Try again.")
                    plymove()
                    pass
                    if plyerror == True:
                        if ply != 'special':
                            print("You end up freezing in place as you forget what you can do in battle.")
                        pass
                if enemyhealth <= 0 and plyhealth > 0:
                    if weapon == 'Nothing':
                        print("You overcome the VOID and manage to destory it with your bare hands.")
                    else:
                        print(f"You overcome the VOID and manage to destory it with your {weapon}.")
                    print('\033[0mYou wake up to find yourself in a massive glass case in what appears to be a museum.\n\033[1;33mYou end up finding a SHARD in your inventory.\n\033[0mWhat now?')
                    inventory.append('Shard')
                    plyturn = True
                    plypos = 3
            if plyturn == False and plyhealth > 0 and enemyhealth > 0:
                enemymove()
                plyturn = True
                pass
                if plyhealth <= 0:
                    print("The VOID manages to choke you out as you lose all of your breath. You collapse and lose all conscience.\n\n\033[1;31mGame Over!\033[0m")
                    plydead = True

# area 3 (museum without stool)
while plypos == 3 and tookstool == False and plydead == False and dinodead == False:
    ply = input('> ').lower()

    if globalcommands():
        pass

    elif ply == "look north":
        print("Through the glass case, you see a museum. The glass is too foggy to make out any details.")

    elif ply == 'break glass' or ply == 'break window' or ply == 'break case':
        if weapon == 'Nothing':
            if brokenhand == False:
                print('You bash your fist against the glass. It rebounds into your own face. \033[1;31mYou take 1 Damage.\033[0m')
                ouch += 1
                plyhealth -= 1
                if plyhealth == 0:
                    print("You somehow manage to deal the final blow to yourself as you faint to the floor, unconscience.\n\n\n\n\033[1;31mGAME OVER\033[0m")
                    plydead = True
                if ouch == 3:
                    print('Your hand has given up on you.\n\033[1;31mYou can\'t use your hand anymore.\033[0m')
                    brokenhand = True
                    plyatck -= 1
                    plyatckDEFAULT -= 1
                else:
                    print('Your hand hurts more than usual.')
            else:
                print("You attempt to break the glass with your fist. It doesn't want to move.")
        elif weapon == 'Splinters':
            print("You prick the splinters into the glass. It unfortunatly does not budge.")
        elif weapon == 'Pretend Splinters':
            print("You pretend to prick splinters into the glass. Nothing happens.")
        elif weapon == 'Crowbar':
            print("You attempt to break the glass with the crowbar. You only hear the sound of tapping glass.")
        elif weapon == 'Brick':
            print("You throw the brick at the glass. It splats onto the glass wall, not leaving any dents.")
        elif weapon == 'Shard':
            print("You manage to scrape the glass. It forms a questionable symbol resembling a slashable wall.")
        elif weapon == 'Sword':
            print("""You decimate the glass wall with the sword. As a matter of fact, you decimated the entire glass case.
After the glass collapsed, you notice your surroundings have completly changed. You are surrounded entirely by glass.
Strangely, you feel healthier than usual.
You aren\'t where you were before.""")
            plypos = 12
            plyhealthDEFAULT += 2
            plyhealth = plyhealthDEFAULT
        else:
            print("You look at the glass. You feel as if you have broken the game somehow.")

    elif ply == 'eat glass':
        print("You press your mouth against the glass and attempt to take a bite. Unfortunately, the surface is too smooth and your teeth harmlessly slide against it.")

    elif ply == 'check glass':
        glasscheck()

    elif ply == "check dinosaur" and dinoseen == False:
        print("What dinosaur?")

    elif (ply == 'attack dinosaur' or ply == 'fight dinosaur') and dinoseen == False:
        print("Your prehistoric rage goes unquenched, as you haven't seen any dinosaurs so far.")

    elif (ply == 'attack dinosaur' or ply == 'fight dinosaur') and dinoseen == True:
        print("You initiate a battle with \033[1;35mthe dinosaur.\033[0m \nBATTLE START!")
        plasticDino()
        plyspecial()
        battlestart()
        plypos = 4

    elif ply == "check dinosaur" and dinoseen == True:
        print("You go to check the dinosaur. It reacts. \nBATTLE START!")
        plasticDino()
        plyspecial()
        battlestart()
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
        print('Without looking first, you casually walk straight into the jaws of a prehistoric predator. \n\033[1;31mGame over.\033[0m')
        plydead = True

    elif ply == 'check vent':
        print("You check the vent. You notice a slight crack that can be budged.")

    elif ply == 'open vent':
        print('You attempt to open the vent. You cannot achieve this as your fingers are not thin and strong enough for this task.')

    elif ply == 'go west' and dinoseen == True:
        print('Wanting to investigate the dinosaur, you walk west. The dinosaur reacts. \nBATTLE START!')
        plasticDino()
        plyspecial()
        battlestart()
        plypos = 4

    else:
        print("Your thoughts seem incomprehensible.")

# area 4 (battle against a true dino)
while plypos == 4 and plydead == False:

    if plyturn == True and plyhealth > 0:
        plymove()
        plyturn = False
        pass
        if plyerror == True:
            print("That is not a move that you have access to. Try again.")
            plymove()
            pass
            if plyerror == True:
                print("You end up freezing in place as you forget what you can do in battle.")
                pass
        if enemyhealth <= 0 and plyhealth > 0:
            dinodead = True
            print("You won! \nThe plastic dinosaur disappears into dust. It leaves a very large tooth behind.")
            if weapon == 'Shard':
                print("\033[1;33mYour shard transformed into a sword. \033[0mWhat now?\n")
                weapon = Sword
                plyatck += 2
                inventory.append("Sword")
                inventory.remove("Shard")
            else:
                print("What now?\n")
            plypos = 3
            plyturn = True

    if plyturn == False and plyhealth > 0 and enemyhealth > 0:
        enemymove()
        plyturn = True
        pass
        if plyhealth <= 0:
            print("The Plastic Dinosaur brutally tears you apart as you faint to the ground.\n\n\033[1;31mGame Over!\033[0m")
            plydead = True

# area 3 (haha that dino is dead)
while plypos == 3 and tookstool == False and plydead == False and dinodead == True:

    ply = input('> ').lower()

    if globalcommands():
        pass

    elif ply == "look north":
        print("Through the glass case, you see a museum. The glass is too foggy to make out any details.")

    elif ply == 'break glass' or ply == 'break window' or ply == 'break case':
        if weapon == 'Nothing':
            if brokenhand == False:
                print('You bash your fist against the glass. It rebounds into your own face. \033[1;31mYou take 1 Damage.\033[0m')
                ouch += 1
                plyhealth -= 1
                if plyhealth == 0:
                    print("You somehow manage to deal the final blow to yourself as you faint to the floor, unconscience.\n\n\n\n\033[1;31mGAME OVER\033[0m")
                    plydead = True
                if ouch == 3:
                    print('Your hand has given up on you.\n\033[1;31mYou can\'t use your hand anymore.\033[0m')
                    brokenhand = True
                    plyatck -= 1
                    plyatckDEFAULT -= 1
                else:
                    print('Your hand hurts more than usual.')
            else:
                print("You attempt to break the glass with your fist. It doesn't want to move.")
        elif weapon == 'Splinters':
            print("You prick the splinters into the glass. It unfortunatly does not budge.")
        elif weapon == 'Pretend Splinters':
            print("You pretend to prick splinters into the glass. Nothing happens.")
        elif weapon == 'Crowbar':
            print("You attempt to break the glass with the crowbar. You only hear the sound of tapping glass.")
        elif weapon == 'Brick':
            print("You throw the brick at the glass. It splats onto the glass wall, not leaving any dents.")
        elif weapon == 'Shard':
            print("You manage to scrape the glass. It forms a questionable symbol resembling a slashable wall.")
        elif weapon == 'Sword':
            print("""You decimate the glass wall with the sword. As a matter of fact, you decimated the entire glass case.
After the glass collapsed, you notice your surroundings have completly changed. You are surrounded entirely by glass.
Strangely, you feel healthier than usual.
You aren\'t where you were before.""")
            plypos = 12
            plyhealthDEFAULT += 2
            plyhealth = plyhealthDEFAULT
        else:
            print("You look at the glass. You feel as if you have broken the game somehow.")

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
        if 'Tooth' not in inventory:
            print("A particularly large tooth lays on the dust.")

    elif ply == 'attack dinosaur' or ply == 'fight dinosaur':
        print("\033[1;31mYou square up against the dinosaur's ashes.\033[0m\nUnfortuantly, it doesn't engage in combat with you.\nYou stop fighting.")

    elif (ply == 'take tooth' or ply == 'take large tooth') and 'Tooth' not in inventory:
        print("You take the particularly large tooth.\n\033[1;33mTOOTH added to your INVENTORY\033[0m")
        inventory.append('Tooth')
        if firstitem == False:
            print("You can equip items by typing EQUIP ITEM")
            firstitem = True

    elif (ply == 'take tooth' or ply == 'take large tooth') and 'Tooth' in inventory:
        print("You put the tooth back in order to feel the satisfaction of obtaining it again.\n\033[1;33mTOOTH removed from your inventory.\033[0m")
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

    elif ply == 'go west' and 'Tooth' in inventory:
        print('There is a giant pile of presumably microplastics in your way.')

    elif ply == 'go west' and 'Tooth' not in inventory:
        print('There is a giant pile of presumably microplastics in your way. There is a particularly large tooth on top of it.')

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

    ply = input('> ').lower()

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
        if plywallBroken == True:
            print('At least, it used to be.')
    
    elif ply == 'break glass' or ply == 'break window' or ply == 'break case':
        if weapon == 'Nothing':
            if brokenhand == False:
                print('You bash your fist against the glass. It rebounds into your own face. \033[1;31mYou take 1 Damage.\033[0m')
                ouch += 1
                plyhealth -= 1
                if plyhealth == 0:
                    print("You somehow manage to deal the final blow to yourself as you faint to the floor, unconscience.\n\n\n\n\033[1;31mGAME OVER\033[0m")
                    plydead = True
                if ouch == 3:
                    print('Your hand has given up on you.\n\033[1;31mYou can\'t use your hand anymore.\033[0m')
                    brokenhand = True
                    plyatck -= 1
                    plyatckDEFAULT -= 1
                else:
                    print('Your hand hurts more than usual.')
            else:
                print("You attempt to break the glass with your fist. It doesn't want to move.")
        elif weapon == 'Splinters':
            print("You prick the splinters into the glass. It unfortunatly does not budge.")
        elif weapon == 'Pretend Splinters':
            print("You pretend to prick splinters into the glass. Nothing happens.")
        elif weapon == 'Crowbar':
            print("You attempt to break the glass with the crowbar. You only hear the sound of tapping glass.")
        elif weapon == 'Brick':
            print("You throw the brick at the glass. It splats onto the glass wall, not leaving any dents.")
        elif weapon == 'Shard':
            print("You manage to scrape the glass. It forms a questionable symbol resembling a slashable wall.")
        elif weapon == 'Sword':
            print("""You decimate the glass wall with the sword. As a matter of fact, you decimated the entire glass case.
After the glass collapsed, you notice your surroundings have completly changed. You are surrounded entirely by glass.
Strangely, you feel healthier than usual.
You aren\'t where you were before.""")
            plypos = 12
            plyhealthDEFAULT += 2
            plyhealth = plyhealthDEFAULT
        else:
            print("You look at the glass. You feel as if you have broken the game somehow.")
            

    elif ply == 'eat glass':
        print("You press your mouth against the glass and attempt to take a bite. Unfortunately, the surface is too smooth and your teeth harmlessly slide against it.")

    elif ply == "check dinosaur" and dinoseen == True:
        print("A large chunk of plastic in the shape of a dinosaur.")

    elif (ply == 'attack dinosaur' or ply == 'fight dinosaur') and dinoseen == True:
        print("You wished that the dinosaur was alive so you could be responsible for their extinction.")

    elif ply == 'climb dinosaur' and dinoseen == True and 'Stool' in inventory:
        print("You used the stool the climb up onto the plastic dinosaur. You notice a hatch to exit the glass case.")
        plysecondary = input("Exit out? Y/N\n> ").lower()
        if plysecondary == 'y' or plysecondary == 'yes':
            print("""You climb out of the glass case. You find yourself on top of the glass case you were in.
Suddenly, the glass case dissapears from under your feet as you fall to the ground.
You land in a new location that is surrounded by glass.
You feel a little bit healthier than before.
\033[1;33mYou no longer have access to the stool.\033[0m
You are not where you were before.""")
            plypos = 12
            plyhealthDEFAULT += 2
            plyhealth = plyhealthDEFAULT
            inventory.remove('Stool')
            if armor == 'Stool':
                armor = 'Nothing'
                plydefense = plydefenseDEFAULT
        elif plysecondary == 'n' or plysecondary == 'no':
            print("You decide to not climb out yet.\nYou jump back down to the ground.")
        else:
            print("You counldn't comprehend what you meant. You decide to jump back down to the ground.")

    elif ply == 'climb dinosaur' and dinoseen == True and 'Stool' not in inventory:
        print('You attempt to climb the dinosaur. You unfortuantly cannot climb high enough due to your lack of stools.')

    elif ply == 'take dinosaur' and dinoseen == True:
        print('You attempt to take the whole dinosaur. If unfourtnatly is too big to be put in your inventory. You punch it in frustration.')

    elif (ply == "check dinosaur" or ply == "fight dinosaur" or ply == 'attack dinosaur' or ply == "climb dinosaur" or ply == "take dinosaur") and dinoseen == False:
        print("What dinosaur?")

    elif ply == 'look west' and 'Crowbar' in inventory:
        print("Big plastic dinosaur. It looks fake.")

    elif ply == 'take crowbar':
        if tookSplinter == True and 'Crowbar' not in inventory:
            print("You placed the stool down in front of the dinosaur and took the crowbar from its mouth.\n\033[1;33mWhen you step off the stool, it dissovles into dust.\nCROWBAR added into your INVENTORY.\033[0m")
            inventory.append('Crowbar')
            inventory.remove('Stool')
            if armor == 'Stool':
                armor = 'Nothing'
                plydefense = 0
        elif tookSplinter == False and 'Crowbar' not in inventory:
            print("You placed the stool down in front of the dinosaur and took the crowbar from its mouth.\n\033[1;33mWhen you step off the stool, it spontaneously explodes into a pile of splinters.\nCROWBAR added into your INVENTORY.\033[0m")
            inventory.append('Crowbar')
            inventory.remove('Stool')
            stoolExplode = True
            if armor == 'Stool':
                armor = 'Nothing'
                plydefense = 0
        elif 'Crowbar' in inventory:
            print('You already have it.')

    elif ply == 'take stool' and stoolExplode == True and tookSplinter == False:
        print('The stool is sadly dead. You grab a handful of splinters to honor the late stool.\n\033[1;33mSPLINTERS added into your INVENTORY.\033[0m')
        inventory.append('Splinters')
        tookSplinter = True

    elif ply == 'take stool' and stoolExplode == True and tookSplinter == True:
        print('You already took the splinters. You can\'t really think of anything else to do.')
        inventory.append('Splinters')
        tookSplinter = True

    elif ply == 'take stool' and stoolExplode == False and 'Stool' not in inventory:
        print('You salute the dust of the stool for it\'s hard work.')
        inventory.append('Splinters')
        tookSplinter = True

    elif ply == 'look south':
        print("Fake grass. There is an air vent embedded in the ground.")

    elif ply == 'go north':
        print("You smack your face into the glass.")

    elif ply == 'go south':
        print('This room is too small to meaningfully move in any direction.')

    elif ply == 'go east' and plywallBroken == False:
        print('This room is too small to meaningfully move in any direction.')

    elif ply == 'go east' and plywallBroken == True:
        print('Behind the wall, you find a house. It\'s reminiscent of your old childhood home, but you\'ve definitely never been here before.\nThe museum fades from your peripheral as you walk in.\nYou are facing north towards the front door.')
        plypos = 18

    elif ply == 'go west':
        print('It appears there is a giant plastic dinosaur in the way.')
        dinoseen = True

    elif ply == 'open vent' and 'Crowbar' in inventory and ventopen == False:
        print("You pry open the vent with the crowbar. It's too small to climb inside, but there is a red brick inside.")
        ventopen = True

    elif ply == 'take brick' or ply == 'take red brick':
        if ventopen == True and 'Brick' not in inventory:
            print('You took the brick. As you hold it in your hand, it feels more liquid than solid. Yet, it\'s still solid enough to break something.\n\033[1;33mBRICK added into your INVENTORY.\033[0m')
            inventory.append('Brick')
        elif ventopen == True and 'Brick' in inventory:
            print('You already took it.')
        else:
            print('What brick?')

    elif ply == 'open vent' and 'Crowbar' in inventory and ventopen == True:
        print("You close the vent only to immediatly open it again.")

    elif ply == 'open vent' and 'Crowbar' not in inventory:
        print('You try to pull open the vent with your bare hands. It dosen\'t work.')

    elif ply == 'check wall':
        print('A thin plywood wall painted beige. You could probably break it with something heavy enough.')

    elif ply == 'break wall' and plywallBroken == False:
        plysecondary = input('With what?\n> ').lower()
        item_to_equip = plysecondary[0:].strip().title()
        if plysecondary == 'brick' and 'Brick' in inventory:
            print('You throw the brick at the wall. After the brick impacts, the wall is seemingly completely decimated.')
            plywallBroken = True
        elif plysecondary == 'brick' and 'Brick' not in inventory:
            print('You don\'t have one of those')
        elif (plysecondary != 'brick' or plysecondary != 'crowbar' or plysecondary != 'shard') and item_to_equip in inventory:
            print(f'You take out the {plysecondary}. You don\'t know what to do with it. You put it away.')
        elif plysecondary == 'hand' or plysecondary == 'head' or plysecondary == 'me' or plysecondary == 'foot':
            print('You would prefer not to risk breaking any bones. Maybe try using an item instead.')
        elif plysecondary == 'think' and 'Brick' not in inventory or plysecondary == 'check' and 'Brick' not in inventory or plysecondary == 'hint' and 'Brick' not in inventory:
            print('You tried to think. You feel as if what you need to break the wall is somewhere around here.')
        elif plysecondary == 'think' and 'Brick' in inventory or plysecondary == 'check' and 'Brick' in inventory or plysecondary == 'hint' and 'Brick' in inventory:
            print('You tried to think. You feel as if what you need to break the wall is somewhere in your \033[1;33mINVENTORY.\033[0m')
        elif plysecondary == 'crowbar' and 'Crowbar' not in inventory:
            print('You currently don\'t have a crowbar. Perhaps you can find one nearby?')
        elif plysecondary == 'crowbar' and 'Crowbar' in inventory:
            print('You thought about breaking the wall with the crowbar. You\'d perfer to not damage it just yet.')
        elif plysecondary == 'you' or plysecondary == 'them':
            print('Unfortuantly, there isn\'t anyone else in the room that you can refer to.')
        elif plysecondary == 'shard' and 'Shard' in inventory:
            print('You manage to tear down the wall with the Shard instantly.')
            plywallBroken = True
        else:
            print('You know already that that wouldn\'t work.')

    elif ply == 'fight wall' and weapon == 'Shard' and plywallBroken == False:
        print(f"You decide to square up against the wall with your shard. \033[1;31mYou immediatly attack it to deal {plyatck * 3} damage.\033[0m\nThe wall breaks down instantly.\033[1;33mThe Shard transformed into a SWORD.\033[0m")
        inventory.remove('Shard')
        inventory.append('Sword')
        weapon = 'Sword'
        plyatck += 2
        plywallBroken = True

    elif (ply == 'break wall' or ply == 'fight wall') and plywallBroken == True:
        print("The wall has already been broken. There is no point in trying to destroy it again.")

    else:
        print("Your thoughts seem incomprehensible.")

# Area 5 (gregory, have you heard of a)
while plypos == 5 and plydead == False:

    # vent descriptions go like this: 'To your left, ___________.\nTo your right, ___________.\nDirectly ahead of you is _________________.' 
    vent_descriptions = []
    vent_walls = []
    
    vent_start = {
        0: 'To your left, there is a path with three different exits.\nTo your right, there is a path ending in a left turn.\nDirectly ahead of you is a wall.', 
        1: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a path ending in a left turn.', 
        2: 'To your left, there is a path ending in a left turn.\nTo your right, there is a path with three different exits.\nDirectly ahead of you is a wall.', 
        3: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a path with three different exits.'
    }
    
    vent_1 = {
        0: 'To your left, there is a path ending in an intersection.\nTo your right, there is a long path ending in a left turn.\nDirectly ahead of you is a path that ends in a right turn.',
        1: 'To your left, there is a path that ends in a right turn.\nTo your right, there is a wall.\nDirectly ahead of you is a long path ending in a left turn.', 
        2: 'To your left, there is a long path ending in a left turn.\nTo your right, there is a path ending in an intersection.\nDirectly ahead of you is a wall.', 
        3: 'To your left, there is a wall.\nTo your right, there is a path that ends in a right turn.\nDirectly ahead of you is a path ending in an intersection.'
    }
    
    vent_2 = {
        0: 'To your left, there is a wall.\nTo your right, there is a very long stretch with several turns.\nDirectly ahead of you is a wall.',
        1: 'To your left, there is a wall.\nTo your right, there is a path ending in an intersection.\nDirectly ahead of you is a very long stretch with several turns.', 
        2: 'To your left, there is a very long stretch with several turns.\nTo your right, there is a wall.\nDirectly ahead of you is a path ending in an intersection.', 
        3: 'To your left, there is a path ending in an intersection.\nTo your right, there is a wall.\nDirectly ahead of you is a wall.'
    }
    
    vent_3 = {
        0: 'To your left, there is a path ending in a right turn.\nTo your right, there is a long, straight path with four different exits.\nDirectly ahead of you is a wall.',
        1: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a long, straight path with four different exits.', 
        2: 'To your left, there is a long, straight path with four different exits.\nTo your right, there is a path ending in a right turn.\nDirectly ahead of you is a wall.', 
        3: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a path ending in a right turn.'
    }
    
    vent_4 = {
        0: 'To your left, there is a long path ending in a right turn.\nTo your right, there is a long, straight path with three different exits.\nDirectly ahead of you is a path ending in an intersection.', 
        1: 'To your left, there is a path ending in an intersection.\nTo your right, there is a wall.\nDirectly ahead of you is a long, straight path with three different exits.', 
        2: 'To your left, there is a long, straight path with three different exits.\nTo your right, there is a long path ending in a right turn.\nDirectly ahead of you is a wall.', 
        3: 'To your left, there is a wall.\nTo your right, there is a long path leading to an intersection.\nDirectly ahead of you is a long path ending in a right turn.'
    }
    
    vent_5 = {
        0: 'To your left, there is a long straight path with three different exits.\nTo your right, there is a long path with two different exits.\nDirectly ahead of you is a wall.', 
        1: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a long straight path with three different exits.', 
        2: 'To your left, there is a long path with two different exits.\nTo your right, there is a long straight path with three different exits.\nDirectly ahead of you is a wall.', 
        3: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a long path with two different exits.'
    }
    
    vent_6 = {
        0: 'To your left, there is a long, straight path with two different exits.\nTo your right, there is a path with three different exits.\nDirectly ahead of you is a wall.\nSomething seems off about here.', 
        1: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a path with three different exits.\nSomething seems off about here.', 
        2: 'To your left, there is a path with three different exits.\nTo your right, there is a long, straight path with two different exits.\nDirectly ahead of you is a wall.\nSomething seems off about here.', 
        3: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a long, straight path with two different exits.\nSomething seems off about here.'
    }
    
    vent_7 = {
        0: 'To your left, you see a light.\nTo your right, there is a wall.\nDirectly ahead of you is a wall.', 
        1: 'You are surrounded by walls. There is a bright light shining behind you.', 
        2: 'To your left, there is a wall.\nTo your right, there is a light.\nDirectly ahead of you is a wall.', 
        3: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a light.'
    }
    
    vent_8 = {
        0: 'To your left, there is a blinding light that singes your retinas.\nTo your right, there is a dead end.\nDirectly ahead of you is a wall.',
        1: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a dead end.', 
        2: 'To your left, there is a dead end.\nTo your right, there is a blinding light that singes your retinas.\nDirectly ahead of you is a wall.', 
        3: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a blinding light that singes your retinas.'
    }
    
    vent_9 = {
        0: 'To your left, there is a long path with three exits.\nTo your right, there is a wall.\nDirectly ahead of you is a path ending in a left turn.',
        1: 'To your left, there is a path ending in a left turn.\nTo your right, there is a wall.\nDirectly ahead of you is a wall.', 
        2: 'To your left, there is a wall.\nTo your right, there is a long path with three exits.\nDirectly ahead of you is a wall.', 
        3: 'To your left, there is a wall.\nTo your right, there is a path ending in a left turn.\nDirectly ahead of you is a long path with three exits.'
    }
    
    vent_10 = {
        0: 'To your left, there is a long path ending in a dead end.\nTo your right, there is a wall.\nDirectly ahead of you is a wall.',
        1: 'To your left, there is a wall.\nTo your right, there is a path ending in a right turn.\nDirectly ahead of you is a wall.', 
        2: 'To your left, there is a wall.\nTo your right, there is a long path ending in a dead end.\nDirectly ahead of you is a path ending in a right turn.', 
        3: 'To your left, there is a path ending in a right turn.\nTo your right, there is a wall.\nDirectly ahead of you is a long path ending in a dead end.'
    }
    
    vent_11 = {
        0: 'To your left, there is a path ending in a dead end.\nTo your right, there is a path ending in a right turn.\nDirectly ahead of you is a wall.',
        1: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a path ending in a right turn.', 
        2: 'To your left, there is a a path ending in a right turn.\nTo your right, there is a path ending in a dead end.\nDirectly ahead of you is a wall.', 
        3: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a path ending in a dead end.'
    }
    
    vent_12 = {
        0: 'To your left, there is a wall.\nTo your right, there is a long path ending in a right turn.\nDirectly ahead of you is a wall.',
        1: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a long path ending in a right turn.', 
        2: 'To your left, there is a long path ending in a right turn.\nTo your right, there is a wall.\nDirectly ahead of you is a wall.', 
        3: 'You are surrounded by walls.'
    }
    
    vent_13 = {
        0: 'To your left, there is a wall.\nTo your right, there is a long path with two different exits.\nDirectly ahead of you is a long path ending in a right turn.',
        1: 'To your left, there is a long path ending in a right turn.\nTo your right, there is a dead end.\nDirectly ahead of you is a long path with two different exits.', 
        2: 'To your left, there is a long path with two different exits.\nTo your right, there is a wall.\nDirectly ahead of you is a dead end.', 
        3: 'To your left, there is a dead end.\nTo your right, there is a long path ending in a right turn.\nDirectly ahead of you is a wall.'
    }
    
    vent_14 = {
        0: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a path ending in a right turn.',
        1: 'To your left, there is a path ending in a right turn.\nTo your right, there is a path with a left turn.\nDirectly ahead of you is a wall.', 
        2: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a path with a left turn.', 
        3: 'To your left, there is a path with a left turn.\nTo your right, there is a path ending in a right turn.\nDirectly ahead of you is a wall.'
    }
    
    vent_15 = {
        0: 'To your left, there is a wall.\nTo your right, there is a long path with two different exits.\nDirectly ahead of you is a wall.',
        1: 'To your left, there is a wall.\nTo your right, there is a long path with a left turn.\nDirectly ahead of you is a long path with two different exits.', 
        2: 'To your left, there is a long path with two different exits.\nTo your right, there is a wall.\nDirectly ahead of you is a long path with a left turn.', 
        3: 'To your left, there is a long path with a left turn.\nTo your right, there is a wall.\nDirectly ahead of you is a wall.'
    }
    
    vent_16 = {
        0: 'To your left, there is a path ending in a left turn.\nTo your right, there is a path with two different exits.\nDirectly ahead of you is a wall.',
        1: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a path with two different exits.', 
        2: 'To your left, there is a path with two different exits.\nTo your right, there is a path ending in a left turn.\nDirectly ahead of you is a wall.', 
        3: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a path ending in a left turn.'
    }
    
    vent_17 = {
        0: 'To your left, there is a long path ending in a left turn.\nTo your right, there is a path ending in a left turn.\nDirectly ahead of you is a wall.',
        1: 'To your left, there is a wall.\nTo your right, there is a long path ending in an intersection.\nDirectly ahead of you is a path ending in a left turn.', 
        2: 'To your left, there is a path ending in a left turn.\nTo your right, there is a long path ending in a left turn.\nDirectly ahead of you is a long path ending in an intersection.', 
        3: 'To your left, there is a long path ending in an intersection.\nTo your right, there is a wall.\nDirectly ahead of you is a long path ending in a left turn.'
    }
    
    vent_18 = {
        0: 'To your left, there is a long path with two different exits.\nTo your right, there is a wall.\nDirectly ahead of you is a path ending in a right turn.',
        1: 'To your left, there is a path ending in a right turn.\nTo your right, there is a wall.\nDirectly ahead of you is a wall.', 
        2: 'To your left, there is a wall.\nTo your right, there is a long path with two different exits.\nDirectly ahead of you is a wall.', 
        3: 'To your left, there is a wall.\nTo your right, there is a path ending in a right turn.\nDirectly ahead of you is a long path with two different exits.'
    }
    
    vent_19 = {
        0: 'To your left, there is a wall.\nTo your right, there is a long path ending in a right turn.\nDirectly ahead of you is a wall.',
        1: 'To your left, there is a wall.\nTo your right, there is a path ending in a right turn.\nDirectly ahead of you is a long path ending in a right turn.', 
        2: 'To your left, there is a long path ending in a right turn.\nTo your right, there is a wall.\nDirectly ahead of you is a path ending in a right turn.', 
        3: 'To your left, there is a path ending in a right turn.\nTo your right, there is a wall.\nDirectly ahead of you is a wall.'
    }
    
    vent_20 = {
        0: 'To your left, there is a path ending in a left turn.\nTo your right, there is a path ending in a right turn.\nDirectly ahead of you is a wall.',
        1: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a path ending in a right turn.', 
        2: 'To your left, there is a path ending in a right turn.\nTo your right, there is a path ending in a left turn.\nDirectly ahead of you is a wall.', 
        3: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a path ending in a left turn.'
    }
    
    vent_21 = {
        0: 'To your left, there is a long path ending in a left turn.\nTo your right, there is a wall.\nDirectly ahead of you is a wall.',
        1: 'To your left, there is a wall.\nTo your right, there is a long path with two exits. You can see a fan spinning at the end.\nDirectly ahead of you is a wall.', 
        2: 'To your left, there is a wall.\nTo your right, there is a long path ending in a left turn.\nDirectly ahead of you is a long path with two exits. You can see a fan spinning at the end.', 
        3: 'To your left, there is a long path with two exits. You can see a fan spinning at the end.\nTo your right, there is a wall.\nDirectly ahead of you is a long path ending in a left turn.'
    }
    
    vent_22 = {
        0: 'To your left, there is a long, straight path with two exits.\nTo your right, there is a path ending in a left turn.\nDirectly ahead of you is a path ending in a left turn.',
        1: 'To your left, there is a path ending in a left turn.\nTo your right, there is a path leading to a fan that is blowing air in your face.\nDirectly ahead of you is a path ending in a left turn.', 
        2: 'To your left, there is a path ending in a left turn.\nTo your right, there is a long, straight path with two exits.\nDirectly ahead of you is a path leading to a fan that is blowing air in your face.', 
        3: 'To your left, there is a path leading to a fan that is blowing air in your face.\nTo your right, there is a path ending in a left turn.\nDirectly ahead of you is a long, straight path with two exits.'
    }
    
    vent_23 = {
        0: 'To your left, there is a long, straight path with four exits.\nTo your right, there is a wall.\nDirectly ahead of you is a path ending in a dead end.',
        1: 'To your left, there is a path ending in a dead end.\nTo your right, there is a wall.\nDirectly ahead of you is a wall.', 
        2: 'To your left, there is a wall.\nTo your right, there is a long, straight path with four exits.\nDirectly ahead of you is a wall.', 
        3: 'To your left, there is a wall.\nTo your right, there is a path ending in a dead end.\nDirectly ahead of you is a long, straight path with four exits.'
    }
    
    vent_24 = {
        0: 'You are surrounded by walls.',
        1: 'To your left, there is a wall.\nTo your right, there is a path ending in a right turn.\nDirectly ahead of you is a wall.', 
        2: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a path ending in a right turn.', 
        3: 'To your left, there is a path ending in a right turn.\nTo your right, there is a wall.\nDirectly ahead of you is a wall.'
    }
    
    vent_25 = {
        0: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a long path with two exits.',
        1: 'To your left, there is a long path with two exits.\nTo your right, there is a wall.\nDirectly ahead of you is a wall.', 
        2: 'You are surrounded by walls.', 
        3: 'To your left, there is a wall.\nTo your right, there is a long path with two exits.\nDirectly ahead of you is a wall.'
    }
    
    vent_26 = {
        0: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a long path with three exits.',
        1: 'To your left, there is a long path with three exits.\nTo your right, there is a path ending at a fan spinning at an alarming speed.\nDirectly ahead of you is a wall.', 
        2: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a path ending at a fan spinning at an alarming speed.', 
        3: 'To your left, there is a path ending at a fan spinning at an alarming speed.\nTo your right, there is a long path with three exits.\nDirectly ahead of you is a wall.'
    }
    
    vent_27 = {
        0: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a long, straight path with three exits.',
        1: 'To your left, there is a long, straight path with three exits.\nTo your right, there is a fan that seems to have stopped spinning.\nDirectly ahead of you is a wall.', 
        2: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a fan that seems to have stopped spinning.', 
        3: 'To your left, there is a fan that seems to have stopped spinning.\nTo your right, there is a long, straight path with three exits.\nDirectly ahead of you is a wall.'
    }
    
    vent_28 = {
        0: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a path ending in an intersection.',
        1: 'To your left, there is a path ending in an intersection.\nTo your right, there is a path ending in an intersection.\nDirectly ahead of you is a wall.', 
        2: 'To your left, there is a wall.\nTo your right, there is a wall.\nDirectly ahead of you is a path ending in an intersection.', 
        3: 'To your left, there is a path ending in an intersection.\nTo your right, there is a path ending in an intersection.\nDirectly ahead of you is a wall.'
    }

    vent_walls_start = { 
        0: True, 
        1: False, 
        2: True, 
        3: False
    }
    
    vent_walls_1 = { 
        0: False, 
        1: False, 
        2: True, 
        3: False
    }

    vent_walls_2 = { 
        0: True, 
        1: False, 
        2: False, 
        3: True
    }

    vent_walls_3 = { 
        0: True, 
        1: False, 
        2: True, 
        3: False
    }

    vent_walls_4 = { 
        0: False, 
        1: False, 
        2: True, 
        3: False
    }

    vent_walls_5 = { 
        0: True, 
        1: False, 
        2: True, 
        3: False
    }

    vent_walls_6 = { 
        0: False, 
        1: False, 
        2: True, 
        3: False
    }

    vent_walls_7 = { 
        0: True, 
        1: True, 
        2: True, 
        3: False
    }

    vent_walls_8 = { 
        0: True, 
        1: False, 
        2: True, 
        3: False
    }

    vent_walls_9 = { 
        0: False, 
        1: True, 
        2: True, 
        3: False
    }

    vent_walls_10 = { 
        0: True, 
        1: True, 
        2: False, 
        3: False
    }

    vent_walls_11 = { 
        0: True, 
        1: False, 
        2: True, 
        3: False
    }

    vent_walls_12 = { 
        0: True, 
        1: False, 
        2: True, 
        3: True
    }

    vent_walls_13 = { 
        0: False, 
        1: False, 
        2: False, 
        3: True
    }

    vent_walls_14 = { 
        0: False, 
        1: True, 
        2: False, 
        3: True
    }

    vent_walls_15 = { 
        0: True, 
        1: False, 
        2: False, 
        3: True
    }

    vent_walls_16 = { 
        0: True, 
        1: False, 
        2: True, 
        3: False
    }

    vent_walls_17 = { 
        0: True, 
        1: False, 
        2: False, 
        3: False
    }

    vent_walls_18 = { 
        0: False, 
        1: True, 
        2: True, 
        3: False
    }

    vent_walls_19 = { 
        0: False, 
        1: True, 
        2: True, 
        3: False
    }

    vent_walls_20 = { 
        0: True, 
        1: False, 
        2: True, 
        3: False
    }

    vent_walls_21 = { 
        0: False, 
        1: False, 
        2: True, 
        3: True
    }

    vent_walls_22 = { 
        0: False, 
        1: False, 
        2: False, 
        3: False
    }

    vent_walls_23 = { 
        0: False, 
        1: True, 
        2: True, 
        3: False
    }

    vent_walls_24 = { 
        0: True, 
        1: True, 
        2: False, 
        3: True
    }

    vent_walls_25 = {
        0: False, 
        1: True, 
        2: True, 
        3: True
    }

    vent_walls_26 = {
        0: False,
        1: True,
        2: False,
        3: True
    }
    
    vent_walls_27 = {
        0: False,
        1: True,
        2: False,
        3: True
    }
    
    vent_walls_28 = {
        0: False,
        1: True,
        2: False,
        3: True
    }
    
    vent_descriptions.append(vent_start)
    vent_descriptions.append(vent_1)
    vent_descriptions.append(vent_2)
    vent_descriptions.append(vent_3)
    vent_descriptions.append(vent_4)
    vent_descriptions.append(vent_5)
    vent_descriptions.append(vent_6)
    vent_descriptions.append(vent_7)
    vent_descriptions.append(vent_8)
    vent_descriptions.append(vent_9)
    vent_descriptions.append(vent_10)
    vent_descriptions.append(vent_11)
    vent_descriptions.append(vent_12)
    vent_descriptions.append(vent_13)
    vent_descriptions.append(vent_14)
    vent_descriptions.append(vent_15)
    vent_descriptions.append(vent_16)
    vent_descriptions.append(vent_17)
    vent_descriptions.append(vent_18)
    vent_descriptions.append(vent_19)
    vent_descriptions.append(vent_20)
    vent_descriptions.append(vent_21)
    vent_descriptions.append(vent_22)
    vent_descriptions.append(vent_23)
    vent_descriptions.append(vent_24)
    vent_descriptions.append(vent_25)
    vent_descriptions.append(vent_26)
    vent_descriptions.append(vent_27)
    vent_descriptions.append(vent_28)

    vent_walls.append(vent_walls_start)
    vent_walls.append(vent_walls_1)
    vent_walls.append(vent_walls_2)
    vent_walls.append(vent_walls_3)
    vent_walls.append(vent_walls_4)
    vent_walls.append(vent_walls_5)
    vent_walls.append(vent_walls_6)
    vent_walls.append(vent_walls_7)
    vent_walls.append(vent_walls_8)
    vent_walls.append(vent_walls_9)
    vent_walls.append(vent_walls_10)
    vent_walls.append(vent_walls_11)
    vent_walls.append(vent_walls_12)
    vent_walls.append(vent_walls_13)
    vent_walls.append(vent_walls_14)
    vent_walls.append(vent_walls_15)
    vent_walls.append(vent_walls_16)
    vent_walls.append(vent_walls_17)
    vent_walls.append(vent_walls_18)
    vent_walls.append(vent_walls_19)
    vent_walls.append(vent_walls_20)
    vent_walls.append(vent_walls_21)
    vent_walls.append(vent_walls_22)
    vent_walls.append(vent_walls_23)
    vent_walls.append(vent_walls_24)
    vent_walls.append(vent_walls_25)
    vent_walls.append(vent_walls_26)
    vent_walls.append(vent_walls_27)
    vent_walls.append(vent_walls_28)
    
    ply = input('> ').lower()

    if globalcommands():
        pass

    elif ply == 'left' or ply == 'go left':
        print("")
        ventmove_left()

    elif ply == 'forward' or ply == 'go forward':
        print("")
        ventmove_forward()

    elif ply == 'right' or ply == 'go right':
        print("")
        ventmove_right()

    elif ply == 'back' or ply == 'go back':
        print("")
        ventmove_back()

    elif ply == 'turn left':
        print('\nYou turn left.')
        ventDirection = (ventDirection - 1) % 4
        ventdesc()

    elif ply == 'turn right':
        print('\nYou turn left')
        ventDirection = (ventDirection + 1) % 4
        ventdesc()

    else:
        print('Your thoughts seem incomprehensible.')

# Area 6 (Sir, curity camera.)
while plypos == 6 and plydead == False:

    ply = input('> ').lower()

    while officepos == 0:

        if ply == 'look north':
            print('A large wooden desk. Underneath it is a bulky computer tower. Mounted on top of the desk and wall are about a dozen computer monitors, each buzzing with static.')

        elif ply == 'look south':
            print('There is a sturdy metal door embedded into the wall.')

        elif ply == 'look east':
            print('A wall made of concrete bricks. There is unintelligible writing across its surface. It says: WKLV LV D SODFHKROGHU. ZDLW IRU FRRO SXCCOH.')

        elif ply == 'look west':
            print('A concrete wall marred by cracks.')

        elif ply == 'go north':
            print('You approach the desk. Would you like to sit down? Y/N')
            officepos = 1
            plysecondary = input('> ').lower()
            if plysecondary == 'y':
                computer = True
                print('You sit down in front of the desk. As you sit, one of the computer monitors displays a lock screen with an input for a password.')
                

    if globalcommands():
        pass


#Area 12 (A very edible substance that makes up the room (True Story))
while plypos == 12 and plydead == False:

    ply = input('> ').lower()

    if globalcommands():
        pass

    elif ply == 'look north':
        print("PLACEHOLDER")

    elif ply == 'look east':
        print("PLACEHOLDER")

    elif ply == 'look west':
        print("PLACEHOLDER")

    elif ply == 'look south':
        print("PLACEHOLDER")

    elif ply == 'go north':
        print("PLACEHOLDER")

    elif ply == 'go east':
        print("PLACEHOLDER")

    elif ply == 'go west':
        print("PLACEHOLDER")

    elif ply == 'go south':
        print("PLACEHOLDER")

    else:
        print("Your thoughts seem incomprehensible.")

# Area 18 (NEW PATCH: 19 now comes before 18 numerically.)
while plypos == 18 and plydead == False and insidehouse == False:

    ply = input('> ').lower()

    if globalcommands():
        pass

    elif ply == 'look north':
        print("It is indeed a door. Unfortunately, it does not look fragile.")

    elif ply == 'look east':
        print("A very climable tree.")

    elif ply == 'look west' and 'Key' not in inventory:
        print("A Skeleton of someone lying on a bench. They seem to be holding a key.")

    elif ply == 'look west' and 'Key' in inventory:
        print("A Skeleton of someone lying on a bench. They seem to now be smiling.")

    elif ply == 'look south':
        print("Nothing but fog and dark roads.")

    elif ply == 'go north':
        print("You bang your head on the door.")

    elif ply == 'go east':
        print("You head towards the tree. Nothing seems to be around it.")

    elif ply == 'go west':
        print("A basic beige wall blocks your path. Doesn't look breakable.")

    elif ply == 'go south':
        if 'Lantern' not in inventory:
            print("You can't see well enough to be confident to go that way.")
        else:
            if weapon == 'Lantern':
                print("You head into the fog with your lantern lit. It is very foggy, but visable enough to see close around you.\nWhat now?")
                plypos = 20
            else:
                print("You unfortuantly cannot see well enough as you do not have your lantern equipped.")

    elif ply == 'take key' or ply == 'grab key':
        print("You take the solid key from the skeleton.\n\033[1;33mKEY was added to your inventory.\033[0m")
        inventory.append('Key')

    elif ply == 'break door' or ply == 'fight door' or ply == 'kill door' or ply == 'attack door':
        if weapon == 'Sword':
            print(f"\033[1;31mYou manage to deal {plyatck * 5} damage to the metal door. \033[0mUnfortunatly, this door doesn't want to budge.")
        else:
            print("You attempt to destory the door. However, it is stronger than the previous door and does not budge.")

    elif ply == 'open door' and 'Key' not in inventory:
        print("You jiggle the handle. The door is locked.")

    elif (ply == 'open door' or ply == 'unlock door') and 'Key' in inventory:
        print("You open the door with the key. You are now inside the house. The door remains open.")
        insidehouse = True
        # It took me 5 hours to realize I accidentaly put a == instead of a =.

    elif ply == 'check door':
        print("The house's front door. It looks to be made of metal.")

    elif ply == 'take door':
        print("You try to take the door. It is lodged into the house and doesn't look to be coming out.")

    elif ply == 'eat door':
        print("You put your mouth on the door. The metal gives you an icky taste.")

    elif ply == 'close door':
        print("You try to close the closed door. It does not budge.")

    elif ply == 'unlock door' and 'Key' not in inventory:
        print("You try to unlock the door. Your finger does not fit through the lock.")

    elif ply == 'take skeleton' and 'Key' not in inventory:
        print("You try to take the entire skeleton. It seems to be stuck to the bench. The key remains in the skeleton's hand.")
        #  ,̶'̶ ̶ ̶,̶ ̶|̶ ̶,̶'̶ ̶_̶'̶ 

    elif ply == 'take skeleton' and 'Key' in inventory:
        print("Rather than taking the skeleton, you shake the skeleton's hand for reciving the key.")

    elif ply == 'check skeleton':
        print("A very old skeleton. Looks to have scars scratched all around it.")
        if 'Key' not in inventory:
            print("The skeleton seems to be holding a key.")

    elif ply == 'fight skeleton' or ply == 'attack skeleton' or ply == 'kill skeleton':
        if weapon == 'Sword' and 'Key' in inventory:
            print(f"You slash the skeleton for {plyatck * 3} damage. The skeleton immediatly breaks and the skull falls to the floor. \033[1;33mThe sword grew stronger.\033[0m")
            plyatck += 1
            swordstrength += 1
        else:
            print("You'd perfer not to fight a skeleton at this time.")

    elif (ply == 'enter house' or ply == 'go in house') and 'Key' in inventory:
        print("You open the door with the key to enter the house. You are now inside. The door remains open.")
        insidehouse = True

    elif (ply == 'enter house' or ply == 'go in house') and 'Key' not in inventory:
        print("You attempt to go into the house. A locked metal door blocks your path.")

    elif (ply == 'climb tree' or ply == 'check tree' or ply == 'eat tree' or ply == 'take tree') and 'Branch' in inventory:
        print("There is no tree.")

    elif ply == 'climb tree':
        print("You climb the tree. While up there, you get a good glimpse of the path covered in fog to the south.\nThere seems to be an outline of a person wondering around aimlessly.\nYou jump down from the tree.")

    elif ply == 'check tree':
        print("A tree that has tons of climable branches.")

    elif ply == 'eat tree':
        print("You take a bite of the tree. Tastes odd.")

    elif ply == 'take tree':
        print("You try to take the tree. It is unfortunatly apart of the ground.")

    elif ply == 'attack tree' or ply == 'fight tree' or ply == 'chop tree' or ply == 'chop the tree down' or ply == 'chop tree':
        if weapon == 'Sword':
            print("You manage to chop the tree with your sword. The tree immediatly collapses and fades to nothing. \033[1;33mThe sword grew stronger.\nBRANCH added to your inventory.\033[0m")
            plyatck += 1
            swordstrength += 1
            inventory.append('Branch')
        else:
            print("You attempt to chop the tree down. Unfortuantly, you do not have the right tools for this task.")

    else:
        print("Your thoughts seem incomprehensible.")

    if insidehouse == True:

        while insidehouse == True and plydead == False:

            ply = input('> ').lower()

            if globalcommands():
                pass

            elif ply == 'look north':
                print("A wall that contains a photo of a family. The faces look to be scratched out besides one.")

            elif ply == 'look east' and 'Lantern' not in inventory:
                print("A shelf that contains a lantern.")

            elif ply == 'look east' and 'Lantern' in inventory:
                print("A shelf that used to have a lantern.")

            elif ply == 'take lantern':
                if 'Lantern' not in inventory:
                    print("You take the lantern from the shelf.\n\033[1;33mLANTERN added to your inventory.\033[0m")
                    inventory.append("Lantern")
                else:
                    print("You have already taken the lantern. You cannot find another item to take.")

            elif ply == 'look west':
                print("Nothing but packed boxes. They are all sealed shut.")

            elif ply == 'open boxes':
                print("You attempt to open the boxes. They are all fully sealed.")

            elif ply == 'break boxes':
                print("You attempt to break the boxes. For some reason, they don't budge.")

            elif ply == 'take boxes':
                print("You attempt to take the boxes. They feel as if they are glued to the ground.")

            elif ply == 'look south':
                print("The area you were in before. The door is still open.")

            elif ply == 'go north' or ply == 'go east' or ply == 'go west':
                print("The house doesn't seem to be big enough to move in that direction.")

            elif ply == 'go south' or ply == 'exit house' or ply == 'leave house' or ply == 'close door':
                print("You exit the house. You make sure to close and lock the door on your way out.")
                insidehouse = False
            else:
                print("Your thoughts seem incomprehensible.")

# Area 20 (I bet these foggy roads would look really cool, but this is a text only game.)
while plypos == 20 and plydead == False:

    ply = input('> ').lower()

    if ply == 'equip nothing' or ply == 'equip splinters' or ply == 'equip pretend splinters' or ply == 'equip crowbar' or ply == 'equip brick' or ply == 'equip shard' or ply == 'equip sword' or ply == 'equip key':
        print("If you were to equip that, you would lose your vision with the lantern.")

    elif globalcommands():
        pass

    elif ply == 'look north':
        print("Just more road upahead from what you can see.")

    elif ply == 'look east':
        print("An endless supply of dead trees.")

    elif ply == 'look west':
        print("PLACEHOLDER")

    elif ply == 'look south':
        print("The road that you already treched.")

    elif ply == 'go north':
        print("You keep moving forward.")

    elif ply == 'go east':
        print("You go towards the dead trees. You can't seem to find anything in between them.")

    elif ply == 'go west':
        print("PLACEHOLDER")

    elif ply == 'go south':
        print("There's no point in going back.")

    else:
        print("Your thoughts seem incomprehensible.")
