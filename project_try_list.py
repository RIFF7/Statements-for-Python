""" import random

txt = ["Good Morning", "Selamat Pagi", "Ohayo", "Bore Da!"]

index = random.randint(0, 3)

print(txt[index])
 """

#Dynamic List
#Penggunaan list dengan input
""" mylist = []

def prinList():
    print()
    for item in mylist:
        print(item)
    print()

while True:
    item = input("What's next Agenda in list? ")
    mylist.append(item)
    prinList() """


#Penggun list untuk menambah dan menghapus
""" mylist = []

def prinList():
    print()
    for item in mylist:
        print(item)
    print()

while True:
    
    menu = input("Add or Remove? ")
    
    if menu == "add" or menu == "Add":
        item = input("What's next Agenda in list? ")
        mylist.append(item)    
    elif menu == "remove" or menu == "Remove":
        
        item = input("What do you want to remove? ")
        
        if item in mylist:
            mylist.remove(item)
        else:
            print()
            print(f"{item}, was not in the list!")
        
    prinList() """
    
#Dynamic List berikutnya
#Menambah, melihat, menghapus

myList = []

def prinList():
    print()
    for item in myList:
        print(item)
    print()

while True:
    
    menu = input("What do you want Add, View or Remove? ")
    if menu == "view" or menu == "View":
        prinList()
    elif menu == "add" or menu == "Add":
        item = input("What's next To Do List? ")
        myList.append(item)
    elif menu == "remove" or menu == "Remove":
        item = input("What do you want to remove? ")
        if item in myList:
            myList.remove(item)
        else:
            print(f"{item}", "data not in To Do List!")
    else:
        exit()
