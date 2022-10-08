premiere = input()
rows = int(input())
columns = int(input())
price = 0

if premiere == "Premiere":
    price = rows * columns * 12.00
elif premiere == "Normal":
    price = rows * columns * 7.50
elif premiere == "Discount":
    price = rows * columns * 5.00

print(f"{price:.02f}")