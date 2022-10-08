group_budget = int(input())
season = str(input())
fishermen = int(input())

discount = 0
price_for_boat_rent = 0

if season == "Summer" or season == "Autumn":
    price_for_boat_rent += 4200
elif season == "Spring":
    price_for_boat_rent += 3000
elif season == "Winter":
    price_for_boat_rent += 2600

if fishermen <= 6:
    discount += 0.10
if 7 <= fishermen <= 11:
    discount += 0.15
if fishermen >= 12:
    discount += 0.25

if season != "Autumn" and fishermen % 2 == 0:
        price_for_boat_rent -= price_for_boat_rent * 0.05

price_for_boat_rent -= price_for_boat_rent * discount
need_money = abs(group_budget - price_for_boat_rent)

if group_budget >= price_for_boat_rent:
    print(f"Yes! You have {need_money:.2f} leva left.")
else:
    print(f"Not enough money! You need {need_money:.2f} leva.")