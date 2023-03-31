import requests

url = 'http://apis.data.go.kr/B553530/RENEWABLE/ENTE_LIST'
params ={'serviceKey' : 'U7TCyPP1H/dN/NSqmby2ep6u9Mp2IJ+ymK4QhmZ/xkX7C4+IHA+CdHYHsGXEkIFvf/zYC4lwD1X02l0RC3d4nA==', 'pageNo' : '1', 'numOfRows' : '10', 'apiType' : 'json'}

response = requests.get(url, params=params)
print(response.content)