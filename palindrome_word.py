# Kode di bawah adalah implementasi rekursif 
# untuk memeriksa apakah sebuah kata merupakan
# palindrome atau tidak. Palindrome adalah 
# kata yang terbaca sama baik dari depan
# maupun dari belakang. 

# Example kata palindrome:

# "level"
# "deified"
# "rotor"
# "madam"
# "racecar"
# "refer"
# "civic"
# "radar"
# "noon"
# "tenet"

# Jika diperhatikan kata diatas jika 
# pembacaannya baik itu dari depan atau 
# belakang maka akan tetap terbaca 1 kata saja
# contoh jika dibaca depan "level" dan jika
# dibaca belakang tetap "level" juga

# Mari kita bahas langkah-langkahnya:
#  Ini adalah deklarasi fungsi palindrome 
# yang mengambil satu argumen word, 
# yaitu kata yang ingin diperiksa apakah 
# palindrome atau tidak.
def palindrome(word):
    #  Ini adalah blok kondisi pertama. 
    # Jika panjang word kurang dari atau 
    # sama dengan 1, maka itu dianggap 
    # palindrome. Mengapa? Karena kata 
    # dengan panjang 0 atau 1 pasti 
    # palindrome (seperti "a" atau ""), 
    # dan ini menjadi dasar dari rekursi.
    if len(word) <= 1:
        return True
    # Di dalam blok kondisi kedua, 
    # ini memeriksa apakah karakter 
    # pertama (word[0]) tidak sama dengan 
    # karakter terakhir (word[-1]). 
    # Jika tidak, maka kata tersebut bukan 
    # palindrome, dan fungsi akan 
    # mengembalikan False.
    if word[0] != word[-1]:
        return False
    # Di dalam blok kondisi kedua, jika 
    # karakter pertama dan terakhir sama, 
    # maka rekursi terjadi. Fungsi palindrome 
    # dipanggil kembali dengan argumen 
    # word[1:-1], yaitu kata yang 
    # menghilangkan karakter pertama dan 
    # terakhirnya. Ini mengulangi proses 
    # pemeriksaan palindrome untuk kata yang 
    # lebih pendek.
    return palindrome(word[1:-1])
# Pemanggilan fungsi palindrome dengan 
# argumen "level". Fungsi ini akan mencoba 
# memeriksa apakah kata "level" adalah 
# palindrome atau tidak, dan hasilnya akan 
# dicetak.
print(palindrome("level"))
