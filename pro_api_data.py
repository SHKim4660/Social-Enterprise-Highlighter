import requests
import json
pageNo = 1
numOfRows = 10

url = 'http://apis.data.go.kr/B553530/RENEWABLE/ENTE_LIST'
params ={'serviceKey' : 'U7TCyPP1H/dN/NSqmby2ep6u9Mp2IJ+ymK4QhmZ/xkX7C4+IHA+CdHYHsGXEkIFvf/zYC4lwD1X02l0RC3d4nA==', 'pageNo' : {pageNo}, 'numOfRows' : {numOfRows}, 'apiType' : 'json'}

response = requests.get(url, params=params)
data = json.loads(response.text)

for i in range(numOfRows):
    print(data.get("opentable").get("field")[i].get("ENTE_TERM"))

# (주),(유) 등 필요 없는거 날리기
def pro_name(filename):
    file = open(filename,'r')
    reader = csv.reader(file)
    for line in reader:
        pro_line = line[0].replace("㈜","").replace("(주)","").replace(" ","").replace("(유)","").replace("(사)","").replace("유)","").replace("(사단)","").replace("주)","").replace("(사단법인)","")
        pro_line_list.append([pro_line])