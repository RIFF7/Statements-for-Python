"""Berikut adalah penjelasan mengapa nilai tip dibagi 100 dan dikalikan dengan spend:

1. Dalam baris divid = tip / 100 * spend, kita membagi tip dengan 100 
untuk mengubah persentase tip menjadi nilai desimal. 
Misalnya, jika tip yang dimasukkan adalah 15, maka 15/100 = 0.15.

2. Setelah itu, hasil pembagian tersebut dikalikan dengan spend (tip / 100 * spend) 
untuk mendapatkan jumlah tip yang sesuai 
dengan persentase tip dan total pengeluaran (spend). 
Misalnya, jika spend adalah 100 dan tip adalah 15, maka 0.15 * 100 = 15.

3. Jumlah tip tersebut kemudian ditambahkan ke total pengeluaran (spend) 
untuk mendapatkan total keseluruhan (total). 
Misalnya, jika spend adalah 100 dan tip adalah 15, maka total = spend + tip = 100 + 15 = 115.

-> Sebagai contoh, misalkan pengguna menghabiskan $100 (spend), 
ingin memberikan tip sebesar 15% (tip), 
dan ada 4 orang dalam grup (people). 
Dalam hal ini, nilai tip awalnya adalah 15 (15% dari $100). 
Namun, agar sesuai dengan total pengeluaran (spend), 
kita perlu mengubah nilai tip tersebut menjadi 0.15 (15% dalam bentuk desimal) dengan membaginya dengan 100. 

Kemudian, kita mengalikan 0.15 dengan $100 untuk mendapatkan jumlah tip sebesar $15 yang akan ditambahkan ke total pengeluaran. 
Jadi, total keseluruhan yang harus dibayarkan adalah $115. 
Jumlah ini kemudian dibagi dengan jumlah orang dalam grup (people) untuk mendapatkan jumlah yang harus dibayarkan 
oleh masing-masing orang (totals)."""


print("Tip Calculator\n")

spend = float(input("How Much did you spend? "))
tip = int(input("What percentage do you want to tip? "))
people = int(input("How many people in your group? "))

divid = tip / 100 * spend
total = spend + divid
totals = total / people
totals = round(totals, 2)
print("You each owe $" + str(totals))
