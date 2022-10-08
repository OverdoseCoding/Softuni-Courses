from sys import maxsize

number = int(input())
max_number = -maxsize
current_number = 0
all_sum = 0
all_sum_without_max = 0

for i in range(number):
    current_number = int(input())
    all_sum += current_number

    if current_number > max_number:
        max_number = current_number

    all_sum_without_max = all_sum - max_number

if all_sum_without_max == max_number:
    print('Yes')
    print(f'Sum = {all_sum_without_max}')
else:
    diff = abs(all_sum_without_max - max_number)
    print('No')
    print(f'Diff = {diff}')