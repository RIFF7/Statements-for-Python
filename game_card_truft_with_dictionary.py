# Project Game Kartu TRUFT dengan dictionary
import os, time, random

# Pertama kita akan membuat variabel "card"
# untuk menampung isi dalam dictionary yang 
# akan dibuat 
card = {}

# Code dibawah adalah key dan sub keys serta value
# yang telah dibuat dan akan ditampung pada variabel
# "card"
card["Arres"] = {"Intelligence": 170, "Speed": 99,
                 "Guile": 77, "Baldness Level": 0}
card["Joy Boy"] = {"Intelligence": 157, "Speed": 80,
                 "Guile": 89, "Baldness Level": 75}
card["Kelly"] = {"Intelligence": 190, "Speed": 99,
                 "Guile": 65, "Baldness Level": 90}

# Dibawah adalah perulangan while, yang akan digunakan
# untuk menanyakan pada player / user untuk memilih
# character yang ada dalam dictionary "card"
while True:
    print()
    print("🌟 Top Trumps 🌟")
    print()
    print("Welcome to the Top Trumps 'Most Handsome Computing Teachers' Simulator")
    print()
    print("Character")
    print()
    # Perulangan dibawah akan menampilkan isi dalam
    # keys dictionary yang ada pada variabel "card"
    for key in card:
        print(key)
    # Setelah perulangan tercapai maka player / user
    # akan diminta untuk memilih karakter yang ada
    # dalam dictionary pada variabel "card"
    user = input("Pick your character\n> ")
    # Setelah user / player selesai memilih
    # maka selanjutnya giliran komputer yang akan 
    # memilih, namun disini pilihan komputer akan
    # ditentukan secara random berdasarkan keys list
    # yang ada pada dictionary "card"
    comp = random.choice(list(card.keys()))
    print("Computer has picked", comp)
    
    print("Chose your stat: Intelligence, Speed, Guile & Baldness Level")
    # Lalu setelah user dan komputer selesai memilih
    # maka selanjutnya code dibawah akan dijalankan
    # untuk meminta user / player memilih 
    # sub key berdasarkan data 
    # dalam dictionary "card"
    answer = input("> ")
    # Setelah sub key selesai dipilih maka code
    # dibawah akan dijalankan untuk menampilkan
    # hasil pilihan yang dimasukkan sebelumnya
    # yaitu sub key, sehingga jika user / player
    # memilih salah satu data sub key yang ada
    # dalam dictionary "card" maka setelah itu 
    # akan menampilkan data dari key, sub key dan 
    # value yang ada dalam dictionary "card"
    print(f"{user}: {card[user][answer]}")
    print(f"{comp}: {card[comp][answer]}")
    # Code dibawah akan melakukan pengecekan pada
    # key, sub key dan value dari dictionary
    # jika key dan sub key dari user / player
    # lebih besar valuenya, maka perintah "if"
    # akan dijalankan, namun 
    # jika key dan sub key dari komputer lebih
    # besar valuenya, maka perintah "elif" akan
    # dijalankan dan ketika valuenya sama, maka
    # code dari "else" akan dijalankan
    if card[user][answer] > card[comp][answer]:
        print(user, "wins!")
    elif card[user][answer] < card[comp][answer]:
        print(comp, "wins!")
    else:
        print("DRAW!")
    # code dibawah untuk menjeda tampilan hasil
    # dari resul pengecekan statement if - elif
    time.sleep(2)
    # code dibawah akan melakukan pembersihan 
    # tampilan, agar kembali ke tampilan awal
    # dari perulangan while lagi
    os.system("cls")
