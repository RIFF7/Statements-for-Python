#from getpass import getpass as input

print("G A M E   🪨  📄 ✂️    B A T T L E \n")
print("Select your move (R, P or S)\n")

scor = 0
scor2 = 0

while True:
    play1 = input("Player 1 > ")
    play2 = input("Player 2 > ")
    if play1 == "R" or play1 == "r":
        if play2 == "R" or play2 == "r":
            print("You both picked Rock, draw!")
        elif play2== "S" or play2    == "s":
            print("Player 1 smashed Player 2's Scissors into dust with their Rock!")
            scor += 1
        elif play2== "P" or play2 == "p":
            print("Player 1's Rock is smothered by Player2's Paper!")
            scor2 += 1
        else:
            print("Please check the RULE in this GAME!")
    elif play1== "P" or play1 == "p":
        if play2=="R" or play2 == "r":
            print("Player 2's Rock is smothered by Player 1's Paper!")
            scor += 1
        elif play2== "S" or play2 == "s":
            print("Player 1's Paper is cut into tiny pieces by Player 2's Scissors!")
            scor2 += 1
        elif play2== "P" or play2 == "p":
            print("Two bits of paper flap at each other. Dissapointing. Draw.")
        else:   
            print("Please check the RULE in this GAME!")
    elif play1== "S" or play1 == "s":
        if play2== "R" or play2 == "r":
            print("Player 2's Rock makes metal-dust out of Player 1's Scissors")
            scor2 += 1
        elif play2== "S" or play2 == "s":
            print("Klaaaangg! Scissors bounce off each other like a dodgy sword fight! Draw.")
        elif play2== "P" or play2 == "p":
            print("Player1's Scissors make cut out of Player2's paper!")
            scor2 += 1
        else:
            print("Please check the RULE in this GAME!")
    else:
        print("Please check the RULE in this GAME!")
    
    if scor == 3 or scor2 == 3:
        print("Game Over", "This Game Player 1 >", scor, "and Player 2 >", scor2)
        break
    if scor < 3 or scor2 < 3:
        print("Round", max(scor, scor2) + 1)
        continue
