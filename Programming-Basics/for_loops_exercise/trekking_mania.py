number_of_groups = int(input())

all_people = 0
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for i in range(1, number_of_groups + 1):
    number_of_people_in_the_group = int(input())
    all_people += number_of_people_in_the_group

    if number_of_people_in_the_group <= 5:
        musala += number_of_people_in_the_group
    if 6 <= number_of_people_in_the_group <= 12:
        monblan += number_of_people_in_the_group
    if 13 <= number_of_people_in_the_group <= 25:
        kilimandjaro += number_of_people_in_the_group
    if 26 <= number_of_people_in_the_group <= 40:
        k2 += number_of_people_in_the_group
    if 41 <= number_of_people_in_the_group:
        everest += number_of_people_in_the_group

musala_prcnt = (musala / all_people) * 100
monblan_prcnt = (monblan / all_people) * 100
kilimandjaro = (kilimandjaro / all_people) * 100
k2_prcnt = (k2 / all_people) * 100
everest_prcnt = (everest / all_people) * 100

print(f'{musala_prcnt:.2f}%')
print(f'{monblan_prcnt:.2f}%')
print(f'{kilimandjaro:.2f}%')
print(f'{k2_prcnt:.2f}%')
print(f'{everest_prcnt:.2f}%')