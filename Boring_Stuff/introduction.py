# Menulis code untuk membaca file berisis password
'''
    Untuk membaca sebuah file pada folder, jika muncul error seperti dibawah ini:
    
    FileNotFoundError: [Errno 2] No such file or directory: 'SecretPasswordFile.txt'
    
    Maka yang perlu diperhatikan saat ini adalah, pastikan untuk menuliskan file
    secara lengkap beserta nama foldernya.
'''
passwordFile = open('F:\Fokus-Python\GitHub\Statements-for-Python\Boring_Stuff\SecretPasswordFile.txt')
secretPassword = passwordFile.read()
print('Enter Your Password.')
typePassword = input()
if typePassword == secretPassword:
    print('Access Granted!')
    if typePassword == '12345':
        print('That password is one that an idiot puts on their luggage.')
else:
    print('Access Denied')