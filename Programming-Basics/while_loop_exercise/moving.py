width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())
total_meters = width_free_space * length_free_space * height_free_space
total_number_of_boxes = 0

command = input()
while command != 'Done':
    number_of_boxes = int(command)
    total_number_of_boxes += number_of_boxes

    diff = abs(total_meters - total_number_of_boxes)

    if total_number_of_boxes >= total_meters:
        print(f'No more free space! You need {diff} Cubic meters more.')
        break

    command = input()

    if command == 'Done':
        print(f'{diff} Cubic meters left.')
        break