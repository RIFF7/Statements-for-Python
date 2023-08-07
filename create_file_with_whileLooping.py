# Membuat file dan melakukan inputan pada
# data yang ada pada file tersebut
import os, time

while True:
    print()
    print("HIGH SCORE TABLE")
    print()
    # Code dibawah akan meminta kita untuk
    # memasukkan inputan untuk data dalam file
    # yang akan kita buat
    initial = input("INITIALS > ")
    score = input("SCORE > ")
    # Code dibawah akan membuat file baru
    # dengan extantion .score dengan fungsi append
    # Mode a+ digunakan untuk membuka file 
    # dalam mode tambah dengan akses baca 
    # dan tulis.
    f = open("try_days_48.score", "a+")
    # Code dibawah digunakan untuk mengisi data
    # yang sebelumnya kita input pada variabel
    # initial dan score
    f.write(f"{initial} {score}\n")
    print()
    # Sedangkan code dibawah akan memunculkan
    # pertanyaan masukkan apakah kita akan melakukan
    # penambahan data kembali atau tidak
    close = input("Again? y/n > ")
    if close == "n":
        print()
        print("ADDED!")
        f.close()
        break
    time.sleep(1)
    os.system("cls")
