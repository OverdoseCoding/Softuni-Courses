fruit = input()
day = input()
quantity = float(input())
price = 0

days1 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
days2 = ['Saturday', 'Sunday']

if fruit == "banana":
    if day in days1:
        price = 2.50 * quantity
        print(f"{price:.02f}")
    elif day in days2:
        price = 2.70 * quantity
        print(f"{price:.02f}")
    else:
        print("error")
elif fruit == "apple":
    if day in days1:
        price = 1.20 * quantity
        print(f"{price:.02f}")
    elif day in days2:
        price = 1.25 * quantity
        print(f"{price:.02f}")
    else:
        print("error")
elif fruit == "orange":
    if day in days1:
        price = 0.85 * quantity
        print(f"{price:.02f}")
    elif day in days2:
        price = 0.90 * quantity
        print(f"{price:.02f}")
    else:
        print("error")
elif fruit == "grapefruit":
    if day in days1:
        price = 1.45 * quantity
        print(f"{price:.02f}")
    elif day in days2:
        price = 1.60 * quantity
        print(f"{price:.02f}")
    else:
        print("error")
elif fruit == "kiwi":
    if day in days1:
        price = 2.70 * quantity
        print(f"{price:.02f}")
    elif day in days2:
        price = 3.00 * quantity
        print(f"{price:.02f}")
    else:
        print("error")
elif fruit == "pineapple":
    if day in days1:
        price = 5.50 * quantity
        print(f"{price:.02f}")
    elif day in days2:
        price = 5.60 * quantity
        print(f"{price:.02f}")
    else:
        print("error")
elif fruit == "grapes":
    if day in days1:
        price = 3.85 * quantity
        print(f"{price:.02f}")
    elif day in days2:
        price = 4.20 * quantity
        print(f"{price:.02f}")
    else:
        print("error")
else:
    print("error")