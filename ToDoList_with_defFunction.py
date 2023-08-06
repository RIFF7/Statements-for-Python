# Membuat list dengan tampilan
# | Name | Date | Priority

import os, time

# Code dibawah digunakan untuk menampung list yang dibuat
TodoList = []

# Subrutin dibawah digunakan utuk melakukan perintah
# tambah (add) data pada TodoList
def add():
    time.sleep(1)
    os.system("cls")
    # Code dibawah digunakan untuk membuat masukan pada perintah "Add"
    name = input("Name: ")
    date = input("Due Date: ")
    priority = input("Priority: ").capitalize()
    # Code dibawah digunakan untuk menggabungkan masukan sebagai list dengan index
    row = [name, date, priority]
    # Code dibawah digunakan untuk menambahkan data yang 
    # sudah diinput dalam row list, 
    # sehingga masuk pada penyimpanan 
    # variabel TodoList
    TodoList.append(row)
    # Code dibawah akan dijalankan 
    # jika kita telah berhasil menambahkan 
    # data pada TodoList
    print("Added!")

# Subrutin dibawah akan memerintahkan untuk
# menampilkan data yang ada pada TodoList
# berdasarkan priority yang telah dimasukkan
# sebelumnya pada perintah subrutin (add)
def view():
    time.sleep(1)
    os.system("cls")
    # Code dibawah akan memunculkan pilihan 
    # dimana kita harus memilih antara 1 jika 
    # ingin menampilkan seluruh priority yang ada 
    # pada list TodoList dan jika kita memilih 2 
    # maka kita akan diminta untuk memilih priority 
    # sesuai dengan yang kita masukkan pada list di 
    # perintah Add sebelumnya dan data yang akan tampil
    # adalah data dalam priority High, Low atau 
    # lainnya yang kita masukkan pada TodoList
    option = input("1. All\n2. By Priority\n> ")
    print()
    # Jika pilihan kita adalah string dengan karakter 1
    # maka data yang ditampilkan adalah seluruh priority
    # yang ada pada TodoList berdasarkan row yang telah 
    # dimasukkan sebelumnya
    if option == "1":
        for row in TodoList:
            for item in row:
                print(item, end=" | ")
            print()
        print()
    # Nmaun jika string yang kita masukkan adalah 
    # karakter 2, maka perintah dibaawah akan 
    # dijalankan dan meminta kita untuk memasukkan 
    # pilihan priority yang ada pada TodoList
    # berdasarkan row yang telah kita masukkan 
    # sebelumnya pada TodoList
    else:
        priority = input("What Priority? ").capitalize()
        print()
        for row in TodoList:
            if priority in row:
                for item in row:
                    print(item, end=" | ")
                print()
        print()
    time.sleep(1)

# Subrutin yang dibawah digunakan untuk melakukan
# perubahan (edit) pada data yang sebelumnya ada
# dalam Todolist
def edit():
    time.sleep(1)
    os.system("cls")
    # Code dibawah meminta kita untuk memasukkan 
    # kata yang ada pada TodoList yang akan kita ubah
    find = input("Name of To Do List Edit? ")
    # Pada nilai awal kata (found) 
    # akan kita buat False
    found = False
    # Sehingga kata yang kita masukkan akan dicek
    # terlebih dahulu pada row di dalam TodoList
    # kata yang kita masukkan sebelumnya ada atau 
    # tidak
    for row in TodoList:
        # Jika kata yang kita masukkan ada dalam
        # TodoList, maka kata (found) akan diubah
        # menjadi True dan lanjut pada perintah 
        # "for berikutnya"
        if find in row:
            found = True
    # Namun jika kata (found) yang kita masukkan 
    # sebelumnya tidak ada dalam row TodoList
    # Code dibawah yang akan berjalan
    # sehingga akan mencetak kata yang ada pada 
    # perintah print() dan mengembalikan kembali pada 
    # perintah inputan sebelumnya yaitu "find"
    # untuk mengulang kembali kata yang dicari 
    # untuk dilakukan perubahan (edit)
    if not found:
        print("Couldn't find that!")
        return
    # Jika kata yang dimasukkan sesuai dengan list
    # yang ada pada TodoList, maka perintah dibawah
    # akan dijalankan untuk melakukan penghapusan
    # pada daftar pertama kali yang ditambahkan pada
    # row TodoList dan setelah dilakukan penghapusan
    # data yang ada pada TodoList, maka selanjutnya
    # kita akan diminta untuk menginput kembali
    # data baru untuk dimasukkan sebagai pengganti
    # data pada row sebelumnya
    for row in TodoList:
        if find in row:
            TodoList.remove(row)
    # Setelah sebelumnya dilakukan penghapusan pada
    # row yang ada pada TodoList, kita akan memasukkan
    # kembali data baru dengan perintah input()
    # dibawah ini
    name = input("Name: ")
    date = input("Due Date: ")
    priority = input("Priority: ").capitalize()
    # Setelah data input() dari 3 variabel dimasukkan
    # maka, kita akan meletakkannya pada row dalam 
    # bentuk list dibawah ini
    row = [name, date, priority]
    # Setelah data dari 3 variabel sebelumnya ada
    # pada satu variabel yaitu row, maka code
    # dibawah akan memerintahkan untuk menambahkan
    # value dari row pada list TodoList dengan 
    # peintah append()
    TodoList.append(row)
    # Jika data baru berhasil ditambahkan, 
    # maka perintah cetak dibawah akan ditampilkan
    print("Edited!")

# Subrutin dibawah akan melakukan perintah hapus
# pada data yang ada dalam TodoList berdasarkan row
# yang ada dalam data Todolist
def remove():
    time.sleep(1)
    os.system("cls")
    # Code dibawah akan meminta kita untuk memasukkan
    # kata yang akan kita hapus berdasarkan row yang 
    # ada pada TodoList    
    find = input("Name of To Do List Remove? ")
    # Kata yang sudah dimasukkan sebelumnya
    # akan dicek berdasarkan row yang ada pada 
    # TodoList dengan code dibawah ini
    for row in TodoList:
        # Jika kata (find) yang dimasukkan sesuai pada
        # row dalam TodoList, maka data tersebut
        # akan dilakukan penghapusan
        if find in row:
            # Code dibawah adalah perintah
            # untuk melakukan penghapusan datanya
            # dengan fungsi remove() berdasarkan row
            TodoList.remove(row)

# Code dibawah akan membuat menu perulangan
# yang menampilkan 4 pilihan Add, View, Edit, Remove
while True:
    # Code dibawah meminta kita untuk memilih
    # dari angka 1 - 4 
    menu = input("1. Add\n2. View\n3. Edit\n4. Remove\n> ")
    # Jika menu sama dengan 1 yaitu Add
    # code dibawah akan dijalankan berdasarkan
    # subrutin (add) yang telah dibuat sebelumnya
    if menu == "1":
        add()
    # Namun jika menu sama dengan 2, maka
    # code dibawah akan dijalankan dengan 
    # subrutin view yang telah dibuat sebelumnya
    elif menu == "2":
        view()
    # Dan jika menu sama degan 3, maka
    # code dibawah akan dijalankan berdasarkan
    # subrutin edit yang telah dibuat sebelumnya
    elif menu == "3":
        edit()
    # Untuk pilihan lainnya maka akan menjalankan 
    # code dibawah, yaitu subrutin dari remove
    # yang telah dibuat sebelumnya
    else:
        remove()
    
    time.sleep(1)
    os.system("cls")
