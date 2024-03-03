#######################################################
# 「直行生」の研究室割り当てアルゴリズム（過年度生は手作業で）

from Labo import Labo, read_labs_from_csv

# 研究室データをCSVファイルから読み込む
labs = read_labs_from_csv('labs2023.csv')
num_of_labs = len(labs)  # 研究室数

print("Number of labs = ", num_of_labs)
# for lab in labs:
#     print(f"Lab Name: {lab.lab_name}, Lower Limit: {lab.l_limit}, Upper Limit: {lab.u_limit}")
# print()

from Student import Student, read_students_from_csv

# 学生データをCSVファイルから読み込む
students = read_students_from_csv('students2023.csv', num_of_labs)
num_of_students = len(students)  # 学生数

print("Number of students = ", num_of_students)
# for student in students:
#     print(f"ID {student.student_id}, Name: {student.name}, GPA: {student.gpa}, Spec_P: {student.spec_p}, TOEIC: {student.toeic}, Preferences: {student.preferences}")
print()

# 正当な不満のない研究室割り当てアルゴリズム
def allocate_students(students, labs):
    n = len(students)
    c = 1 + n - sum([lab.l_limit for lab in labs])
    
    # 学生データを gpa, spec_p, toeic の順のキーでソートする
    sorted_students = sorted(students, key=lambda x: (x.gpa, x.spec_p, x.toeic), reverse=True)

    ###################################################################
    # 同じgpa、spec_p、toeicを持つ学生を抽出する
    same_values_students = []

    # sorted_studentsをループして、連続する学生が同じgpa、spec_p、toeicを持つかどうかをチェックします
    for i in range(len(sorted_students) - 1):
        if (sorted_students[i].gpa, sorted_students[i].spec_p, sorted_students[i].toeic) == \
           (sorted_students[i + 1].gpa, sorted_students[i + 1].spec_p, sorted_students[i + 1].toeic):
            same_values_students.append(sorted_students[i])
            same_values_students.append(sorted_students[i + 1])
        else:
            # 連続する学生のうち、同じgpa、spec_p、toeicを持たない場合、ループを終了します
            break

    # 同じgpa、spec_p、toeicを持つ学生のリストを出力します
    print("GPA, 専門平均, TOEICがすべて同じ学生のリストは次のとおりです：")
    if len(same_values_students) == 0:
        print("なし")
    for student in same_values_students:
        print(student.student_id, student.name, student.gpa, student.spec_p, student.toeic)
    print()
    ###################################################################

    for student in sorted_students:
        for lab_name in student.preferences:
            lab = next((lab for lab in labs if lab.lab_name == lab_name), None)
            if lab and lab.assign_count < lab.l_limit:
                lab.assign_count += 1
                lab.assigned_students.append(student)
                print(c, student.student_id, student.name, lab.lab_name, lab.assign_count) # デバッグ用
                break
            elif lab and lab.l_limit <= lab.assign_count < lab.u_limit and c > 0:
                lab.assign_count += 1
                lab.assigned_students.append(student)
                print(c, student.student_id, student.name, lab.lab_name, lab.assign_count) # デバッグ用
                c -= 1
                break

# 学生の配属を実行
allocate_students(students, labs)

print()
# 結果出力
for lab in labs:
    print(f"Lab {lab.lab_name}: Assigned {lab.assign_count} students.")
    lab.print_assigned_students()
    print()
