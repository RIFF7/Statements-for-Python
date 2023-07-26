myName = []

def printName():
    print()
    for i in myName:
        print(i)
    print()

while True:
    addFirstname = input("Frist Name: ").strip().capitalize()
    addLastname = input("Last Name: ").strip().capitalize()
    name = f"{addFirstname} {addLastname}"
    #Perintah dibawah akan mengevaluasi inputan sama atau tidak
    #Jika inputahn sama maka option else akan dijalankan
    if name not in myName:
        myName.append(name)
    else:
        print("ERROR: Duplicate name")
    printName()
