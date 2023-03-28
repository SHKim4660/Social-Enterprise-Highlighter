import requests
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, dump, ElementTree
import pprint

page = 1
url = (f"https://api.odcloud.kr/api/socialEnterpriseList/v1/authCompanyList?page{page}=&perPage=10&serviceKey=U7TCyPP1H%2FdN%2FNSqmby2ep6u9Mp2IJ%2BymK4QhmZ%2FxkX7C4%2BIHA%2BCdHYHsGXEkIFvf%2FzYC4lwD1X02l0RC3d4nA%3D%3D")

response = requests.get(url)
data = response.text

print(data)

