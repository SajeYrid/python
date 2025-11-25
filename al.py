plydeaths = 0
def retry():
    # the holy and pure and innocent variable block
    # booleans
    global doorbroken, plydead, brokenhand, dinodead, dinoseen, enemythink, plydefending, plycharge, enemydefending, enemycharge, enemyspecial, ventopen, tookstool, tookSplinter, pretendLMAO, plywallBroken
    global stoolExplode, plyturn, plyerror, kys, insidehouse, firstitem, computer, forwardcheck, companiondefending, photocheck
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
    forwardcheck = False
    companiondefending = False
    photocheck = False

    # strings
    global ply, plysecondary, equippeditem, weapon, weaponspecial, armor, enemyname, enemyphrase, enemyspecialmove, companion, companionphrase
    ply = ""
    plysecondary = ""
    equippeditem = "None"
    weapon = "Nothing"
    weaponspecial = 'Nothing'
    armor = "Nothing"
    enemyname = ""
    enemyphrase = ""
    enemyspecialmove = ""
    companion = ""
    companionphrase = ""

    # lists
    global inventory, locations, wiseguy, wiseguycount
    inventory = ['Nothing']
    locations = [1, 2, 3, 4, 5, 6, 12, 18, 20, 21, 22]
    wiseguy = ['q', 'w', 'e', 'r', 't', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'm']
    wiseguycount = ['q', 'w', 'e', 'r', 't', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'm']

    # integers
    global plypos, plychoke, ouch, plyhealthDEFAULT, plyhealth, plyatckDEFAULT, plyatck, plyatckplus, plydefenseDEFAULT, plydefense, plydefenseMAX, weaponability, weaponnumber, specialcharge, specialchargeDEFAULT
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
    plydefenseMAX = 0
    weaponability = 0
    weaponnumber = 0
    specialcharge = 0
    specialchargeDEFAULT = 0
    global enemyhealth, enemyatck, enemyatckplus, enemyatckDEFAULT, enemydefense, enemyspecialtype, enemyspecialnumber, enemyspecialcount, enemyspecialcountDEFAULT, enemyaction, enemytarget
    enemyhealth = 0
    enemyatck = 0
    enemyatckplus = 0
    enemyatckDEFAULT = 0
    enemydefense = 0
    enemyspecialtype = 0
    enemyspecialnumber = 0
    enemyspecialcount = 0
    enemyspecialcountDEFAULT = 0
    enemyaction = 0
    enemytarget = 0
    global companionhealth, companionatck, companionatckDEFAULT, companiondefense
    companionhealth = 0
    companionatck = 0
    companionatckDEFAULT = 0
    companiondefense = 0
    global swordstrength, glassTicker, ventpos, ventDirection, officepos, talkcounter
    swordstrength = 5
    glassTicker = 2
    ventpos = 0
    ventDirection = 0
    officepos = 0
    talkcounter = 0

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
    'Shield' : 'SHIELD - A shield that is meant for blocking incoming danger. The way you obtained it felt odd.',
    'Sword' : 'SWORD - A sword shaped object that formed from the shard. Perfect for slaying anything in your way.',
    'Key' : 'KEY - A key that you obtained from a skeleton. Looks to have the ability to unlock various locks.',
    'Lantern' : 'LANTERN - An ordinary lantern with no oddities whatsoever.',
    'Branch' : 'BRANCH - A part of the tree that was left to die.',
    'Map' : 'MAP - Found on a basic beige wall. Every vent seems to be labeled with a number.',
    'Bandana' : 'BANDANA - The bandana of a fallen warrior. Sacrifices defense for even more strength.',
    'Alien Blaster': 'ALIEN BLASTER - You have no info on this item.'
}
#For the roomhints and self checkroom, format it like this - ROOM NUMBER THEY ARE IN - (OPTIONAL: IF IT IS A DIFFERENT VERSION OF THE ROOM) - VARIATION OF THE HINT
    #EXAMPLE - 3BB would be mean plypos = 3 (museum), this is the B varient of the room (stool varient), and this is the 2nd hint (After crowbar is obtained)
roomhints = {
    '1A' : 'You tried to think. You observe that there is a unbroken door in front of you.',
    '1B' : 'You tried to think. You observe that the brick wall in the doorframe looks unnatural.',
    '3A' : 'You tried to think. You observe a strange feeling of being watched.',
    '3B' : 'You tried to think. You observe a suspicious looking dinosaur.',
    '3C' : 'You tried to think. You observe a sense of satisfaction from killing a dinosaur.',
    '3BA' : 'You tried to think. You observe a dangling crowbar from the Plastic Dinosaur that is too high to reach.',
    '3BB' : 'You tried to think. You thought about the destruction of buildings.',
    '1XA' : 'You tried to think. You observe a puzzle you have already completed before.',
    '5A' : 'You tried to think. You thought about the minotaur in the labyrinth.',
    '6A' : 'You tried to think. You observe a strange message.',
    '12A' : 'PLACEHOLDER',
    '18A' : 'PLACEHOLDER',
    '18B' : 'PLACEHOLDER',
    '20A' : 'PLACEHOLDER',
    '22A' : 'PLACEHOLDER',
    '22B' : 'PLACEHOLDER'
}

