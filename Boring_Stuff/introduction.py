# Menulis code untuk membaca file berisis password
'''
    Untuk membaca sebuah file pada folder, jika muncul error seperti dibawah ini:
    
    FileNotFoundError: [Errno 2] No such file or directory: 'SecretPasswordFile.txt'
    
    Maka yang perlu diperhatikan saat ini adalah, pastikan untuk menuliskan file
    secara lengkap beserta nama foldernya.
'''

# ORIGINAL

# passwordFile = open('..\Statements-for-Python\Boring_Stuff\SecretPasswordFile.txt')
# secretPassword = passwordFile.read()
# print('Enter Your Password.')
# typePassword = input()
# if typePassword == secretPassword:
#     print('Access Granted!')
#     if typePassword == '12345': # Hasilnya tidak sesuai yang diharapkan
#         print('That password is one that an idiot puts on their luggage.')
# else:
#     print('Access Denied')

#--------------------------------------------------------------------------------------------------------------
    
# Modifikasi code 1

# passwordFile1 = open('..\Statements-for-Python\Boring_Stuff\SecretPasswordFile.txt')
# secretPassword1 = passwordFile1.read()
# typePassword1 = input('Enter Your Password: ')
# if typePassword1 == secretPassword1:
#     print('Access Granted!')
# elif typePassword1 == '12345':
#     print('That password is one that an idiot puts on their luggage.')
# else:
#     print('Access Denied!')

#--------------------------------------------------------------------------------------------------------------

# Modifikasi code 2

while True:
    passwordFile2 = open('..\Statements-for-Python\Boring_Stuff\SecretPasswordFile.txt')
    secretPassword2 = passwordFile2.read()
    
    typePassword2 = input('Enter Your Password: ')
    if typePassword2 == secretPassword2:
        print('Access Granted!')
        break
    elif typePassword2 == '12345':
        print('That password is one that an idiot puts on their luggage.')
    else:
        print('Access Denied!')
        break