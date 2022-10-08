processor_in_dollars = float(input())
video_card_in_dollars = float(input())
ram_in_dollars = float(input())
number_rams = int(input())
discount = float(input())

processor_in_leva = processor_in_dollars * 1.57
video_card_in_leva = video_card_in_dollars * 1.57
ram_in_leva = ram_in_dollars * 1.57
total_ram_price = ram_in_leva * number_rams

discount_for_processor = processor_in_leva * (1 - discount)
discount_for_video_card = video_card_in_leva * (1 - discount)

total_price = discount_for_processor + discount_for_video_card + total_ram_price

print(f'Money needed - {total_price:.2f} leva.')