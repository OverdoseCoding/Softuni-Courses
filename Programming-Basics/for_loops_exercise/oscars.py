actors_name = input()
first_points = float(input())
raters = int(input())

points = first_points
name_character_points = 0

for i in range(1, raters + 1):
        name_of_the_rater = input()
        points_from_the_rater = float(input())

        name_character_points = len(name_of_the_rater)
        total_given_points_from_the_rater = (name_character_points * points_from_the_rater) / 2
        points += total_given_points_from_the_rater

        if points >= 1250.5:
                break

if points >= 1250.5:
        print(f"Congratulations, {actors_name} got a nominee for leading role with {points:.1f}!")
else:
        needed_points = 1250.5 - points
        print(f"Sorry, {actors_name} you need {needed_points:.1f} more!")