# Membuat Character Game 
# dengan OOP (Object Oriented Programing)

class character:
    name = None
    health = None
    magicPoint = None
    def __init__(self, name, health, magicPoint):
        self.name = name
        self.health = health
        self.magicPoint = magicPoint
        
    def describe(self):
        print("🌟 Generic RPG 🌟")
        print("🗡  Player 🗡")
        print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoint}")

class player(character):
    nickname = None
    lives = None
    def __init__(self, nickname, lives):
        self.nickname = nickname
        self.health = 100
        self.magicPoint = 50
        self.lives = lives
        
    def DescPLay(self):
        print("🌟  Generic RPG 🌟")
        print("🗡  Player 🗡")
        print(f"Name: {self.nickname}\nHealth: {self.health}\nMagic Points: {self.magicPoint}\nLives: {self.lives}")

    def isAlive(self):
        if self.lives > 0:
            print(f"{self.nickname} lives on!")
            return True
        else:
            print(f"{self.nickname} has expired!")
            return False
        
class enemy(character):
    types = None
    strength = None
    def __init__(self, name, types, strength):
        self,name = name
        self.types = types
        self.strength = strength

class vampire(enemy):
    day = True
    def __init__(self, name, health, magicPoint, types, strength, day):
        self.name = name
        self.health = health
        self.magicPoint = magicPoint
        self.types = types
        self.strength = strength
        self.day = day
    
    def desVamp(self):
        print("🌟  Generic RPG 🌟")
        print("🦇  Vampire 🦇")
        print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoint}\nType: {self.types}\nDay: {self.day}")
        #input(f"Day/Night : {self.day}")
  
class orc(enemy):
    speed = None
    def __init__(self, name, health, magicPoint, types, strength, speed):
        self.name = name
        self.health = health
        self.magicPoint = magicPoint
        self.types = types
        self.strength = strength
        self.speed = speed
    
    def desOrc(self):
        print("🌟  Generic RPG 🌟")
        print("👾  Monster 👾")
        print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoint}\nType: {self.types}\nSpeed: {self.speed}")

play = player("David", 3)
play.DescPLay()
print(play.isAlive())

print()

vamp = vampire("Boris", 45, 70, "Vampire", 3, False)
vamp.desVamp()

print()

vamp2 = vampire("Rishi", 60, 10, "Vampire", 75, True)
vamp2.desVamp()

print()

Orc = orc("Bill", 60, 5, "Orc", 75, 90)
Orc.desOrc()

print()

Orc2 = orc("Ted", 75, 40, "Orc", 80, 45)
Orc2.desOrc()

print()

Orc3 = orc("Station", 35, 40, "Orc", 49, 50)
Orc3.desOrc()
