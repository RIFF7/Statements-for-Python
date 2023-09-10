# OOP (Object Oriented Programming)
# Pada code dibawah ini kita akan membuat 3 variabel
# dengan nama job, salary, hoursWorked
class job:
    job = None
    salary = None
    hoursWorked = None
    # Metode __init__ menginisialisasi 
    # atribut-atribut ini ketika objek 
    # dari kelas ini dibuat.
    def __init__(self, job, salary, hoursWorked):
        self.job = job
        self.salary = salary
        self.hoursWorked = hoursWorked
        
    # Metode describe digunakan untuk mencetak 
    # detail pekerjaan, termasuk jenis pekerjaan, 
    # gaji, dan jam kerja.    
    def describe(self):
        print(f"""
              ======= JOB =======
              """)
        print(f"""
              Job Type: {self.job}
              Salary: ${self.salary}
              Hours Worked: {self.hoursWorked}
              """)
        
# Kelas teacher (Diturunkan dari job):
# Kelas ini mewarisi atribut dan metode dari kelas 
# job tetapi memberikan atribut tambahan: 
# subject dan position.
class teacher(job):
    subject = None
    position = None
    
    # Metode __init__ menggantikan metode dari kelas 
    # induknya untuk mengatur nilai-nilai yang 
    # spesifik untuk pekerjaan seorang guru.
    def __init__(self, subject, position):
        self.job = "Teacher"
        self.salary = 17.7
        self.hoursWorked = "All of Them"
        self.subject = subject
        self.position = position
    
    # Metode describe juga digantikan untuk memasukkan 
    # atribut tambahan (subject dan position) 
    # saat mencetak detail pekerjaan.
    def describe(self):
        print(f"""
              ======= JOB =======
              """)
        print(f"""
              Job Type: {self.job}
              Salary: ${self.salary}
              Hours Worked: {self.hoursWorked}
              Subject: {self.subject}
              Position: {self.position}
              """)
# Kelas doctor (Diturunkan dari job):
# Sama seperti kelas teacher, kelas ini mewarisi 
# dari job tetapi menambahkan atribut khusus: 
# experience dan speciality.
class doctor(job):
    experience = None
    speciality = None
    
    # Metode __init__ sekali lagi menggantikan 
    # metode dari kelas induknya untuk mengatur 
    # nilai-nilai yang spesifik untuk pekerjaan 
    # seorang dokter.
    def __init__(self, experience, speciality):
        self.job = "Doctor"
        self.salary = 23.70
        self.hoursWorked = 50
        self.speciality = speciality
        self.experience = experience
    
    # Metode describe digantikan untuk memasukkan 
    # atribut khusus dokter saat mencetak detail 
    # pekerjaan.
    def describe(self):
        print(f"""
              ======= JOB =======
              """)
        print(f"""
              Job Type: {self.job}
              Salary: ${self.salary}
              Hours Worked: {self.hoursWorked}
              Speciality: {self.speciality}
              Years of Experience: {self.experience}
              """)

# Membuat Objek
# Tiga objek dibuat berdasarkan kelas-kelas ini:
# lawyer: Sebuah instansi dari kelas job yang 
# mewakili seorang pengacara.

# cher: Sebuah instansi dari kelas teacher 
# yang mewakili seorang guru bernama Cher.

# doc: Sebuah instansi dari kelas doctor yang mewakili 
# seorang dokter.

# Memanggil Metode describe:
# Metode describe dipanggil pada setiap objek ini 
# untuk mencetak detail pekerjaan yang bersangkutan. 
# Metode yang khusus untuk setiap kelas akan 
# dieksekusi, memberikan informasi tentang jenis 
# pekerjaan, gaji, jam kerja, dan atribut tambahan 
# yang khusus untuk profesi tersebut.
lawyer = job("Lawyer", 1.56, 60)
lawyer.describe()

cher = teacher("Computer Science", "Classroom Teacher")
cher.describe()

doc = doctor("Pediatric Consultant", 7)
doc.describe()

# Secara ringkas, kode ini menunjukkan penggunaan 
# pemrograman berorientasi objek dalam Python 
# untuk memodelkan berbagai profesi 
# (pengacara, guru, dan dokter) sebagai kelas-kelas. 
# Setiap kelas memiliki atribut dan metode sendiri, 
# dan instansi dari kelas-kelas ini diciptakan 
# untuk mewakili individu dalam profesi tersebut. 
# Metode describe digunakan untuk mencetak detail 
# tentang setiap pekerjaan.
