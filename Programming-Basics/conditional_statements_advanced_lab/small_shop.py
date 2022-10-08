product = input()
city = input()
amount = float(input())

if product == "coffee":
    if city == "Sofia":
        print(amount * 0.50)
    elif city == "Plovdiv":
        print(amount * 0.40)
    elif city == "Varna":
        print(amount * 0.45)
elif product == "water":
    if city == "Sofia":
        print(amount * 0.80)
    elif city == "Plovdiv":
        print(amount * 0.70)
    elif city == "Varna":
        print(amount * 0.70)
elif product == "beer":
    if city == "Sofia":
        print(amount * 1.20)
    elif city == "Plovdiv":
        print(amount * 1.15)
    elif city == "Varna":
        print(amount * 1.10)
elif product == "sweets":
    if city == "Sofia":
        print(amount * 1.45)
    elif city == "Plovdiv":
        print(amount * 1.30)
    elif city == "Varna":
        print(amount * 1.35)
elif product == "peanuts":
    if city == "Sofia":
        print(amount * 1.60)
    elif city == "Plovdiv":
        print(amount * 1.50)
    elif city == "Varna":
        print(amount * 1.55)