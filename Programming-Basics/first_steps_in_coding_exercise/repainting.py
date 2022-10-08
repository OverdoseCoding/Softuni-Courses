needed_nylon = int(input())
needed_paint = int(input())
needed_thinner = int(input())
hours_needed = int(input())

sum_of_nylon = (needed_nylon + 2) * 1.50
sum_of_paint = (needed_paint + needed_paint / 10) * 14.50
sum_of_thinner = needed_thinner * 5.00
bags = 0.40

end_sum_for_materials = sum_of_nylon + sum_of_paint + sum_of_thinner + bags

percent = end_sum_for_materials * 0.3

sum_for_crafstmen = percent * hours_needed

all_sum = end_sum_for_materials + sum_for_crafstmen

print(all_sum)