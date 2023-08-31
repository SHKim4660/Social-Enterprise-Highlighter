import csv
import re
import os
import pandas as pd

# path == os.path.join('data', 'data.csv')

# test_filepath = os.path.join('data', 'data_test.csv')

def remove_data(filepath,data):
    with open(filepath, 'rt', encoding='UTF8') as file:
        lines = file.readlines()
    with open(filepath, "w") as file:
        for line in lines:
            if line.strip("\n") != data:     # <= 이 문자열만 골라서 삭제
                file.write(line)

def add_data(filepath,data):
    with open(filepath, "a") as file:
        file.write(f"\n{data}\n")


# remove_data(filepath,"가나다")
# add_data(test_filepath,"가라다")