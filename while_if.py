num = 0

while True:
    answer = int(input("Input your numbers: "))
    num += answer
    answer2 = int(input("Input your numbers for 2: "))
    num += answer2
    if num == answer:
        continue
    question = int(input("Input your number again: "))
    question += answer
    print(question)
    ques = input("You move close? ")
    if ques == "yes":
        break

print("You Done challange!")
