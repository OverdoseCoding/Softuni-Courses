engaged_tournirs = int(input())
first_points = int(input())

points = 0
final_points = 0
average_points = 0
percent_for_won_tournirs = 0
won_tourninrs = 0

for i in range(1, engaged_tournirs + 1):
#The stage might be W, F or SF
    stage_for_the_torunir = input()

    if stage_for_the_torunir == "W":
        points += 2000
        won_tourninrs += 1
    elif stage_for_the_torunir == "F":
        points += 1200
    elif stage_for_the_torunir == "SF":
        points += 720

percent_for_won_tournirs = won_tourninrs / engaged_tournirs

print(f'Final points: {points + first_points}')
print(f'Average points: {int(points / engaged_tournirs)}')
print(f'{100 * percent_for_won_tournirs:.2f}%')