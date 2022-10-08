number_of_floor = int(input())
number_of_flats = int(input())

flat_number = 0
flat_name = 0

for floor in range(number_of_floor, 0, -1):
    for flats in range(number_of_flats):
        flat_number = floor * 10 + flats

        if floor == number_of_floor:
            flat_name = f'L{flat_number}'
        elif floor % 2 != 0:
            flat_name = f'A{flat_number}'
        else:
            flat_name = f'O{flat_number}'

        print(flat_name, end=' ')
    print()