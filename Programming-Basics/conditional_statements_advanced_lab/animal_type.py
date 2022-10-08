animal_name = str(input())

mammal = ["dog"]
reptile = ["crocodile", "tortoise", "snake"]
others = ["uknown"]

if animal_name in mammal:
    print("mammal")
elif animal_name in reptile:
    print("reptile")
else:
    print("unknown")