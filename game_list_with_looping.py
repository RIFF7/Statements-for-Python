import random, os, time

listWord = ["Love", "Heart", "People", "Human"]
letterPick = []
lives = 6

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word = random.choice(listWord)

while True:
    #time.sleep(1)
    #os.system("cls")
    letter = input("Chooxe the letter: ").lower()
    
    if letter in letterPick:
        print("You've tried that before")
        continue
    
    letterPick.append(letter)
    
    if letter in word:
        print("You found a letter")
    else:
        print("Nope, not in there")
        lives -= 1
        
    allLetters = True
    print()
    for i in word:
        if i in letterPick:
            print(i, end="")
        else:
            print("_", end="")
            allLetters = False
    print()
    
    if allLetters:
        print(f"You won with {lives} left!")
        break
    
    if lives <= 0:
        print(f"You ran out of lives! The answer was {word}")
        print(HANGMANPICS[6])
        break
    elif lives <= 1:
        print(f"Only {lives} left")
        print(HANGMANPICS[5])
    elif lives <= 2:
        print(f"Only {lives} left")
        print(HANGMANPICS[4])
    elif lives <= 3:
        print(f"Only {lives} left")
        print(HANGMANPICS[3])
    elif lives <= 4:
        print(f"Only {lives} left")
        print(HANGMANPICS[2])
    elif lives <= 5:
        print(f"Only {lives} left")
        print(HANGMANPICS[1])
    else:
        print(f"Only {lives} left")
        print(HANGMANPICS[0])
