count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegeterian_menu = int(input())

price_chicken_menu = count_chicken_menu * 10.35
price_fish_menu = count_fish_menu * 12.40
price_vegeterian_menu = count_vegeterian_menu * 8.15
all_price_menus = price_fish_menu + price_chicken_menu + price_vegeterian_menu
price_dessert = all_price_menus *  0.2
price_delivery = 2.50

all_price_order = all_price_menus + price_dessert + price_delivery

print(all_price_order)
