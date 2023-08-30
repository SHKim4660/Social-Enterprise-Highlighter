import csv
import re
import os
import pandas as pd

# path == os.path.join('data', 'data.csv')

file = os.path.join('data', 'data_test.csv')

def remove_data(filepath,data):
    filepath,data

# target_rows = []
# for row_index, row in file.iterrows():    
#     if row.loc[0] == "가나다":
#         target_rows.append(row_index)

with open(file, 'rt', encoding='UTF8'):
    lines = file.readlines()
with open(file, "w"):
    for line in lines:
        if line.strip("\n") != "가나다":     # <= 이 문자열만 골라서 삭제
            file.write(line)

