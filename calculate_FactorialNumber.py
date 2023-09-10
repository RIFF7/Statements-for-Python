# Proejct calculate factorial

# Ini adalah deklarasi fungsi factorial yang mengambil 
# satu argumen number, yang akan menjadi bilangan 
# untuk menghitung faktorialnya.
def factorial(number):
    # Ini adalah blok kondisi pertama. 
    # Jika number adalah 1, maka faktorial dari 1 
    # adalah 1. Pada titik ini, fungsi mengembalikan 
    # nilai 1.
    if number == 1:
        return 1
    # Ini adalah blok kondisi kedua. 
    # Jika number bukan 1, maka fungsi akan melakukan 
    # langkah-langkah di dalam blok ini.
    else:
        # Di dalam blok kondisi kedua, ini adalah rekursi. 
        # Fungsi factorial dipanggil kembali dengan 
        # argumen number - 1, sehingga menghitung 
        # faktorial dari angka yang lebih kecil. 
        # Nilai ini dikalikan dengan number dan 
        # dijadikan nilai kembalian. Ini adalah dasar 
        # dari rekursi, di mana perhitungan faktorial 
        # untuk angka yang lebih besar dipindahkan ke 
        # perhitungan faktorial angka yang lebih kecil 
        # hingga mencapai basis (faktorial 1).
        return number * factorial(number - 1)
# Di sini, program meminta pengguna memasukkan angka 
# untuk menghitung faktorialnya. Input tersebut diubah 
# menjadi tipe data integer.
number = int(input("Input a number > "))
# Ini adalah pemanggilan fungsi factorial dengan 
# argumen number yang dimasukkan oleh pengguna. 
# dan disimpan pada variabel "factor"
factor = factorial(number)
# Code dibawah akan menampilkan hasim inputan dan
# perhitungan yang dilakukan pada subrutin "factorial()"
print(f"The factorial of {number} is {factor}.")
