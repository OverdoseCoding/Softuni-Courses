from math import ceil
tvserial = str(input())
duration_of_episode = int(input())
duration_of_break = int(input())

lunch = duration_of_break / 8
rest = duration_of_break / 4
left_time = duration_of_break - (lunch + rest)

left_time_with_episode = left_time - duration_of_episode

needed_time = duration_of_episode - left_time

if left_time >= duration_of_episode:
    print(f"You have enough time to watch {tvserial} and left with {ceil(left_time_with_episode)} minutes free time.")
else:
    print(f"You don't have enough time to watch {tvserial}, you need {ceil(needed_time)} more minutes.")