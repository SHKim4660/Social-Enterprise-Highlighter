import requests
import pprint

headers = {
    'accept': 'application/json',
    'Authorization': ["U7TCyPP1H/dN/NSqmby2ep6u9Mp2IJ+ymK4QhmZ/xkX7C4+IHA+CdHYHsGXEkIFvf/zYC4lwD1X02l0RC3d4nA=="],
    'Content-Type': 'application/json',
	}

params = (
    ('serviceKey', ["U7TCyPP1H/dN/NSqmby2ep6u9Mp2IJ+ymK4QhmZ/xkX7C4+IHA+CdHYHsGXEkIFvf/zYC4lwD1X02l0RC3d4nA=="]),
	)

data = '{ "b_no": [ "1234567890" ]}'

response = requests.post('https://api.odcloud.kr/api/socialEnterpriseList/v1/authCompanyList', headers=headers, params=params, data=data)

pprint.pprint(response.json())