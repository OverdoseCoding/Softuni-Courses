packet_chemicals = float(5.80)
packet_markers = float(7.20)
preparati = float(1.20)

number_packet_chemicals = int(input())
number_packet_markers = int(input())
liters_preparati = int(input())
percentage_discount = int(input())

price_chemicals = number_packet_chemicals * packet_chemicals
price_markers = number_packet_markers * packet_markers
price_preparat = liters_preparati * preparati
all_price = price_preparat + price_markers + price_chemicals
percent = percentage_discount * 0.01
price_with_discount = all_price - (all_price * percent)

print(price_with_discount)