print("🌟 Current Leader 🌟")
# Code dibawah akan membuka file
# hihgh.score dan membacanya dengan fungsi "r"
f = open("high.score", "r")
# Setelah data dibuka dan dibaca, maka variabel 
# dibawah akan melakukan pembacaan data yang
# ada di dalam file high.score lalu memmecahnya
# menjadi 2 komponen pada list, sehingga akan
# menampilkan data dalam bentuk list dengan
# masing - masing indexnya
score = f.read().split("\n")
f.close()
# Dimulai dari max_score dengan nilai 0
max_score = 0
# Lalu varibael "name" tanpa ada value
name = None
# Setelahnya akan dilakukan perulangan untuk
# menemukan score tertinggi dari data yang ada
# pada file high.score berdasarkan index yang 
# sudah dibuat sebelumnya.
# Dimulai dari membuat row untuk masing - masing data
# yang ada pada varibael "score"
for row in score:
    #Pada baris code dibawah, row adalah 
    # sebuah string yang berisi satu baris 
    # dari variabel score, yang kemungkinan 
    # memiliki beberapa bagian atau kolom 
    # yang dipisahkan oleh karakter spasi 
    # (atau karakter pemisah lainnya,
    # seperti koma atau titik koma).
    # Sehingga nantinya data yang ditampilkan
    # akan berupa list dengan index, seperti ini:
    # ['DMO', '20332']
    data = row.split()
    #print(data)
    # Untuk code dibawah, ini adalah kondisi 
    # pertama yang memeriksa apakah data bukan 
    # list kosong. Kondisi ini berguna untuk 
    # memastikan bahwa data tidak kosong sebelum 
    # kita mencoba mengakses elemen-elemen 
    # di dalamnya. Jika data adalah list kosong, 
    # artinya data tidak memiliki elemen apapun, 
    # dan kita tidak dapat mengakses indeks apapun 
    # di dalamnya. Oleh karena itu, kita ingin 
    # melewati baris tersebut jika data kosong.
    if data != []:
        # Dan untuk kondisi "if" kedua, Kondisi 
        # kedua ini memeriksa apakah nilai 
        # skor yang terdapat di data 
        # (elemen kedua dalam list) 
        # lebih besar daripada nilai max_score.
        # Variabel max_score adalah variabel 
        # yang menyimpan nilai tertinggi yang 
        # telah ditemukan sebelumnya selama 
        # iterasi sebelumnya dalam sebuah 
        # perulangan.

        #Jika kondisi kedua ini terpenuhi, 
        # artinya nilai skor di data lebih 
        # besar daripada max_score, maka kita 
        # akan melakukan hal-hal berikut:
        if int(data[1]) > max_score:
            max_score = int(data[1])
            name = data[0]
            
print("Analyzing high scores......")
print("The winner is", name, "with", max_score)
