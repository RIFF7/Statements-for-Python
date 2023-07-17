close = ""

while close != "yes":
    animal = input("What animal do you want? ")
    if animal == "cow" or animal == "Cow":
        print("A cow goes moo.")
    elif animal == "lemur" or animal == "Lemur":
        print("Ummm...the Lesser Spotter Lemur goes awooga.")
    elif animal == "pig" or animal == "Pig":
        print("Ngroooookkkk")
    else:
        print("I don't know that animal sound. Try again.")
    close = input("Exit? ")
