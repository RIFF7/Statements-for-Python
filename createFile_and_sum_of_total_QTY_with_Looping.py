import os, time

# Code dibawah adalah tempat untuk menyimpan
# data yang telah kita masukkan pada subrutin
# pizzaAdd()
listEat = []

# Code try an except digunakan untuk
# melakukan pengecekan apakah file "List Eating.txt"
# ada pada file atau tidak, jika tidak maka perintah
# except akan dijalankan
try:
    f = open("List Eating.txt", "r")
    listEat = eval(f.read())
    f.close()
except:
    print("ERROR: No data to load in file List Eating!")

# Code dibawah akan membuat subrutin dimana akan
# kita gunakan sebagai perintah inputan pada data
# yang akan dimasukkan pada "listEat" yang nantinya
# disimpan pada file "list Eating.txt"
def pizzaAdd():
    time.sleep(1)
    os.system("cls")
    name = input("Name: ")
    toppings = input("Toppings: ")
    size = input("Size (s/m/l): ").lower()
    # Pada perintah while True dibawah akan digunakan
    # untuk perulangan pengecekan try dan except
    # jika inputan bukan berupa angka maka perintah
    # except akan dijalankan, namun jika inputan
    # berupa angka maka akan dimasukkan untuk 
    # perhitungan selanjutnya
    while True:
        try:
            qty = int(input("Quantity: "))
            break
        except:
            print("Error: Quantity must be a whole number!")
    
    # Pada code dibawah akan menentukan harga 
    # berdasarkan size yang kita pilih 
    cost = 0
    if size == "s":
        cost = 5.99
    elif size == "m":
        cost = 9.99
    else:
        cost = 14.99
    
    # Setelah harga ditentukan, maka selanjutnya
    # proses perhitungan akan dijalankan
    # perhitungan dilakukan dengan mengalikan
    # cost dengan qty, yang nanti ahsilnya akan
    # disimpan pada variabel total
    total = cost * qty
    # selanjutnya variabel total diubah kembali
    # menggunakan funsgi round untuk membulatkan
    # suatu angka menjadi sejumlah digit desimal tertentu
    # pada code dibawah akan membulatkan nilai
    # "total" menjadi dua digit desimal
    total = round(total, 2)
    # Setelah semua data selesai diprose maka
    # selanjutnya akan diletakkan pada variabel
    # "row" dalam bentuk list
    row = [name, toppings, size, qty, total]
    # Lalu variabel "row" akan ditambahkan dengan
    # fungsi append(), sehingga value masuk pada
    # variabel "listEat" yang disimpan pada file
    # "List Eating.txt"
    listEat.append(row)
    print("Added!")

# Code dibawah akan membuat subrutin dengan perintah
# untuk menampilkan data yang sudah kita input sebelumnya
# pada file "list Eating.txt"
def pizzaView():
    # Code dibawah digunakan menjadi header pada
    # tampilan:
    # Name    Toppiung    Size    Qty    Total
    # data1    data1      data1   data1  data1
    # dataN    dataN      dataN   dataN  dataN
    h1 = "Name"
    h2 = "Topping"
    h3 = "Size"
    h4 = "Qty"
    h5 = "Total"
    
    # Code dibawah akan menampilkan data sesusai
    # dengan contoh diatas, dimana dari h1 sampai h5
    # akan berada pada center(tengah) dengan nilai 25
    print(f"{h1:^25}{h2:^25}{h3:^25}{h4:^25}{h5:^25}")
    # Code dibawah akan menampilkan isi data dari 
    # variabel listEat berdasrkan "row" dalam list
    for row in listEat:
        print(f"{row[0]:^25}{row[1]:^25}{row[2]:^25}{row[3]:^25}{row[4]:^25}")
    time.sleep(5)

# Code dibawah akan emlakukan perulangan untuk 
# setiap pilihan yang ada pada menu, jika kita
# memilih angka 1 maka akan diminta untuk memasukkan
# data dan ketika selesai akan kembali lagi ke 
# menu awal dan kita diminta untuk memilih kembali
# jika kita memasukkan angka 2 maka akan menampilkan 
# data yang ada pada variabel "listEat" dimana
# sesuai pada file "List Eating.txt"
while True:
    time.sleep(1)
    os.system("cls")
    print("Romanos Pizza")
    print()
    menu = input("1. Add Pizza\n2. View Pizza\n> ")
    if menu == "1":
        pizzaAdd()
    else:
        pizzaView()
    
    # Code dibawah akan membuat sebuah file bernama
    # "List Eating.txt" jika sebelumnya tidak ada
    # dalam file, namun jika ada maka perintah
    # try yang diawal akan dijalankan untuk membaca 
    # data serta melakukan penambahan pada data    
    f = open("List Eating.txt", "w")
    f.write(str(listEat))
    f.close()
