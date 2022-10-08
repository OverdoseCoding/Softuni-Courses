deposit_sum = float(input())
term_of_deposit = int(input())
year_debt_percent = float(input())

sum = deposit_sum + term_of_deposit * ((deposit_sum * year_debt_percent / 100) / 12)


print(sum)