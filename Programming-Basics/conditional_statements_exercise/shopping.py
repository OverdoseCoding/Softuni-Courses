peters_budget = float(input())
videographics = int(input())
processors = int(input())
ram = int(input())

one_videographic = videographics * 250
one_processor = processors * (one_videographic * 0.35)
one_ram = ram * (one_videographic * 0.1)

total_price = one_videographic + one_processor + one_ram

if videographics > processors:
    total_price = total_price - (total_price * 0.15)

if peters_budget >= total_price:
    left_budget = peters_budget - total_price
    print(f"You have {left_budget:.02f} leva left!")
else:
    needed_money = total_price - peters_budget
    print(f"Not enough money! You need {needed_money:.02f} leva more!")