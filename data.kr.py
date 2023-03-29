import requests
import json
import csv
import pandas

# pro ~~~ = 처리된 데이터
# raw ~~~ = 처리되지 않은 데이터

# page = 1
# perpage = 10
# url = (f"https://api.odcloud.kr/api/socialEnterpriseList/v1/authCompanyList?page={page}&perPage={perpage}&serviceKey=U7TCyPP1H%2FdN%2FNSqmby2ep6u9Mp2IJ%2BymK4QhmZ%2FxkX7C4%2BIHA%2BCdHYHsGXEkIFvf%2FzYC4lwD1X02l0RC3d4nA%3D%3D")
pro_data_list = []
pro_line_list = []

#데이터 받아오기
def get_data(page,perpage):
    page = page
    perpage = perpage
    url = (f"https://api.odcloud.kr/api/socialEnterpriseList/v1/authCompanyList?page={page}&perPage={perpage}&serviceKey=U7TCyPP1H%2FdN%2FNSqmby2ep6u9Mp2IJ%2BymK4QhmZ%2FxkX7C4%2BIHA%2BCdHYHsGXEkIFvf%2FzYC4lwD1X02l0RC3d4nA%3D%3D")
    response = requests.get(url)
    data = json.loads(response.text)

    for i in range(perpage):
        pro_data = data.get("data")[i].get("entNmV")
        pro_data_list.append([pro_data])
        
#파일에 데이터 저장
def save_data(filename,index):
    file = open(filename,'w',newline='')
    writer = csv.writer(file)
    writer.writerows(index)

# (주),(유) 등 필요 없는거 날리기
def pro_name(filename):
    file = open(filename,'r')
    reader = csv.reader(file)
    for line in reader:
        pro_line = line[0].replace("㈜","").replace("(주)","").replace(" ","").replace("(유)","").replace("(사)","").replace("유)","").replace("(사단)","").replace("주)","").replace("(사단법인)","")
        pro_line_list.append([pro_line])

# for i in range(1000):
#     get_data(i,10)
#     print(pro_data_list)
#     save_data("raw_name_data.csv",pro_data_list)

file = open("raw_name_data.csv",'r')
reader = csv.reader(file)

pro_name("raw_name_data.csv")
save_data("pro_name_data.csv",pro_line_list)