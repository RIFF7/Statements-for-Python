""" Dalam kode yang diberikan, 
.title() digunakan untuk mengubah huruf 
pertama dari setiap kata pada string 
yang dimasukkan oleh pengguna menjadi 
huruf kapital, sedangkan huruf-huruf 
lainnya menjadi huruf kecil.  """

import os, time

TodoList = []

def drafList():
    #os.system("cls")
    print()
    print("MY LIST")
    print()
    counter = 1
    for list1 in TodoList:
        print(f"{counter}: {list1}")
        counter += 1
    #time.sleep(1)
    
while True:
    print()
    print("To Do List\n")
    menu = input("Do you want to view, add, edit, remove or delete an item from the to do list? ")
    if menu == "add" or menu == "Add":
        add = input("What do you want to Add? ")
        TodoList.append(add)
    elif menu == "view" or menu == "View":
        drafList()
    elif menu == "remove" or menu == "Remove":
        trash = input("What do you want to remove? ")
        if trash in TodoList:
            sure = input("Are you sure you want to remove this? ")
            if sure == "yes":
                TodoList.remove(trash)
            else:
                continue
        else:
            print()
            print(f"{trash}, was not in the To Do List")
    elif menu == "edit" or menu == "Edit":
        edit = input("What do you want to Edit? ")
        new = input("What do you want to change it to? ")
        for i in range(0, len(TodoList)):
            if TodoList[i] == add:
                TodoList[i] = new
            """ else:
                print(f"{edit}, was not in the To Do List") """
    elif menu == "delete" or menu == "Delete":
        TodoList = []
    else:
        exit()
        #print("Thank you for trying!")
            
