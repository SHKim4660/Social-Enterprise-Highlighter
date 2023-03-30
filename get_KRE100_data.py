import requests

url = 'http://apis.data.go.kr/B553530/RENEWABLE/ENTE_LIST'
params ={'serviceKey' : '서비스키', 'pageNo' : '1', 'numOfRows' : '10', 'apiType' : 'xml', 'q1' : 'kea공단', 'q2' : '2021', 'q3' : '2050' }

response = requests.get(url, params=params)
print(response.content)