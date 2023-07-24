def colorChange(color):
    if color == "red":
        return ("\033[31m")
    elif color == "white":
        return ("\033[0m")
    elif color == "blue":
        return ("\033[34m")
    elif color == "yellow":
        return ("\033[33m")
    elif color == "green":
        return ("\033[32m")
    elif color == "purple":
        return ("\033[35m")

title = f"{colorChange('red')} ={colorChange('white')}={colorChange('blue')}= {colorChange('yellow')} Music App {colorChange('blue')}={colorChange('white')}={colorChange('red')}="
print(f"        {title:^35}")
print(f"🔥▶️\t{colorChange('white')} Radio")
print(f"\t{colorChange('yellow')}Memories One Piece")


prev = "PREV"
nxt = "NEXT"
paus = "PAUSED"

print(f"{colorChange('white')}{prev:<17}")
print(f"{colorChange('green')}{nxt:^17}")
print(f"{colorChange('purple')}{paus:>18}")

print("\033[0m")

print("=====================================\n")

header = "WELCOME TO"
print(f"{colorChange('white')}{header:^35}")

header2 = "--- ARM BOOK ---"
print(f"{colorChange('blue')}{header2:^34}")

print()

txt = "Definitely not a rip off of"
print(f"{colorChange('yellow')}{txt:>37}")

txt2 = "a certain other social"
print(f"{colorChange('yellow')}{txt2:>37}")

txt2 = "networking site."
print(f"{colorChange('yellow')}{txt2:>37}")

print("\033[0m")

header3 = "Honest."
print(f"{colorChange('red')}{header3:^34}")

print()

user = "Username:"
input(f"{colorChange('white')}{user:^34}")

pas = "Password:"
input(f"{colorChange('white')}{pas:^34}")
