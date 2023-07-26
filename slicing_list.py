# String Slicing

# Example 1
# This code outputs the 'H' from 'Hello'
print("This code outputs the 'H' from 'Hello'\n")
myString = "Hello there my friend."
print(myString[0])
print()

# This code outputs 'there'.
# stringName[index starting position, index after ending position]
print("This code outputs 'there'.\n")
myString = "Hello there my friend."
print(myString[6:11])
print()

# This code outputs 'Hello there'.
print("This code outputs 'Hello there'\n")
myString = "Hello there my friend."
print(myString[:11])
print()

# This code outputs 'my friend.'.
print("This code outputs 'my friend.'.\n")
myString = "Hello there my friend."
print(myString[12:])
print()

# stringName[index starting position, index after ending position, number of characters to move]
# This code outputs 'Hlo' (every second character from 'Hello').
print("This code outputs 'Hlo' (every second character from 'Hello').\n")
myString = "Hello there my friend."
print(myString[0:6:2])
print()

# This code outputs 'Hltrmfe!' (every third character from the whole string).
print("This code outputs 'Hltrmfe!' (every third character from the whole string).\n")
myString = "Hello there my friend."
print(myString[::3])
print()

# This code reverses the string, outputting '.dneirf ym ereht olleH'
print("This code reverses the string, outputting '.dneirf ym ereht olleH'\n")
myString = "Hello there my friend."
print(myString[::-1])
print()

# SPLIT
# This code outputs ['Hello', 'there', 'my', 'friend.']
print("This code outputs ['Hello', 'there', 'my', 'friend.']\n")
myString = "Hello there my friend."
print(myString.split())
print()

# This code outputs Hell
print("This code outputs Hell\n")
myString = "Hello there my friend."
print(myString[0:4])
print()

# This code outputs Error, cause slice step cannot be zero (0)
""" myString = "Hello there my friend."
print(myString[0:4:0]) """

# This code should output 'Hello there'
myString = "Hello there my friend."
print(myString[0:11:1])

#Project 1

print("STAR WARS NAME GENERATOR")

""" Fungsi split() digunakan untuk memisahkan 
input berdasarkan spasi dan menyimpannya 
sebagai elemen-elemen dalam sebuah list. """

all = input("Enter your first name, last name, Mum's maiden name and the city you were born in: ").split()

""" Fungsi strip() digunakan untuk menghapus 
spasi tambahan di awal dan akhir setiap data 
jika ada. 

Sedangkang fungsi all[] akan memisahkan 
kata berdasarkan fungsi split di variabel 
all berdasarkan fungsi split() yaitu spasi
sehingga akan dipisah menjadi beberapa variabel
yaitu all(index) dan fungsi strip()
akan menghapus spasi pada setiap karakter
di awal dan akhir kata jika ada """

first = all[0].strip()
last = all[1].strip()
maiden = all[2].strip()
city = all[3].strip()

name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

print(f"Your Star Wars name is {name}")

#=============================================================================================

#Code Me
print("🌟 Star Wars Name Generator 🌟")
print()

firstName = input("Input your first name: ")
lastName = input("Input your lastname: ")
motherName = input("Input your mother's maiden name: ")
born = input("Input the city where you were born: ")

print(f"Your Star Wars name is {firstName[:3].title()}{lastName[:-3].lower()} {motherName[:2].title()}{born[4:].lower()}")
