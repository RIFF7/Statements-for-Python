import csv, os
# Code dibawah digunakan untuk membuka file csv
# dengan nama file "100MostStreamedSongs.csv" dengan
# alias sebagai "file"
with open("100MostStreamedSongs.csv") as file:
    # Code dibawah menjadikan file csv menjadi
    # sebuah Dictionary yang memiliki keys dan value
    # dari data csv "100MostStreamedSongs.csv" dengan
    # alias sebagaoi "file"
    reader = csv.DictReader(file)
    # Code dibawah akan melakukan iterasi sebanyak
    # data yang ada pada file "100MostStreamedSongs.csv" 
    for row in reader:
        # Baris ini mengambil daftar nama berkas dan 
        # direktori dalam direktori kerja saat ini.
        dir = os.listdir()
        # Baris ini mengambil nilai dari kolom 
        # "Artist(s)" pada baris saat ini dalam berkas 
        # CSV dan mengubahnya menjadi huruf kapital 
        # awal untuk menghasilkan nama artis yang 
        # lebih teratur.
        artist = row["Artist(s)"].title()
        print(artist)
        # Code dibawah ini adalah pernyataan if yang memeriksa 
        # apakah nama artis yang sudah diolah tidak ada 
        # dalam daftar berkas dan direktori saat ini. 
        # Jika tidak ada, pernyataan ini akan membuat 
        # direktori baru dengan nama artis.
        if artist not in dir:
            # Jika nama artis belum ada dalam daftar 
            # berkas dan direktori, baris ini akan 
            # membuat direktori baru dengan nama artis.
            os.mkdir(artist)
        # Code dibawah ini mengambil nilai dari kolom "Song" 
        # pada baris saat ini dalam berkas CSV.    
        song = row["Song"]
        print(row["Song"])
        # Code dibawah ini membuat jalur lengkap untuk 
        # berkas yang akan dibuat. Jalur ini 
        # menggabungkan nama artis (yang juga adalah 
        # nama direktori) dengan nama lagu untuk 
        # membentuk jalur berkas.
        path = os.path.join(f"{artist}/", song)
        # Code dibawah ini membuka berkas yang telah 
        # dijelaskan sebelumnya dengan mode "w" (write) 
        # untuk menulis data ke berkas.
        f = open(path, "w")
        # Codee dibawah setelah berkas dibuka dan ditutup, 
        # berkas yang baru telah dibuat.
        f.close()

# Jadi, tujuan dari potongan kode diatas adalah untuk 
# membaca baris-baris dari berkas CSV, 
# membuat direktori dengan nama artis jika belum ada, 
# dan kemudian membuat berkas dengan nama lagu dalam 
# direktori artis yang sesuai.
