import pandas as pd

address = pd.read_excel("address.xlsx")
x = {"x": []}
y = {"y": []}
address = address.append(x, ignore_index=True)
address = address.append(y, ignore_index=True)

print(address)

import requests
import json
url = "https://dapi.kakao.com/v2/local/search/address.json"
apiKey = "8b8cfda77635c6b0e68406c3c307d327"

header = {"Authorization": "KakaoAK " + apiKey}
parameters = {"query" : "경기 과천시 별양로 64(별양동)"}

response = requests.get(url, headers=header, params=parameters)
# print (response)
# print (response.text)
jsonResponse = json.loads(response.text)
# print(json.dumps(jsonResponse, indent=4, ensure_ascii=False))
# print(jsonResponse)

print(jsonResponse["meta"])

# 데이터 로드하기
#{'address_name': '경기 과천시 별양로 64', 'building_name': '3단지병원상가', 'main_building_no': '64', 'region_1depth_name': '경기', 'region_2depth_name': '과천시', 'region_3depth_name': '별양동', 'road_name': '별양로', 'sub_building_no': '', 'underground_yn': 'N',
# 'x': '126.993978608765', 'y': '37.4244751958748', 'zone_no': '13834'}
print(jsonResponse["documents"][0]["road_address"])

alist = address["소재지도로명주소"]

for i in range(0,len(address["소재지도로명주소"])) :
    try :
        parameters = {"query": address["소재지도로명주소"][i]}
        response = requests.get(url, headers=header, params=parameters)
        jsonResponse = json.loads(response.text)
        print("x :", jsonResponse["documents"][0]["road_address"]['x'], "y :",
              jsonResponse["documents"][0]["road_address"]['x'])
        address["x"][i] = jsonResponse["documents"][0]["road_address"]['x']
        address["y"][i] = jsonResponse["documents"][0]["road_address"]['y']
    except:
        continue
    else :
        print("x :", jsonResponse["documents"][0]["road_address"]['x'], "y :",
              jsonResponse["documents"][0]["road_address"]['x'])
        #print("x :",jsonResponse["documents"][0]["road_address"]['x'],"y :",jsonResponse["documents"][0]["road_address"]['x'])
        # address["x"][i] = jsonResponse["documents"][0]["road_address"]['x']
        # address["y"][i] = jsonResponse["documents"][0]["road_address"]['y']

print(address)
address.to_excel(excel_writer='address(x,y).xlsx')