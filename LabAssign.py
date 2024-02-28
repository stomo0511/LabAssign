import csv

###############################################################
# 研究室クラス
class Labo:
    def __init__(self, lab_name, l_limit, u_limit):
        if int(l_limit) > int(u_limit):
            raise ValueError("Lower limit cannot be greater than upper limit.")
        self.lab_name = lab_name
        self.l_limit = int(l_limit)
        self.u_limit = int(u_limit)
        self.assign_count = 0  # 配属数を0で初期化

# 研究室データをCSVファイルから読み込む
#  データ形式：研究室名（文字列）, 配属下限, 配属上限
#  例："Lab1", 1, 3
def read_labs_from_csv(file_path):
    labs = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            lab = Labo(*row)
            labs.append(lab)
    return labs

labs = read_labs_from_csv('labs.csv')
num_of_labs = len(labs)

# 研究室情報を出力する
for lab in labs:
    print(f"Lab Name: {lab.lab_name}, Lower Limit: {lab.l_limit}, Upper Limit: {lab.u_limit}")
print()
print()

###############################################################
# 学生クラス
class Student:
    def __init__(self, student_id, name, gpa, spec_p, toeic, preferences):
        if float(gpa) < 0:
            raise ValueError("GPA value should be greater than zero.")
        if float(spec_p) < 0:
            raise ValueError("spec_p value should be greater than zero.")
        if int(toeic) < 0:
            raise ValueError("TOEIC score should be greater than zero.")
        if len(preferences) != num_of_labs:
            raise ValueError("The length of preferences must be equal to the number of labs.")
        
        self.student_id = student_id # 学籍番号
        self.name = name # 氏名
        self.gpa = float(gpa) # GPA値
        self.spec_p = float(spec_p) # 専門科目加重平均点
        self.toeic = int(toeic) # TOEIC値
        self.preferences = preferences # 研究室の希望リスト

# 学生データをCSVファイルから読み込む
#  データ形式：学籍番号, 氏名, GPA値, 専門科目加重平均点, TOEIC値, 希望リスト
def read_students_from_csv(file_path):
    students = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # ヘッダー行をスキップ
        for row in reader:
            student = Student(*row)
            students.append(student)
    return students

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

# 学生のリストを作成する
students = [
    Student("S001", "Alice", 3.8, 85, 750, ["Lab2", "Lab1", "Lab3"]),
    Student("S002", "Bob", 3.5, 78, 670, ["Lab1", "Lab3", "Lab2"]),
    Student("S003", "Charlie", 3.9, 92, 800, ["Lab3", "Lab2", "Lab1"])
]

# 学生の配属を実行
allocate_students(students, labs)

# 結果出力
for lab in labs:
    print(f"Lab {lab.lab_name}: Assigned {lab.assign_count} students.")
