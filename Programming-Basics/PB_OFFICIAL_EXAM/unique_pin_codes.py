up_num1 = int(input())
up_num2 = int(input())
up_num3 = int(input())

flag = True

for n1 in range(2, up_num1 + 1, 2):
    for n2 in range(2, up_num2 + 1):
        for n3 in range(2, up_num3 + 1, 2):
            if n2 == 2 or n2 == 3 or n2 == 5 or n2 == 7:
                print(f"{n1} ", end='')
                print(f"{n2} ", end='')
                print(f"{n3}",)