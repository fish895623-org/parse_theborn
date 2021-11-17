import requests

# curl -G "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode" \
# --data-urlencode "query={주소}" \
# --data-urlencode "coordinate={검색_중심_좌표}" \
# -H "X-NCP-APIGW-API-KEY-ID: {애플리케이션 등록 시 발급받은 client id값}" \
# -H "X-NCP-APIGW-API-KEY: {애플리케이션 등록 시 발급받은 client secret값}" -v
headers = {"X-NCP-APIGW-API-KEY-ID": "", "X-NCP-APIGW-API-KEY": ""}
params = {"query": "", "coordinate": ""}
a = requests.get(
    url="https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode",
    headers=headers,
    params=params,
)
