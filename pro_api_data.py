import csv
import re
import os

# "사회적기업정보" , "\data\pro_name_data.csv"
# "K-RE100참여기업" , "\data\pro_KRE_data.csv"

pattern = r'\([^)]*\)'
pro_data_list = []

def pro_data(name):
    pro_data_list = []

    if name == "사회적기업정보":                                    # 파일 불러오기
        filename = os.path.join('data', 'raw_name_data.csv')
        target_file = os.path.join('data', 'pro_name_data.csv')

    if name == "K-RE100참여기업":
        filename = os.path.join('data', 'raw_KRE_data.csv')
        target_file = os.path.join('data', 'pro_KRE_data.csv')

    file = open(filename,'r') 
    reader = csv.reader(file)                           # (주),(유) 등 필요없는 항목 제거
    for line in reader:
        pro_data = re.sub(pattern=pattern, repl='', string= line[0]).replace("㈜","").replace("유)","").replace("주)","").replace("사)","").replace(" ","").replace("주식회사","").replace("사단법인","")
        pro_data_list.append([pro_data])
    
    save_data(target_file,pro_data_list)          # 저장
    print(pro_data_list)

        
def save_data(filename,index):
    file = open(filename,'a',newline='')
    writer = csv.writer(file)
    writer.writerows(index)

pro_data("사회적기업정보")
pro_data("K-RE100참여기업")
