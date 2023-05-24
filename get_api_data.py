import requests
import json
import csv
import os

# "사회적기업정보" , "\data\raw_name_data.csv"
# "K-RE100참여기업" , "\data\raw_KRE_data.csv"

pro_data_list = []

#data.kr에서 api 데이터 받아오기
def get_data(dataname,page,perpage):
    pro_data_list = []
    try:
        if dataname == "사회적기업정보":
         url = (f"https://api.odcloud.kr/api/socialEnterpriseList/v1/authCompanyList?page={page}&perPage={perpage}&serviceKey=U7TCyPP1H%2FdN%2FNSqmby2ep6u9Mp2IJ%2BymK4QhmZ%2FxkX7C4%2BIHA%2BCdHYHsGXEkIFvf%2FzYC4lwD1X02l0RC3d4nA%3D%3D")
         response = requests.get(url)
         data = json.loads(response.text)
         for i in range(perpage):
              pro_data = data.get("data")[i].get("entNmV")  # 데이터를 받아와서 리스트 형태로 취합
              pro_data_list.append([pro_data])
              
         save_data(os.path.join('data', 'raw_name_data.csv'),pro_data_list) # 데이터를 csv파일 평태로 저장
         print(pro_data_list)
    
        if dataname == "K-RE100참여기업":
         url = (f"https://apis.data.go.kr/B553530/RENEWABLE/ENTE_LIST?serviceKey=U7TCyPP1H%2FdN%2FNSqmby2ep6u9Mp2IJ%2BymK4QhmZ%2FxkX7C4%2BIHA%2BCdHYHsGXEkIFvf%2FzYC4lwD1X02l0RC3d4nA%3D%3D&pageNo={page}&numOfRows={perpage}&apiType=json")
         response = requests.get(url)
         data = json.loads(response.content)
         for i in range(perpage):
               pro_data = data.get("opentable").get("field")[i].get("ENTE_TERM")  # 데이터를 받아와서 리스트 형태로 취합
               pro_data_list.append([pro_data])  

         save_data(os.path.join('data', 'raw_KRE_data.csv'),pro_data_list)  # 데이터를 csv파일 평태로 저장
         print(pro_data_list)
    except(IndexError,TypeError):pass
        
#파일에 데이터 저장
def save_data(filename,index):
    file = open(filename,'a',newline='')
    writer = csv.writer(file)
    writer.writerows(index)

#실행 코드
print("-------------------------사회적기업정보-------------------------")
for i in range(3300):
    get_data("사회적기업정보",i,1)
print("------------------------K-RE100 참여기업------------------------")
for i in range(230): 
    get_data("K-RE100참여기업",i,1)
