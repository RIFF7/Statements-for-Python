#perlu diingat pada function range(start, stop, step atau increment)

print("Loan Calculator\n")
print("$1000 over 10 years at 5% APR\n")

money = 1000
apr = 5 / 100

for year in range(1, 11):
    interest = money * apr
    money += interest
    print("You paid $" + str(round(money, 2)) + " in interest!")
