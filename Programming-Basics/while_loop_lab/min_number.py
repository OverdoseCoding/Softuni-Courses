from sys import maxsize
line = input()

min_number = maxsize

while line != "Stop":
    number1 = float(line)

    line = input()
    if number1 < min_number:
        min_number = number1

print(f'{int(min_number)}')