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
    variable dari argument yang dibuat
'''

# Mode 1
print('what is your name?')
myName = input()
print('My Name is ' + myName)

# Mode 2
myName = input('What is your name? ')
print('My Name is ' + myName)

#--------------------------------------------------------------------------------------------------------------

