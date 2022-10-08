hours = int(input())
minutes = int(input())

all_time_in_mins = hours * 60 + minutes + 15

time_in_hours = all_time_in_mins // 60
time_in_mins = all_time_in_mins % 60

if time_in_hours > 23:
    time_in_hours = 0

print(f"{time_in_hours}:{time_in_mins:02d}")