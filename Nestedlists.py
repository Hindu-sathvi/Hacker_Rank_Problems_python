 #  https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
 #nested-list
 #code
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
unique_grades = sorted(set(student[1] for student in students))
second_lowest_grade = unique_grades[1]
second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
second_lowest_students.sort()
for student in second_lowest_students:
        print(student)