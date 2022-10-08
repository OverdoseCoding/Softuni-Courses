name_of_the_student = input()

current_class = 0
average_grade = 0
total_sum_of_grades = 0
bad_grades = 0

while True:
    grades = float(input())
    current_class += 1

    if grades < 4:
        bad_grades += 1
        if bad_grades == 2:
            print(f'{name_of_the_student} has been excluded at {current_class} grade')
            break
        current_class -= 1

    else:
        total_sum_of_grades += grades

    if current_class == 12:
        average_grade = total_sum_of_grades / 12
        print(f'{name_of_the_student} graduated. Average grade: {average_grade:.2f}')
        break