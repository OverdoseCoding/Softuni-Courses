start_interval = int(input())
end_interval = int(input())
magic_number = int(input())
counter = 0
flag = False

for start in range(start_interval, end_interval + 1):
    for end in range(start_interval, end_interval + 1):
        counter += 1
        if start + end == magic_number:
            flag = True
            print(f'Combination N:{counter} ({start} + {end} = {magic_number})')
            break
    if flag:
        break
if not flag:
    print(f'{counter} combinations - neither equals {magic_number}')