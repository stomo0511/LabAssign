# Moodleの小テストから配属希望リストを作成する

import csv
from collections import defaultdict

# 学生データをCSVファイルから読み込む
#  データ形式：姓（学籍番号）, 名（氏名）, メールアドレス, 開始日時, 受験完了, 所要時間, 評点/1.00, 解答1
def read_data_from_csv(file_path):
    data = defaultdict(list)
    with open(file_path, mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        # print(reader.fieldnames)
        for row in reader:
            if row['状態'] == '終了':
                full_name = row['姓'] + row['名']
                data[full_name].append(row)
    return data

# 新しいCSVファイルにデータを書き込む関数
def write_data_to_csv(data, file_path):
    fieldnames = ['学籍番号', '氏名', '希望リスト']
    with open(file_path, mode='w', newline='', encoding='utf-16') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter='\t')
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def main(input_file, output_file):
    data = read_data_from_csv(input_file)
    
    # データを整理して新しい形式に変換する
    new_data = []
    for full_name, rows in data.items():
        latest_row = max(rows, key=lambda x: x['受験完了'])
        student_id = latest_row['姓']
        name = latest_row['名']
        preferences = latest_row['解答 1']
        new_data.append({'学籍番号': student_id, '氏名': name, '希望リスト': preferences})

    # '学籍番号'の昇順にソート
    new_data_sorted = sorted(new_data, key=lambda x: x['学籍番号'])

    # 新しいCSVファイルにデータを書き込む
    write_data_to_csv(new_data_sorted, output_file)

# メイン処理の実行
if __name__ == '__main__':
    main('2022CS-LabAssign_OrigDat.csv', '2022CS-LabAssign_temp.csv')