import random

scor = 0

for i in range(10):
    number = random.randint(1, 101)
    question = int(input("Pick a number between 1 and 1.000.000: "))
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
    
