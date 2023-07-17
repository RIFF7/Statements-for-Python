print("Penggunaan range() untuk Perkalian")

num = int(input("Masukkan pilihan tabel berkalian dari (1 - 10): "))

poin = 0

for i in range(1, 11):
    print(i, "X", num, "=")
    hasil = i * num
    jawab = int(input("Masukkan Jawaban: "))
    if jawab == hasil:
        print("Greed 🥳")
        poin += 1
    else:
        print("Haaaahhh 😵‍💫")

print("Nilai Kamu adalah >", poin)

if poin == 10:
    print("Wow! Kamu mendapatkan nilai sempurna!")
else:
    print("Kamu mendapat nilai", poin, "dari total 10 soal!")
