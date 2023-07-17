#PENJELASAN TERKAIT DENGAN FUNGSI ROUND

"""Fungsi round() pada Python digunakan untuk membulatkan suatu angka menjadi 
    sejumlah digit desimal tertentu. Dalam contoh yang Anda berikan, round(number_score, 2) 
    akan membulatkan nilai number_score menjadi dua digit desimal.

Misalnya, jika number_score memiliki nilai 3.14159, maka round(number_score, 2) 
akan menghasilkan nilai 3.14. Fungsi round() akan membulatkan angka tersebut menjadi dua digit 
desimal berdasarkan aturan pembulatan, yaitu jika digit ketiga desimal lebih besar atau sama dengan 5, 
maka digit kedua desimal akan dinaikkan satu.

Kegunaan dari membulatkan angka dengan menggunakan round() adalah untuk mengontrol jumlah digit desimal
yang ingin ditampilkan atau diproses dalam suatu perhitungan atau tampilan hasil. 
Ini dapat berguna dalam situasi seperti perhitungan keuangan, 
penanganan data yang memerlukan presisi tertentu, atau saat menampilkan angka 
kepada pengguna dengan format yang diinginkan.

Dalam kasus round(number_score, 2), angka 2 mengindikasikan bahwa kita ingin membulatkan 
hingga dua digit desimal. Jika Anda ingin menampilkan atau memproses angka dengan 
tingkat presisi lebih tinggi atau lebih rendah, Anda dapat mengubah angka tersebut 
sesuai dengan kebutuhan Anda. Misalnya, jika ingin tiga digit desimal, 
Anda dapat menggunakan round(number_score, 3).
    """

#PENJELASAN TERKAIT DENGAN TANDA TITIK PADA ANGKA

"""Dalam kode yang Anda berikan, tanda titik ("."), 
yang digunakan sebelum angka (seperti .90), digunakan untuk mewakili 
angka desimal dalam format pecahan. Pada Python, tanda titik yang diikuti 
oleh angka secara default dianggap sebagai representasi angka desimal.

Dalam konteks kode Anda, .90 mewakili angka desimal 0.90. 
Kondisi score_akhir >= .90 memeriksa apakah nilai score_akhir lebih besar 
atau sama dengan 0.90. Jika kondisi tersebut terpenuhi, maka pesan yang sesuai akan dicetak.

Penting untuk dicatat bahwa jika Anda ingin menggantikan tanda titik dengan angka, 
Anda harus menggunakan format yang benar, seperti 0.90. 
Jika hanya menggunakan 90 tanpa tanda titik, itu akan dianggap sebagai angka bulat (integer) 
dan bukan desimal."""

#Menampilkan nilai dengan huruf dan menghitung persentase
print("Exam Grade Calculator\n")
exam = input("Masukkan mata pelajaran kamu: ")
score_total = int(input("Max Nilai pada pelajaran ini: ")) 
score_kamu = int(input("Masukan Nilai kamu: "))

number_score = float(score_kamu / score_total)
score_akhir = round(number_score, 2)
dalam_persentase = round(float(score_kamu / score_total) * 100, 2)

print("Hasil Nilai kamu " + str(dalam_persentase) + "%")

if score_akhir >= .90:
    print("Bagus Kamu mendapatkan nilai sempurna " + "\033[32m" + "A+" + "\033[0m")
elif score_akhir >= .80 and score_akhir <= .89:
    print("Bagus Kamu mendapatkan nilai Hampir Sempurna " + "\033[36m" + "A" + "\033[0m")
elif score_akhir >= .70 and score_akhir <= .79:
    print("Semangat teruslah belajar " + "\033[34m" + "B" + "\033[0m")
elif score_akhir >= .60 and score_akhir <= .69:
    print("Kamu harus banyak belajar lagi " + "\033[33m" + "C" + "\033[0m")
elif score_akhir >= .50 and score_akhir <= .59:
    print("Really??? Ayo lah belajar lagi " + "\033[31m" + "D" + "\033[0m")
elif score_akhir <= .49:
    print("Kuasai Materi Secepatnya!!! " + "\033[31m" + "D" + "\033[0m")
else:
    print("\033[31m" + "Tolong Rajinlah BELAJAR!!!" + "\033[0m")
