import os, time

# Code dibawah digunakan untuk menyimpan data
# yang telah dimasukkan dengan bentuk list
TodoList = []

# Code dibawah digunakan untuk membaca data
# namun jika diawal data file "list.txt" sudah
# ada pada folder, jika belum ada maka akan 
# menampilkan error, cara mengatasinya kita hanya
# perlu off kan saja code dibawah dengan perintah
# hastag (#)
f = open("list.txt", "r")
TodoList = eval(f.read())
f.close()

# Sedangkan penjelasan dari 4 subrutin dibawah
# dapat dilihat pada branches list dengan judul 
# ToDoList_with_defFunction.py
def add():
    time.sleep(1)
    os.system("cls")
    name = input("Name: ")
    date = input("Due Date: ")
    priority = input("Priority: ").capitalize()
    # Code dibawah akan menempatkan 3 data pada
    # variabel diatas dijadikan dalam 1 list pada
    # varibel "row" yang nantinya akan dimasukkan
    # pada varibel "TodoList" sebagai list baru
    # setiap dilakukan penambahan data
    row = [name, date, priority]
    TodoList.append(row)
    print("Added!")

def view():
    time.sleep(1)
    os.system("cls")
    option = input("1. All\n2. By Priority\n> ")
    print()
    if option == "1":
        for row in TodoList:
            for item in row:
                print(item, end=" | ")
            print()
        print()
    else:
        priority = input("What Priority? ").capitalize()
        print()
        for row in TodoList:
            if priority in row:
                for item in row:
                    print(item, end=" | ")
                print()
        print()
    time.sleep(2)

def edit():
    time.sleep(1)
    os.system("cls")
    character = input("Name of To Do List Edit? ")
    found = False
    for row in TodoList:
        if character in row:
            found = True
    
    if not found:
        print("Couldn't Character that!")
        return
    
    for row in TodoList:
        if character in row:
            TodoList.remove(row)
    
    name = input("Name: ")
    date = input("Due Date: ")
    priority = input("Priority: ").capitalize()
    row = [name, date, priority]
    TodoList.append(row)
    print("Edit!")

def remove():
    time.sleep(1)
    os.system("cls")
    character = input("Name of To Do List Remove? ")
    
    for row in TodoList:
        if character in row:
            TodoList.remove(row)

while True:
    print()
    menu = input("1. Add\n2. View\n3. Edit\n4. Remove\n> ")
    if menu == "1":
        add()
    elif menu == "2":
        view()
    elif menu == "3":
        edit()
    else:
        remove()
    
    time.sleep(1)
    os.system("cls")
    # Untuk code dibawah akan melakukan perintah
    # pembuatan file pada folder dnegan nama
    # file "list.txt"
    f = open("list.txt", "w")
    f.write(str(TodoList))
    f.close()
