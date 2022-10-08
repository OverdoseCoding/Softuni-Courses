startup_points = int(input())
bonus_point = 0

if startup_points <= 100:
    bonus_point = +5
elif startup_points > 1000:
    bonus_point = startup_points * 0.1
else:
    bonus_point = startup_points * 0.2

if startup_points % 2 == 0:
    bonus_point = bonus_point + 1
elif startup_points % 5 == 0:
    bonus_point = bonus_point + 2

print(bonus_point)
print(startup_points + bonus_point)