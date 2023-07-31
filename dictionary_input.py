name = input("Input your name > ").strip().capitalize()
birthDay = input("Input your date of birth > ").strip()
phoneNumber = input("Input your telephone number > ").strip()
email = input("Input your email > ")
address = input("Input your address > ")

card = {"name": name, "birth": birthDay,
        "number": phoneNumber, "email": email,
        "address": address}
print()
print(f"Hi {card['name']} Our dictionary says that you were born on {card['birth']}, we can call you on {card['number']}, email {card['email']}, or write to {card['address']}")
print()
print("Here's your contact card\n")
print(f"Name: {card['name']}")
print(f"Birthday: {card['birth']}")
print(f"Telephone Number: {card['number']}")
print(f"Email: {card['email']}")
print(f"Address: {card['address']}")
