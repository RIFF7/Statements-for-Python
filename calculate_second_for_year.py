#Menghitung banyaknya detik dalam satu tahun

dalam_tahun = int(input("Berapa banyak hari dalam tahun ini: "))

hari_dalam_tahun = 365
hari_dalam_tahun_kabisat = 366
hari_dalam_jam = 24
menit_dalam_jam = 60
detik_dalam_menit = 60

hasil = hari_dalam_tahun * hari_dalam_jam * menit_dalam_jam * detik_dalam_menit

hasil_kabisat = hari_dalam_tahun_kabisat * hari_dalam_jam * menit_dalam_jam * detik_dalam_menit

if dalam_tahun == 365:
    print("Jumalh detik dalam tahun kabisat:", hasil_kabisat)
else:
    print("Banyaknya detik dalam setahun adalah:", hasil)
