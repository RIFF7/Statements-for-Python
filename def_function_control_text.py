""" ada kode yang diberikan, end="" 
digunakan untuk mengontrol karakter yang 
dicetak setelah baris teks selesai diproses 
oleh fungsi print(). Secara default, 
setelah mencetak baris teks, fungsi print() 
akan menambahkan karakter newline ("\n") 
pada akhir baris, sehingga mencetak baris 
baru dan berpindah ke baris berikutnya. 
Namun, dengan menggunakan end="", 
karakter newline tidak akan ditambahkan, 
sehingga baris berikutnya akan dicetak 
di samping baris sebelumnya. """

""" Sedangkan penggunaan dari sep="" adalah
melakukan penghapusan pada white space pada text

Dalam kode yang diberikan, 
sep="" digunakan untuk mengontrol 
pemisah antara argumen yang dicetak 
dengan menggunakan fungsi print(). 
Secara default, setiap argumen yang 
dilewatkan ke fungsi print() akan dicetak 
dengan menggunakan spasi sebagai pemisah 
di antara argumen-argumen tersebut. 
Namun, dengan menggunakan sep="", 
pemisah atau separator antara argumen 
akan dihilangkan."""

#Dibawah adalah versi manual tanpa Subrutin
""" print('Super Subroutine ', end='', sep='')

print('With my ', '\033[0;35m', 'new program ',
      '\033[0m','I can just call red("and") ', 
      '\033[0;31m', 'and ', '\033[0m',
      'that world will appear in the color I set it to', end='', sep='')

print('With no ', '\033[0;36m', 'weird gaps ', '\033[0m', end='', sep='')

print('Epic') """

#Dibawah ini menggunakan Subrutin
def newPrint(color, word):
    if color == "purple":
        print("\033[0;35m", word, end="", sep="")
    elif color == "red":
        print("\033[0;31m", word, end="", sep="")
    elif color == "cyan":
        print("\033[0;36m", word, end="", sep="")
    else:
        print("\033[0m", word, end="", sep="")

print("Super Subroutine")
newPrint("reset", "With my ")
newPrint('reset', 'I can just call red("and") ')
newPrint("red", "and ")
newPrint("reset", "that world will appear in the color I set it to")
newPrint("reset", "With no ")
newPrint("cyan", "weird gaps ")
newPrint("reset", "Epic")
