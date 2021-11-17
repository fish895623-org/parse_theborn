import requests


def request_geocoding(key: str, secret_key: str, query: str) -> str:
    headers = {
        "X-NCP-APIGW-API-KEY-ID": key,
        "X-NCP-APIGW-API-KEY": secret_key,
    }
    params = {"query": query}
    response = requests.get(
        url="https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode",
        headers=headers,
        params=params,
    )
    return response.text


def create_longlat_dict(store: str, x: str, y: str) -> dict:
    data = []

    return data
