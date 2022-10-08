rows = int(input())

for i in range(rows + 1):
    print(f"{' ' * (rows - i)}{'*' * i} | {'*' * i}")