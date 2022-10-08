text = input()
result = 0

a = 1
e = 2
i = 3
o = 4
u = 5

for x in text:
    if x == "a":
        result += a
    elif x == "e":
        result += e
    elif x == "i":
        result += i
    elif x == "o":
        result += o
    elif x == "u":
        result += u

print(result)