import csv
import pprint

import numpy as np
import pandas as pd

csvfile_path = 'input_files/csv.csv'

with open(csvfile_path) as f:
    f_reader = csv.reader(f)
    for row in f_reader:
        print(row)

# 二次元配列
with open(csvfile_path) as f:
    reader = csv.reader(f)
    l = [row for row in reader]
    print(l)

    # 数値に変換
    print([[int(v) for v in row] for row in l])

# 浮動小数点数に変換して取得
with open(csvfile_path) as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    l_f = [row for row in reader]
    print(l_f)

# numpyを使用して読み込み
a = np.loadtxt(csvfile_path, delimiter=',')
print(a)

# 範囲を指定して抽出
print(a[1:, :2])

# pandasで読み込み
df = pd.read_csv(csvfile_path, header=None)
print(df)
