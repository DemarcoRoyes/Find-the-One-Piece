print("welcome to Laughtale.")
print("Your mission is to find the One Piece.")
left_or_right = input("Do you wanna go left or right? ")

if left_or_right == "right":
  print("Crocodile got you with his poison.")
  print("Game over")
elif left_or_right == "left":
  swim_or_wait = input("Do you wanna swim or wait? ")
  if swim_or_wait == "swim":
    print("You have a devil fruit.")
    print("Why would you do that?")
    print("Game Over.")
  elif swim_or_wait == "wait":
    which_door = input(
        "Which door do you wanna go through, red, yellow or blue? ")
    if which_door == "red":
      print("You were KIDNAPPED by CP0.")
      print("Game Over")
    elif which_door == "yellow":
      print("You found the One Piece")
      print("You're the Pirate King")
    elif which_door == "blue":
      print("You were killed by Blackbeard")
      print("Game Over")
    else:
      print("Game Over")
  else:
    print("Game Over")
else:
  print("Game Over")
