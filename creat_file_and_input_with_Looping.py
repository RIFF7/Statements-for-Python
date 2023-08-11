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
        
# Versi kedua menggunakan subrutin agar lebih simple

# Secara output baik cara pertama dan kedua semuanya
# memiliki fungsi yang sama yaitu menginput sebuah
# data pada file yang kita buat
import os, time, random

# Subrutin dibawah digunakan untuk membuat file dan 
# menambahkan data pada file yang telah dibuat dengan
# fungsi "w" (write) untuk membuat file dan "a+" untuk
# menambah data dalam file dan membaca file
def add():
    os.system("cls")
    idea = input("Idea > ")
    f = open("my.ideas", "a+")
    f.write(f"{idea}\n")
    f.close()
    time.sleep(1)
    os.system("cls")

# Subrutin dibawah ini digunakan untuk membaca
# data dengan fungsi "r" (read) dan menampilkannya
# secara acak menggunakan funsgi 
# random.choice(variabel)
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

# Perulangan dibawah akan meminta user untuk
# memasukan pilihan antara tambah data atau 
# tampilkan data secara acak    
while True:
    question = input("1. Add an ideas\n2. Load up a random ideas\n> ")
    # Jika user memilih option 1, maka perintah
    # dari subrutin add() akan dijalankan
    if question == "1":
        add()
    # Namun jika user memasukan string selain 1,
    # maka perintah subrutin dari show() akan
    # dijalankan
    else:
        show()
