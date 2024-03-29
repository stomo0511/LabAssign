## 希望リストのエクスポート
1. 「研究室希望順序」の提出
2. 小テスト管理
3. 受験結果
4. 解答
5. 「テーブルデータをダウンロードする」
   - カンマ区切り値（.csv）
   - ダウンロード
6. 「コース名」-「研究室希望順序」の提出-解答.csv

202?CS-LabAssign_OrigDat.csv として保存

## 希望リスト（CSV）のファイル形式
makePrefList.py の入力ファイル名、出力ファイル名を修正/変更して実行

- 性：学籍番号
- 名：氏名
- メールアドレス：
- 状態：
- 開始日時：
- 受験完了：
- 所要時間：
- 評点/1.00：
- 解答1：希望リスト

性、名、解答1のみ使用する → ヘッダを「学籍番号」、「氏名」、「希望リスト」に変更する

students202?.csv として保存
- makePrefList.py の出力ファイルは CSV として認識されないことがある
  - Excel でCSVファイルとして「名前をつけて保存」する
- <font color="red">重要</font>：過年度生は手作業で配属するので、直行生のみのファイルとする

## 希望リストファイルにGPA， 専門科目加重平均, TOEIC値を追加
手作業でCSVファイルを編集する
- '氏名'の後に'GPA値'、'専門科目加重平均点', 'TOEIC値'フィールドを追加
- GPA値は「成績データ」からコピー
- 専門科目加重平均点は「成績データ」に計算式を入力して算出する
  - 小数点以下２桁
- TOEIC値は Moodle の「TOEICスコア入力」からエクスポート
  - ただし、スコアシートの点数と同一であることを確認する
- <font color="red">重要</font>：最下位学生のGPA値、加重平均点、TOEIC値は「0点」とする

## 配属プログラム実行
研究室ファイル、学生ファイルの2つを引数として LabAssign.py を実行する

## メモ
- 2022年度配属は、配属希望を提出していない卒論着手可能者が1名あり -> studenst2022にダミーデータを1行追加（この学生にも２研究室のどちらかを選ばせるため）
- 2023年度配属は、茅・朱研究室の上限が4だった。過年度生1名の配属を先に決めたので、直行生用上限が1つ減った