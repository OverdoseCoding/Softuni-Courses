days_counter = 1
number_in_meters = 5364

command = input()
while command != "END":
    command1 = int(input())

    if command == "Yes":
        days_counter += 1
        if days_counter > 5:
            print("Failed!")
            print(f"{number_in_meters}")
            break
        number_in_meters += command1
    else:
        number_in_meters += command1
    if number_in_meters >= 8848:
        print(f"Goal reached for {days_counter} days!")
        break

    command = input()

if command == "END":
    if number_in_meters >= 8848:
        print(f"Goal reached for {days_counter} days!")
    else:
        print("Failed!")
        print(f"{number_in_meters}")