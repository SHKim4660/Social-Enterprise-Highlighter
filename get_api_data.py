import requests
import json
import csv

# "사회적기업정보" , "\data\raw_name_data.csv"
# "K-RE100참여기업" , "\data\raw_KRE_data.csv"

pro_data_list = []

#데이터 받아오기
def get_data(dataname,page,perpage):
    pro_data_list = []
    try:
        if dataname == "사회적기업정보":
         url = (f"https://api.odcloud.kr/api/socialEnterpriseList/v1/authCompanyList?page={page}&perPage={perpage}&serviceKey=U7TCyPP1H%2FdN%2FNSqmby2ep6u9Mp2IJ%2BymK4QhmZ%2FxkX7C4%2BIHA%2BCdHYHsGXEkIFvf%2FzYC4lwD1X02l0RC3d4nA%3D%3D")
         response = requests.get(url)
         data = json.loads(response.text)
         # return data
         for i in range(perpage):
              pro_data = data.get("data")[i].get("entNmV")
              pro_data_list.append([pro_data])
              
         save_data("data\\raw_name_data.csv",pro_data_list)
         print(pro_data_list)
    
        if dataname == "K-RE100참여기업":
         url = (f"https://apis.data.go.kr/B553530/RENEWABLE/ENTE_LIST?serviceKey=U7TCyPP1H%2FdN%2FNSqmby2ep6u9Mp2IJ%2BymK4QhmZ%2FxkX7C4%2BIHA%2BCdHYHsGXEkIFvf%2FzYC4lwD1X02l0RC3d4nA%3D%3D&pageNo={page}&numOfRows={perpage}&apiType=json")
         response = requests.get(url)
         data = json.loads(response.content)
         # print(data.get("opentable").get("field")[i].get("ENTE_TERM"))
         # return data

         for i in range(perpage):
               pro_data = data.get("opentable").get("field")[i].get("ENTE_TERM")
               pro_data_list.append([pro_data])

         save_data("data\\raw_KRE_data.csv",pro_data_list)
         print(pro_data_list)
    except(IndexError,TypeError):pass
        
#파일에 데이터 저장
def save_data(filename,index):
    file = open(filename,'a',newline='')
    writer = csv.writer(file)
    writer.writerows(index)

for i in range(3300):
    get_data("사회적기업정보",i,1)
for i in range(230): 
    get_data("K-RE100참여기업",i,1)
