from sys import maxsize
line = input()

max_number = -maxsize

while line != "Stop":
    number1 = float(line)

    line = input()
    if number1 > max_number:
        max_number = number1

print(f'{int(max_number)}')