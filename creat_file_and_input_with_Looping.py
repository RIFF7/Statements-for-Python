# Versi pertama menggunakan kondisi if - elif
""" print("🌟 Idea Storage 🌟")
print()

import random, os, time

while True:
    print("IDEAS")
    print()
    question = input("1. Add an ideas\n2. Load up a random ideas\n> ")
    print()
    
    f = open("my.ideas", "a+")
    
    if question == "1":
        ideas = input("Idea > ")
        f.write(f"{ideas}\n")
        f.close()
        time.sleep(1)
        os.system("cls")
    elif question == "2":
        f = open("my.ideas", "r")
        idea = f.read().split("\n")
        f.close()
        idea.remove("")
        ide = random.choice(idea)
        print(ide)
        time.sleep(1)
        os.system("cls") """
        
# Versi kedua menggunakan subrutin
import os, time, random

def add():
    os.system("cls")
    idea = input("Idea > ")
    f = open("my.ideas", "a+")
    f.write(f"{idea}\n")
    f.close()
    time.sleep(1)
    os.system("cls")
    
def show():
    os.system("cls")
    f = open("my.ideas", "r")
    ideas = f.read().split("\n")
    f.close()
    ideas.remove("")
    idea = random.choice(ideas)
    print(idea)
    time.sleep(2)
    os.system("cls")
    
while True:
    question = input("1. Add an ideas\n2. Load up a random ideas\n> ")
    if question == "1":
        add()
    else:
        show()
