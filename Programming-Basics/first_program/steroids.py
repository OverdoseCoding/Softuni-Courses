steroid_name = str(input("Enter steroid: "))
number_of_steroid = int(input("Enter number of steroid: "))
budget = float(input("Enter your budget: "))
how_much_time_would_you_like_the_cycle_to_be_in_weeks = int(input("How much time would you like the cycle to be in weeks: ")) * 7
mgs_per_weeks = int(input("What mgs you want per week: "))
price = 0
syringes = 0
needles = 0

if steroid_name == "Omnadren":
    price = 23.30 * number_of_steroid
    ampules = number_of_steroid * 5
    syringes = ampules
    needles = syringes * 2
budget -= price

if mgs_per_weeks == 750:
    ampules = how_much_time_would_you_like_the_cycle_to_be_in_weeks / 2

# Make commands that will count the total cycle in days, ampuls, blood tests, food, anti-estrogen, igli, ZMA, vitamini,
# Jiletka, etc..
# Napravi da razpredelq
print(f'{steroid_name} costs {price:.2f} leva.')
print(f'Total ampules: {ampules}; Total syringes: {syringes}; Total needles: {needles}')
print(f'And your left money are {budget:.2f} leva.')