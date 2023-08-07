# Mmebuat tampilan rows dalam dictionary berdasarkan
# keys dan laue yang telah diinput dan di simpan
# pada variabel moked
moked = {}

# Pada code dibawah akan meminta program untuk
# menampilkan data rows dictionary yang ada pada 
# moked dengan tampilan yang mudah dibaca bagi user
def prettyPrint():
    print()
    # code dibawah akan melakukan iterasi pertama
    # melalui pasangan kunci - nilai (key, value)
    # dalam dictionary moked menggunakan metode
    # items() untuk mendapatkan keys dan value
    # karena setiap elemen dalam dictionary akan
    # ditempatkan dalam variabel keys dan value
    for key, value in moked.items():
        print(f"Name: {key}", end=" | ")
        # Perulangan kedua digunakan untuk mengiterasi
        # melalui pasangan keys dan value dalam dictionary
        # value.
        # untuk variabel "value" pada perulangan
        # kedua ini adalah dictionary yang merupakan
        # nilai dari dictionary pada variabel "moked"
        for subkey, subvalue in value.items():
            print(subkey, subvalue, end=" | ")
        print()

# Untuk code dibawah adalah perulangan yang meminta
# user untuk memasukan value dalam 5 varibel    
while True:
    print()
    print("🌟 MokeBeast Generator 🌟")
    name = input("Input the beast name > ")
    elemnet = input("Input the beast element > ")
    move = input("Input the beast special move > ")
    hp = input("Input the beast starting HP > ")
    mp = input("Input the beast starting MP > ")
    # Setelah kelima variabel dimasukan valuenya
    # maka akan disimpan dalam dictionary moked
    moked[name] = {"Element:": elemnet, "Move:": move,
                   "HP:": hp, "MP:": mp}
    
    print()
    # Menampilkan data dalam dictionary yang mudah
    # untuk dibaca, sesuai dengan perintah subrutin
    # yang telah dibuat sebelumnya
    prettyPrint()
    print()
    # Ketika data dictionary telah selesai diinput
    # dan ditampilkan, maka code dibawah akan berjalan
    # meminta apakah user ingin melanjutkan inputan
    # atau keluar dari program
    question = input("Again? y/n > ")
    if question == "n":
        print()
        break
