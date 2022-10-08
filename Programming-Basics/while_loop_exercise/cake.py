width = int(input())
length = int(input())
all_cake = width * length

cake_piece_counter = 0

while all_cake > cake_piece_counter:
    command = input()

    if command == 'STOP':
        break

    number_of_cakes = int(command)
    cake_piece_counter += number_of_cakes

left_cake = abs(cake_piece_counter - all_cake)

if all_cake < cake_piece_counter:
    print(f'No more cake left! You need {left_cake} pieces more.')
else:
    print(f'{left_cake} pieces are left.')