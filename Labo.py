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
