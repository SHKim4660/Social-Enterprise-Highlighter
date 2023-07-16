import requests
import json
import csv
import re
import os


def get_data(name,page,perpage):
    data_list = []
    pattern = r'\([^)]*\)'
    try:
        if name == "사회적기업정보":
            url = (f"https://api.odcloud.kr/api/socialEnterpriseList/v1/authCompanyList?page={page}&perPage={perpage}&serviceKey=U7TCyPP1H%2FdN%2FNSqmby2ep6u9Mp2IJ%2BymK4QhmZ%2FxkX7C4%2BIHA%2BCdHYHsGXEkIFvf%2FzYC4lwD1X02l0RC3d4nA%3D%3D")
            api_response = requests.get(url)
            api_data = json.loads(api_response.text)
            for i in range(perpage):
                 raw_data = api_data.get("data")[i].get("entNmV")  # 데이터를 받아와서 리스트 형태로 취합
                 pro_data = re.sub(pattern=pattern, repl='', string= raw_data).replace("㈜","").replace("유)","").replace("주)","").replace("사)","").replace(" ","").replace("주식회사","").replace("사단법인","")
                 pro_pro_data = f"{pro_data}0"
                 data_list.append([pro_pro_data])
              
            save_data(os.path.join('data', 'data.csv'),data_list) # 데이터를 csv파일 평태로 저장
            print(data_list)
        
        if name == "K-RE100참여기업":
            url = (f"https://apis.data.go.kr/B553530/RENEWABLE/ENTE_LIST?serviceKey=U7TCyPP1H%2FdN%2FNSqmby2ep6u9Mp2IJ%2BymK4QhmZ%2FxkX7C4%2BIHA%2BCdHYHsGXEkIFvf%2FzYC4lwD1X02l0RC3d4nA%3D%3D&pageNo={page}&numOfRows={perpage}&apiType=json")
            api_response = requests.get(url)
            api_data = json.loads(api_response.content)
            for i in range(perpage):
                 raw_data = api_data.get("opentable").get("field")[i].get("ENTE_TERM")  # 데이터를 받아와서 리스트 형태로 취합
                 pro_data = re.sub(pattern=pattern, repl='', string= raw_data).replace("㈜","").replace("유)","").replace("주)","").replace("사)","").replace(" ","").replace("주식회사","").replace("사단법인","")
                 pro_pro_data = f"{pro_data}1"
                 data_list.append([pro_pro_data])

            save_data(os.path.join('data', 'data.csv'),data_list)  # 데이터를 csv파일 평태로 저장
            print(data_list)

    except(IndexError,TypeError):print(name,"ERROR!!!!!!!")

#파일에 데이터 저장
def save_data(filename,index):
    file = open(filename,'a',newline='')
    writer = csv.writer(file)
    writer.writerows(index)


#실행 코드
print("-------------------------사회적기업정보-------------------------")
for i in range(3500):
    get_data("사회적기업정보",i,1)
print("------------------------K-RE100 참여기업------------------------")
for i in range(300): 
    get_data("K-RE100참여기업",i,1)