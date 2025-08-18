This will be all the stored commands + ideas that we would like to program soon.


TO DO:

GENERAL:
  start game? y/n option on title screen
  'up' commands (look up, go up, stuff like that)
  Add a function of commands you should be able to do in every room. These commands include
    Quitting the game
    Thinking for a hint
    Opening your inventory
    Equiping items in your inventory (such as Crowbar and Splinters)
      The Crowbar should increase your attack by 1
      The Splinters should increase your defense by 1
      The Pretend Splinters should lower your defense by 1
      The Nothing should increase both your attack and defense by 0 (You have Nothing as default to all of the item slots)
      NOTES FOR THIS FEATURE
        Equipping an item like the crowbar should not remove it from your inventory.
        Attempting to equip an item you already have equipped should say "You already have (ITEM) equipped.)
        If an item isn't equippable or the item isn't in their inventory/doesn't exsist, it should say "You can't equip (ITEM)" or "You don't have (ITEM) yet (even if it isn't a real item)"
        If the item that is equipped ends up being used up (like the crowbar breaking in a room if that ever happens), that item should be replaced by nothing in the equip menu.
    Add the ability to check yourself by saying "check me" or "check myself" or "check self". It should list this.
    look around ('look' should also initiate this command)
      YOU
      CURRENT HP: {plyhealth}
      ATTACK: {plyattack}(atk_item)
      DEFENSE: {plydefense}(def_item)
      EXTRA INFO BASED ON WHAT IS GOING ON, SUCH AS:
        Area 1 (Unbroken Door): Trying to investigate this strange door that they found.
        Area 1 (Broken Door): Certified Door Breaker
        Area 2 (V O I D): Has no idea what they are getting themselves into.
        stuff like this y'know.
  'open inventory' should perform the same command as 'inventory'

Area 1 (Unbroken Door)
  Trying to perform actions on the key such as 'throw key', 'punch key', 'fight key' should initiate the same command as 'take key'
  Door Fight:
    NONE
Area 1 (Broken Door)
  NONE

Area 2 (Void)
  Check void should initiate the command 'You checked the Void. You couldn't notice anything except what looked like broken glass.'
  better hinting

Area 3 (Museum)
  GENERAL AREA 3 STUFF:
    eat glass
  MAIN ROUTE STUFF:
    NONE

Area 3 (Battle Against a True Dinosaur)
  NONE

Area 3 (Museum WITH STOOL)
  When obtaining the brick, there should be a way to eat/drink the brick.
  If you have the brick, typing the command 'break (fourth/4th) wall' should say 'You attempt to smash the fourth wall. You succeeded, but not in the way that you think.'

FUTURE IDEAS (Later Areas):

Area 6 (Glass Room):
  NONE

IMPLEMENTED/FIXED:

GENERAL CHANGES:
  CHANGED: Made the minor fights use the "miscfight" input to make coding a bit easier
  ADDED: Added # Areas for convience purposes.
  CHANGED: Quitting now uses quit() to close the program rather than simply saying "GAME OVER"

Area 1 (Unbroken Door)
  GENERAL:
    ADDED: Look around should hint about moving and looking North, South, East, and West.
    ADDED: Take door should say something like, "It's lodged in the frame." or smth idk
  Key:
    ADDED: "Equip Key", "Get Key", and "Pick Up Key" should perform the same command as "Take Key"
  Battle against door:
    ADDED: Punch and Fight Door should perform the same command as attack door does.
    TWEAK: The HP of the player and the door should be displayed. (Door should have like ??? HP)

Area 1 (Broken Door)
  GENERAL:
    ADDED: The ability to also type "Brick Wall" rather than just "Wall"
    ADDED: Take door should add "Splinters" to your inventory
  Wall:
    ADDED: Eat Wall
    ADDED: You can now engage in combat with the Wall
    CHANGED: Break wall now has edited dialog to fit with other actions.
    ADDED: Take Wall should result in the players hand going right through the wall.
    FIXED: Fix attacking the wall breaking your hand in only 2 attacks rather than 3

Area 2 (Void)
    GENERAL:
      FIXED: Think, Check, and Help needs to be fixed to work in that area.
      ADDED: Kill yourself should result in you breaking
      ADDED: Eat or Eat Void should result in the player losing 2 choke points rather than 1.
      ADDED: Open Void should result in the player opening the void, heading to area 3 (Museum)
      ADDED: Make Choke Points 5 (Mention every turn how much they have left with "You have ___ actions left" once they have 3 or less actions left)

Area 3 (Museum)
    GENERAL:
      ADDED: Moving in directions should be possible in this area or at the very least have a note saying you can't.
    DINOSAUR:
      ADDED: Think, Check, and Help shouldn't mention the dinosaur if it hasn't been seen yet.
      ADDED: Fight Dinosaur should perform the same command as Check Dinosaur
    STOOL:
      ADDED: After using the Stool to get the Crowbar, there should either:
        Be a way to take back the stool
        Mention that the stool broke and is no longer in your inventory
        Not remove the stool from inventory
      ADDED: If the player hasn't taken the splinters from the door, they should be able to take splinters from the broken stool.

Area 3 (Battle Against a True Dinosaur)
    GENERAL:
      ADDED: Think, Check, and Help should explain what Attack, Defend, and Charge do
        Attack: Deals 5 Damage to the Dinosaur if it isn't defending.
        Defend: Allows you to take 0 Damage This Turn
        Charge: Powers up Attack to deal Double Damage next turn
      ADDED: If you end up dying and killing the dinosaur at the same time, both the you died and you won text show up. To fix this, either:
        Make killing the dinosaur the inititave so the player can progress
        Make unique dialog that says "As you see the dinosaur collapse, you slowly lose conscience and fall over. YOU DIED"
