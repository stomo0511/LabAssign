# Moodleの小テストから配属希望リストを作成する

import csv
from collections import defaultdict
import sys

# 学生データをCSVファイルから読み込む
#  ヘッダ：姓（学籍番号）, 名（氏名）, メールアドレス, 開始日時, 受験完了, 所要時間, 評点/1.00, 解答1
def read_data_from_csv(file_path):
    data = defaultdict(list)
    with open(file_path, mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        # print(reader.fieldnames) # デバッグ用
        for row in reader:
            if row['状態'] == '終了':   # '状態'が'終了'の行のみを処理する
                full_name = row['姓'] + row['名']
                data[full_name].append(row)
    return data

# 新しいCSVファイルにデータを書き込む関数
#  ヘッダ：学籍番号, 氏名, 希望リスト
def write_data_to_csv(data, file_path):
    fieldnames = ['学籍番号', '氏名', '希望リスト']
    # Excal for Mac 用には encoding='utf-16' とする
    with open(file_path, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter='\t')
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# main関数
def main(input_file, output_file):
    data = read_data_from_csv(input_file)
    
    # データを整理して新しい形式に変換する
    new_data = []
    for full_name, rows in data.items():
        # 同一学生の中で最新の受験完了日時を持つ行を取得する
        latest_row = max(rows, key=lambda x: x['受験完了'])
        student_id = latest_row['姓']       # '性' -> 学籍番号
        name = latest_row['名']             # '名' -> 氏名
        preferences = latest_row['解答 1']  # '解答 1' -> 希望リスト
        new_data.append({'学籍番号': student_id, '氏名': name, '希望リスト': preferences})

    # '学籍番号'の昇順にソート
    new_data_sorted = sorted(new_data, key=lambda x: x['学籍番号'])

    # 新しいCSVファイルにデータを書き込む
    write_data_to_csv(new_data_sorted, output_file)

# メイン処理の実行
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python makePrefList.py <input_file> <output_file>")
        sys.exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)