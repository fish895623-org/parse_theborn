import json

# curl -G "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode" \
# --data-urlencode "query={주소}" \
# --data-urlencode "coordinate={검색_중심_좌표}" \
# -H "X-NCP-APIGW-API-KEY-ID: {애플리케이션 등록 시 발급받은 client id값}" \
# -H "X-NCP-APIGW-API-KEY: {애플리케이션 등록 시 발급받은 client secret값}" -v
headers = {"X-NCP-APIGW-API-KEY-ID": "54sc1ydcbt", "X-NCP-APIGW-API-KEY": "ruiLGEgPms9vVlfNr5T6TR5ln5nyNAMkto6qvzlP"}
params = {"query": "경기 안산시 단원구 선부광장북로 36 상가동 210호(선부동, 벽산블루밍아파트)"}


# a = requests.get(
#     url="https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode",
#     headers=headers,
#     params=params,
# )

def parse_json() -> dict:
    with open("sample.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    data = parse_json()
    for key in data:
        print(data[key])