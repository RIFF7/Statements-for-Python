import random, os, time

def rollDice(sides):
    result = random.randint(1, sides)
    return result

""" def rollDice(side):
    result = random.randint(1, side)
    return result """

def generateHealt():
    roll_side_6 = rollDice(6)
    roll_side_12 = rollDice(12)
    result = int((roll_side_6 * roll_side_12) / 2 + 10)
    return result

def generateStrength():
    roll_side_6 = rollDice(6)
    roll_side_12 = rollDice(8)
    result = int((roll_side_6 * roll_side_12) / 2 + 12)
    return result

#close = "yes"

while True:
    #clear DATA
    os.system("cls")
    #Show Menu
    print("⚔️  Character Builder ⚔️")
    time.sleep(1)
    print("Press 1 to build character")
    time.sleep(1)
    print("Press 2 to Exit Menu")
    time.sleep(1)
    print("Press anything else to see the menu again!")
    #Take user Input
    userInput = int(input())
    if userInput == 1:
        character1 = input("Name Your Legend: ")
        typeCharacter1 = input("Character Type (Human, Elf, Wiard, Orc): ")
        print(character1)
        healt1 = generateHealt()
        print("HEALT:", healt1)
        strength1 = generateStrength()
        print("STRENGTH:", strength1)
        
        print()
        print("Who are they battling?")
        print()
        
        character2 = input("Name Your Legend: ")
        typeCharacter2 = input("Character Type (Human, Elf, Wiard, Orc): ")
        print(character2)
        healt2 = generateHealt()
        print("HEALT:", healt2)
        strength2 = generateStrength()
        print("STRENGTH:", strength2)
        
        round = 1
        winner = None
        
        while True:
            time.sleep(1)
            print()
            print("⚔️ BATTLE TIME ⚔️")
            print()
            print("The battle begins!")
            print()
            
            play1 = rollDice(6)
            play2 = rollDice(6)
            
            difference = abs(strength1 - strength2) + 1
            
            if play1 > play2:
                healt2 -= difference
                if round == 1:
                    print(character1, "wins the first blow")
                else:
                    print(character1, "wins round", round)
            elif play2 > play1:
                healt1 -= difference
                if round == 1:
                    print(character2, "wins the first blow")
                else:
                    print(character2, "wins round", round)
            else:
                print("Their swords clash and they draw round", round)
            
            print()
            print(character1)
            print("HEALT: ", healt1)
            print()
            print(character2)
            print("HEALT: ", healt2)
            print()
            
            if healt1 <= 0:
                print(character1, "has died!")
                winner = character2
                break
            elif healt2 <= 0:
                print(character2, "has died!")
                winner = character1
                break
            else:
                print("And they're both standing for the next round")
                round += 1
        print()
        print("May your name go down in Legend...")
    elif userInput == 2:
        exit()
    else:
        continue
    
    again = input("Again? ")
    if again == "NO" or again == "no":
        print()
        print("⚔️ BATTLE TIME ⚔️")
        print()
        print(winner, "has won in", round, "rounds")
        break
    time.sleep(1)
