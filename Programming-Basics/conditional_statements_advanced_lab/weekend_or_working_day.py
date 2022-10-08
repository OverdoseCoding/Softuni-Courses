day = str(input())

working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
not_working_days = ["Saturday", "Sunday"]

if day in working_days:
    print("Working day")
elif day in not_working_days:
    print("Weekend")
else:
    print("Error")