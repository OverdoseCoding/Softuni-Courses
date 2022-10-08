lily_age = int(input())
price_washing = float(input())
toy_price = int(input())

toys = 0
got_money = 0
total_money = 0

for age in range(1, lily_age + 1):
    if age % 2 == 0:
        got_money = (age * 5) - 1
        total_money += got_money
    else:
        toys += 1 * toy_price

total_money += toys
diff = abs(total_money - price_washing)

if total_money >= price_washing:
    print(f"Yes! {diff:.2f}")
else:
    print(f'No! {diff:.2f}')