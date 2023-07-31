""" nameSite = input("Input the website name: ").strip().capitalize()
url = input("Input the URL: ").strip()
desCribe = input("Input your a description: ").strip()
star = input("Input the a star rating out of 5: ")

myCard = {"name": nameSite, "url": url, "describe": desCribe,  "star": star}
print()
for name, value in myCard.items():
    print(f"{name}: {value}") """

#Create Simple Code
website = {"name": None, "url": None, 
           "desc": None, "star": None}

for name in website.keys():
    website[name] = input(f"{name}: ")

print()

for name, value in website.items():
    print(f"{name}: {value}")
