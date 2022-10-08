movie_budget = float(input())
number_of_statists = int(input())
price_for_dress_of_statists = float(input())

price_movie_decor = movie_budget * 0.1
price_for_dress_for_all_statists = price_for_dress_of_statists * number_of_statists

if number_of_statists >= 150:
    price_for_dress_for_all_statists -= price_for_dress_for_all_statists * 0.1

total_movie_price = price_movie_decor + price_for_dress_for_all_statists
left_money_none = movie_budget - total_movie_price
left_money = (left_money_none)

if total_movie_price > movie_budget:
    not_enough_money = movie_budget - total_movie_price
    print("Not enough money!")
    print(f"Wingard needs {abs(not_enough_money):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {left_money:.2f} leva left.")