kv_meters = float(input())

all_sum = kv_meters * 7.61
discount = 0.18 * all_sum
end_sum =  all_sum - discount


print(f"The final price is: {end_sum} lv.")
print(f"The discount is: {discount} lv.")