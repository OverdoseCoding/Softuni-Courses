t_shirt = float(input())
needed_sum_to_win_the_ball = float(input())

pants = t_shirt * 0.75
sockets = pants * 0.2
boots = (t_shirt + pants) * 2

total_sum = t_shirt + pants + sockets + boots
total_sum_after_discount = total_sum - (total_sum * 0.15)

if total_sum_after_discount >= needed_sum_to_win_the_ball:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum_after_discount:.2f} lv.")
else:
    needed_money = abs(total_sum_after_discount - needed_sum_to_win_the_ball)
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {needed_money:.2f} lv. more.")