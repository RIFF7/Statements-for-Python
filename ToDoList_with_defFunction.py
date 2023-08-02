# Membuat list dengan tampilan
# | Name | Date | Priority

import os, time

TodoList = []

def add():
    time.sleep(1)
    os.system("cls")
    name = input("Name: ")
    date = input("Due Date: ")
    priority = input("Priority: ").capitalize()
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
    time.sleep(1)

def edit():
    time.sleep(1)
    os.system("cls")
    find = input("Name of To Do List Edit? ")
    found = False
    for row in TodoList:
        if find in row:
            found = True
    
    if not found:
        print("Couldn't find that!")
        return
    
    for row in TodoList:
        if find in row:
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
    find = input("Name of To Do List Remove? ")
    
    for row in TodoList:
        if find in row:
            TodoList.remove(row)

while True:
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
