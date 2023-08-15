# Menghitung cost dan quantity pada file csv

# Versi 1
""" import csv

total = 0.0

with open("Day54Totals.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cost = float(row["Cost"])
        quantity = float(row["Quantity"])
        #print(row["Cost"], end=", ")
        #print(row["Quantity"])
        total += cost * quantity

print(f"Total: ${round(total, 2)}") """

# Veris 2
import csv

# Code dibawah akan memulai nilai total dengan 0.0
total = 0.0

# Pada code dibawah akan membuka file csv
# "Day54Totals.csv" dengan alias "file"
with open("Day54Totals.csv") as file:
    # Code dibawah adalah cara untuk membuat 
    # objek pembaca yang akan membaca isi file 
    # CSV yang disebut file dalam mode berbasis 
    # kamus. Ini berarti bahwa setiap baris dalam 
    # file CSV akan dibaca sebagai sebuah kamus 
    # (dictionary) di mana kunci-kunci kamusnya 
    # adalah nama kolom di file CSV, dan 
    # nilai-nilai kamusnya adalah nilai-nilai dari 
    # kolom tersebut.
    reader = csv.DictReader(file)
    # Code dibawah akan melakukan iterasi
    # sebanyak data yang ada
    for row in reader:
        # Pada code dibawah setiap kali kita membaca 
        # baris dari file CSV, kita langsung 
        # menghitung total biaya dengan mengalikan 
        # quantity dan cost dari baris tersebut dan 
        # menambahkannya ke total keseluruhan. 
        # Dengan kata lain, kita melakukan penambahan 
        # langsung ke total pada setiap iterasi loop, 
        # sehingga total akhir akan mencerminkan 
        # jumlah total biaya dari seluruh baris dalam 
        # file.
        total += float(row["Quantity"]) * float(row["Cost"])
# Setelah selesai melakukan iterasi dan menghitung 
# total maka akan di cetak dengan code dibawah
# fungsi round adalah mengambil pembulatan 
# angka total yang dicetak ke dalam format uang 
# (dalam hal ini, format dolar) menjadi dua 
# tempat desimal setelah titik desimal.
print(f"Total: ${round(total, 2)}")
