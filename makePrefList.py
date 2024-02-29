# Moodleの小テストから配属希望リストを作成する

import csv

###############################################################
# 学生クラス
class Student:
    def __init__(self, student_id=None, name=None, gpa=None, spec_p=None, toeic=None, preferences=None):
        self.student_id = student_id # 学籍番号
        self.name = name # 氏名
        self.gpa = float(gpa) if gpa is not None else 0.0 # GPA値
        self.spec_p = float(spec_p) if spec_p is not None else 0.0 # 専門科目加重平均点
        self.toeic = int(toeic) if toeic is not None else 0 # TOEIC値
        self.preferences = preferences # 研究室の希望リスト

    def validate_preferences(self, num_of_labs):
        if len(self.preferences) != num_of_labs:
            raise ValueError("The length of preferences must be equal to the number of labs.")

# 学生データをCSVファイルから読み込む
#  データ形式：性（学籍番号）, 名（氏名）, 開始日時, 受験完了, 所要時間, 評点/1.00, 解答1
def read_preferences_from_csv(file_path, num_of_labs):
    students = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # ヘッダー行をスキップ
        for row in reader:
            student = Student(*row)
            student.validate_preferences(num_of_labs) # 希望リストの長さを検証
            students.append(student)
    return students

# 学生データをCSVファイルに書き出す
# データ形式：学籍番号, 氏名, GPA値, 専門科目加重平均点, TOEIC値, 希望リスト
# GPA値、専門科目加重平均点、TOEIC値は 0 として出力 -> 手入力する
def write_preferences_to_csv(file_path, students):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['学籍番号', '氏名', 'GPA値', '専門科目加重平均点', 'TOEIC値', '希望リスト'])
        for student in students:
            writer.writerow([student.student_id, student.name, student.gpa, student.spec_p, student.toeic, student.preferences])

num_of_labs = 15

# 学生データをCSVファイルから読み込む
students = read_preferences_from_csv('2023CS-LabAssign.csv', num_of_labs)
num_of_students = len(students)  # 学生数