""" def pinPicker(number):: Ini adalah definisi fungsi pinPicker yang mengambil satu parameter bernama number. Parameter number akan menentukan panjang PIN yang akan dibuat.

import random: Ini adalah pernyataan untuk mengimpor modul random yang diperlukan untuk menghasilkan bilangan acak.

pin = "": Membuat variabel pin yang awalnya berisi string kosong. Nantinya, kita akan menambahkan karakter-karakter acak untuk membangun PIN.

for i in range(number):: Loop for akan dijalankan sebanyak number kali, sesuai dengan panjang PIN yang ditentukan.

pin += str(random.randint(0, 9)): Pada setiap iterasi, kita memilih angka acak antara 0 dan 9 menggunakan fungsi random.randint(0, 9), dan kemudian menggabungkannya ke variabel pin dengan menggunakan operator +=. Fungsi str() digunakan untuk mengubah angka menjadi string sebelum ditambahkan ke pin.

return pin: Setelah loop selesai, fungsi mengembalikan PIN yang telah dibangun.

myPin = pinPicker(4): Memanggil fungsi pinPicker dengan argumen 4, sehingga fungsi ini akan menghasilkan PIN dengan panjang 4 karakter dan menugaskan hasilnya ke variabel myPin.

print(myPin): Mencetak PIN yang dihasilkan. """

""" Berikut adalah contoh iterasinya dengan mengambil number = 4:

Misalkan hasil dari random.randint(0, 9) pada setiap iterasi adalah: 8, 3, 5, dan 0.

Iterasi 1:

pin = "" (awal)
Angka acak: 8
pin += "8"
Hasil pin: "8"
Iterasi 2:

pin = "8" (hasil dari iterasi sebelumnya)
Angka acak: 3
pin += "3"
Hasil pin: "83"
Iterasi 3:

pin = "83" (hasil dari iterasi sebelumnya)
Angka acak: 5
pin += "5"
Hasil pin: "835"
Iterasi 4:

pin = "835" (hasil dari iterasi sebelumnya)
Angka acak: 0
pin += "0"
Hasil pin: "8350" """


def pinPicker(number):
    import random
    pin = ""
    for i in range(number):
        pin += str(random.randint(0, 9))
    return pin

myPin = pinPicker(4)
print(myPin)

#Contoh lainnya

""" Fungsi areaOfTriangle adalah sebuah fungsi untuk menghitung luas segitiga berdasarkan panjang alas (base) dan tinggi (height) yang diberikan. Berikut adalah penjelasan langkah demi langkah dari kode tersebut:

def areaOfTriangle(base, height):: Ini adalah definisi fungsi areaOfTriangle yang mengambil dua parameter, yaitu base (panjang alas) dan height (tinggi).

area = 0.5 * base * height: Dalam fungsi ini, kita menghitung luas segitiga menggunakan rumus luas segitiga, yaitu 0.5 * base * height. Hasil perhitungan tersebut disimpan dalam variabel area.

return area: Setelah menghitung luas segitiga, fungsi ini mengembalikan nilai area.

area = areaOfTriangle(5, 22): Kode ini memanggil fungsi areaOfTriangle dengan dua argumen, yaitu 5 untuk base dan 22 untuk height. Sehingga fungsi akan menghitung luas segitiga dengan alas 5 dan tinggi 22.

print(area): Ini akan mencetak nilai yang dikembalikan oleh fungsi areaOfTriangle, yaitu luas segitiga yang dihitung sebelumnya, yaitu 55.0.

Jadi, kode tersebut akan mencetak nilai 55.0, yang merupakan luas segitiga dengan alas 5 dan tinggi 22. """
def areaOfTriangle(base, height):
    area = 0.5 * base * height
    return area

area = areaOfTriangle(5, 22)
print(area)

#PR
""" Let's extend Day 24's project and create a health stats generator for a character in a video game.

Create a subroutine that rolls a dice of any size and returns that number.
Then, create a second subroutine that rolls one six-sided dice and one eight-sided dice.
Multiply the number from the six-sided dice and eight-sided dice together and return that subroutine as a character's health stats for a video game.
Print out the character's health stats.
Add a loop to give the user the option to generate health stats for another character.
(We genuinely see this in video games!)

🥳 Extra points if you ask for the character's name and double extra points if you use different colors!

⚔️ Character Stats Generator ⚔️
Name your warrior: Agnes
Their health is: 20hp
Name your warrior: Ian
Their health is: 6hp
Name your warrior: Penelope
Their health is: 48hp """

import random

def rollDice(sides):
  result = random.randint(1,sides)
  return result

def roll_6_and_8():
  roll_6_sided_dice = rollDice(6)
  roll_8_sided_dice = rollDice(8)
  health = roll_6_sided_dice * roll_8_sided_dice
  return health

print("⚔️Character stats generator⚔️")
  

haveACharacter = "yes"

while haveACharacter == "yes":
  character = input("Name your warrior: ")
  health = str(roll_6_and_8())
  print("Their health is ", health,"hp" ) 
  haveACharacter = input("Want to create another character?")
