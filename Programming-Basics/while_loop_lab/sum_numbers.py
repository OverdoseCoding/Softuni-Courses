first_number = int(input())
second_numbers = int(input())

while True:
    second_numbers += int(input())
    if second_numbers >= first_number:
        break

print(second_numbers)