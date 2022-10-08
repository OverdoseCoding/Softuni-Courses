text = input()
all_steps = 0

while text != 'Going home':
    steps = int(text)
    all_steps += steps

    if all_steps >= 10000:
        break

    text = input()

if text == 'Going home':
    steps_to_home = int(input())
    all_steps += steps_to_home

if all_steps >= 10000:
    print("Goal reached! Good job!")
    print(f'{abs(all_steps - 10000)} steps over the goal!')
else:
    print(f'{abs(10000 - all_steps)} more steps to reach goal.')