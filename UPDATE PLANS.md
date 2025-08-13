This will be all the stored commands + ideas that we would like to program soon.


to do:

Area 1 (Unbroken Door)
  NONE
  Door Fight:
    NONE
Area 1 (Broken Door)
  Wall Fight:
    Fix attacking the wall breaking your hand in only 2 attacks rather than 3
Area 2 (Void)
  NONE
Area 3 (Museum)
  STOOL:
    If the player hasn't taken the splinters from the door, they should be able to take splinters from the broken stool.
Area 3 (Battle Against a True Dinosaur)
  NONE

IMPLEMENTED/FIXED:

GENERAL CHANGES:
  Made the minor fights use the "miscfight" input to make coding a bit easier

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

Area 3 (Battle Against a True Dinosaur)
    GENERAL:
      ADDED: Think, Check, and Help should explain what Attack, Defend, and Charge do
        Attack: Deals 5 Damage to the Dinosaur if it isn't defending.
        Defend: Allows you to take 0 Damage This Turn
        Charge: Powers up Attack to deal Double Damage next turn
