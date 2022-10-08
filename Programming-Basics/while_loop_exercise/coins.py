from math import floor

sum = float(input())
change_Sum = sum * 100
coin_counter = 0

while change_Sum > 0:
    if change_Sum >= 200:
        change_Sum -= 200
        coin_counter += 1
    elif 200 < change_Sum >= 100:
        change_Sum -= 100
        coin_counter += 1
    elif 100 < change_Sum >= 50:
        change_Sum -= 50
        coin_counter += 1
    elif 50 < change_Sum >= 20:
        change_Sum -= 20
        coin_counter += 1
    elif 20 < change_Sum >= 10:
        change_Sum -= 10
        coin_counter += 1
    elif 10 < change_Sum >= 5:
        change_Sum -= 5
        coin_counter += 1
    elif 5 < change_Sum >= 2:
        change_Sum -= 2
        coin_counter += 1
    elif 2 < change_Sum >= 1:
        change_Sum -= 1
        coin_counter += 1

print(floor(coin_counter))