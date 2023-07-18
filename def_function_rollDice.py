#Percobaan dengan satu argumen (bahan)

""" def cake(bahan):
    if bahan == "Cherry":
        print("Wow cake dengan Cherry greed!")
    elif bahan == "Cheese":
        print("Uhmm... not bad")
    else:
        print("Yeah what ever...!")
cake("Cheese") """

#Percobaan dengan banyak argumen (argumen1, argumen2, argumenN)
""" def cake(bahan, bahan2, bahan3):
    if bahan == "Cherry":
        print("Wow cake dengan Cherry greed!")
    elif bahan == "Cheese":
        print("Uhmm... not bad")
    else:
        print("Yeah it's delicious", bahan, "and", bahan2, "more", bahan3)
cake("Cokalt", "Keju", "Jelly") """

""" def cake(bahan, bahan2, bahan3):
    if bahan == "Cherry":
        print("Wow cake dengan Cherry greed!")
    elif bahan == "Cheese":
        print("Uhmm... not bad")
    else:
        print("Yeah it's delicious", bahan, "and", bahan2, "more", bahan3)
        
bahan = input("Masukkan pilihan 1: ")
bahan2 = input("Masukkan pilihan 2: ")
bahan3 = input("Masukkan pilihan 3: ")
cake(bahan, bahan2, bahan3) """

import random

dice = int(input("How Many Sides? "))
close = "yes"

def rollDice(dice):
    print("You rolled", random.randint(1, dice))

while close == "yes":
    rollDice(dice)
    close = input("Roll again? ")
