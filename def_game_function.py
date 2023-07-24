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

close = "yes"

while close == "yes":
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
        character = input("Name Your Legend: ")
        typeCharacter = input("Character Type (Human, Elf, Wiard, Orc): ")
        print(character)
        healt = str(generateHealt())
        print("HEALT:", healt)
        strength = str(generateStrength())
        print("STRENGTH:", strength)
        print("May your name go down in Legend...")
    elif userInput == 2:
        exit()
    else:
        continue
    close = input("Again? ")
