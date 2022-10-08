num = int(input())
flag = True

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = False
            break

if flag:
    print("prime number")
else:
    print("not a prime number")