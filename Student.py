import csv

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
        
        self.student_id = student_id # 学籍番号
        self.name = name # 氏名
        self.gpa = float(gpa) # GPA値
        self.spec_p = float(spec_p) # 専門科目加重平均点
        self.toeic = int(toeic) # TOEIC値
        self.preferences = preferences # 研究室の希望リスト

    def validate_preferences(self, num_of_labs):
        if len(self.preferences) != num_of_labs:
            raise ValueError("The length of preferences must be equal to the number of labs.")

# 学生データをCSVファイルから読み込む
#  データ形式：学籍番号, 氏名, GPA値, 専門科目加重平均点, TOEIC値, 希望リスト
def read_students_from_csv(file_path, num_of_labs):
    students = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # ヘッダー行をスキップ
        for row in reader:
            student = Student(*row)
            student.validate_preferences(num_of_labs) # 希望リストの長さを検証
            students.append(student)
    return students
