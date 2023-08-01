""" def nameChange(name):
    if name == "earth":
        print("\033[0;33m", end="")
    elif name == "fire":
        print("\033[31m", end="")
    elif name == "air":
        print("\033[37m", end="")
    elif name == "water ":
        print("\033[34m", end="")
    elif name == "spirit":
        print("\033[33m", end="") """

print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾\n")

""" name = input("Input your beast's name > ")
types = input("Input your beast's type > ").lower()
move = input("Input your beast's special move > ")
hp = input("Input your beast's staring HP > ")
mp = input("Input your beast's staring MP > ")

pokemon = {"Beast Name": name, "Type": types, 
           "Special Move": move, "HP": hp,
           "MP": mp}

for name, value in pokemon.items():
    if name == "Type":
        if value == "earth":
            print("\033[0;33m", f"{name}: {value}", "\033[0m")
        elif value == "fire":
            print("\033[31m", f"{name}: {value}", "\033[0m")
        elif value == "air":
            print("\033[37m", f"{name}: {value}", "\033[0m")
        elif value == "water":
            print("\033[34m", f"{name}: {value}", "\033[0m")
        elif value == "spirit":
            print("\033[33m", f"{name}: {value}", "\033[0m")
        #print("\033[0m", end="")
    else:
        print(f"{name}: {value}") """
        
#Percobaan 2
""" pokemon = {"Beast Name": None, "Type": None, 
           "Special Move": None, "HP": None,
           "MP": None}

for name in pokemon.keys():
    pokemon[name] = input(f"{name}: ")

for name, value in pokemon.items():
    print(f"{name}: {value}")
    if name == "Type":
        if value == "earth":
            print("\033[0;33m", end="")
        elif value == "fire":
            print("\033[31m", end="")
        elif value == "air":
            print("\033[37m", end="")
        elif value == "water ":
            print("\033[34m", end="")
        elif value == "spirit":
            print("\033[33m", end="") """

#Percobaan ke-3 [DONE]
name = input("Input your beast's name > ")
types = input("Input your beast's type > ")
move = input("Input your beast's special move > ")
hp = input("Input your beast's staring HP > ")
mp = input("Input your beast's staring MP > ")
print()

pokemon = {"Beast Name": name, "Type": types, 
           "Special Move": move, "HP": hp,
           "MP": mp}

# Set the color based on the type
type_color = "\033[0m"  # Default color
if types == "Earth":
    type_color = "\033[35m"
elif types == "Fire":
    type_color = "\033[31m"
elif types == "Air":
    type_color = "\033[37m"
elif types == "Water":
    type_color= "\033[34m"
elif types == "Spirit":
    type_color = "\033[32m"
else:
    type_color = "\033[33m"

for name, value in pokemon.items():
    print(f"{type_color}{name:<15}: {type_color}{value}\033[0m")
