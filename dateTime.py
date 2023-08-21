# Kode di bawah digunakan untuk membuat 
# kalkulator hitungan mundur menuju sebuah 
# acara.

# Ini mengimpor modul datetime yang 
# memungkinkan kita untuk bekerja dengan 
# tanggal dan waktu di Python.
import datetime

print("🌟 Event Countdown Timer 🌟\n")

# Ini meminta pengguna untuk memasukkan 
# nama acara.
event = input("Input the event > ")
# Ini meminta pengguna untuk memasukkan 
# tahun acara.
year = int(input("Input the year > "))
#  Ini meminta pengguna untuk memasukkan 
# bulan acara.
month = int(input("Input the month > "))
# Ini meminta pengguna untuk memasukkan 
# tanggal acara.
days = int(input("Input the day > "))

# Ini mengambil tanggal saat ini dan 
# menyimpannya dalam variabel today.
today = datetime.date.today()

# Ini menggunakan input pengguna untuk 
# membuat objek tanggal yang mewakili 
# tanggal acara yang dimasukkan.
holiday = datetime.date(year, month, days)

# Ini menghitung selisih waktu antara 
# tanggal acara (holiday) dan tanggal 
# saat ini (today), dan menyimpannya 
# dalam variabel difference.
difference = holiday - today
# Karena difference adalah objek timedelta, 
# kita perlu mengakses atribut days untuk 
# mendapatkan selisih waktu dalam bentuk hari.
difference = difference.days

# Ini adalah kondisi jika selisih waktu 
# positif (artinya acara belum terjadi).
if difference > 0:
    print("Coming Soon!")
# Ini adalah kondisi jika selisih waktu 
# negatif (artinya acara telah berlalu).
elif difference < 0:
    print("Hope You enjoyed it!")
# Ini adalah kondisi jika selisih waktu 
# nol (artinya hari ini adalah tanggal acara).
else:
    print("Happy Birthday!!!")

# Ini mencetak selisih waktu dalam bentuk 
# jumlah hari.
print(difference)

# Hasil dari kode diatas akan menunjukkan 
# pesan berdasarkan selisih waktu antara 
# tanggal acara dan tanggal saat ini. 
# Jika selisih waktu positif, akan mencetak 
# "Coming Soon!". Jika selisih waktu negatif, 
# akan mencetak "Hope You enjoyed it!". 
# Jika selisih waktu nol, akan mencetak 
# "Happy Birthday!!!". Terakhir, kode ini 
# akan mencetak jumlah hari selisih waktu.
