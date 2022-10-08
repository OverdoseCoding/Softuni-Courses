opened_tabs = int(input())
salary = int(input())
fine = 0

for website_names in range(opened_tabs):
    website_names1 = input()

    if website_names1 == "Facebook":
        fine = 150
    elif website_names1 == "Instagram":
        fine = 100
    elif website_names1 == "Reddit":
        fine = 50
    else:
        fine = 0

    salary -= fine

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)