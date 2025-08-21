This will be all the stored commands + ideas that we would like to program soon.


TO DO:

GENERAL:
  GLOBAL COMMANDS:
    ***HUGE CHANGE, BUT REALLY HELPFUL: Change the formating to be modules packages. This would require a lot of coding fixes, but it allows us to work on different areas without the worry of accidentally overwriteing the others code.
    Equipping Items:
      Attempting to equip an item you already have equipped should say "You already have (ITEM) equipped.)

Area 1 (Unbroken Door)
  SUGGESTION: The key command of your hand phasing through the key should activate if 'key' is included in the command the player gives rather than needing the specific 'take key' command.
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
  Equipped items should increase the amount of damage you deal / take.

Area 3 (Museum WITH STOOL)
  Attempting to take the splinters displays nothing.
  Attempting to eat the glass displays nothing.
  Currently, going east does nothing (Proceeds to New Area)

FUTURE IDEAS (Later Areas):

Area 6 (Glass Room):
  NONE

IMPLEMENTED/FIXED:

GENERAL CHANGES:
  ADDED: Global Commands, which include
    Quitting the game
    Thinking for a hint
    Opening your inventory
    Checking Yourself to display your stats.
      ADDED: Displays additional info unique to the position the player is in.
      ADDED: The Attack and Defense now display what weapon or armor you have next to it.
    FIXED: Using any global commands currently displays "Your thoughts seemed incomprehensible" after running the command
  CHANGED: Made the minor fights use the "miscfight" input to make coding a bit easier
  ADDED: Added # Areas for convience purposes.
  CHANGED: Quitting now uses quit() to close the program rather than simply saying "GAME OVER"
  ADDED: You can now equip items. They will either be equipped as a weapon or an armor. They do effect your stats.
  ADDED: start game? y/n option on title screen
  ADDED: 'open inventory' should perform the same command as 'inventory'

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
      ADDED: When obtaining the brick, there should be a way to eat/drink the brick.
      ADDED: If you have the brick, typing the command 'break (fourth/4th) wall' should say 'You attempt to smash the fourth wall. You succeeded, but not in the way that you think.'
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
