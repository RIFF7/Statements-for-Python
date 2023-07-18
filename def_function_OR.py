#Percobaan program LOGIN tanpa LOGIKA

""" print("Replit Login System")

def login():
    while True:
        username = input("What is your username? ")
        if username == "Arres":
            password = input("What is your password? ")
            if password == "hello":
                print("Welcome to Replit!")
                break
            else:
                print("Whoops! I don't recognize that username or password. Try again!")
        else:
            continue

login() """

#PERCOBAAAN LOGIN DENGAN LOGIKA AND

def login():
    while True:
        username = input("What is your username? ")
        password = input("What is your password? ")
        if username == "Arres" and password == "hello":
            print("Welcome to Replit!")
            break
        else:
            print("Whoops! I don't recognize that username or password. Try again!")
            continue
login()
