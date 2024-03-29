# Part 1 BASICS PYTHON

# Penjumlahan
2 + 2

# Output
2

# Operator Aritmatika
# Penjumlahan dan Perkalian (Tanpa Fokus Bilangan) -> Addition and Multiplication
2 + 3 * 6

'''
    Addition and Multiplication
    Penjumlahan dan Perkalian (Dengan Fokus Bilangan -> (Fokus bilangan dalam kurung))
'''
(2 + 3) * 6

# Perkalian (Multification)
48565878 * 578453

# Pangkat (Exponent)
2 ** 8

# Pembagian Koma (Division)
23 / 7

# Pembagian Bulat (Integer Division / Floored Quotient)
23 // 7

# Sisa Hasil Bagi (Modulus / Reminder)
23 % 7

# Penjumlahan Dengan Test Spasi
2       +       2

'''
    Penjumlahan, Pengurangan, Perkalian, Pembagian 
    dengan fokus bilangan dalam kurung
'''
(5 - 1) * ((7 + 1) / (3 - 1))

#--------------------------------------------------------------------------------------------------------------

# Pengenalan Integer, Floating-Point dan String Data Types

# String Concatenation and Replication
# Penggabungan (Concatenation)
'Alice' + 'Bob'

'''
    Penggabungan dibawah ini akan menghasilkan error
    karena string tidak bisa digabungkan dengan tipe data
    integer
'''
'Alice' + 42

'''
    Code dibawah ini akan menampilkan string
    sebanyak nilai yang dikalikan dengannya
'''
'Alice' * 5 # Tanpa koma dan spasi
'Alice,' * 5 # Dengan Koma
'Alice ' * 5 # Dengan Spasi

'''
    Code dibawah akan menghasilkan error
    karena value dari string tidak bisa 
    dikalikan dengan string juga
'''
'Alice' * 'Bob'

'''
    Code dibawah akan menghasilkan error juga
    karena value string tidak bisa dikalikan dengan
    value dari nilai float
'''
'Alice' * 5.0

# Menyimpan Nilai dalam Variabel (Storing Values in Variables)
# Assigment Statements
spam = 40 # variable dengan satu value
spam # Ketika memanggil variable value akan muncul pada output

eggs = 2 # variable dengan satu value
spam + eggs # Melakukan penjumlahan dengan variable yang sudah ada isi value

spam + eggs + spam

spam = spam + 2
spam

'''
    Code dibawah akan mengisi variable spam menjadi 'Hello'
    pada penggantian pertama value dari nilai sebelumnya dimana
    adalah sebuah angka
'''
spam = 'Hello'
spam

'''
    Code dibawah akan melakukan pergantian kembali pada vaiable spam
    dimana value akan berubah menjadi tulisan 'GoodBye'
'''
spam = 'GoodBye'
spam

#--------------------------------------------------------------------------------------------------------------

# First Program

# This program says hello and asks for my name
# Menanyakan Nama
print('Hello World!')
print('What is your name? ')
myName = input()
print('It is good to meet you, ' + myName)

# Menampilkan panjang karakter nama
print('The length of your name is:')
print(len(myName))

# Menanyakan umur
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

#--------------------------------------------------------------------------------------------------------------

# Comment

'''
    Penggunaan Comment dapat digunakan dengan tanda Kres/Sharp (#)
    bisa juga digunakan dengan petik sebanyaka 6 kali (''' ''')
'''

#--------------------------------------------------------------------------------------------------------------

# print()

'''
    Penggunaan fungsi print() pada python adalah untuk mencetak output 
    yang akan dikeluarkan nantinya
    
    fungsi print() dapat dipadukan juga dengan fungsi 'f-string', example:
    - print(f'Some_Think')
'''

print('Hello World!')
print('What is your name?') #ask for their name

#--------------------------------------------------------------------------------------------------------------

# Fungsi Input & Tampilan Output dari hasil Input

'''
    Untuk penggunaan fungsi input() disini adalah untuk memasukkan
    variable dari argument yang dibuat dimana hasilnya akan ditampilkan
    pada perintah print() setelahnya, hasil output ini diambil dari hasil
    input sebelumnya, example dibawah ini:
'''

# Mode 1
print('what is your name?')
myName = input()
print('My Name is ' + myName)

# Mode 2
myName = input('What is your name? ')
print('My Name is ' + myName)

#--------------------------------------------------------------------------------------------------------------

# Fungsi len() atau panjang dari karakter

'''
    Fungsi dari len() ini akan menghitung panjang
    karakter dari hasil input atau arugument
'''
print('The length of your name is:')
print(len(myName)) # Ini akan menghitung karakter input yang ada pada variable 'myName'

len('hello')

len('My very energetic monster just scarfed nachos.')

len('')
#--------------------------------------------------------------------------------------------------------------

# Fungsi str(), int(), and float()
'''
    Jika suatu saat kamu ingin menghubungkan variable
    string dengan integer pada sebuag kalimat dengan 
    menggunakan concatination (+) maka kamu dapat mengubah
    variable tersebut sesuai dengan tipe datanya terlebih dahulu
    
    Jika tipe data tidak diubah maka akan terjadi error ketika
    menggunakan concatination, example:
'''

print('I am  ' + 29 + ' years old.') # Code ini akan menghasilkan error, karena tipe data value tidak diubah

str('26')

print('I am ' + str(26) + ' years old.') # Code ini adalah yang sesuai, dimana value diubah terlebih dahulu tipe datanya

str(0) # Dari int diubah menjadi string

str(-3.14) # Dari float diubah menjadi string

int('42') # Dari string diubah menjadi int

int('-99') # Dari string diubah menjadi int

int(1.25) # Dari float diubah dibulatkan menjadi int

int(1.99) # Dari float diubah dibulatkan menjadi int

float('3.14') # Dari string diubah menjadi float

float(10) # Dari int diubah menjadi float

# Contoh lainnya

spam = input() # Setiap hasil input akan dibaca sebagai string (walaupun itu int)
spam

# Cara untuk mengatasi permasalah diatas adalah mengubah tipe data yang akan diinput, seperti dibawah ini:

# Cara 1, mengubah tipe data dari variable
spam = int(spam)
spam

# Cara 2, langsung ubah tipe data pada hasil input
spam = int(input())
spam

spam * 10/5

'''
    Contoh dibawah ini akan menghasilkan error
'''
int('99.99') # Fungsi int hanya akan berguna untuk nilai bulat float pada nomor dibawahnya (Tidak bisa dengan string)

int('twelve') # Karakter tulisan jelas tidak bisa dibuat menjadi int

'''
    Contoh yang benar, seperti dibawah ini
'''
int(7.7)

int(7.7) + 1

# PROGRAM
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

#--------------------------------------------------------------------------------------------------------------
