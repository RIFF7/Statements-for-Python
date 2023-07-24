""" f-string (format string) 
adalah cara terbaik untuk menggabungkan 
variabel dan teks secara bersamaan. 
Semuanya sampai sekarang telah ... yah ... canggung.

Mari kita lihat bagaimana 
kita menggabungkan variabel dan 
teks di masa lalu...menggabungkan. """

""" name = "Katie"
age = "28"
pronouns = "she/her"

print("This is", name, 
      "using", pronouns, 
      "pronouns and is age", age) """

""" =============================================== """

""" Sekarang mari kita gunakan f-string 
untuk kode yang sama ini. Perubahan apa 
yang saya lakukan pada kode ini? """

""" name = "Katie"
age = "28"
pronouns = "she/her"

print("This is {}, using {} pronouns, and is {} years old.".format(name, pronouns, age)) """

""" =============================================== """

""" Kita dapat mengatur variabel lokal 
di dalam f-string itu sendiri. 
Sekarang tidak masalah urutan variabelnya.

Melihat kode ini lagi, saya dapat mengatur 
variabel saya di dalam teks itu sendiri. 
Lihat ini: """

""" Perubahan 1: Ganti {}dengan nama variabel. 
Perubahan 2: Ganti setiap variabel di dalam {} 
dengan apa yang telah didefinisikan 
dalam format.( = ) """

""" name = "Katie"
age = "28"
pronouns = "she/her"

print("This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age)) """

""" =============================================== """

""" f-string juga bekerja dengan tipe variabel 
yang berbeda: int, float, dan string.

Kita dapat menetapkan kalimat gabungan ke variabel. 
Menonton ini. Kami membuat variabel yang disebut 
respons dan membuatnya sama dengan kalimat gabungan. 
Sekarang saya dapat menggunakan respons ini 
dengan mudah di mana pun saya mau. """

""" name = "Katie"
age = "28"
pronouns = "she/her"

response = "This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age)

print(response) """

""" =============================================== """

""" Alih-alih semua yang faffing tentang... 
coba ini sebagai gantinya. Gunakan huruf f 
sebelum string apa pun dengan {} untuk 
nama variabel (dan lupakan tentang .format itu). """

""" Lihatlah kode yang sama ini dan 
lihat perbedaannya menggunakan teknik ini: """

""" name = "Katie"
age = "28"
pronouns = "she/her"

response = f"This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far"

print(response) """

""" =============================================== """

""" Alignment
kiri: <, kanan: >, tengah: ^

Program ini menunjukkan berapa banyak dari 
100 Days of Code yang telah kita selesaikan 
sejauh ini. Saya ingin ini terlihat seperti daftar. 
Namun, begitu kita memasuki hari ke-10, 
mulai terlihat agak berantakan. 
Pastikan Anda menyertakan f saat menggunakan 
perataan."""

""" for i in range(1, 31):
  print(f"Day {i} of 30") """
  
""" Mari kita perbaiki dengan menambahkan 
perataan kiri sepanjang 2 karakter. """

""" for i in range(1, 31):
  print(f"Day {i: <2} of 30") """
  
#EXAMPLE

""" food = "pizza"
location = "beach"
color = "green"
friend = "Quinn"

response = f"Alejandra ordered {food} to eat at the {location} with her friend, {friend}. She got to the {location} and looked for a {color} umbrella where {friend} said they would be waiting. By the time, Sally found {friend}, the {food} was cold and the {location} was lame."

print(response) """

#PROJECT

print("30 Days Down - What did you think?")
print()
for i in range(1, 31):
  thought = input(f"Day {i}:\n")
  print()
  myText = f"You thought Day {i} was"
  print(f"{myText:^35}")
  print(f"{thought:^35}")
  print()
