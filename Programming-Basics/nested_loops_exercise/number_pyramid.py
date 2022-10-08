n = int(input())
counter = 1

flag = False
for i in range(1, n + 1):
    for j in range(0, i):
        print(f'{counter}', end=' ')
        counter += 1

        if counter > n:
            flag = True
            break
    if flag:
        break
    print()