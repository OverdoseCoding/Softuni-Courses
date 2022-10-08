first_number = int(input())

left_sum = 0
right_sum = 0

for i in range(first_number):
    entered_numbers = int(input())
    left_sum += entered_numbers

for i in range(first_number):
    entered_numbers = int(input())
    right_sum += entered_numbers

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diff = abs(left_sum - right_sum)
    print(f'No, diff = {diff}')