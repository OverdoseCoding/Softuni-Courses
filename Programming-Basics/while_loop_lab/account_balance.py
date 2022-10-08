all_sum = 0

while True:
    current_money = input()

    if current_money == "NoMoreMoney":
        break

    current_money = float(current_money)

    if current_money >= 0:
        all_sum += current_money
        print(f'Increase: {float(current_money):.2f}')
    else:
        print("Invalid operation!")
        break

print(f"Total: {all_sum:.2f}")