from src.geocoding import *
from src.scraper import *

if __name__ == "__main__":
    data = scrapping_franchise()
    longlat_dict = []
    # data = {"aaaa": "부산 수영구 수영로 480", "bbbb": "부산 수영구 수영로 481"}
    for key, value in data.items():
        longlat = request_geocoding(key=sys.argv[1], secret_key=sys.argv[2], query=value)
        longlat_dict.append({"key": key, "x": longlat["addresses"][0]['x'], "y": longlat["addresses"][0]['y']})
