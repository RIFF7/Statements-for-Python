from getpass import getpass as input

print("Game ✂️ 🪨  📝 in Terminal Code\n")
print("You can select inicial (R, S, P)\n")

play1 = input("Player 1 > ")
play2 = input("Player 2 > ")

if play1 == "R" or play1 == "r":
    if play2 == "R" or play2 == "r":
        print("You both picked Rock, draw!")
    elif play2== "S" or play2 == "s":
        print("Player 1 smashed Player 2's Scissors into dust with their Rock!")
    elif play2== "P" or play2 == "p":
        print("Player 1's Rock is smothered by Player2's Paper!")
    else:
        print("Please check the RULE in this GAME!")
elif play1== "P" or play1 == "p":
    if play2=="R" or play2 == "r":
        print("Player 2's Rock is smothered by Player 1's Paper!")
    elif play2== "S" or play2 == "s":
        print("Player 1's Paper is cut into tiny pieces by Player 2's Scissors!")
    elif play2== "P" or play2 == "p":
        print("Two bits of paper flap at each other. Dissapointing. Draw.")
    else:
        print("Please check the RULE in this GAME!")
elif play1== "S" or play1 == "s":
    if play2== "R" or play2 == "r":
        print("Player 2's Rock makes metal-dust out of Player 1's Scissors")
    elif play2== "S" or play2 == "s":
        print("Klaaaangg! Scissors bounce off each other like a dodgy sword fight! Draw.")
    elif play2== "P" or play2 == "p":
        print("Player1's Scissors make cut out of Player2's paper!")
    else:
        print("Please check the RULE in this GAME!")
else:
  print("Please check the RULE in this GAME!")
