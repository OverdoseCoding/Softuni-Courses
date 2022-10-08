year_tax_basketball = int(input())

percent_tax = year_tax_basketball * 0.4
price_sneakers = year_tax_basketball - percent_tax

percent_sneakers = price_sneakers * 0.2
price_outfit = price_sneakers - percent_sneakers
price_ball = price_outfit * 0.25
price_accessories = price_ball * 0.2

all_price = year_tax_basketball + price_sneakers + price_outfit + price_ball + price_accessories

print(all_price)