destination = input()
neededMoney = 0
savedMoney = 0
money = 0

while destination != 'End':
    neededMoney = float(input())
    while neededMoney >= savedMoney:
        money = float(input())
        savedMoney += money
        if neededMoney <= savedMoney:
            print(f'Going to {destination}!')
            break
    savedMoney = 0
    destination = input()