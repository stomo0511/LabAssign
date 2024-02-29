from Labo import Labo, read_labs_from_csv

# 研究室データをCSVファイルから読み込む
labs = read_labs_from_csv('labs2023.csv')
num_of_labs = len(labs)  # 研究室数

print("Number of labs = ", num_of_labs)
for lab in labs:
    print(f"Lab Name: {lab.lab_name}, Lower Limit: {lab.l_limit}, Upper Limit: {lab.u_limit}")
print()

from Student import Student, read_students_from_csv

# 学生データをCSVファイルから読み込む
students = read_students_from_csv('students2023.csv', num_of_labs)
num_of_students = len(students)  # 学生数

print("Number of students = ", num_of_students)
for student in students:
    print(f"ID {student.student_id}, Name: {student.name}, GPA: {student.gpa}, Spec_P: {student.spec_p}, TOEIC: {student.toeic}, Preferences: {student.preferences}")
print()

exit()

# 正当な不満のない研究室割り当てアルゴリズム
def allocate_students(students, labs):
    n = len(students)
    c = 1 + n - sum([lab.l_limit for lab in labs])
    sorted_students = sorted(students, key=lambda x: (x.gpa, x.spec_p, x.toeic), reverse=True)
    
    for student in sorted_students:
        for lab_name in student.preferences:
            lab = next((lab for lab in labs if lab.lab_name == lab_name), None)
            if lab and lab.assign_count < lab.l_limit:
                lab.assign_count += 1
                break
            elif lab and lab.l_limit <= lab.assign_count < lab.u_limit and c > 0:
                lab.assign_count += 1
                c -= 1
                break

# 学生の配属を実行
allocate_students(students, labs)

# 結果出力
for lab in labs:
    print(f"Lab {lab.lab_name}: Assigned {lab.assign_count} students.")
