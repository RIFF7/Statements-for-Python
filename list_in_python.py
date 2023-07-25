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
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
print(f"The first color is {colors[1]}")

#Project
import random

txt = ["Good Morning", "Selamat Pagi", "Ohayo", "Bore Da!"]

index = random.randint(0, 3)

print(txt[index])
