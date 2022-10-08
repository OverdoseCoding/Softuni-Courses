hour = int(input())
day = input()

working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',]

if hour >= 10 and hour <= 18:
    if day in working_days:
        print("open")
    else:
        print("closed")
else:
    print("closed")