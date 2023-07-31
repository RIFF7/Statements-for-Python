import random, os, time

listWord = ["Love", "Heart", "People", "Human"]
letterPick = []
lives = 6

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word = random.choice(listWord)

while True:
    #time.sleep(1)
    #os.system("cls")
    letter = input("Chooxe the letter: ").lower()
    
    if letter in letterPick:
        print("You've tried that before")
        continue
    
    letterPick.append(letter)
    
    if letter in word:
        print("You found a letter")
    else:
        print("Nope, not in there")
        lives -= 1
        
    allLetters = True
    print()
    for i in word:
        if i in letterPick:
            print(i, end="")
        else:
            print("_", end="")
            allLetters = False
    print()
    
    if allLetters:
        print(f"You won with {lives} left!")
        break
    
    if lives <= 0:
        print(f"You ran out of lives! The answer was {word}")
        print(HANGMANPICS[6])
        break
    elif lives <= 1:
        print(f"Only {lives} left")
        print(HANGMANPICS[5])
    elif lives <= 2:
        print(f"Only {lives} left")
        print(HANGMANPICS[4])
    elif lives <= 3:
        print(f"Only {lives} left")
        print(HANGMANPICS[3])
    elif lives <= 4:
        print(f"Only {lives} left")
        print(HANGMANPICS[2])
    elif lives <= 5:
        print(f"Only {lives} left")
        print(HANGMANPICS[1])
    else:
        print(f"Only {lives} left")
        print(HANGMANPICS[0])

""" Kode di atas adalah permainan sederhana yang menantang pengguna untuk menebak sebuah kata secara acak 
dari daftar listWord. Pengguna diminta untuk memasukkan satu huruf pada setiap giliran. 
Jika huruf yang dimasukkan ada dalam kata yang harus ditebak, maka huruf tersebut akan ditampilkan. 
Jika huruf yang dimasukkan tidak ada dalam kata, maka nyawa pengguna akan berkurang dan gambar hangman 
yang terkait akan ditampilkan. Jika pengguna berhasil menebak seluruh huruf dalam kata sebelum nyawa habis, 
maka pengguna menang. Jika nyawa habis, pengguna kalah.

Penjelasan langkah demi langkah dari kode tersebut adalah sebagai berikut:

1. import random, os, time: Mendatangkan modul random, os, dan time 
yang digunakan dalam permainan ini.

2. listWord = ["Love", "Heart", "People", "Human"]: Ini adalah daftar kata-kata 
yang mungkin akan dipilih oleh program sebagai kata yang harus ditebak oleh pengguna.

3. letterPick = []: Ini adalah list yang berfungsi 
untuk menyimpan huruf-huruf yang telah dipilih oleh pengguna.

4. lives = 6: Ini adalah jumlah 
nyawa yang dimiliki pengguna untuk menebak kata.

5. HANGMANPICS = [''' ... ''']: Ini adalah gambar-gambar 
hangman yang akan ditampilkan saat nyawa pengguna berkurang.

6.word = random.choice(listWord): Program akan memilih sebuah kata secara acak 
dari listWord untuk menjadi kata yang harus ditebak oleh pengguna.

7. while True:: Ini adalah loop 
utama yang akan berjalan selama permainan.

8. Pengguna diminta untuk memasukkan huruf dengan perintah 
letter = input("Chooxe the letter: ").lower(). 
Huruf yang dimasukkan oleh pengguna akan diubah menjadi huruf kecil menggunakan 
.lower() agar program tidak sensitif terhadap huruf kapital atau huruf kecil.

9. Program memeriksa apakah huruf yang dimasukkan pengguna 
sudah pernah dipilih sebelumnya. Jika iya, maka program akan mencetak 
"You've tried that before" dan melanjutkan loop ke 
langkah berikutnya menggunakan pernyataan continue.

10. Jika huruf belum dipilih sebelumnya, maka huruf akan ditambahkan 
ke dalam letterPick dengan perintah letterPick.append(letter).

11. Program memeriksa apakah huruf yang dimasukkan 
pengguna ada dalam kata yang harus ditebak. 
Jika iya, maka program akan mencetak "You found a letter".

12. Jika huruf tidak ada dalam kata, maka nyawa pengguna 
akan berkurang (lives -= 1) dan program akan 
mencetak "Nope, not in there".

13. Program kemudian mencetak lirik yang telah terisi 
huruf-huruf yang benar dan menampilkan tanda garis 
bawah untuk huruf-huruf yang belum terisi dengan 
menggunakan loop for dan if.

14. Program memeriksa apakah seluruh huruf dalam kata telah terisi. 
Jika iya, maka pengguna menang dan permainan berakhir 
dengan mencetak "You won with [lives] left!".

15. Jika nyawa habis (lives <= 0), maka program mencetak 
"You ran out of lives! The answer was [word]" dan 
menampilkan gambar hangman yang lengkap.

16. Jika nyawa berkurang, program akan mencetak pesan yang 
menampilkan sisa nyawa yang dimiliki dan 
menampilkan gambar hangman yang sesuai.

Dengan cara ini, program menciptakan permainan sederhana di mana pengguna 
dapat menebak kata acak dari daftar kata dengan 
memilih huruf-huruf yang tepat. """
