import pandas as pd

m = pd.read_excel("address.xlsx")

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

# print(jsonResponse["meta"])

# 데이터 로드하기
print(jsonResponse["documents"][0]["road_address"])