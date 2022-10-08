first_number = int(input())
second_number = int(input())
third_number = int(input())

all_time = first_number + second_number + third_number

all_time_minutes = int(all_time / 60)
all_time_seconds = int(all_time % 60)

if all_time_seconds <= 9:
    print(f"{all_time_minutes}:0{all_time_seconds}")
elif all_time_seconds >= 9:
    print(f"{all_time_minutes}:{all_time_seconds}")