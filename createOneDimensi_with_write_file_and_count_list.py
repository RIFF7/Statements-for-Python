# Membuat list dengan menggunakan file sebagai 
# penyimpanan sementara yang dimana hasilnya akan
# menampildan jumlah data pada list terdapat berapa
# dengan menggunakan fungsi 
# "myList.count(variabel iterasi)"
import os, time

# Code dibawah akan menjadi penyimpanan sementara
# guna menampung masukkan yang kita input pada
# subrutin addGame()
listGame = []

try:
    f = open("List Game.txt", "r")
    # Pada kode eval() digunakan untuk 
    # mengubah isi dari file "List Game.txt" 
    # menjadi struktur data Python, seperti 
    # list atau dictionary, jika teks dalam file 
    # mengandung representasi Python yang valid. 
    # Namun, ini juga berarti bahwa jika teks 
    # dalam file tidak aman atau berisi kode 
    # yang tidak diharapkan, itu dapat memiliki 
    # dampak yang merugikan.
    f = eval(f.read())
    f.close()
except:
    #print("Error: No Data to Load!")
    # Ketika suatu pengecualian terjadi, blok 
    # except akan menangkap pengecualian tersebut 
    # dan melanjutkan eksekusi program tanpa 
    # menghasilkan pesan kesalahan atau tindakan 
    # khusus. Dengan kata lain, dalam kode Anda, 
    # ketika terjadi pengecualian saat membaca 
    # atau mengevaluasi file, program akan 
    # melanjutkan ke langkah berikutnya tanpa 
    # menampilkan pesan kesalahan atau melakukan 
    # tindakan khusus.
    pass # Fungsi ini tidak akan memuncukan apapun

def addGame():
    time.sleep(1)
    os.system("cls")
    print("INVENTORY")
    print("=========")
    print()
    item = input("Input the item to add: ").capitalize()
    # Pada code dibawah kita langsung menyimpan
    # data yang telah kita input dan tidak menggunakan
    # row karema disini kita akan berencara membuat
    # list dengan 1 dimensi saja
    listGame.append(item)
    print(item, "has been added to your inventory.")

def viewGame():
    time.sleep(1)
    os.system("cls")
    print("INVENTORY")
    print("=========")
    print()
    
    # Untuk code dibawah akan menampilkan jumlah
    # dari data yang kita input, example:
    # kita memiliki data "Ham", "Burger", "Burger"
    # maka ketika ditampilkan akan menjadi:
    # Ham 1
    # Burger 2
    # Burger 2
    """ for item in listGame:
        print(f"{item} {listGame.count(item)}") """
    # lalu bagaimana jika kita ingin menampilkan
    # Burger 2 satu kali saja?
    # Maka kita dapat menggunakan 2 pendekatan
    # dibawah ini:
    
    # Pendekatan pertama menggunakan "seen = []"
    # Di sini, kita menggunakan list seen untuk 
    # melacak item yang sudah kita lihat 
    # sebelumnya. Dalam loop for, kita iterasi 
    # melalui setiap item dalam listGame, 
    # dan kita periksa apakah item tersebut 
    # sudah ada dalam list seen. Jika belum ada, 
    # kita mencetak hasil perhitungan berapa kali 
    # item tersebut muncul dalam listGame 
    # menggunakan listGame.count(item), 
    # dan kemudian kita tambahkan item ke dalam 
    # list seen.
    """ seen = []
    for item in listGame:
        if item not in seen:
            print(f"{item} {listGame.count(item)}")
            seen.append(item)
    time.sleep(3) """
    
    # Pendekatan kedua menngunakan "seen = set()"
    # Di sini, kita menggunakan tipe data set 
    # untuk membuat himpunan unik dari item dalam 
    # listGame. Ini akan menghapus duplikat dan 
    # hanya menyisakan satu instance dari setiap 
    # item. Kemudian, dalam loop for, kita iterasi 
    # melalui set seen yang berisi item unik, 
    # dan kita menggunakan metode 
    # listGame.count(item) untuk menghitung 
    # berapa kali item tersebut muncul dalam 
    # listGame dan mencetak hasilnya.
    seen = set(listGame)
    for item in seen:
        print(f"{item} {listGame.count(item)}")

    # Perbedaan dari kedua pendekatan adalah 
    # Efisiensi dan Urutan
    
    # Pendekatan pertama dengan menggunakan 
    # list seen lebih mempertahankan urutan 
    # asli item dalam listGame, tetapi lebih 
    # tidak efisien karena memerlukan perulangan 
    # tambahan untuk memeriksa apakah item sudah 
    # ada dalam list seen.
    
    # Perbedaan kedua antara kedua pendekatan 
    # ini adalah pada efisiensi dan urutan 
    # perulangan. Pendekatan kedua dengan 
    # menggunakan set seen lebih efisien dalam 
    # hal waktu dan memori karena menghilangkan 
    # duplikat sejak awal dan hanya perlu 
    # menghitung sekali untuk setiap item unik. 
    # Namun, karena set adalah tipe data yang 
    # tidak terurut, urutan item yang dicetak 
    # mungkin berbeda dengan urutan asli dalam 
    # listGame.

    # Pilihan antara kedua pendekatan tergantung 
    # pada prioritas Anda terhadap efisiensi dan 
    # urutan output. Jika urutan tidak menjadi 
    # masalah, pendekatan kedua dengan set 
    # dapat memberikan kinerja yang lebih baik. 
    # Jika Anda perlu mempertahankan urutan asli, 
    # pendekatan pertama dengan list dapat digunakan.

def removeGame():
    time.sleep(1)
    os.system("cls")
    print("INVENTORY")
    print("=========")
    print()
    item = input("Input the item to add: ").capitalize()
    if item in listGame:
        listGame.remove(item)
        print("Remove for data!")
    else:
        print("No Item in file List Game!")

while True:
    time.sleep(1)
    os.system("cls")
    print()
    print("🌟 RPG Inventory 🌟")
    print()
    menu = input("1. Add\n2. View\n3. Remove\n4. Exit\n> ")
    if menu == "1":
        addGame()
    elif menu == "2":
        viewGame()
    elif menu == "3":
        removeGame()
    else:
        exit()
    
    f = open("List Game.txt", "w")
    f.write(str(listGame))
    f.close()
