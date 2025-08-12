This will be all the stored commands + ideas that we would like to program soon.

Area 1 (Unbroken Door)
  Look around should hint about moving and looking North, South, East, and West.
  Key:
    "Equip Key", "Get Key", and "Pick Up Key" should perform the same command as "Take Key"
  Battle against door:
    Punch and Fight Door should perform the same command as attack door does.
Area 1 (Broken Door)
  Wall:
    Eat Wall
    The ability to also type "Brick Wall" rather than just "Wall"
Area 2 (Void)
  Think, Check, and Help needs to be fixed to work in that area.
  Kill yourself should result in you breaking
Area 3 (Museum)
  Moving in directions should be possible in this area or at the very least have a note saying you can't.
  Dinosaur:
    Think, Check, and Help shouldn't mention the dinosaur if it hasn't been seen yet.
    Fight Dinosaur should perform the same command
Area 3 (Battle Against a True Dinosaur)
  Think, Check, and Help should explain what Attack, Defend, and Charge do
    Attack: Deals 5 Damage to the Dinosaur if it isn't defending.
    Defend: Allows you to take 0 Damage This Turn
    Charge: Powers up Attack to deal Double Damage next turn
  An error occurs when the Dinosaur attacks:
    Traceback (most recent call last):
    File "C:\Users\THunt001\Documents\GitHub\Python\door.py", line 325, in <module>
      dinomove()
    File "C:\Users\THunt001\Documents\GitHub\Python\door.py", line 280, in dinomove
      print(f"PLASTIC DINO bit you for {dinoatck}!")
  UnboundLocalError: cannot access local variable 'dinoatck' where it is not associated with a value
