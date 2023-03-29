import requests
import json
import csv
import pandas

# page = 1
# perpage = 10
# url = (f"https://api.odcloud.kr/api/socialEnterpriseList/v1/authCompanyList?page={page}&perPage={perpage}&serviceKey=U7TCyPP1H%2FdN%2FNSqmby2ep6u9Mp2IJ%2BymK4QhmZ%2FxkX7C4%2BIHA%2BCdHYHsGXEkIFvf%2FzYC4lwD1X02l0RC3d4nA%3D%3D")
pro_data_list = []

def get_data(page,perpage):
    page = page
    perpage = perpage
    url = (f"https://api.odcloud.kr/api/socialEnterpriseList/v1/authCompanyList?page={page}&perPage={perpage}&serviceKey=U7TCyPP1H%2FdN%2FNSqmby2ep6u9Mp2IJ%2BymK4QhmZ%2FxkX7C4%2BIHA%2BCdHYHsGXEkIFvf%2FzYC4lwD1X02l0RC3d4nA%3D%3D")
    response = requests.get(url)
    data = json.loads(response.text)

    for i in range(perpage):
        pro_data = data.get("data")[i].get("entNmV")
        pro_data_list.append([pro_data])
        
def save_data(filename):
    file = open(filename,'w',newline='')
    writer = csv.writer(file)
    writer.writerows(pro_data_list)

for i in range(1000):
    get_data(i,10)
    print(pro_data_list)
    save_data("bis_name_data.csv")