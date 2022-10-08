price_for_tour = float(input())
number_of_puzzels = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

total_numbers = number_of_trucks + number_of_minions + number_of_bears + number_of_dolls + number_of_puzzels

price_of_puzzels = number_of_puzzels * 2.60
price_of_dolls = number_of_dolls * 3
price_of_bears = number_of_bears * 4.10
price_of_minions = number_of_minions * 8.20
price_of_trucks = number_of_trucks * 2

total_price = price_of_puzzels + price_of_dolls + price_of_bears + price_of_minions + price_of_trucks

if total_numbers >= 50:
    total_price -= total_price * 0.25

total_price -= (total_price * 0.1)


if total_price >= price_for_tour:
    left_money = total_price - price_for_tour
    print(f"Yes! {left_money:.2f} lv left.")
else:
    needed_money = price_for_tour - total_price
    print(f"Not enough money! {needed_money:.2f} lv needed.")