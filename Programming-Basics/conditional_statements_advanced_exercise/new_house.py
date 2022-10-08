type_of_flower = str(input())
number_of_flowers = int(input())
budget = int(input())
price = 0
discount = 0
antidiscount = 0

if type_of_flower == "Roses":
    price = 5

    if number_of_flowers > 80:
        discount = 0.10
if type_of_flower == "Dahlias":
    price = 3.80

    if number_of_flowers > 90:
        discount = 0.15
if type_of_flower == "Tulips":
    price = 2.80

    if number_of_flowers > 80:
        discount = 0.15
        price = price
if type_of_flower == "Narcissus":
    price = 3

    if number_of_flowers < 120:
        antidiscount = 0.15
if type_of_flower == "Gladiolus":
    price = 2.50

    if number_of_flowers < 80:
        antidiscount = 0.20

total_price = price * number_of_flowers
total_price -= total_price * discount
total_price += total_price * antidiscount

need_money = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {need_money:.2f} leva left.")
else:
    print(f"Not enough money, you need {need_money:.2f} leva more.")