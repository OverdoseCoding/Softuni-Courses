#Total count is stored here and in 'total_cnt' too.
n = int(input())
p1_cnt = 0
p2_cnt = 0
p3_cnt = 0
p4_cnt = 0
p5_cnt = 0

#Total count is stored here and in 'n' too.
total_cnt = 0

for i in range(n):
    nums = int(input())
    total_cnt += 1

    if nums < 200:
        p1_cnt += 1
    if 200 <= nums <= 399:
        p2_cnt += 1
    if 400 <= nums <= 599:
        p3_cnt += 1
    if 600 <= nums <= 799:
        p4_cnt += 1
    if 800 <= nums:
        p5_cnt += 1

p1_prcnt = p1_cnt / total_cnt * 100
p2_prcnt = p2_cnt / total_cnt * 100
p3_prcnt = p3_cnt / total_cnt * 100
p4_prcnt = p4_cnt / total_cnt * 100
p5_prcnt = p5_cnt / total_cnt * 100

print(f'{p1_prcnt:.2f}%')
print(f'{p2_prcnt:.2f}%')
print(f'{p3_prcnt:.2f}%')
print(f'{p4_prcnt:.2f}%')
print(f'{p5_prcnt:.2f}%')