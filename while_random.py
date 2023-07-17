import random

number = random.randint(1,101)
scor = 0

while True:
    question = int(input("Pick a number between 1 and 100: "))
    if question < 0:
        print("Please input number Positif!")
        exit()
    if question < number:
        print("Too Low")
        scor += 1
    elif question > number:
        print("Too High")
        scor += 1
        continue
    elif question == number:
        print("Correct!!!")
        scor += 1
        break
    else:
        print("What's Wrong!!!")

print("It took you", scor, "attemps(s) to get the correct answer!")
