from math import floor

number_of_pages = int(input())
pages_for_1hour = int(input())
number_of_days = int(input())

common_time = floor(number_of_pages / pages_for_1hour)
needed_hours_per_day = common_time / number_of_days

print(int(needed_hours_per_day))