selfcheckroom = {
    '1A' : 'Trying to investigate this strange door they found.',
    '1B' : 'Certified Destroyer of Doors.',
    '3A' : 'Feels broken.',
    '3B' : 'Feels a prehistoric rage overtaking them.',
    '3C' : 'Plastic Dinosaur exterminator.',
    '3BA' : 'Ready to climb their newly obtained stool.',
    '3BB' : 'Already broke their newly obtained stool.',
    '1XA' : 'Still trying to investigate this unique door they found.',
    '5A' : 'Crawling through the vents.',
    '6A' : 'idk what to write here, but it is for the security room.'
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
    def __init__(self, name, ability, number, charge):
        self.name = name
        self.ability = ability
        self.number = number
        self.charge = charge

# Enemies

def truedoor():
    global enemyname, enemyhealth, enemyatck, enemyatckDEFAULT, enemydefense, enemyphrase, enemydefending, enemycharge, enemyspecial, enemyspecialmove, enemyspecialtype, enemyspecialnumber, enemytarget
    doorenemy = Enemy("TRUE DOOR", 100, 1, -5, "attacked", False)
    enemyname = doorenemy.name
    enemyhealth = doorenemy.health
    enemyatck = doorenemy.attack
    enemyatckDEFAULT = doorenemy.attack
    enemydefense = doorenemy.defense
    enemyphrase = doorenemy.atckphrase
    enemyspecial = doorenemy.special

    enemyspecialmove = ""
    enemyspecialtype = 0
    enemyspecialnumber = 0
    
    enemydefending = False
    enemycharge = False
    enemytarget = 0

def plasticDino():
    global enemyname, enemyhealth, enemyatck, enemyatckDEFAULT, enemydefense, enemyphrase, enemydefending, enemycharge, enemyspecial, enemyspecialmove, enemyspecialtype, enemyspecialnumber, enemytarget
    plasticDino = Enemy("The Plastic Dinosaur", 30, 2, 0, "bit", False)
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
    enemytarget = 0

def voidenemy():
    global enemyname, enemyhealth, enemyatck, enemyatckDEFAULT, enemydefense, enemyphrase, enemydefending, enemycharge
    global enemyspecial, enemyspecialmove, enemyspecialtype, enemyspecialnumber, enemyspecialcount, enemyspecialcountDEFAULT, enemytarget
    voidenemy = Enemy("The VOID", 50, 3, 1, "suffocated", True)
    enemyname = voidenemy.name
    enemyhealth = voidenemy.health
    enemyatck = voidenemy.attack
    enemyatckDEFAULT = voidenemy.attack
    enemydefense = voidenemy.defense
    enemyphrase = voidenemy.atckphrase
    enemyspecial = voidenemy.special

    voidspecial = Special("Life Drain", 1, 4, 5)
    enemyspecialmove = voidspecial.name
    enemyspecialtype = voidspecial.ability
    enemyspecialnumber = voidspecial.number
    enemyspecialcount = voidspecial.charge
    enemyspecialcountDEFAULT = voidspecial.charge

    enemydefending = False
    enemycharge = False
    enemytarget = 0

def beastenemy():
    global enemyname, enemyhealth, enemyatck, enemyatckDEFAULT, enemydefense, enemyphrase, enemydefending, enemycharge
    global enemyspecial, enemyspecialmove, enemyspecialtype, enemyspecialnumber, enemyspecialcount, enemyspecialcountDEFAULT, enemytarget
    beastenemy = Enemy("The Beast", 45, 3, 1, "swipes at", True)
    enemyname = beastenemy.name
    enemyhealth = beastenemy.health
    enemyatck = beastenemy.attack
    enemyatckDEFAULT = beastenemy.attack
    enemydefense = beastenemy.defense
    enemyphrase = beastenemy.atckphrase
    enemyspecial = beastenemy.special

    beastspecial = Special("Enrage", 2, 5, 6)
    enemyspecialmove = beastspecial.name
    enemyspecialtype = beastspecial.ability
    enemyspecialnumber = beastspecial.number
    enemyspecialcount = beastspecial.charge
    enemyspecialcountDEFAULT = beastspecial.charge

    enemydefending = False
    enemycharge = False
    enemytarget = 0

def alienenemy():
    global enemyname, enemyhealth, enemyatck, enemyatckDEFAULT, enemydefense, enemyphrase, enemydefending, enemycharge
    global enemyspecial, enemyspecialmove, enemyspecialtype, enemyspecialnumber, enemyspecialcount, enemyspecialcountDEFAULT, enemytarget
    alienenemy = Enemy("The 🅐🅛🅘🅔🅝", 75, 4, -5, "ᎴᏋፈᎥᎷᏗᏖᏋᏕ", True)
    enemyname = alienenemy.name
    enemyhealth = alienenemy.health
    enemyatck = alienenemy.attack
    enemyatckDEFAULT = alienenemy.attack
    enemydefense = alienenemy.defense
    enemyphrase = alienenemy.atckphrase
    enemyspecial = alienenemy.special

    alienenemy = Special("\033[1;30m𝕯𝕰𝕬𝕿𝕳\033[0m", 4, 1, 10)
    enemyspecialmove = alienenemy.name
    enemyspecialtype = alienenemy.ability
    enemyspecialnumber = alienenemy.number
    enemyspecialcount = alienenemy.charge
    enemyspecialcountDEFAULT = alienenemy.charge

    enemydefending = False
    enemycharge = False
    enemytarget = 0

def shreksecretenemy():
    global enemyname, enemyhealth, enemyatck, enemyatckDEFAULT, enemydefense, enemyphrase, enemydefending, enemycharge
    global enemyspecial, enemyspecialmove, enemyspecialtype, enemyspecialnumber, enemyspecialcount, enemyspecialcountDEFAULT, enemytarget
    shrekenemy = Enemy("Shrek?", 100, 10, 3, "ogers", True)
    enemyname = shrekenemy.name
    enemyhealth = shrekenemy.health
    enemyatck = shrekenemy.attack
    enemyatckDEFAULT = shrekenemy.attack
    enemydefense = shrekenemy.defense
    enemyphrase = shrekenemy.atckphrase
    enemyspecial = shrekenemy.special

    shrekenemy = Special("Onions", 3, 10, 10)
    enemyspecialmove = shrekenemy.name
    enemyspecialtype = shrekenemy.ability
    enemyspecialnumber = shrekenemy.number
    enemyspecialcount = shrekenemy.charge
    enemyspecialcountDEFAULT = shrekenemy.charge

    enemydefending = False
    enemycharge = False
    enemytarget = 0

def markipliersecretenemy():
    global enemyname, enemyhealth, enemyatck, enemyatckDEFAULT, enemydefense, enemyphrase, enemydefending, enemycharge
    global enemyspecial, enemyspecialmove, enemyspecialtype, enemyspecialnumber, enemyspecialcount, enemyspecialcountDEFAULT, enemytarget
    shrekenemy = Enemy("Markiplier", 87, 4, 5, "beats the ass of", True)
    enemyname = shrekenemy.name
    enemyhealth = shrekenemy.health
    enemyatck = shrekenemy.attack
    enemyatckDEFAULT = shrekenemy.attack
    enemydefense = shrekenemy.defense
    enemyphrase = shrekenemy.atckphrase
    enemyspecial = shrekenemy.special

    shrekenemy = Special("Five Nights at Freddy", 1, 87, 5)
    enemyspecialmove = shrekenemy.name
    enemyspecialtype = shrekenemy.ability
    enemyspecialnumber = shrekenemy.number
    enemyspecialcount = shrekenemy.charge
    enemyspecialcountDEFAULT = shrekenemy.charge

    enemydefending = False
    enemycharge = False
    enemytarget = 0

def mysteriousPerson():
    global enemyname, enemyhealth, enemyatck, enemyatckDEFAULT, enemydefense, enemyphrase, enemydefending, enemycharge, enemyspecial, enemyspecialmove, enemyspecialtype, enemyspecialnumber, enemytarget
    mysteriousperson = Enemy("The Mysterious Person", 20, 1, 0, "throws a rock at", False)
    enemyname = mysteriousperson.name
    enemyhealth = mysteriousperson.health
    enemyatck = mysteriousperson.attack
    enemyatckDEFAULT = mysteriousperson.attack
    enemydefense = mysteriousperson.defense
    enemyphrase = mysteriousperson.atckphrase
    enemyspecial = mysteriousperson.special

    enemyspecialmove = ""
    enemyspecialtype = 0
    enemyspecialnumber = 0
    
    enemydefending = False
    enemycharge = False
    enemytarget = 0

def customenemy():
    global enemyname, enemyhealth, enemyatck, enemyatckDEFAULT, enemydefense, enemyphrase, enemydefending, enemycharge
    global enemyspecial, enemyspecialmove, enemyspecialtype, enemyspecialnumber, enemyspecialcount, enemyspecialcountDEFAULT, enemytarget
    customchoice = str(input('What is the name of the enemy?\n>'))
    enemyname = customchoice
    customchoice = input('What is the health of the enemy?\n>')
    try:
        enemyhealth = int(customchoice)
    except:
        print("That is not a number. Enemy will start off at 30 HP")
        enemyhealth = 30
    customchoice = input('What is the attack of the enemy?\n>')
    try:
        enemyatck = int(customchoice)
        enemyatckDEFAULT = int(customchoice)
    except:
        print("That is not a number. Enemy will start off at 2 Attack")
        enemyatck = 2
        enemyatckDEFAULT = 2
    customchoice = input('What is the defense of the enemy?\n>')
    try:
        enemydefense = int(customchoice)
    except:
        print("That is not a number. Enemy will start off at 0 Defense")
        enemydefense = 0
    customchoice = str(input('What is the phrase when the enemy attacks?\n>'))
    enemyphrase = customchoice
    customchoice = str(input('Does the enemy have a special?\n>')).lower()
    if customchoice == 'true' or customchoice == 'yes':
        enemyspecial = True
        customchoice = str(input('What is the name of the special?\n>'))
        enemyspecialmove = customchoice
        customchoice = input('What is the type of ability the enemy has?\n>')
        try:
            if customchoice == '1' or customchoice == '2' or customchoice == '3' or customchoice == '4':
                enemyspecialtype = int(customchoice)
            else:
                print("That is not a valid special type. Enemy will have an attack special (1).")
                enemyspecialtype = 1
        except:
            print("That is not a valid special type. Enemy will have an attack special (1).")
            enemyspecialtype = 1
        customchoice = input('What number will the special use?\n>')
        try:
            enemyspecialnumber = int(customchoice)
        except:
            print("That is not a number. Setting special number to 5.")
            enemyspecialnumber = 5
        customchoice = input('How long until the enemy can use it?\n>')
        try:
            enemyspecialcount = int(customchoice)
            enemyspecialcountDEFAULT = int(customchoice)
        except:
            print("That is not a number. Setting special cooldown to 5 turns.")
            enemyspecialcount = 5
            enemyspecialcountDEFAULT = 5
    else:
        enemyspecial = False
        enemyspecialmove = ""
        enemyspecialtype = 0
        enemyspecialnumber = 0

    enemydefending = False
    enemycharge = False
    enemytarget = 0

# Companions

def customcompanion():
    global companion, companionhealth, companionatck, companionatckDEFAULT, companiondefense, companionphrase, companiondefending
    customchoice = str(input('What is the name of the companion?\n>'))
    companion = customchoice
    customchoice = input('What is the health of the companion?\n>')
    try:
        companionhealth = int(customchoice)
    except:
        print("That is not a number. Setting Companion health to 10.")
        companionhealth = 10
    customchoice = input('What is the attack of the companion?\n>')
    try:
        companionatck = int(customchoice)
        companionatckDEFAULT = int(customchoice)
    except:
        print("That is not a number. Setting Companion Attack to 1.")
        companionatck = 1
        companionatckDEFAULT = 1
    customchoice = input('What is the defense of the companion?\n>')
    try:
        companiondefense = int(customchoice)
    except:
        print("That is not a number. Setting Companion Defense to 0.")
        companiondefense = 0
    customchoice = str(input('What is the phrase when the companion attacks?\n>'))
    companionphrase = customchoice

    companiondefending = False

def mysteriouscompanion():
    global companion, companionhealth, companionatck, companionatckDEFAULT, companiondefense, companionphrase, companiondefending
    if photocheck == True:
        mysteriousperson = Enemy("Lenard", 10, 1, 0, "throws a rock at", False)
    else:
        mysteriousperson = Enemy("The Mysterious Person", 10, 1, 0, "throws a rock at", False)
    companion = mysteriousperson.name
    companionhealth = mysteriousperson.health
    companionatck = mysteriousperson.attack
    companionatckDEFAULT = mysteriousperson.attack
    companiondefense = mysteriousperson.defense
    companionphrase = mysteriousperson.atckphrase

    companiondefending = False

def shrekcompanion():
    global companion, companionhealth, companionatck, companionatckDEFAULT, companiondefense, companionphrase, companiondefending
    shrek = Enemy("Shrek", 100, 10, 3, "ogers", False)
    companion = shrek.name
    companionhealth = shrek.health
    companionatck = shrek.attack
    companionatckDEFAULT = shrek.attack
    companiondefense = shrek.defense
    companionphrase = shrek.atckphrase

    companiondefending = False

def markipliercompanion():
    global companion, companionhealth, companionatck, companionatckDEFAULT, companiondefense, companionphrase, companiondefending
    shrek = Enemy("Markiplier", 87, 4, 5, "beats the ass of", False)
    companion = shrek.name
    companionhealth = shrek.health
    companionatck = shrek.attack
    companionatckDEFAULT = shrek.attack
    companiondefense = shrek.defense
    companionphrase = shrek.atckphrase

    companiondefending = False

# Weapon Specials
    # NOTE THIS: The Special follows this class:
        #Name - What the special move is called
        #Ability - What type of ability it has (1 = Deals Damage, 2 = Increases Attack, 3 = Heals HP, 4 = Increases Defense)
        #Number - What number is used for the ability

def plyspecial():
    global specialweapon, weapon, weaponspecial, weaponability, weaponnumber, specialcharge, specialchargeDEFAULT
    match weapon:
        case 'Splinters':
            specialweapon = Special("Splinter Knuckles", 2, 2, 3)
        case 'Crowbar':
            specialweapon = Special("Spinning Crowbar", 1, 10, 4)
        case 'Brick':
            specialweapon = Special("Solid Drink", 3, 5, 5)
        case 'Shard':
            specialweapon = Special("Kill", 1, 20, 5)
        case 'Sword':
            specialweapon = Special("Eliminate", 1, 40, 10)
        case 'Lantern':
            specialweapon = Special("Light it up", 2, 4, 5)
        case 'Alien Blaster':
            specialweapon = Special("Defense Crediblity", 4, 1, 10)
        case _:
            specialweapon = Special("Nothing", 0, 0, 0)

    weaponspecial = specialweapon.name
    weaponability = specialweapon.ability
    weaponnumber = specialweapon.number
    specialcharge = specialweapon.charge
    specialchargeDEFAULT = specialweapon.charge


# the truly neutral functions
def roomdebug():
    global plypos, ply, inventory, weapon, tookstool
    match plypos:
        case 3:
            print("Which version of the room do you want? (Default, Stool)")
            ply = input('>').lower()
            match ply:
                case 'default':
                    print("You're the boss.")
                case 'stool':
                    print("Granting you the STOOL.")
                    inventory.append('Stool')
                    tookstool = True
                case _:
                    print("I'll assume that means the default room, boss.")
        case 4:
            print('Boss, get ready for a rough battle against the PLASTIC DINOSAUR!')
            plasticDino()
            plyspecial()
            battlestart()
        case 5 | 6:
            print('Granting you the TOOTH.')
            inventory.append('Tooth')
        case 18:
            print("Granting you the CROWBAR, and BRICK.")
            inventory.append('Crowbar')
            inventory.append('Brick')
        case 20:
            print("Granting you the LANTERN")
            inventory.append('Lantern')
            weapon = 'Lantern'
        case 21:
            print('Boss, get ready for a rough battle against the BEAST!')
        case 22:
            print('Granting you the CROWBAR, BRICK, and LANTERN.')
            inventory.append('Crowbar')
            inventory.append('Brick')
            inventory.append('Lantern')
            print("Which version of the room do you want? (Default, Alone")
            ply = input('>').lower()
            match ply:
                case 'default':
                    print("The MYSTERIOUS PERSON is now your companion.")
                    companion = 'Mysterious Person'
                case 'alone':
                    print("You're the boss.")
                case _:
                    print("I'll assume that means the default room, boss.")
                    print("The MYSTERIOUS PERSON is now your companion.")
                    companion = 'Mysterious Person'
        
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
    global weaponspecial, specialchargeDEFAULT, plydefenseMAX
    plydefenseMAX = plydefense
    if weaponspecial != 'Nothing':
        print(f"""
Your actions are:
\033[1;31mATTACK
\033[1;34mDEFEND
\033[1;32mCHARGE
\033[1;30mSPECIAL: {weaponspecial} (Ready in {specialchargeDEFAULT} Turns)\033[0m""")
    else:
        print("""
Your actions are:
\033[1;31mATTACK
\033[1;34mDEFEND
\033[1;32mCHARGE\033[0m""")

def plymove():
    global ply, plyhealth, enemydefending, enemyhealth, plyatck, enemydefense, plycharge, enemythink, enemyname, plydefending, plyerror, enemyatck, plydefense, specialcharge, specialchargeDEFAULT, weaponspecial
    global weaponability, weaponnumber, plyatckplus, companion, companionhealth, companionatck, companiondefense, enemytarget

    if plyerror == True:
        plyerror = False
    else:
        if specialcharge == 0 and weaponspecial != 'Nothing':
            print(f"Your special move, \033[1;3{weaponability}m{weaponspecial}\033[0m is now ready. Type SPECIAL to use it.")
        else:
            if weaponspecial != "Nothing":
                specialcharge -= 1

    if companion != '':
        if enemytarget == 0:
            print(f"{enemyname} looks to be targeting you.")
        else:
            print(f"{enemyname} looks to be targeting {companion}.")

    if companion == '':
        print(f"\033[1;32mYour health is: {plyhealth}. \033[1;35m{enemyname}'s health is {enemyhealth}. \033[0mWhat do you do?")
    else:
        print(f"\033[1;32mYour health is: {plyhealth}. \033[1;33m{companion}'s health is {companionhealth}. \033[1;35m{enemyname}'s health is {enemyhealth}. \033[0mWhat do you do?")

    ply = input('>').lower()

    import math

    if ply == 'attack' and enemydefending == False:
        if plyatck - enemydefense > 0:
            print(f"\033[1;31mYou attacked {enemyname} for {plyatck - enemydefense} damage!\033[0m")
            enemyhealth = enemyhealth - (plyatck - enemydefense)
        else:
            print(f"\033[1;31mYou attacked {enemyname} for 1 damage!\033[0m")
            enemyhealth -= 1
        if plyatckplus != 0:
            plyatck -= plyatckplus
            plyatckplus = 0
        if plycharge == True:
            plyatck = math.floor(plyatck / 2)
            plycharge = False

    elif ply == 'attack' and enemydefending == True:
        print(f"\033[1;31mYou attacked {enemyname}! \033[1;35mBut {enemyname} defended.\033[0m")
        if plyatckplus != 0:
            plyatck -= plyatckplus
            plyatckplus = 0
        if plycharge == True:
            plyatck = math.floor(plyatck / 2)
            plycharge = False
        enemydefending = False

    elif ply == 'defend':
        print('\033[1;34mYou defended! You won\'t take damage this turn.\033[0m')
        enemydefending = False
        plydefending = True

    elif ply == 'charge' and plycharge == False:
        print('\033[1;32mYou charged! You will do double damage on your next attack!\033[0m')
        if plyatckplus != 0:
            plyatck -= plyatckplus
            plyatck *= 2
            plyatck += plyatckplus
        else:
            plyatck *= 2
        plycharge = True
        if companion == '':
            enemydefending = False

    elif ply == 'charge' and plycharge == True:
        print('\033[1;32mYou tried to charge again!\033[0m But nothing happened...')
        if companion == '':
            enemydefending = False

    elif ply == 'special':
        if specialcharge == 0 and weaponability == 1:
            if enemydefending:
                print(f"\033[1;31mYou use {weaponspecial}! You deal {(weaponnumber + plyatck) // 4} damage to {enemyname}!\033[0m")
                enemyhealth -= ((plyatck + weaponnumber) // 4)
            else:
                print(f"\033[1;31mYou use {weaponspecial}! You deal {weaponnumber + plyatck} damage to {enemyname}!\033[0m")
                enemyhealth -= (plyatck + weaponnumber)
            if plycharge == True:
                plyatck = math.floor(plyatck / 2)
                plycharge = False
            if companion == '':
                enemydefending = False
            specialcharge = specialchargeDEFAULT
        elif specialcharge == 0 and weaponability == 2:
            if companion == '':
                print(f"\033[1;32mYou use {weaponspecial}! You gain +{weaponnumber} attack for your next attack.\033[0m")
                plyatck += weaponnumber
                plyatckplus += weaponnumber
                specialcharge = specialchargeDEFAULT
                enemydefending = False
            else:
                print(f"\033[1;32mYou use {weaponspecial}! You and {companion} gain +{weaponnumber} attack for your next attack.\033[0m")
                plyatck += weaponnumber
                plyatckplus += weaponnumber
                specialcharge = specialchargeDEFAULT
                companionatck += weaponnumber
        elif specialcharge == 0 and weaponability == 3:
            if companion == '':
                print(f"\033[1;33mYou use {weaponspecial}! You healed +{weaponnumber} health.\033[0m")
                plyhealth += weaponnumber
                specialcharge = specialchargeDEFAULT
                enemydefending = False
            else:
                print(f"\033[1;33mYou use {weaponspecial}! You and {companion} healed +{weaponnumber} health.\033[0m")
                plyhealth += weaponnumber
                companionhealth += weaponnumber
                specialcharge = specialchargeDEFAULT
        elif specialcharge == 0 and weaponability == 4:
            print(f"\033[1;34mYou use {weaponspecial}! You gain +{weaponnumber} defense for the rest of the fight.\033[0m")
            plydefense += weaponnumber
            specialcharge = specialchargeDEFAULT
        elif specialcharge != 0 and weaponspecial != 'Nothing':
            print(f"\033[1;30mYou cannot use {weaponspecial} yet. You still have to wait {specialcharge} turns.\033[0m")
            plyerror = True
        else:
            plyerror = True

    elif ply == 'check':
        if companion == '':
            print(f"""\033[1;32mYOU:
    CURRENT HP - {plyhealth}
    CURRENT ATTACK - {plyatck} ({weapon})
    CURRENT DEFENSE - {plydefense}
\033[1;35m{enemyname}:
    CURRENT HP - {enemyhealth}
    CURRENT ATTACK - {enemyatck}
    CURRENT DEFENSE - {enemydefense}\033[0m""")
        else:
            print(f"""\033[1;32mYOU:
    CURRENT HP - {plyhealth}
    CURRENT ATTACK - {plyatck} ({weapon})
    CURRENT DEFENSE - {plydefense}
\033[1;33m{companion}
    CURRENT HP - {companionhealth}
    CURRENT ATTACK - {companionatck}
    CURRENT DEFENSE - {companiondefense}
\033[1;35m{enemyname}:
    CURRENT HP - {enemyhealth}
    CURRENT ATTACK - {enemyatck}
    CURRENT DEFENSE - {enemydefense}\033[0m""")

    elif ply == 'check self' or ply == 'check me':
        print(f"""\033[1;32mYOU:
    CURRENT HP - {plyhealth}
    CURRENT ATTACK - {plyatck} ({weapon})
    CURRENT DEFENSE - {plydefense}\033[0m""")

    elif ply == 'check companion':
        if companion == '':
            print("You do not have a companion.")
        else:
            print(f"""\033[1;35m{companion}:
    CURRENT HP - {companionhealth}
    CURRENT ATTACK - {companionatck}
    CURRENT DEFENSE - {companiondefense}\033[0m""")

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
                print(f"\033[1;31mSPECIAL: {weaponspecial} - Deals {weaponnumber + plyatck} damage to {enemyname}. Deals only a fourth of the damage if {enemyname} is defending.\033[0m")
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

    elif ply == 'quit':
        quit()

    else:
        plyerror = True

    global companiondefending, companionatckDEFAULT

    if companion != '':

        if ply == 'attack':
            if companionatck - enemydefense > 0:
                print(f"\033[1;31m{companion} {companionphrase} {enemyname} for {companionatck - enemydefense} damage!\033[0m")
                enemyhealth = enemyhealth - (companionatck - enemydefense)
            else:
                print(f"\033[1;31m{companion} {companionphrase} {enemyname} for 1 damage!\033[0m")
                enemyhealth -= 1
            companionatck = companionatckDEFAULT

        elif ply == 'defend':
            print(f'\033[1;34m{companion} defended! They won\'t take damage this turn.\033[0m')
            companiondefending = True

        elif ply == 'charge' and enemydefending == False:
            if companionatck - enemydefense > 0:
                print(f"\033[1;31m{companion} {companionphrase} {enemyname} for {companionatck - enemydefense} damage!\033[0m")
                enemyhealth = enemyhealth - (companionatck - enemydefense)
            else:
                print(f"\033[1;31m{companion} {companionphrase} {enemyname} for 1 damage!\033[0m")
                enemyhealth -= 1
            companionatck = companionatckDEFAULT

        elif ply == 'charge' and enemydefending == True:
            print(f"\033[1;31m{companion} {companionphrase} {enemyname}. \033[1;35mBut {enemyname} defended.\033[0m")
            enemydefending = False
            companionatck = companionatckDEFAULT

        else:
            if enemydefending == False:
                if companionatck - enemydefense > 0:
                    print(f"\033[1;31m{companion} {companionphrase} {enemyname} for {companionatck - enemydefense} damage!\033[0m")
                    enemyhealth = enemyhealth - (companionatck - enemydefense)
                else:
                    print(f"\033[1;31m{companion} {companionphrase} {enemyname} for 1 damage!\033[0m")
                    enemyhealth -= 1
                companionatck = companionatckDEFAULT
            elif enemydefending == True:
                print(f'\033[1;34m{companion} defended! They won\'t take damage this turn.\033[0m')
                companiondefending = True
                enemydefending = False
    return True

def enemymove():
    import random
    global plydefense, plyhealth, enemyatck, enemydefense, enemyhealth, enemycharge, enemydefense, enemydefending, plydefending, enemytarget
    global enemyspecial, enemyspecialcount, enemyspecialcountDEFAULT, enemyspecialmove, enemyspecialtype, enemyspecialnumber, enemyatckplus
    global companion, companiondefending, companionhealth

    enemyaction = random.randint(1, 9)
    if enemytarget == 0:
        if enemyspecial == True:
            if enemyspecialcount == 0:
                print(f"\033[1;3{enemyspecialtype}m{enemyname} used their speical move, {enemyspecialmove}!\033[0m")
                if enemyspecialtype == 1:
                    if plydefending == True:
                        print(f"\033[1;3{enemyspecialtype}m{enemyname} deals {int(enemyspecialnumber / 4)} damage to you.\033[0m")
                        plyhealth -= int(enemyspecialnumber / 4)
                    else:
                        print(f"\033[1;3{enemyspecialtype}m{enemyname} deals {enemyspecialnumber} damage to you.\033[0m")
                        plyhealth -= enemyspecialnumber
                    plydefending = False
                    enemydefending = False
                    companiondefending = False
                elif enemyspecialtype == 2:
                    print(f"\033[1;3{enemyspecialtype}m{enemyname} gains +{enemyspecialnumber} attack for their next attack.\033[0m")
                    enemyatck += enemyspecialnumber
                    enemyatckplus += enemyspecialnumber
                    plydefending = False
                    enemydefending = False
                    companiondefending = False
                elif enemyspecialtype == 3:
                    print(f"\033[1;3{enemyspecialtype}m{enemyname} heals {enemyspecialnumber} health.\033[0m")
                    enemyhealth += enemyspecialnumber
                    plydefending = False
                    enemydefending = False
                    companiondefending = False
                elif enemyspecialtype == 4:
                    print(f"\033[1;3{enemyspecialtype}m{enemyname} gains +{enemyspecialnumber} defense for the rest of the fight.\033[0m")
                    enemydefense += enemyspecialnumber
                    plydefending = False
                    enemydefending = False
                    companiondefending = False
                else:
                    print("But it didn't do anything because they don't have a valid command.")
                enemyspecialcount = enemyspecialcountDEFAULT
            else:
                enemyspecialcount -= 1
                if enemyaction > 6 and plydefending == True:
                    print(f"\033[1;31m{enemyname} {enemyphrase} you. \033[1;34mBut you defended!\033[0m")
                    enemyatck = enemyatckDEFAULT
                    enemycharge = False
                    enemydefending = False
                    plydefending = False
                    companiondefending = False
                elif enemyaction > 6 and plydefending == False:
                    if enemyatck - plydefense > 0:
                        print(f"\033[1;31m{enemyname} {enemyphrase} you for {enemyatck - plydefense} damage!\033[0m")
                        plyhealth = plyhealth - (enemyatck - plydefense)
                    else:
                        print(f"\033[1;31m{enemyname} {enemyphrase} you for 1 damage!\033[0m")
                        plyhealth -= 1
                    enemyatck = enemyatckDEFAULT
                    enemycharge = False
                    enemydefending = False
                    companiondefending = False
                elif enemyaction < 4:
                    print(f"\033[1;34m{enemyname} defended! {enemyname} won't take damage next turn!\033[0m")
                    enemydefending = True
                    plydefending = False
                    companiondefending = False
                elif enemyaction > 3 and enemyaction < 7 and enemycharge == False:
                    print(f"\033[1;32m{enemyname} charged! {enemyname}'s next attack will do double damage!\033[0m")
                    enemycharge = True
                    if enemyatckplus != 0:
                        enemyatck -= enemyatckplus
                        enemyatck *= 2
                        enemyatck += enemyatckplus
                    else:
                        enemyatck *= 2
                    enemydefending = False
                    plydefending = False
                    companiondefending = False
                elif enemyaction > 3 and enemyaction < 7 and enemycharge == True:
                    print(f"\033[1;32m{enemyname} tried to charge! \033[0mBut {enemyname} already did.")
                    plydefending = False
                    companiondefending = False
                else:
                    print("This will only print if something went horribly wrong.")
                if enemyspecialcount == 1:
                    print(f"\033[1;3{enemyspecialtype}m{enemyname} looks to be readying something strong.\033[0m")
                    enemyspecialcount = 0
        else:
            if enemyaction > 6 and plydefending == True:
                print(f"\033[1;31m{enemyname} {enemyphrase} you. \033[1;34mBut you defended!\033[0m")
                enemyatck = enemyatckDEFAULT
                enemycharge = False
                enemydefending = False
                plydefending = False
                companiondefending = False
            elif enemyaction > 6 and plydefending == False:
                if enemyatck - plydefense > 0:
                    print(f"\033[1;31m{enemyname} {enemyphrase} you for {enemyatck - plydefense} damage!\033[0m")
                    plyhealth = plyhealth - (enemyatck - plydefense)
                else:
                    print(f"\033[1;31m{enemyname} {enemyphrase} you for 1 damage!\033[0m")
                    plyhealth -= 1
                enemyatck = enemyatckDEFAULT
                enemycharge = False
                enemydefending = False
                companiondefending = False
            elif enemyaction < 4:
                print(f"\033[1;34m{enemyname} defended! {enemyname} won't take damage next turn!\033[0m")
                enemydefending = True
                plydefending = False
                companiondefending = False
            elif enemyaction > 3 and enemyaction < 7 and enemycharge == False:
                print(f"\033[1;32m{enemyname} charged! {enemyname}'s next attack will do double damage!\033[0m")
                enemycharge = True
                enemyatck *= 2
                enemydefending = False
                plydefending = False
                companiondefending = False
            elif enemyaction > 3 and enemyaction < 7 and enemycharge == True:
                print(f"\033[1;32m{enemyname} tried to charge! \033[0mBut {enemyname} already did.")
                plydefending = False
                companiondefending = False
            else:
                print("This will only print if something went horribly wrong.")
    elif enemytarget == 1:
        if enemyspecial == True:
            if enemyspecialcount == 0:
                print(f"\033[1;3{enemyspecialtype}m{enemyname} used their speical move, {enemyspecialmove}!\033[0m")
                if enemyspecialtype == 1:
                    if companiondefending == True:
                        print(f"\033[1;34mBut {companion} defended.")
                    else:
                        print(f"\033[1;3{enemyspecialtype}m{enemyname} deals {enemyspecialnumber} damage to {companion}.\033[0m")
                        companionhealth -= enemyspecialnumber
                    plydefending = False
                    companiondefending = False
                    enemydefending = False
                elif enemyspecialtype == 2:
                    print(f"\033[1;3{enemyspecialtype}m{enemyname} gains +{enemyspecialnumber} attack for their next attack.\033[0m")
                    enemyatck += enemyspecialnumber
                    enemyatckplus += enemyspecialnumber
                    plydefending = False
                    companiondefending = False
                    enemydefending = False
                elif enemyspecialtype == 3:
                    print(f"\033[1;3{enemyspecialtype}m{enemyname} heals {enemyspecialnumber} health.\033[0m")
                    enemyhealth += enemyspecialnumber
                    plydefending = False
                    companiondefending = False
                    enemydefending = False
                elif enemyspecialtype == 4:
                    print(f"\033[1;3{enemyspecialtype}m{enemyname} gains +{enemyspecialnumber} defense for the rest of the fight.\033[0m")
                    enemydefense += enemyspecialnumber
                    plydefending = False
                    companiondefending = False
                    enemydefending = False
                else:
                    print("But it didn't do anything because they don't have a valid command.\033[0m")
                enemyspecialcount = enemyspecialcountDEFAULT
            else:
                enemyspecialcount -= 1
                if enemyaction > 6 and companiondefending == True:
                    print(f"\033[1;31m{enemyname} {enemyphrase} {companion}. \033[1;34mBut {companion} defended!\033[0m")
                    enemyatck = enemyatckDEFAULT
                    enemycharge = False
                    enemydefending = False
                    plydefending = False
                    companiondefending = False
                elif enemyaction > 6 and companiondefending == False:
                    if enemyatck - companiondefense > 0:
                        print(f"\033[1;31m{enemyname} {enemyphrase} {companion} for {enemyatck - companiondefense} damage!\033[0m")
                        companionhealth -= (enemyatck - companiondefense)
                    else:
                        print(f"\033[1;31m{enemyname} {enemyphrase} {companion} for 1 damage!\033[0m")
                        companionhealth -= 1
                    enemyatck = enemyatckDEFAULT
                    enemycharge = False
                    enemydefending = False
                    plydefending = False
                elif enemyaction < 4:
                    print(f"\033[1;34m{enemyname} defended! {enemyname} won't take damage next turn!\033[0m")
                    enemydefending = True
                    plydefending = False
                    companiondefending = False
                elif enemyaction > 3 and enemyaction < 7 and enemycharge == False:
                    print(f"\033[1;32m{enemyname} charged! {enemyname}'s next attack will do double damage!\033[0m")
                    enemycharge = True
                    if enemyatckplus != 0:
                        enemyatck -= enemyatckplus
                        enemyatck *= 2
                        enemyatck += enemyatckplus
                    else:
                        enemyatck *= 2
                    enemydefending = False
                    plydefending = False
                    companiondefending = False
                elif enemyaction > 3 and enemyaction < 7 and enemycharge == True:
                    print(f"\033[1;32m{enemyname} tried to charge! \033[0mBut {enemyname} already did.")
                    plydefending = False
                    companiondefending = False
                else:
                    print("This will only print if something went horribly wrong.")
                if enemyspecialcount == 1:
                    print(f"\033[1;3{enemyspecialtype}m {enemyname} looks to be readying something strong.\033[0m")
                    enemyspecialcount = 0
        else:
            if enemyaction > 6 and companiondefending == True:
                print(f"\033[1;31m{enemyname} {enemyphrase} {companion}. \033[1;34mBut {companion} defended!\033[0m")
                enemyatck = enemyatckDEFAULT
                enemycharge = False
                enemydefending = False
                plydefending = False
                companiondefending = False
            elif enemyaction > 6 and companiondefending == False:
                if enemyatck - companiondefense > 0:
                    print(f"\033[1;31m{enemyname} {enemyphrase} {companion} for {enemyatck - companiondefense} damage!\033[0m")
                    companionhealth = companionhealth - (enemyatck - companiondefense)
                else:
                    print(f"\033[1;31m{enemyname} {enemyphrase} {companion} for 1 damage!\033[0m")
                    companionhealth -= 1
                enemyatck = enemyatckDEFAULT
                enemycharge = False
                enemydefending = False
            elif enemyaction < 4:
                print(f"\033[1;34m{enemyname} defended! {enemyname} won't take damage next turn!\033[0m")
                enemydefending = True
                plydefending = False
                companiondefending = False
            elif enemyaction > 3 and enemyaction < 7 and enemycharge == False:
                print(f"\033[1;32m{enemyname} charged! {enemyname}'s next attack will do double damage!\033[0m")
                enemycharge = True
                enemyatck *= 2
                enemydefending = False
                plydefending = False
                companiondefending = False
            elif enemyaction > 3 and enemyaction < 7 and enemycharge == True:
                print(f"\033[1;32m{enemyname} tried to charge! \033[0mBut {enemyname} already did.")
                plydefending = False
            else:
                print("This will only print if something went horribly wrong.")

    if companion != '':
        enemytarget = random.randint(0, 1)

def battletrainer():
    global ply, weapon, armor, plyturn, plyerror, enemyhealth, plyhealth, enemymove, companionhealth, enemyname, plydead, plydefense, swordstrength, plyatck, plyhealth
    global companion, companionhealth, companionatck, companionatckDEFAULT, companiondefense, companiondefending, enemytarget, photocheck

    ply = input('What health do you want to start at?\n>')
    if ply.isdigit():
        plyhealth = int(ply)
        if plyhealth <= 0:
            print('You will start at 1 HP.')
            plyhealth = 1
        else:
            print(f'You will start at {plyhealth} HP.')
    else:
        print("Invalid Input. You will start at 10 HP")
        plyhealth = 10

    ply = input('What weapon would you like?\n>').lower()
    match ply:
        case 'splinters':
            print("Granting you access to the SPLINTERS (+1 Attack)")
            weapon = 'Splinters'
            plyatck = 6
        case 'pretend splinters':
            print("Granting you access to the PRETEND SPLINTERS (-1 Attack)")
            weapon = 'Pretend Splinters'
            plyatck = 4
        case 'crowbar':
            print("Granting you access to the CROWBAR (+2 Attack)")
            weapon = 'Crowbar'
            plyatck = 7
        case 'brick':
            print("Granting you access to the BRICK (+1 Attack)")
            weapon = 'Brick'
            plyatck = 6
        case 'shard':
            print("Granting you access to the SHARD (+3 Attack)")
            weapon = 'Shard'
            plyatck = 8
        case 'sword':
            weapon = 'Sword'
            ply = input('What strength is the sword?\n>')
            if ply.isdigit():
                swordstrength = int(ply)
            else:
                print("That is not a number.")
                swordstrength = 5
            print(f"Granting you access to the SWORD (+{swordstrength} Attack)")
            plyatck = 5 + swordstrength
        case 'key':
            print("Granting you access to the KEY (+1 Attack)")
            weapon = 'Key'
            plyatck = 6
        case 'lantern':
            print("Granting you access to the LANTERN (+1 Attack)")
            weapon = 'Lantern'
            plyatck = 6
        case 'alien blaster':
            print("Granting you access to the ALIEN BLASTER (+10 Attack)")
            weapon = 'Alien Blaster'
            plyatck = 15
        case _:
            print("You will start with no weapon.")
            weapon = 'Nothing'
            plyatck = 5

    ply = input('What armor would you like?\n>').lower()
    match ply:
        case 'stool':
            print("Granting you access to the STOOL (+1 Defense)")
            armor = 'Stool'
            plydefense = 1
        case 'tooth':
            print("Granting you access to the TOOTH (+1 Defense)")
            armor = 'Tooth'
            plydefense = 1
        case 'splinters':
            print("Granting you access to the SPLINTERS (+1 Defense)")
            armor = 'Splinters'
            plydefense = 1
        case 'shield':
            ply = input('What strength is the shield?\n>')
            if ply.isdigit():
                ply = int(ply)
            else:
                ply = 3
                print("That is not a number.")
            print(f"Granting you access to the SHIELD (+{ply} Defense)")
            armor = 'Shield'
            plydefense = ply
        case 'bandana':
            print("Granting you access to the BANDANA (+2 Attack, -1 Defense)")
            armor = 'Shield'
            plyatck += 2
            plydefense = -1
        case _:
            print("You will start with no armor.")
            armor = 'Nothing'
            plydefense = 0

    ply = input('What companion would you like?\n>').lower()
    match ply:
        case 'mysterious person':
            print("MYSTERIOUS PERSON is now your companion.")
            mysteriouscompanion()
        case 'lenard':
            print("LENARD is now your companion.")
            photocheck = True
            mysteriouscompanion()
        case 'shrek':
            print("""\033[1;32m⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⡇⠀⠿⡀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
   ⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
     ⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀
    ⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
  ⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿
  ⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀
  ⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
       ⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
        ⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
         ⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
       ⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
       ⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
        ⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠉⠛⠻⠿⠿⠿⠿⠛⠉\033[0m""")
            shrekcompanion()
        case 'markiplier':
            print("""\033[1;93m            ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣮⣝⡯⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢼⣧⣿⣿⣿⡿⠻⠿⢿⣯⣿⣮⣀⡁⢑⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⡟⠁⠀⠙⠧⠞⠈⢓⣿⣿⣿⣿⢿⣾⣷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣫⠟⠀⠀⠀⠀⠀⠀⠀⠀⡙⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⢈⢻⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⠁⠚⣛⣒⠀⠀⠀⡀⠐⢒⡒⠳⠤⢺⣟⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠋⠀⠋⠚⠛⠃⢈⣩⣓⢮⠿⠯⠷⠀⠀⢽⣿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠄⠀⠀⠀⠀⠀⠀⢸⠩⠀⠀⠀⠀⠀⠀⠀⢻⡤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠔⡸⡎⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠈⠀⡳⣿⠆⠄⠀⠀⠁⠀⠠⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠘⠤⡔⢎⣵⣸⢯⠜⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⣠⣆⣿⣿⣾⣹⣏⢳⣄⡀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣸⠤⠋⠙⠓⠶⠖⣾⠾⠟⠋⢣⣲⣦⡾⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣶⣶⣾⣽⣿⢷⠀⢈⠃⢙⠃⠀⠀⠀⢐⡾⣾⡿⠃⠀⠀⠠⣄⠀⠀⠀⠀
⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣯⣆⢣⣑⣄⠴⡇⣽⣦⣢⣾⣾⠋⡀⠐⠀⠁⢀⣿⣷⣄⠀⠀
⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣗⣉⣛⣿⣶⣟⣿⣿⣛⣁⣐⣀⣀⣀⣠⣶⣿⣡⣨⣟⣑⣢""")
            print('\"Hello everybody, my name is Markiplier and welcome, to ALIEN.\nNow normally, I would be chilling in the background doing nothing, but these greedy developers have decided to put me in as a companion.\nLuckily for you, it means that you\'ll watch me be on the winning side of this war.\"\033[0m')
            markipliercompanion()
        case 'custom':
            print("You will have a CUSTOM COMPANION.")
            customcompanion()
        case _:
            print("You will have no companion.")
            companion = ''

    ply = input('What enemy would you like to fight?\n>').lower()
    match ply:
        case 'door' | 'true door':
            print("You will fight the TRUE DOOR")
            truedoor()
        case 'void':
            print("You will fight the VOID")
            voidenemy()
        case 'beast':
            print("You will fight the BEAST")
            beastenemy()
        case 'mysterious person':
            print("You will fight the MYSTERIOUS PERSON")
            mysteriousPerson()
        case 'alien':
            print("You will fight the \033[1;36m🅐🅛🅘🅔🅝\033[0m")
            alienenemy()
        case 'custom':
            print("You will fight a CUSTOM ENEMY")
            customenemy()
        case 'shrek':
            print("""\033[1;31m⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⡇⠀⠿⡀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
   ⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
     ⢀⡀⠁⠀⠀    ⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀
    ⢀⡾⣁⣀⠀     ⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
  ⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿   ⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿
  ⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿  ⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀
  ⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
       ⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
        ⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
         ⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
       ⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
       ⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
        ⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠉⠛⠻⠿⠿⠿⠿⠛⠉\033[0m""")
            shreksecretenemy()
        case 'markiplier':
            if companion != 'Markiplier':
                print("""\033[1;33m            ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣮⣝⡯⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢼⣧⣿⣿⣿⡿⠻⠿⢿⣯⣿⣮⣀⡁⢑⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⡟⠁⠀⠙⠧⠞⠈⢓⣿⣿⣿⣿⢿⣾⣷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣫⠟⠀⠀⠀⠀⠀⠀⠀⠀⡙⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⢈⢻⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⠁⠚⣛⣒⠀⠀⠀⡀⠐⢒⡒⠳⠤⢺⣟⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠋⠀⠋⠚⠛⠃⢈⣩⣓⢮⠿⠯⠷⠀⠀⢽⣿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠄⠀⠀⠀⠀⠀⠀⢸⠩⠀⠀⠀⠀⠀⠀⠀⢻⡤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠔⡸⡎⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠈⠀⡳⣿⠆⠄⠀⠀⠁⠀⠠⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠘⠤⡔⢎⣵⣸⢯⠜⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⣠⣆⣿⣿⣾⣹⣏⢳⣄⡀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣸⠤⠋⠙⠓⠶⠖⣾⠾⠟⠋⢣⣲⣦⡾⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣶⣶⣾⣽⣿⢷⠀⢈⠃⢙⠃⠀⠀⠀⢐⡾⣾⡿⠃⠀⠀⠠⣄⠀⠀⠀⠀
⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣯⣆⢣⣑⣄⠴⡇⣽⣦⣢⣾⣾⠋⡀⠐⠀⠁⢀⣿⣷⣄⠀⠀
⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣗⣉⣛⣿⣶⣟⣿⣿⣛⣁⣐⣀⣀⣀⣠⣶⣿⣡⣨⣟⣑⣢""")
                print('\"Hello everybody, my name is Markiplier and welcome, to ALIEN.\nNow this game seems to have put me in as a very secret boss fight that you can only find in the battle trainer.\nWhoops. It seems that someone has activated that calling, so I must put you all on hold and go beat some ass.\"\033[0m')
            else:
                print("""\033[1;30m            ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣮⣝⡯⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢼⣧⣿⣿⣿⡿⠻⠿⢿⣯⣿⣮⣀⡁⢑⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⡟⠁⠀⠙⠧⠞⠈⢓⣿⣿⣿⣿⢿⣾⣷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣫⠟⠀⠀⠀⠀⠀⠀⠀⠀⡙⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⢈⢻⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⠁⠚⣛⣒⠀⠀⠀⡀⠐⢒⡒⠳⠤⢺⣟⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠋⠀    ⢈⣩⣓⢮   ⠀⠀⢽⣿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠄⠀⠀⠀⠀⠀⠀⢸⠩⠀⠀⠀⠀⠀⠀⠀⢻⡤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠔⡸⡎⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠈⠀⡳⣿⠆⠄⠀⠀⠁⠀⠠⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠘⠤⡔⢎⣵⣸⢯⠜⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⣠⣆⣿⣿⣾⣹⣏⢳⣄⡀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣸⠤⠋⠙⠓⠶⠖⣾⠾⠟⠋⢣⣲⣦⡾⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣶⣶⣾⣽⣿⢷⠀⢈⠃⢙⠃⠀⠀⠀⢐⡾⣾⡿⠃⠀⠀⠠⣄⠀⠀⠀⠀
⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣯⣆⢣⣑⣄⠴⡇⣽⣦⣢⣾⣾⠋⡀⠐⠀⠁⢀⣿⣷⣄⠀⠀
⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣗⣉⣛⣿⣶⣟⣿⣿⣛⣁⣐⣀⣀⣀⣠⣶⣿⣡⣨⣟⣑⣢""")
                print('\"Hey all, Mark here. Welcome to ALIEN.\nNow normally, I would be busy NOT playing Five Nights at Freddy\'s, but it seems that my counterpart has teamed up with the player.\nUnfortuantly for me, it means I have to do my job of beating some ass.\"\033[0m')
            markipliersecretenemy()
        case _:
            print("You will fight the PLASTIC DINOSAUR")
            plasticDino()

    plyspecial()
    battlestart()
    plypos = -1

    while plypos == -1:

        if plyturn == True and plyhealth > 0:
            plymove()
            plyturn = False
            pass
            if plyerror == True:
                print("That is not a move that you have access to. Try again.")
                plymove()
                pass
                if plyerror == True:
                    print("You end up forgeting what viable moves you have while training.")
                    pass
            if enemyhealth <= 0 and plyhealth > 0:
                print("You won!\nReturning to Start Screen.\033[0m")
                plyturn = True
                plypos = 0
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

        if plyturn == False and plyhealth > 0 and enemyhealth > 0:
            enemymove()
            plyturn = True
            pass
            if plyhealth <= 0:
                print("You lose.\n\nReturning to Start Screen.")
                plypos = 0
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
            if companionhealth <= 0 and companion != '':
                print("The enemy manages to defeat your companion.")
                companion = ''
                companionhealth = 0
                companionatck = 0
                companionatckDEFAULT = 0
                companiondefense = 0
                companiondefending = False
                enemytarget = 0

def companiontalk():
    global talkcounter
    if companion == 'Lenard':
        if talkcounter == 0:
            print('You try to talk to Lenard.')
            print('They don\'t seem to be up for conversation right now.')
        match plypos:
            case 22:
                if talkcounter == 3:
                    if photocheck == True:
                        print('You talk to Lenard. You explain that you saw their name on a photo at a weird house south.')
                        print('They talks about how he used to live there with a loving family. However, they mentions that the beast you recently fought ended up killing their family in an incident.')
                        print('You feel remorse.')
                    else:
                        print('You talk to Lenard. You ask them if they knows anything about that beast you encountered.')
                        print('They slightly turn their head away from you.')
                    talkcounter -= 1
                elif talkcounter == 2:
                    if photocheck == True:
                        print('You talk to Lenard again. You ask them if they know anything about an alien you\'re on the search for.')
                        print('They respond by telling you they have not seen any aliens around here, but they also consider that the beast might be associated with them.')
                    else:
                        print('You ask Lenard what if anything is wrong.')
                        print('They look frustrated.')
                    talkcounter -= 1
                elif talkcounter == 1:
                    if photocheck == True:
                        print('You ask Lenard where they get all of their rocks from.')
                        print('Lenard starts to have a confused look as they realize that they too do not know how they have so many rocks with them.')
                    else:
                        print('You try to talk to Lenard.')
                        print('They tell you to shut up.')
                    talkcounter -= 1

def globalcommands():
    # skip the void for this one, it parses commands differently
    global ply, inventory, plyhealth, plydefense, doorbroken, plydead, plypos, tookstool, dinodead, dinoseen, equippeditem, plyatck, weapon, armor, kys, swordstrength
    match ply:
        case 'look around' | 'look':
            print("Perhaps you should try to specify what direction you want to look in.")
            return True
        case "kill me" | "kill myself":
            if kys == True:
                print("You decide to not attempt self-harm again.")
            elif plyatck < 10:
                print("You punched yourself multiple times. You're too weak to deal any damage.")
                kys = True
            elif plyatck >= 10 and plyatck < 100:
                print("You punched yourself multiple times. You managed to make a dent on yourself. \033[1;31mYou take 1 Damage.\033[0m")
                plyhealth -= 1
                if plyhealth == 0:
                    print("Amazingly, you managed to dispatch yourself using your own fists. Moron.\n\n\n\033[1;31mGame Over, I guess?")
                    plydead = True
                kys = True
            elif plyatck >= 100:
                print("You already have enough power, you cannot stop here.")
                kys = True
            return True
        case 'check inventory' | 'inventory' | 'open inventory':
            currentitem = ''
            if len(inventory) == 0:
                print('\033[1;33mYou do not have any items in your inventory currently.\033[0m')
            else:
                for x in inventory:
                    currentitem = x
                    if currentitem == weapon and currentitem != 'Nothing':
                        print('\033[1;31m' + x + '\033[0m')
                    elif currentitem == armor and currentitem != 'Nothing':
                        print('\033[1;34m' + x + '\033[0m')
                    else:
                        print('\033[1;33m' + x + '\033[0m')
            return True
        case 'quit':
            print("Ok, bye then.")
            quit()
        case ':(':
            print('Why are you mad?')
            return True
        case ':)':
            print('What are you smirking about?')
            return True
        case 'talk':
            if companion != '':
                companiontalk()
                return True
            else:
                return False
        case 'equip item':
            print("Please make sure to specify what item to equip. (EXAMPLE: Equip Hammer)")
            return True
        case 'toss branch':
            if weapon == 'Sword' and 'Branch' in inventory:
                print("You end up tossing away the branch.\n\033[1;33mBRANCH removed from your inventory.\033[0m")
                inventory.remove('Branch')
                return True
            else:
                return False
        case 'toss splinters':
            if weapon == 'Sword' and stoolExplode == False and 'Splinters' in inventory:
                print("You end up tossing away the splinters.\n\033[1;33mSPLINTERS removed from your inventory.\033[0m")
                inventory.remove('Splinters')
                return True
            else:
                return False
        case 'toss brick':
            if weapon == 'Sword' and 'Brick' in inventory:
                print("You end up tossing away the brick.\n\033[1;33mBRICK removed from your inventory.\033[0m")
                inventory.remove('Brick')
                return True
            else:
                return False
        case 'toss map':
            if weapon == 'Sword' and 'Map' in inventory:
                print("You end up tossing away the map.\n\033[1;33mMAP removed from your inventory.\033[0m")
                inventory.remove('Map')
                return True
            else:
                return False
        case 'toss nothing':
            if weapon == 'Sword' and 'Nothing' in inventory:
                print("You end up tossing away nothing.\n\033[1;33mNOTHING removed from your inventory.\033[0m")
                inventory.remove('Nothing')
                return True
            else:
                return False
        case 'toss crowbar':
            if weapon == 'Sword' and 'Crowbar' in inventory:                    
                print("You end up tossing away the crowbar.\n\033[1;33mCROWBAR removed from your inventory.\033[0m")
                inventory.remove('Crowbar')
                return True
            else:
                return False
        case 'toss key':
            if weapon == 'Sword' and 'Key' in inventory and plypos != 18:
                print("You end up tossing away the key.\n\033[1;33mKEY removed from your inventory.\033[0m")
                inventory.remove('Key')
                return True
            else:
                return False
        case 'toss pretend splinters':
            if weapon == 'Sword' and 'Pretend Splinters' in inventory:
                print("You pretend to toss away the pretend splinters.\n\033[1;33mPRETEND SPLINTERS removed from your inventory.\033[0m")
                inventory.remove('Pretend Splinters')
                return True
            else:
                return False
        case 'toss alien blaster':
            if weapon == 'Sword' and 'Alien Blaster' in inventory:
                print("Don't get why you would throw away a really good item, but ok?\n\033[1;33mALIEN BLASTER removed from your inventory.\033[0m")
                inventory.remove('Alien Blaster')
                return True
            else:
                return False
        case 'idk' | 'i dont know' | 'i don\'t know' | 'i dunno':
            print("Then figure \033[1;31mit\033[0m out.")
            return True
        case 'think' | 'check' | 'hint':
            if plypos == 1 and doorbroken == False and plydead == False and plydeaths == 0:
                print(roomhints['1A'])
            elif plypos == 1 and doorbroken == True and plydead == False:
                print(roomhints['1B'])
            elif plypos == 3 and tookstool == False and plydead == False and dinodead == False and dinoseen == False:
                print(roomhints['3A'])
            elif plypos == 3 and tookstool == False and plydead == False and dinodead == False and dinoseen == True:
                print(roomhints['3B'])
            elif plypos == 3 and tookstool == False and plydead == False and dinodead == True:
                print(roomhints['3C'])
            elif plypos == 3 and tookstool == True and plydead == False and 'Stool' in inventory:
                print(roomhints['3BA'])
            elif plypos == 3 and tookstool == True and plydead == False and 'Stool' not in inventory:
                print(roomhints['3BB'])
            elif plypos == 1 and doorbroken == False and plydead == False and plydeaths != 0:
                print(roomhints['1XA'])
            elif plypos == 5 and plydead == False:
                print(roomhints['5A'])
            elif plypos == 6 and plydead == False:
                print(roomhints['6A'])
            return True
        case "check me" | "check myself" | "check self":
            print("YOU \nCURRENT HP: " + str(plyhealth) + "\n\033[1;31mATTACK: " + str(plyatck) + " \033[1;33m(" + weapon + ")\n\033[1;34mDEFENSE: " + str(plydefense) + " \033[1;33m(" + armor + ")\033[0m")
            if plypos == 1 and doorbroken == False and plydead == False:
                print(selfcheckroom['1A'])
            elif plypos == 1 and doorbroken == True and plydead == False:
                print(selfcheckroom['1B'])
            elif plypos == 3 and tookstool == False and plydead == False and dinodead == False and dinoseen == False:
                print(selfcheckroom['3A'])
            elif plypos == 3 and tookstool == False and plydead == False and dinodead == False and dinoseen == True:
                print(selfcheckroom['3B'])
            elif plypos == 3 and tookstool == False and plydead == False and dinodead == True:
                print(selfcheckroom['3C'])
            elif plypos == 3 and tookstool == True and plydead == False and 'Stool' in inventory:
                print(selfcheckroom['3BA'])
            elif plypos == 3 and tookstool == True and plydead == False and 'Stool' not in inventory:
                print(selfcheckroom['3BB'])
            elif plypos == 1 and doorbroken == False and plydead == False and plydeaths != 0:
                print(selfcheckroom['1XA'])
            elif plypos == 5 and plydead == False:
                print(selfcheckroom['5A'])
            elif plypos == 6 and plydead == False:
                print(selfcheckroom['6A'])
            return True
        case 'kill skeleton but awesome':
            if weapon == 'Sword':
                print('You activate the failsafe.\n\033[1;33mThe Sword gained \033[1;31m+15 attack power.\033[0m')
                swordstrength += 15
                plyatck = plyatckDEFAULT + swordstrength
            else:
                print('You cannot kill a skeleton awesomely.') # Fuck you.
            return True
        case _:
            if ply.startswith("equip "):
                item_to_equip = ply[6:].strip().title()
                if item_to_equip in inventory:
                    equippeditem = item_to_equip
                else:
                    return False
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
                            print("You feel an overwhelming sense of power.\033[1;31m\nYou gained +3 Attack\033[0m")
                            weapon = "Shard"
                            plyatck = plyatckDEFAULT + 3
                        elif equippeditem == 'Shield':
                            print("You feel an overwhelming sense of courage.\033[1;34m\nYou gained +3 Defense\033[0m")
                            armor = "Shield"
                            plydefense = plydefenseDEFAULT + 3
                        elif equippeditem == 'Sword':
                            print(f"You feel an even greater overwhelming sense of power.\033[1;31m\nYou gained +{swordstrength} Attack\033[0m")
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
                            print("\033[1;30mExcept there was no need. It would only hinder your abilities.\033[0m")
                        elif equippeditem == 'Map':
                            print("\033[1;30mIt doesn't seem to increse your power, but you now can see where you're going in vents.\033[0m")
                            weapon = 'Map'
                            plyatck = plyatckDEFAULT
                        elif equippeditem == 'Bandana':
                            print("You feel the power of a warrior.\n\033[1;31mYou gained +2 Attack.\033[1;34m\nYou gained -1 Defense.\033[0m")
                            armor = "Bandana"
                            plydefense = plydefenseDEFAULT - 1
                        elif equippeditem == 'Alien Blaster':
                            print("\033[1;31mYou gained +10 Attack\033[0m")
                            weapon = "Alien Blaster"
                            plyatck = plyatckDEFAULT + 10
                        else:
                            print(f"\033[1;33mYou don't have a \"{item_to_equip}\" in your inventory.\033[0m")
                        if armor == 'Bandana':
                            plyatck += 2
                return True
            elif ply.startswith("check "):
                item_to_equip = ply[6:].strip().title()
                if item_to_equip in inventory:
                    print("\033[1;33m" + items[item_to_equip] + "\033[0m")
                    return True
            elif 'alien' in ply:
                if 'Alien Blaster' not in inventory:
                    print("You sob due to the lack of aliens in your area.")
                else:
                    print("You relish in the defeat of the secret alien.")
                return True
            elif 'blast' in ply and weapon == 'Alien Blaster':
                print('You fire the alien blaster multiple times. You miss everything you were aiming at. You believe that the blaster only locks on to enemies.')
                return True
            else:
                return False
        
def ventdesc():
    global vent_descriptions, ventpos, ventDirection, plypos
    print((vent_descriptions[ventpos])[ventDirection])

def ventmove_left():
    global vent_walls, ventdesc, ventpos, ventDirection
    if (vent_walls[ventpos])[(ventDirection -1) % 4] == True:
        print('You slam your shoulder into the galvanized steel sheet on your left. It doesn\'t budge.')
    elif (vent_walls[ventpos])[(ventDirection - 1) % 4] == False:
        if ventpos == 6 and ventDirection == 1:
            print('You slam your shoulder into the galvanized steel sheet on your left. Suprisingly, you pass right through it.')
            ventDirection = int((ventDirection - 1) % 4)
            ventpos = 7
            ventdesc()
        elif ventpos == 27 and ventDirection == 3:
            print('You attempt to pass through the stopped fan. While you are halfway through, the fan starts up again. You are cleanly bisected in two. \nGame Over.')
            plydead = True
        elif ventpos == 8 and ventDirection == 0:
            print('You walk into the light. You... walk? Weren\'t you just crawling?\nYou appear to be in some sort of security office. Computer monitors line one wall just above a desk. You are facing east.')
            plypos = 6
        else:
            print("You go left.")
            match ventDirection:
                case 0:
                    ventDirection = 3
                    match ventpos:
                        case 0:
                            ventpos = 1
                            ventdesc()
                        case 1:
                            ventpos = 13
                            ventdesc()
                        case 3:
                            ventpos = 2
                            ventdesc()
                        case 4:
                            ventpos = 3
                            ventdesc()
                        case 5:
                            ventpos = 4
                            ventdesc()
                        case 6:
                            ventpos = 5
                            ventdesc()
                        case 7:
                            ventpos = 8
                            ventdesc()
                        case 9:
                            ventpos = 0
                            ventdesc()
                        case 10:
                            ventpos = 11
                            ventdesc()
                        case 11:
                            ventpos = 12
                            ventdesc()
                        case 16:
                            ventpos = 15
                            ventdesc()
                        case 17:
                            ventpos = 16
                            ventdesc()
                        case 18:
                            ventpos = 17
                            ventdesc()
                        case 20:
                            ventpos = 19
                            ventdesc()
                        case 21:
                            ventpos = 20
                            ventdesc()
                        case 22:
                            ventpos = 6
                            ventdesc()
                        case 23:
                            ventpos = 22
                            ventdesc()
                case 1:
                    ventDirection = 0
                    match ventpos:
                        case 1:
                            ventpos = 2
                            ventdesc()
                        case 4:
                            ventpos = 28
                            ventdesc()
                        case 9:
                            ventpos = 10
                            ventdesc()
                        case 13:
                            ventpos = 14
                            ventdesc()
                        case 14:
                            ventpos = 15
                            ventdesc()
                        case 18:
                            ventpos = 19
                            ventdesc()
                        case 22:
                            ventpos = 21
                            ventdesc()
                        case 23:
                            ventpos = 24
                            ventdesc()
                        case 25:
                            ventpos = 13
                            ventdesc()
                        case 26:
                            ventpos = 22
                            ventdesc()
                        case 27:
                            ventpos = 26
                            ventdesc()
                        case 28:
                            ventpos = 17
                            ventdesc()
                case 2:
                    ventDirection = 1
                    match ventpos:
                        case 0:
                            ventpos = 9
                            ventdesc()
                        case 1:
                            ventpos = 0
                            ventdesc()
                        case 2:
                            ventpos = 3
                            ventdesc()
                        case 3:
                            ventpos = 4
                            ventdesc()
                        case 4:
                            ventpos = 5
                            ventdesc()
                        case 5:
                            ventpos = 6
                            ventdesc()
                        case 6:
                            ventpos = 22
                            ventdesc()
                        case 8:
                            ventpos = 7
                            ventdesc()
                        case 11:
                            ventpos = 10
                            ventdesc()
                        case 12:
                            ventpos = 11
                            ventdesc()
                        case 13:
                            ventpos = 1
                            ventdesc()
                        case 15:
                            ventpos = 16
                            ventdesc()
                        case 16:
                            ventpos = 17
                            ventdesc()
                        case 17:
                            ventpos = 18
                            ventdesc()
                        case 19:
                            ventpos = 20
                            ventdesc()
                        case 20:
                            ventpos = 21
                            ventdesc()
                        case 22:
                            ventpos = 23
                            ventdesc()
                case 3:
                    ventDirection = 2
                    match ventpos:
                        case 2:
                            ventpos = 1
                            ventdesc()
                        case 10:
                            ventpos = 9
                            ventdesc()
                        case 13:
                            ventpos = 25
                            ventdesc()
                        case 14:
                            ventpos = 13
                            ventdesc()
                        case 15:
                            ventpos = 14
                            ventdesc()
                        case 17:
                            ventpos = 28
                            ventdesc()
                        case 19:
                            ventpos = 18
                            ventdesc()
                        case 21:
                            ventpos = 22
                            ventdesc()
                        case 22:
                            ventpos = 26
                            ventdesc()
                        case 24:
                            ventpos = 23
                            ventdesc()
                        case 26:
                            ventpos = 27
                            ventdesc()
                        case 28:
                            ventpos = 4
                            ventdesc()

def ventmove_forward():
    global vent_walls, ventdesc, ventpos, ventDirection, plypos
    if (vent_walls[ventpos])[ventDirection % 4] == True:
        print('You slam your face into the galvanized steel sheet in front of you. It doesn\'t budge.')
    elif (vent_walls[ventpos])[ventDirection % 4] == False:
        if ventpos == 6 and ventDirection == 0:
            print('You slam your face into the galvanized steel sheet in front of you. Suprisingly, you pass right through it.')
            ventpos = 7
            ventdesc()
        elif ventpos == 27 and ventDirection == 2:
            print('You attempt to pass through the stopped fan. While you are halfway through, the fan starts up again. You are cleanly bisected across the waist. \nGame Over.')
            plydead = True
        elif ventpos == 8 and ventDirection == 3:
            print('You walk into the light. You... walk? Weren\'t you just crawling?\nYou appear to be in some sort of security office. Computer monitors line one wall just above a desk. You are facing west.')
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
                    ventpos = 8
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
    global vent_walls, ventdesc, ventpos, ventDirection, plypos
    if (vent_walls[ventpos])[(ventDirection + 1) % 4] == True:
        print('You slam your shoulder into the galvanized steel sheet in front of you. It doesn\'t budge.')
    elif (vent_walls[ventpos])[(ventDirection + 1) % 4] == False:
        if ventpos == 6 and ventDirection == 3:
            print('You slam your face into the galvanized steel sheet in front of you. Suprisingly, you pass right through it.')
            ventDirection = int((ventDirection + 1) % 4)
            ventpos = 7
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
                    ventpos = 8
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
    global vent_walls, ventdesc, ventpos, ventDirection, plypos
    if (vent_walls[ventpos])[(ventDirection - 2) % 4] == True:
        print('You crawl backwards into the galvanized steel sheet behind you. It doesn\'t budge.')
    elif (vent_walls[ventpos])[(ventDirection - 2) % 4] == False:
        if ventpos == 6 and ventDirection == 0:
            print('You crawl backwards into the galvanized steel sheet behind you. Suprisingly, you pass right through it.')
            ventpos = 7
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
                    ventpos = 8
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

while plypos == 0 and plydead == False:
    ply = input('>').lower()
    if ply in wiseguy:
        if len(wiseguycount) < 5:
            if ply in wiseguycount:
                wiseguycount.remove(ply)
            if len(wiseguycount) == 0:
                print("You think you're so funny? Typing every letter EXCEPT the letters I SPECIFIED you should press? Know what? Congrats, here's your secret! Go fight this alien.")
                alienenemy()
                plyspecial()
                battlestart()
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
                            print("You SOMEHOW manage to defeat the alien despite the odds being stacked against you.\n\n")
                            print('\033[0mYou are now facing towards a door. However, \033[1;33myou now have the ALIEN BLASTER in your inventory.\033[0m You also feel quite healthy.\nYou already know what to do.')
                            inventory.append('Alien Blaster')
                            plyturn = True
                            if plyhealth == 10:
                                plyhealthDEFAULT += 10
                            else:
                                plyhealthDEFAULT += 5
                            plyhealth = plyhealthDEFAULT
                            plypos = 1
                    if plyturn == False and plyhealth > 0 and enemyhealth > 0:
                        enemymove()
                        plyturn = True
                        pass
                        if plyhealth <= 0:
                            print("Before even setting foot in this world, you managed to meet your end. You should probably learn when to stop trying to look for something you're not meant to find.\n\n\033[1;31mGame Over!\033[0m")
                            plydead = True
            else:
                print("I said stop. Just type Y or N.")
        elif len(wiseguycount) < 13:
            if ply in wiseguycount:
                wiseguycount.remove(ply)
            print("Ok, haha, you're typing every single letter except for Y and N. Here's your secret, you can stop now.")
        else:
            if ply in wiseguycount:
                wiseguycount.remove(ply)
            print('That isn\'t an option. type \'Y\' for Yes and \'N\' for No')
    else:
        match ply:
            case 'y' | 'yes' | 'start':
                plypos = 1
                print("Instructions:\nComplete the game using any method necessary. Use cardinal directions. type 'Think' or 'Hint' for a hint.\nGood luck.\n")
                print("There is a door here. You are facing north.")
            case 'n' | 'no' | 'quit':
                print("Ok? Dunno why you decided to show up then. I mean, like, we spent a long while programming this game. It's got tons of routes and options for you to do. It's a pretty good game if I say so myself. But I guess if you don't want to play that's... alright. Like yeah, who cares about alien? I surely, definitly, definitivly, absoulutly do not care about this wonderful creation that I made. You, on the other hand, absoulutly do care about this game considering you are either reading this via the source code or through Python idle and are taking your time to read all of this. But yeah, sure, leave. It's not like I wanted you to be here anyway.")
                quit()
            case 'break' | 'attack' | 'punch' | 'fight':
                plypos = 1
                print("With a fiery mind, you start the game with the mindset of dealing more damage.")
                print("Instructions:\nComplete the game using any method necessary. Use cardinal directions. type 'Think' or 'Hint' for a hint.\nGood luck.\n")
                print("There is a door here. You are facing north.")
                plyatckDEFAULT += 1
                plyatck = plyatckDEFAULT
            case 'defend' | 'block' | 'coward':
                plypos = 1
                print("With a strategic mind, you decide to start the game with the mindset of taking as little damage as possible.")
                print("Instructions:\nComplete the game using any method necessary. Use cardinal directions. type 'Think' or 'Hint' for a hint.\nGood luck.\n")
                print("There is a door here. You are facing north.")
                plydefenseDEFAULT += 1
                plydefense = plydefenseDEFAULT
            case 'weak' | 'hard' | 'hard mode' | 'challenge':
                plypos = 1
                print("You decide to activate hard mode. You only have 1 attack from now on.")
                print("Instructions:\nComplete the game using any method necessary. Use cardinal directions. type 'Think' or 'Hint' for a hint.\nGood luck.\n")
                print("There is a door here. You are facing north.")
                plyatckDEFAULT += -4
                plyatck = plyatckDEFAULT
            case 'PZI$}VP|`HPI$H JUIO$PA$V|LI$PZI$} |>IOJI$H K$I>IO{PZ|' | 'room debug':
                plysecondary = int(input('Where to, boss?\n'))
                if plysecondary in locations:
                    print('On it, boss')
                    plypos = plysecondary
                    roomdebug()
                else:
                    print('Boss, that ain\'t possible.')
            case 'battle':
                print('Loading battle simulator.')
                battletrainer()
            case _:
                print('That isn\'t an option. type \'Y\' for Yes and \'N\' for No')

# area 1 (Fields: That stupid door blocks the path.)
while plypos == 1 and doorbroken == False and plydead == False:
    
    ply = input(">").lower()

    match ply:
        case 'check door':
            print("It's just a simple, fragile door.")
        case 'check key' | 'inspect key':
            print("The key is the same color as the floor.")
        case 'look north' | 'look forward':
            print("The same thing as usual.")
        case 'look west' | 'look left':
            print("Nothing. A blank void.")
        case 'look east' | 'look right':
            if 'Stool' in inventory:
                print("There is a small golden key lying on the floor.")
            else:
                print("There is a small golden key lying on a stool.")
        case 'eat key':
            print("You heard a loud crunch sound. You didn't bite down yet.")
        case 'take stool':
            if 'Stool' not in inventory:
                print('You took the stool.\n\033[1;33mSTOOL added into your INVENTORY.\033[0m')
                inventory.append('Stool')
                tookstool = True
                if firstitem == False:
                    print("You can equip items by typing EQUIP ITEM")
                    firstitem = True
            else:
                print('Amazingly, you already took the stool.')
        case 'look south' | 'look back':
            print("You aren't an owl, are you?")
        case 'open door':
            print("You jiggle the handle. The door is locked.")
        case 'eat door':
            print("You put your mouth on the door. The door is too big to be eaten in one sitting.")
        case 'close door':
            print("You close the closed door.")
        case 'unlock door':
            print("You try to unlock the door. Your finger does not fit through the lock.")
        case 'take door':
            print("You attempt to take the door. It's lodged into the door frame")
        case 'break door':
            print("\033[1;31mYou broke down the door.\033[0m There is nothing beyond the frame but a brick wall. \nThere is no longer a door here")
            doorbroken = True
        case 'fight door' | 'attack door':
            print("You prepare for battle against a \033[1;35mtrue door.")
            plyspecial()
            battlestart()
            print(f"\033[1;32mYour health is: {plyhealth}. \033[1;35mDOOR's health is ???")
            plysecondary = input("\033[0mWhat will you do? \n").lower()
            match plysecondary:
                case 'attack' | 'kill' | 'punch' | 'fight door':
                    print(f"\033[1;31mYou attack the door with brute force for {plyatck} damage. It instantly breaks down.\033[0m \nThere is only a brick wall beyond the frame.\nThere is no longer a door here")
                    doorbroken = True
                    if plyatck >= 6:
                        plyatck += 1
                        plyatckDEFAULT += 1
                        print("You felt a tad bit stronger.")
                case 'defend':
                    print("\033[1;34mYou defended.\033[0m The door doesn't do anything. You stop fighting it.")
                case 'charge':
                    print("\033[1;32mYou charged.\033[0m The door doesn't do anything. Perhaps it's best you save your energy for something else.")
                case 'quit':
                    quit()
                case _:
                    print("You can't think of how to perform that on a door. You disengage in combat.")
        case 'kill door':
            print("\033[1;31mYou brutally attack the door until it's nothing but rubble. \nYour hand hurts, but there is now a brick wall where the door was.\n\033[0mThere is no longer a door here")
            doorbroken = True
            ouch += 1
        case 'go north':
            print('You bang your head against the door.')
        case 'go east':
            print('Your feet don\'t seem to move no matter how much you will them to go.')
        case 'go west':
            print('Your feet don\'t seem to move no matter how much you will them to go.')
        case 'go south':
            print('You attempt to go backwards. You trip over your own feet. When you get back up, you haven\'t moved at all.')
        case 'what':
            print("huh?")
        case _:
            if globalcommands():
                pass
            elif ply.endswith(" key") or ply.endswith(" key on stool"):
                print("Your hand passes through the key like it wasn't even there.")  
            else:
                print("Your thoughts seem incomprehensible.")
        
# area 1 (Fields: That stupid wall blocks the path.)
while plypos == 1 and doorbroken == True and plydead == False:
    ply = input('>').lower()

    match ply:
        case "check door":
            print("Nothing but splinters.")
        case 'check wall' | 'check brick wall':
            print('A red brick wall. The surface ripples when you touch it.')
        case 'take wall' | 'take brick wall':
            if brokenhand == True:
                print("You attempt to take the wall. You have a bad reaction. You stop your attempt to take the wall.")
            elif ouch == 3:
                print('You attempt to take the wall. Your hand passes right through the wall.\nOnce you took out your hand, if felt broken.\n\033[1;31mYou can\'t use your hand anymore.\033[0m')
                brokenhand = True
                plyatck -= 1
                plyatckDEFAULT -= 1
            else:
                print('You attempt to take the wall. Your hand passes right through the wall.\nOnce you took out your hand, it felt injured.')
                ouch += 1
        case 'eat wall' | 'eat brick wall':
            print('You sink your teeth into the wall. Suprisingly, your teeth glide through it. Tastes like water.')
        case 'break wall' | 'break brick wall':
            if brokenhand == True:
                print("You unfortunately don't have the strength to do that.")
            elif ouch == 3:
                print('You violently punch the wall. Your hand passes right through the wall.\nOnce you took out your hand, if felt broken.\n\033[1;31mYou can\'t use your hand anymore.\033[0m')
                brokenhand = True
                plyatck -= 1
                plyatckDEFAULT -= 1
            else:
                print('You violently punch the wall. Your hand passes right through the wall.\nOnce you took out your hand, it felt injured.')
                ouch += 1
        case 'look north':
            print("A brick wall standing in a doorframe. The surface ripples when you touch it.")
        case 'look west':
            print("Nothing.")
        case 'look east':
            if 'Stool' not in inventory:
                print("There is a stool with nothing on it whatsoever.")
            else:
                print("There was a stool here.")
        case 'look south':
            print("You aren't an owl, are you?")
        case 'go north' | 'enter wall' | 'enter brick wall':
            print('You pass through brick like water. You choked to death. This is the end.\n\033[1;31mGame Over\n\n\n\n  \033[0mor is it?\n\033[1;31mThere is no here.')
            plypos = 2
        case 'go east' | 'go west' | 'go south':
            print('You trip over your own feet. When you get back up, you haven\'t moved at all.')
        case 'take stool':
            if 'Stool' not in inventory:
                print('You took the stool.\n\033[1;33mSTOOL added into your INVENTORY.\033[0m')
                inventory.append('Stool')
                tookstool = True
                if firstitem == False:
                    print("You can equip items by typing EQUIP ITEM")
                    firstitem = True
            else:
                print('Amazingly, you already took the stool.')
        case 'open door':
            print("You can't open splinters.")
        case 'break door':
            print("It's already broken.")
        case 'close door':
            print("You try to figure out how to inact this outrageous thought. You come up with nothing.")
        case 'take door':
            if tookSplinter and pretendLMAO:
                print("You already took the pretend splinters. You cannot fathom about what comes after pretend splinters.")
            elif tookSplinter and pretendLMAO == False:
                print("You already took the splinters. You pretended to take more splinters.\n\033[1;33mPRETEND SPLINTERS added into your INVENTORY\033[0m")
                inventory.append('Pretend Splinters')
                pretendLMAO = True
            else:
                print("You unfortunatly cannot take the entire door as it is broken. You instead take splinters in remembrance of the broken door.\n\033[1;33mSPLINTERS added into your INVENTORY\033[0m")
                inventory.append('Splinters')
                tookSplinter = True
                if firstitem == False:
                    print("You can equip items by typing EQUIP ITEM")
                    firstitem = True
        case 'take splinters':
            if tookSplinter and pretendLMAO:
                print("You already took the pretend splinters. You cannot fathom about what comes after pretend splinters.")
            elif tookSplinter and pretendLMAO == False:
                print("You already took the splinters. You pretended to take more splinters.\n\033[1;33mPRETEND SPLINTERS added into your INVENTORY\033[0m")
                inventory.append('Pretend Splinters')
                pretendLMAO = True
            else:
                print("You take splinters in remembrance of the broken door.\n\033[1;33mSPLINTERS added into your INVENTORY\033[0m")
                inventory.append('Splinters')
                tookSplinter = True
                if firstitem == False:
                    print("You can equip items by typing EQUIP ITEM")
                    firstitem = True
        case 'fight wall' | 'attack wall' | 'fight brick wall' | 'attack brick wall':
            print(f"You prepare for battle against a \033[1;35mbrick wall.")
            plyspecial()
            battlestart()
            print(f"\033[1;32mYour health is: {plyhealth}. \033[1;35mWALL's health is 0")
            plysecondary = input("\033[0mWhat will you do? \n").lower()
            match plysecondary:
                case 'attack' | 'kill' | 'punch' | 'fight wall' | 'fight brick wall' | 'attack brick wall' | 'attack wall':
                    if brokenhand == True:
                        print("\033[1;31mYou try to attack the wall. \033[0mYour hand doesn't move. You cannot fight it in this state.")
                    elif plyatck >= 7:
                        print(f"\033[1;31mWith full force, you manage to deal {plyatck * 2} damage to the wall.\033[0m\nYou end up passing straight through the wall and suffocating. \n\033[1;31mGame Over\n\n\n\n  \033[0mor is it?\n\033[1;31mThere is no here.")
                        plypos = 2
                        plyatck += 1
                        plyatckDEFAULT += 1
                    else:
                        print("\033[1;31mYou attempt to attack the wall.\033[0m Your hand passes right through the wall.")
                        if ouch != 3:
                            print("Once you pulled out your hand, it felt injured.")
                            ouch += 1
                        elif ouch == 3:
                            print("Once you pulled out your hand, if felt broken.\n\033[1;31mYou cannot use your hand anymore.\033[0m")
                            brokenhand = True
                            plyatck -= 1
                            plyatckDEFAULT -= 1
                case 'defend':
                    print("\033[1;34mYou defended.\033[0m The wall slightly ripples. You stop fighting it.")
                case 'charge':
                    print("\033[1;32mYou charged.\033[0m The wall violently ripples. You look confused and stop fighting.")
                case 'quit':
                    quit()
                case _:
                    print("You can't think of how to perform that on a wall. You disengage in combat.")
        case _:
            if globalcommands():
                pass
            else:
                print("Your thoughts seem incomprehensible.")

# area 2 (V O I D: yum yum in my tum tum ooo baby yes)
while plypos == 2 and plydead == False:

    ply = input('>').lower().split()

    if ('break' in ply and brokenhand == False) or ('kill' in ply and 'myself' in ply):
        print('You broke. \033[1;33mYou lost Nothing.\n\n\n\n\n\n\n\n\033[0mYou wake up to find yourself in a massive glass case in what appears to be a museum.\nWhat now?')
        plypos = 3
        plychoke = 5
        inventory.remove('Nothing')

    elif 'check' in ply:
        print('You checked... something. It gave the impression of broken glass.')

    elif 'eat' in ply or 'breathe' in ply:
        print('As soon as you open your mouth, you feel the air rush out. Bad idea.')
        if plychoke > 1:
            plychoke -= 2
        else:
            plychoke -= 1
        if plychoke <= 3 and plychoke != 0:
            print(f'\033[1;35mYou have {plychoke} actions left.\033[1;31m')

    elif 'fight' in ply and plyatck >= 8 or 'attack' in ply and plyatck >= 8:
        print("You decide to use all of your power to fight the void. You encounter VOID \nBATTLE START!")
        voidenemy()
        plyspecial()
        battlestart() 
        plychoke = 8

    elif 'defend' in ply and plydefense >= 2:
        print("You feel as if something was coming at you and block. You end up blocking the VOID's attack. You encounter VOID.\nBATTLE START!")
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
                    if plyatck >= 8:
                        print('\033[0mYou wake up to find yourself in a massive glass case in what appears to be a museum. You feel slightly healthier.\n\033[1;33mYou end up finding a SHARD in your inventory.\n\033[0mWhat now?')
                        inventory.append('Shard')
                    else:
                        print('\033[0mYou wake up to find yourself in a massive glass case in what appears to be a museum. You feel slightly healthier.\n\033[1;33mYou end up finding a SHIELD in your inventory.\n\033[0mWhat now?')
                        inventory.append('Shield')
                    plyturn = True
                    if plyhealth == 10:
                        plyhealthDEFAULT += 5
                    else:
                        plyhealthDEFAULT += 1
                    plyhealth = plyhealthDEFAULT
                    plypos = 3
                    plydefense = plydefenseMAX
            if plyturn == False and plyhealth > 0 and enemyhealth > 0:
                enemymove()
                plyturn = True
                pass
                if plyhealth <= 0:
                    print("The VOID manages to choke you out as you lose all of your breath. You collapse and lose all conscience.\n\n\033[1;31mGame Over!\033[0m")
                    plydead = True

# area 3 (Museum: The butterfly effect should NOT do THIS much damage.)
while plypos == 3 and plydead == False:

    ply = input('>').lower()
    mutualcheck = False

    if tookstool == True:
        match ply:
            case 'check glass':
                glasscheck()
            case 'look west':
                if 'Crowbar' not in inventory:
                    print("Big plastic dinosaur. A crowbar dangles from its mouth.")
                    dinoseen = True
                else:
                    print("Big plastic dinosaur. It looks fake.")
            case 'look east':
                if plywallBroken == True:
                    print('What used to be a basic beige wall. Now just rubble.')
                else:
                    print('A basic beige wall.')
            case 'check dinosaur':
                if dinoseen:
                    print("A large chunk of plastic in the shape of a dinosaur.")
                else:
                    print("What dinosaur?")
            case 'attack dinosaur' | 'fight dinosaur':
                if dinoseen:
                    print("You wished that the dinosaur was alive so you could be responsible for their extinction.")
                else:
                    print("What dinosaur?")
            case 'climb dinosaur':
                if dinoseen and 'Stool' in inventory:
                    print("You used the stool the climb up onto the plastic dinosaur. You notice a hatch to exit to glass case.")
                    plysecondary = input("Exit out? Y/N\n>").lower()
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
                else:
                    print('You attempt to climb the dinosaur. You unfortuantly cannot climb high enough due to your lack of stools.')
            case 'take dinosaur':
                if dinoseen:
                    print('You attempt to take the whole dinosaur. If unfortunately is too big to be put in your inventory. You punch it in frustration.')
                else:
                    print("What dinosaur?")
            case 'take crowbar':
                print("You placed the stool down in front of the dinosaur and took the crowbar from its mouth.")
                if 'Crowbar' not in inventory:
                    if tookSplinter == True:
                        print('\033[1;33mWhen you step off the stool, it dissovles into dust.')
                    else:
                        print('\033[1;33mWhen you step off the stool, it spontaneously explodes into a pile of splinters.')
                        stoolExplode = True
                    print('CROWBAR added to your inventory.\033[0m')
                    inventory.append('Crowbar')
                    inventory.remove('Stool')
                    if armor == 'Stool':
                        armor = 'Nothing'
                        plydefense = 0
                else:
                    print('You already have it.')
            case 'take stool':
                if stoolExplode and tookSplinter == False:
                    print('The stool is sadly dead. You grab a handful of splinters to honor the late stool.\n\033[1;33mSPLINTERS added into your INVENTORY.\033[0m')
                    inventory.append('Splinters')
                    tookSplinter = True
                elif stoolExplode and tookSplinter:
                    print('You already took the splinters. You can\'t really think of anything else to do.')
                elif stoolExplode == False and 'Stool' not in inventory:
                    print('You salute the dust of the stool for it\'s hard work.')
                else:
                    pass
            case 'go east':
                if plywallBroken:
                    print('Behind the wall, you find a house. It\'s reminiscent of your old childhood home, but you\'ve definitely never been here before.\nThe museum fades from your peripheral as you walk in.\nYou are facing north towards the front door.')
                    plypos = 18
            case 'go west':
                print('It appears there is a giant plastic dinosaur in the way.')
                dinoseen = True
            case 'open vent':
                if 'Crowbar' in inventory and ventopen == False:
                    print("You pry open the vent with the crowbar. It's too small to climb inside, but there is a red brick inside.")
                    ventopen = True
                elif 'Crowbar' in inventory and ventopen:
                    print("You close the vent only to immediatly open it again.")
                else:
                    print('You try to pull open the vent with your bare hands. It dosen\'t work.')
            case 'take brick' | 'take red brick':
                if ventopen and 'Brick' not in inventory:
                    print('You took the brick. As you hold it in your hand, it feels more liquid than solid. Yet, it\'s still solid enough to break something.\n\033[1;33mBRICK added into your INVENTORY.\033[0m')
                    inventory.append('Brick')
                elif ventopen and 'Brick' in inventory:
                    print('You already took it.')
                else:
                    print('What brick?')
            case 'break wall':
                if plywallBroken == True:
                    print("It's already broken.")
                else:
                    plysecondary = input('With what?\n>').lower()
                    item_to_equip = plysecondary[0:].strip().title()
                    match plysecondary:
                        case 'brick':
                            if 'Brick' in inventory:
                                print('You throw the brick at the wall. After the brick impacts, the wall is seemingly completely decimated.')
                                plywallBroken = True
                            else:
                                print('You don\'t have one of those')
                        case 'hand' | 'head' | 'me' | 'foot':
                            print('You would prefer not to risk breaking any bones. Maybe try using an item instead.')
                        case 'think' | 'check' | 'hint':
                            if 'Brick' in inventory:
                                print('You tried to think. You feel as if what you need to break the wall is somewhere in your \033[1;33mINVENTORY.\033[0m')
                            elif 'Brick' not in inventory and ventopen:
                                print('You tried to think. You feel as if you have already seen what you need to break the wall.')
                            elif 'Brick' not in inventory and ventopen == False:
                                print('You tried to think. You feel as if what you need to break the wall is somewhere around here.')
                        case 'crowbar':
                            if 'Crowbar' in inventory:
                                print('You thought about breaking the wall with the crowbar. However, you would perfer to not damage it at this time.')
                            else:
                                print('You currently don\'t have a crowbar. Perhaps you can find one nearby?')
                        case 'you' | 'them':
                            print('Unfortuantly, there isn\'t anyone else in the room that you can refer to.')
                        case 'shard':
                            if 'Shard' in inventory:
                                print(f"\033[1;31mYou immediatly attack the wall to deal {plyatck * 3} damage.\033[0m\nThe wall breaks down instantly.\033[1;33mThe Shard transformed into a SWORD.\033[0m")
                                inventory.remove('Shard')
                                inventory.append('Sword')
                                weapon = 'Sword'
                                plyatck += 2
                                plywallBroken = True
                        case _:
                            if item_to_equip in inventory:
                                print(f'You take out the {item_to_equip}. You don\'t know what to do with it, so you instantly put it back.')
                            else:
                                print('You already know that won\'t work.')
            case 'fight wall':
                if weapon == 'Shard' and plywallBroken == False:
                    print(f"You decide to square up against the wall with your shard. \033[1;31mYou immediatly attack it to deal {plyatck * 3} damage.\033[0m\nThe wall breaks down instantly. \033[1;33mThe Shard transformed into a SWORD.\033[0m")
                    inventory.remove('Shard')
                    inventory.append('Sword')
                    weapon = 'Sword'
                    plyatck += 2
                    plywallBroken = True
                elif weapon == 'Shard' and plywallBroken:
                    print("The wall has already been broken. There is no point in trying to destroy it again.")
            case _:
                mutualcheck = True
    elif dinodead == True:
        match ply:
            case 'check glass':
                print('When you look closer, you see the glass is entirely clear. However, you still cannot see anything through it.')
            case 'check dinosaur':
                print("You witness a whole lot of dust.")
                if plyhealth <= 2:
                    print("You felt as if you acted in self defense.")
                else:
                    print("You felt like you did a better job than that stupid meteor.")
                if 'Tooth' not in inventory:
                    print("A particularly large tooth lays on the dust.")
            case 'attack dinosaur' | 'fight dinosaur':
                print("\033[1;31mYou square up against the dinosaur's ashes.\033[0m\nUnfortunately, it doesn't engage in combat with you.\nYou stop fighting.")
            case 'take tooth' | 'take large tooth':
                if 'Tooth' not in inventory:
                    print("You take the particularly large tooth.\n\033[1;33mTOOTH added to your INVENTORY\033[0m")
                    inventory.append('Tooth')
                    if firstitem == False:
                        print("You can equip items by typing EQUIP ITEM")
                        firstitem = True
                    else:
                        print("You put the tooth back in order to feel the satisfaction of obtaining it again.\n\033[1;33mTOOTH removed from your inventory.\033[0m")
                        inventory.remove('Tooth')
                        if armor == 'Tooth':
                            armor = 'Nothing'
                            plydefense = 0
            case 'look west':
                if 'Tooth' not in inventory:
                    print("There is a large pile of dust. A particularly large tooth lays at the top.")
                else:
                    print("Just some simple dust.")
            case 'look east':
                if 'Map' not in inventory:
                    print('A basic beige wall. There seems to be a map of some kind attached to it.')
                else:
                    print('A basic beige wall.')
            case 'check map':
                if 'Map' not in inventory:
                    print("You check the map on the wall. Looks to be directions for a vent system.")
            case 'take map':
                if 'Map' not in inventory:
                    print("You pull the map off the wall. Looks to be a layout for some vents.\n\033[1;33mMAP added to your inventory.\033[0m")
                    inventory.append('Map')
                else:
                    print("You have already taken the map.")
            case 'go west':
                print('There is a giant pile of presumably microplastics in your way.')
                if 'Tooth' not in inventory:
                   print('There is a particularly large tooth on top of it.')
            case 'check vent':
                if ventopen:
                    print('You observe the opened vent.')
                else:
                    print("You check the vent. You notice a slight crack that can be budged.")
            case 'open vent':
                if 'Tooth' in inventory and ventopen == False:
                    ventopen = True
                    print('You open the vent using the tooth. There looks to be a way through the vent.')
                elif ventopen:
                    print('You luckily have already opened the vent.')
                else:
                    print('You attempt to open the vent. You cannot achieve this as your fingers are not thin and strong enough for this task.')
            case 'enter vent' | 'go in vent':
                if ventopen:
                    print('You climb into the vent.\nYou are at an intersection.\nTo your left, there is a path ending in several turns.\nTo your right, there is a path ending in a right turn.\nDirectly ahead of you is a wall.\nWhere do you go?')
                    plypos = 5
                else:
                    print('You attempt to climb into the vent. Unfortunatly, you lack the ability to fit through small holes.')
            case _:
                mutualcheck = True
    else:
        match ply:
            case 'check glass':
                glasscheck()
            case 'check dinosaur':
                if dinoseen:
                    print("You go to check the dinosaur. It reacts. \nBATTLE START!")
                    plasticDino()
                    plyspecial()
                    battlestart()
                    plypos = 4
                else:
                    print("What dinosaur?")
            case 'attack dinosaur' | 'fight dinosaur':
                if dinoseen:
                    print("You initiate a battle with \033[1;35mthe dinosaur.\033[0m \nBATTLE START!")
                    plasticDino()
                    plyspecial()
                    battlestart()
                    plypos = 4
                else:
                    print("Your prehistoric rage goes unquenched, as you haven't seen any dinosaurs so far.")
            case 'blast dinosaur':
                if 'Alien Blaster' in inventory:
                    print("You end up blasting the Plastic Dinosaur, \033[1;31mdealing 15 damage to it.\033[0m The Plastic Dinosaur immediatly reacts to your attack.\nBATTLE START!")
                    plasticDino()
                    plyspecial()
                    battlestart()
                    plypos = 4
            case 'look west':
                print("Big plastic dinosaur. It looks surprisingly life-like.")
                dinoseen = True
            case 'look east':
                if 'Map' not in inventory:
                    print('A basic beige wall. There seems to be a map of some kind attached to it.')
                else:
                    print('A basic beige wall.')
            case 'check map':
                if 'Map' not in inventory:
                    print("You check the map on the wall. Looks to be directions for a vent system.")
            case 'take map':
                if 'Map' not in inventory:
                    print("You pull the map off the wall. Looks to be a layout for some vents.\n\033[1;33mMAP added to your inventory.\033[0m")
                    inventory.append('Map')
                else:
                    print("You have already taken the map.")
            case 'go west':
                if dinoseen:
                    print('Wanting to investigate the dinosaur, you walk west. The dinosaur reacts. \nBATTLE START!')
                else:
                    print('Without looking first, you casually walk straight into the jaws of a prehistoric predator and \033[1;31mget bitten for 3 damage.\n\033[0mBATTLE START!')
                    plyhealth -= 3
                plasticDino()
                plyspecial()
                battlestart()
                plypos = 4
            case 'check vent':
                print("You check the vent. You notice a slight crack that can be budged.")
            case 'open vent':
                print('You attempt to open the vent. You cannot achieve this as your fingers are not thin and strong enough for this task.')
            case _:
                mutualcheck = True

    if mutualcheck == True:
        match ply:
            case 'look north':
                print("Through the glass case, you see a museum. The glass is too foggy to make out any details.")
            case 'break glass' | 'break window' | 'break case':
                match weapon:
                    case 'Nothing':
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
                    case 'Splinters':
                        print("You prick the splinters into the glass. It unfortunatly does not budge.")
                    case 'Pretend Splinters':
                        print("You pretend to prick splinters into the glass. Nothing happens.")
                    case 'Crowbar':
                        print("You attempt to break the glass with the crowbar. You only hear the sound of tapping glass.")
                    case 'Brick':
                        print("You throw the brick at the glass. It splats onto the glass wall, not leaving any dents.")
                    case 'Shard':
                        print("You manage to scrape the glass. It forms a questionable symbol resembling a slashable wall.")
                    case 'Sword':
                        print("""You decimate the glass wall with the sword. As a matter of fact, you decimated the entire glass case.
After the glass collapsed, you notice your surroundings have completly changed. You are surrounded entirely by glass.
Strangely, you feel healthier than usual.
You aren\'t where you were before.""")
                        plypos = 12
                        plyhealthDEFAULT += 2
                        plyhealth = plyhealthDEFAULT
                    case _:
                        print("You look at the glass. You feel as if you have broken the game somehow.")
            case 'eat glass':
                print("You press your mouth against the glass and attempt to take a bite. Unfortunately, the surface is too smooth and your teeth harmlessly slide against it.")
            case 'look south':
                print("Fake grass. There is a metal vent embedded in the ground.")
            case 'go north':
                print("You smack your face into the glass.")
            case 'go south' | 'go east':
                print('This room is too small to meaningfully move in any direction.')
            case _:
                if globalcommands():
                    pass
                else:
                    print("Your thoughts seem incomprehensible.")

    if plypos == 4:
        # HELL YEAH, DINOSAUR FIGHT!!!
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
                        print("\033[1;33mYour shard transformed into a sword. \033[0mWhat now?")
                        weapon = "Sword"
                        plyatck += 2
                        inventory.append("Sword")
                        inventory.remove("Shard")
                    else:
                        print("What now?")
                    plypos = 3
                    plyturn = True
                    plydefense = plydefenseMAX

            if plyturn == False and plyhealth > 0 and enemyhealth > 0:
                enemymove()
                plyturn = True
                pass
                if plyhealth <= 0:
                    print("The Plastic Dinosaur brutally tears you apart as you faint to the ground.\n\n\033[1;31mGame Over!\033[0m")
                    plydead = True

# Area 5 (The Vents: gregory, have you heard of a)
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

    if weapon == 'Map':
        if ventpos == 7 or ventpos == 8: print("This area doesn't appear to be on your map.")
        else: print(f"Looking at the map, you seem to be at vent {ventpos}.")
    
    ply = input('>').lower()
    match ply:
        case 'left' | 'go left':
            print("")
            ventmove_left()
        case 'forward' | 'go forward' | 'ahead' | 'go ahead':
            print("")
            ventmove_forward()
        case 'right' | 'go right':
            print("")
            ventmove_right()
        case 'back' | 'go back' | 'backward' | 'go backward':
            print("")
            ventmove_back()
        case 'turn left':
            print('\nYou turn left.')
            ventDirection = (ventDirection - 1) % 4
            ventdesc()
        case 'turn right':
            print('\nYou turn left')
            ventDirection = (ventDirection + 1) % 4
            ventdesc()
        case _:
            if globalcommands():
                pass
            else:
                print('Your thoughts seem incomprehensible.')

# Area 6 (Security Office: Sir, curity camera.)
while plypos == 6 and plydead == False:

    while officepos == 0:
        ply = input('>').lower()
        match ply:
            case 'look north':
                print('A large wooden desk. Underneath it is a bulky computer tower. Mounted on top of the desk and wall are about a dozen computer monitors, each buzzing with static.')
            case 'look south':
                print('There is a sturdy metal door embedded into the wall.')
            case 'look east':
                print('A wall made of concrete bricks. There is unintelligible writing across its surface. It says: WKLV LV D SODFHKROGHU. ZDLW IRU FRRO SXCCOH.')
            case 'look west':
                print('A concrete wall marred by cracks.')
            case 'go north':
                print('You approach the desk. Would you like to sit down? Y/N')
                officepos = 1
                plysecondary = input('> ').lower()
                if plysecondary == 'y':
                    computer = True
                    print('You sit down in front of the desk. As you sit, one of the computer monitors displays a lock screen with an input for a password.')
                else:
                    print('You decide not to sit down. You are standing by the desk.')
            case 'go south':
                officepos = 3
                print('You approach the steel door. It has no handle.')
            case 'go east':
                officepos = 2
                print('You approach the brick wall. You feel a slight draft coming from its direction.')
            case _:       
                if globalcommands():
                    pass
                else:
                    print('Your thoughts seem incomprehensible.')

#Area 12 (Glasshouse: A very edible substance that makes up the room (True Story))
while plypos == 12 and plydead == False:

    ply = input('>').lower()

    match ply:

        case 'look north':
            print("PLACEHOLDER")
        case 'look west':
            print("PLACEHOLDER")
        case 'look east':
            print("PLACEHOLDER")
        case 'look south':
            print("PLACEHOLDER")
        case 'go north':
            print("PLACEHOLDER")
        case 'go east':
            print("PLACEHOLDER")
        case 'go west':
            print("PLACEHOLDER")
        case 'go south':
            print("PLACEHOLDER")
        case _:
            if globalcommands():
                pass
            else:
                print("Your thoughts seem incomprehensible.")

# Area 18 (Mysterious House: NEW PATCH: 19 now comes before 18 numerically.)
while plypos == 18 and plydead == False and insidehouse == False:

    ply = input('>').lower()

    match ply:
        case 'look north':
            print("It is indeed a door. Unfortunately, it does not look fragile.")
        case 'look east':
            print("A very climable tree.")
        case 'look west':
            if 'Key' in inventory:
                print("A Skeleton of someone lying on a bench. They seem to now be smiling.")
            else:
                print("A Skeleton of someone lying on a bench. They seem to be holding a key.")
        case 'look south':
            print("Nothing but fog and dark roads.")
        case 'go north':
            if 'Key' in inventory:
                print("You end up going north and opening the door using the key. You are now inside the house. The door remains open.")
                insidehouse = True
            else:
                print("You bang your head on the door.")
        case 'go east':
            print("You head towards the tree. Nothing seems to be around it.")
        case 'go west':
            print("A basic beige wall blocks your path. Doesn't look breakable.")
        case 'break wall':
            print("It's not a breakable wall.")
        case 'go south':
            if 'Lantern' not in inventory:
                print("You can't see well enough to be confident to go that way.")
            else:
                if weapon == 'Lantern':
                    print("You head into the fog with your lantern lit. It is very foggy, but visible enough to see close around you.\nWhat now?")
                    plypos = 20
                else:
                    print("You unfortuantly cannot see well enough as you do not have your lantern equipped.")
        case 'take key' | 'grab key':
            if 'Key' not in inventory:
                print("You take the solid key from the skeleton.\n\033[1;33mKEY was added to your inventory.\033[0m")
                inventory.append('Key')
            else:
                print('You take the key out of your inventory to toss it around for a few seconds before immediatly putting it back.')
        case 'break door' | 'fight door' | 'kill door' | 'attack door':
            if weapon == 'Sword':
                print(f"\033[1;31mYou manage to deal {plyatck * 5} damage to the metal door. \033[0mUnfortunatly, this door doesn't want to budge.")
            else:
                print("You attempt to destory the door. However, it is stronger than the previous door and does not budge.")
        case 'open door' | 'unlock door':
            if 'Key' in inventory:
                print("You open the door with the key. You are now inside the house. The door remains open.")
                insidehouse = True
                # It took me 5 hours to realize I accidentaly put a == instead of a =.
            else:
                if ply == 'open door':
                    print("You jiggle the handle. The door is locked.")
                else:
                    print("You try to unlock the door. Your finger does not fit through the lock.")
        case 'check door':
            print("The house's front door. It looks to be made of metal.")
        case 'take door':
            print("You try to take the door. It is lodged into the house and doesn't look to be coming out.")
        case 'eat door':
            print("You put your mouth on the door. The metal gives you an icky taste.")
        case 'close door':
            print("You try to close the closed door. It does not budge.")
        case 'take skeleton':
            if 'Key' not in inventory:
                print("You try to take the entire skeleton. It seems to be stuck to the bench. The key remains in the skeleton's hand.")
                #  ,̶'̶ ̶ ̶,̶ ̶|̶ ̶,̶'̶ ̶_̶'̶
            else:
                print("Rather than taking the skeleton, you shake the skeleton's hand for reciving the key.")
        case 'check skeleton':
            print("A very old skeleton. Looks to have scars scratched all around it.")
            if 'Key' not in inventory:
                print("The skeleton seems to be holding a key.")
        case 'fight skeleton' | 'attack skeleton' | 'kill skeleton':
            if weapon == 'Sword' and 'Key' in inventory:
                print(f"You slash the skeleton for {plyatck * 3} damage. The skeleton immediatly breaks and the skull falls to the floor. \033[1;33mThe sword grew stronger.\033[0m")
                plyatck += 1
                swordstrength += 1
            else:
                print("You'd perfer not to fight a skeleton at this time.")
        case 'enter house' | 'go in house' | 'go inside' | 'go into house' | 'go inside house':
            if 'Key' in inventory:
                print("You open the door with the key to enter the house. You are now inside. The door remains open.")
                insidehouse = True
            else:
                print("You attempt to go into the house. A locked metal door blocks your path.")
        case 'climb tree':
            if 'Branch' in inventory:
                print("There is no tree.")
            else:
                print("You climb the tree. While up there, you get a good glimpse of the path covered in fog to the south.\nThere seems to be an outline of a person wondering around aimlessly.\nYou jump down from the tree.")
        case 'check tree':
            if 'Branch' in inventory:
                print("There is no tree.")
            else:
                print("A tree that has tons of climable branches.")
        case 'eat tree':
            if 'Branch' in inventory:
                print('There is no tree.')
            else:
                print("You take a bite of the tree. Tastes odd.")
        case 'take tree':
            if 'Branch' in inventory:
                print("There is no tree.")
            else:
                print("You try to take the tree. It is unfortunatly apart of the ground.")
        case 'attack tree' | 'fight tree' | 'chop tree' | 'chop the tree down' | 'kill tree':
            if weapon == 'Sword':
                print("You manage to chop the tree with your sword. The tree immediatly collapses and fades to nothing. \033[1;33mThe sword grew stronger.\nBRANCH added to your inventory.\033[0m")
                plyatck += 1
                swordstrength += 1
                inventory.append('Branch')
            else:
                if ply == 'chop the tree down': print('NO!')
                else: print("You attempt to chop the tree down. Unfortuantly, you do not have the right tools for this task.")
        case _:
            if globalcommands():
                pass
            else:
                print("Your thoughts seem incomprehensible.")

    if insidehouse == True:

        while insidehouse == True and plydead == False:

            #SECRET AREA 18.5 d8O3D <-- That's Mario btw

            ply = input('>').lower()

            match ply:

                case 'look north':
                    print("A wall that contains a photo of a family. The faces look to be scratched out besides one.")
                case 'look east':
                    if 'Lantern' not in inventory:
                        print("A shelf that contains a lantern.")
                    else:
                        print("A shelf that used to have a lantern.")
                case 'take lantern':
                    if 'Lantern' not in inventory:
                        print("You take the lantern from the shelf.\n\033[1;33mLANTERN added to your inventory.\033[0m")
                        inventory.append("Lantern")
                    else:
                        print("You have already taken the lantern. You cannot find another item to take.")
                case 'look west':
                    print("Nothing but packed boxes. They are all sealed shut.")
                case 'take photo':
                    print("You attempt to take the photos. They seem to be part of the wall.")
                case 'check photo':
                    print('You take a look at the photos. It appears to be a family of 5. You don\'t recongnize anyone in the photo.\nThe unscratched face appears to look like a middle aged human person. The name \'Lenard\' is written underneath their head.')
                    photocheck = True
                case 'open boxes':
                    print("You attempt to open the boxes. They are all fully sealed.")
                case 'break boxes':
                    print("You attempt to break the boxes. For some reason, they don't budge.")
                case 'fight boxes':
                    if weapon == 'Sword' and 'Bandana' not in inventory:
                        print("You slash all of the boxes. You manage to find a bandana. It looks a bit cursed, but that doesn't bother you.\n\033[1;33mBANDANA added to your INVENTORY.\033[0m")
                        inventory.append('Bandana')
                    elif 'Bandana' in inventory: print("There are no boxes to break.")
                    else: print("Boxes? You want to fight boxes? Like, unless you had a sword, there'd be no reason.")
                case 'take boxes':
                    print("You attempt to take the boxes. They feel as if they are glued to the ground.")
                case 'look south':
                    print("The area you were in before. The door is still open.")
                case 'go north' | 'go east' | 'go west':
                    print("The house doesn't seem to be big enough to move in that direction.")
                case 'go south' | 'exit house' | 'leave house' | 'close door' | 'leave':
                    print("You exit the house. You make sure to close and lock the door on your way out.")
                    insidehouse = False
                case _:
                    if globalcommands():
                        pass
                    else: print("Your thoughts seem incomprehensible.")

# Area 20 (Foggy Roads: I bet this would look really cool, but this is a text only game.)
while plypos == 20 and plydead == False:

    ply = input('>').lower()

    match ply:
        case 'look north':
            if forwardcheck:
                print('A very long stretch of road. There seems to be a person nearby.')
            else:
                print('Just more road up ahead from what you can see.')
        case 'look east':
            print('An endless supply of dead trees.')
        case 'look west':
            print('A nice looking horizon. A cliff seems to be present throughout the entirity of the path.')
        case 'look south':
            print('The road that you already treched.')
        case 'go north':
            if forwardcheck:
                print("You end up running into a person. They are greatly startled and send out a blood curling scream.")
                if photocheck:
                    print("You notice that the person looks exactly like Lenard from the photo.")
                print("Suddenly, both you and the person hear tons of rustling and very heavy footsteps right behind you. The person yells at you to RUN!\nBATTLE START!")
                plypos = 21
                mysteriouscompanion()
                plyspecial()
                beastenemy()
                battlestart()
                plypos = 21
            else:
                print("You keep moving forward. You feel like you see a person, but cannot truly make out the image.")
                forwardcheck = True
        case 'go east':
            print('You attempt to climb inbetween the dead trees. You can\'t seem to fit inside.')
        case 'go west':
            print('You head towards the cliff. Something holds you back from jumping off. You head back to the path.')
        case 'go south':
            if forwardcheck:
                print('You decided to go back towards where you were previously.')
                forwardcheck = False
            else:
                print('There isn\'t any reason to head back to the old house.')
        case 'talk':
            if forwardcheck:
                print("You try to speak to the figure. You hear something said back at you, but cannot make out what it was.")
            else:
                print("You try to call out for someone, saying hello. You feel as if you hear something north from you.")
        case 'kill' | 'fight':
            if forwardcheck:
                if weapon == 'Sword':
                    print("You charge forwards and iniate combat with what is revealed to be a person.\nBATTLE START!")
                    mysteriousPerson()
                    plyspecial()
                    battlestart()
                    plypos = 21
                else:
                    print("Not knowing what you're going up against, you decide against your intrusive thoughts.")
            else:
                if weapon == 'Sword':
                    print('There\'s nothing to fight yet.')
                else:
                    print("You cannot think about what you should fight in this area.")
        case 'equip nothing' | 'equip pretend splinters' | 'equip crowbar' | 'equip brick' | 'equip shard' | 'equip key':
            print("If you were to equip that, you would lose your vision as there would be no more light.")
        case _:
            if ply == 'equip splinters' and stoolexplode == False:
                print('You decide to form the splinters into a protective stool.\n\033[1;33mYou equipped the splinters.\n\033[1;34mYou gained +1 defense.\033[0m')
                armor = 'Splinters'
                plydefense = plydefenseDEFAULT + 1
            elif ply == 'equip sword' and 'Sword' in inventory:
                print(f"When you reached for your sword, it emmited a bright glow. You don't need the lantern anymore.\n\033[1;33mYou tossed away the lantern.\nYou equipped the Sword. \033[1;31mYou gained +{swordstrength} attack.\033[0m")
                inventory.remove('Lantern')
                weapon = 'Sword'
                plyatck = plyatckDEFAULT + swordstrength
                if armor == 'Bandana':
                    plyatck += 2
            elif globalcommands():
                pass
            else:
                print("Your thoughts seem incomprehensible.")

# Area 21 (HELL YEAH, BEAST FIGHT!!!: I have no idea how I'm going to code a chase area, so we fightin' instead.)
while plypos == 21 and plydead == False and enemyname == 'The Beast':

    if plyturn == True and plyhealth > 0:
        plymove()
        plyturn = False
        pass
        if plyerror == True:
            print("That is not a move that you have access to. Try again.")
            plymove()
            pass
            if plyerror == True:
                print("You just keep running as you can't think of what to do.")
                pass
        if enemyhealth <= 0 and plyhealth > 0:
            if ply == 'special' and weapon == 'Sword':
                print("You won!\nThe beast was slained by the sword and falls to the ground.\n\033[1;33mThe Sword grew stronger.\033[0m")
                swordstrength += 2
                plyatck = plyatckDEFAULT + swordstrength
                if armor == 'Bandana':
                    plyatck += 2
                plypos = 22
                plyturn = True
                plydefense = plydefenseMAX
            else:
                if companion != '':
                    print(f"You won!\nThe beast decided to lay off you and {companion}.")
                    talkcounter = 3
                else:
                    print(f"You won!\nThe beast decided to lay off you and ran away.")
                plypos = 22
                plyturn = True
                plydefense = plydefenseMAX

    if plyturn == False and plyhealth > 0 and enemyhealth > 0:
        enemymove()
        plyturn = True
        pass
        if plyhealth <= 0:
            print("The Beast manages to grab and rip you apart into multiple pieces.\n\n\033[1;31mGame Over!\033[0m")
            plydead = True
        if companionhealth <= 0 and companion != '':
            print(f"The Beast manages to grab and rip apart {companion} into pieces.")
            companion = ''
            companionhealth = 0
            companionatck = 0
            companionatckDEFAULT = 0
            companiondefense = 0
            companiondefending = False
            enemytarget = 0

# Area 21: (HELL YEAH, LENARD FIGHT!!!: There's a lot of effort being put in to a route that litteraly no one is going to find.)
while plypos == 21 and plydead == False and (enemyname == 'The Mysterious Person' or enemyname == 'Lenard'):

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
            if ply == 'special':
                print(f"You won! \n{enemyname} has been obliterated to dust. \033[1;33mThe sword got quite stronger.\033[0m")
                swordstrength += 5
            else:
                print(f"You won!\n{enemyname} ended up running away.\033[1;33mThe sword grew stronger.\033[0m")
                swordstrength += 1
            plyatck = plyatckDEFAULT + swordstrength
            if armor == 'Bandana':
                plyatck += 2
            plypos = 22
            plyturn = True
            plydefense = plydefenseMAX

    if plyturn == False and plyhealth > 0 and enemyhealth > 0:
        enemymove()
        plyturn = True
        pass
        if plyhealth <= 0:
            print(f"{enemyname} ends up dealing the final blow to you. You died to a rock.\n\n\033[1;31mGame Over!\033[0m")
            plydead = True

# Area 22 (IDK: Cool caption that I need to decide later.)
    # Lenard is alive :)
if companion == 'The Mysterious Person' or companion == 'Lenard':
    print('As you and the person stop, they introduce themselves to you. They greet you kindly and introduce themselves as Lenard.')
    if companion == 'The Mysterious Person':
        print('You introduce yourself to Lenard. \033[1;33mYou can now talk to Lenard by typing TALK.\033[0m')
        companion == 'Lenard'
    else:
        print('You tell Lenard that you already knew that. They look visablly confused. \033[1;33mYou can now talk to Lenard by typing TALK.\033[0m')
while plypos == 22 and plydead == False and companion == 'Lenard':
    
    ply = input('>').lower()

    if ply == 'go north':
        print("PLACEHOLDER")

    elif globalcommands():
        pass

    else:
        print("Your thoughts seem incomprehensible.")
    # LENARD NO !_! I'm so sad :(
while plypos == 22 and plydead == False and companion != 'Lenard':
    
    ply = input('>').lower()

    if ply == 'go north':
        print("PLACEHOLDER")

    elif globalcommands():
        pass

    else:
        print("Your thoughts seem incomprehensible.")
