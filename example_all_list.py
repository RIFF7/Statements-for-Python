#LIST

""" timetable = ["Computer Science", "Math", 
             "English", "Art", "Sport"] """
             
#print(timetable)

""" print(timetable[0])
print(timetable[1])
print(timetable[2])
print(timetable[3])
print(timetable[4]) """

#Mengganti isi list pada indext ke-4
#timetable[4]= "Watch TV"

#Tampilkan semua list dan list baru
""" print(timetable[0])
print(timetable[1])
print(timetable[2])
print(timetable[3])
print(timetable[4]) """

#Menggunakan funsgi FOR untuk menampilkan isi list
""" timetable = ["Computer Science", "Math", "English", "Art", "Watch TV"]
for lesson in timetable:
  print(lesson) """

#Menampilkan list indext ke-1 dengan fungsi f-strings
""" colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
print(f"The first color is {colors[1]}") """

#Project
""" import random

txt = ["Good Morning", "Selamat Pagi", "Ohayo", "Bore Da!"]

index = random.randint(0, 3)

print(txt[index]) """

#Poject 2
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


#Project 3
import os, time
toDoList = []

def printList():
  print()
  for item in toDoList:
    print(item)
  print()

while True:
  menu = input("ToDoList Manager\n\nDo you want to view, add or edit the todo list?\n")
  if menu=="view":
    printList()
  elif menu=="add":
    item = input("What do you want to add?\n")
    toDoList.append(item)
  elif menu=="edit":
    item = input("What do you want to remove?\n")
    if item in toDoList:
      toDoList.remove(item)
