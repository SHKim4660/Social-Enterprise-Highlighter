import requests
import json
import csv
import re

# "사회적기업정보" , "\data\pro_name_data.csv"
# "K-RE100참여기업" , "\data\pro_KRE_data.csv"

pattern = r'\([^)]*\)'
pro_data_list = []

# (주),(유) 등 필요 없는거 날리기
def pro_data(name):
    pro_data_list = []

    if name == "사회적기업정보":
        filename = "data\\raw_name_data.csv"
        target_file = "data\pro_name_data.csv"

    if name == "K-RE100참여기업":
        filename = "data\\raw_KRE_data.csv"
        target_file = "data\pro_KRE_data.csv"

    file = open(filename,'r')
    reader = csv.reader(file)
    for line in reader:
        pro_data = re.sub(pattern=pattern, repl='', string= line[0]).replace("㈜","").replace("유)","").replace("주)","").replace("사)","")
        pro_data_list.append([pro_data])
    
    save_data(target_file,pro_data_list)
    print(pro_data_list)

        
def save_data(filename,index):
    file = open(filename,'a',newline='')
    writer = csv.writer(file)
    writer.writerows(index)

pro_data("사회적기업정보")
pro_data("K-RE100참여기업")