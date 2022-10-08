number_of_allowed_wrong_grades = int(input())
wrong_grades_counter = 0
grades_counter = 0
all_grades = 0
average_score = 0
last_problem = ''

while True:
    name_of_problem = str(input())
    if name_of_problem == 'Enough':
        print(f'Average score: {average_score:.2f}')
        print(f'Number of problems: {grades_counter}')
        print(f'Last problem: {last_problem}')
        break

    grade_of_problem = int(input())
    grades_counter += 1

    last_problem = name_of_problem
    all_grades += grade_of_problem
    average_score = all_grades / grades_counter

    if grade_of_problem <= 4:
        wrong_grades_counter += 1
    if wrong_grades_counter == number_of_allowed_wrong_grades:
        print(f'You need a break, {wrong_grades_counter} poor grades.')
        break