This will be all the stored commands + ideas that we would like to program soon.


to do:

Area 1 (Unbroken Door)
  Take door should say something like, "It's lodged in the frame." or smth idk
  Door Fight:
    The HP of the player and the door should be displayed. (Door should have like ??? HP or smth.)
Area 1 (Broken Door)
  Fight Wall should start combat like with the door. However, attacking the wall will result in the same result as "break wall"
  Take door should add "Splinters" to your inventory
  Take Wall should result in the players hand going right through the wall.
Area 2 (Void)
  Eat or Eat Void should result in the player losing 2 choke points rather than 1.
  Open Void should result in the player opening the void, heading to area 3 (Museum)
  Make Choke Points 5 (Mention every turn how much they have left with "You have ___ actions left" once they have 3 or less actions left)
Area 3 (Museum)
  Moving in directions should be possible in this area or at the very least have a note saying you can't.
  Dinosaur:
    Think, Check, and Help shouldn't mention the dinosaur if it hasn't been seen yet.
    Fight Dinosaur should perform the same command as Check Dinosaur
  After using the Stool to get the Crowbar, there should either:
        Be a way to take back the stool
        Mention that the stool broke and is no longer in your inventory
        Not remove the stool from inventory
Area 3 (Battle Against a True Dinosaur)
  Think, Check, and Help should explain what Attack, Defend, and Charge do
    Attack: Deals 5 Damage to the Dinosaur if it isn't defending.
    Defend: Allows you to take 0 Damage This Turn
    Charge: Powers up Attack to deal Double Damage next turn

implemented/fixed:
  
An error occurs when the Dinosaur attacks:
    Traceback (most recent call last):
    File "C:\Users\THunt001\Documents\GitHub\Python\door.py", line 325, in <module>
      dinomove()
    File "C:\Users\THunt001\Documents\GitHub\Python\door.py", line 280, in dinomove
      print(f"PLASTIC DINO bit you for {dinoatck}!")
  UnboundLocalError: cannot access local variable 'dinoatck' where it is not associated with a value

Area 1 (Unbroken Door)
  Look around should hint about moving and looking North, South, East, and West.
  Key:
    ADDED: "Equip Key", "Get Key", and "Pick Up Key" should perform the same command as "Take Key"
  Battle against door:
    ADDED: Punch and Fight Door should perform the same command as attack door does.

Area 1 (Broken Door)
    ADDED: The ability to also type "Brick Wall" rather than just "Wall"
    Wall:
      ADDED: Eat Wall
Area 2 (Void)
    FIXED: Think, Check, and Help needs to be fixed to work in that area.
    ADDED: Kill yourself should result in you breaking
