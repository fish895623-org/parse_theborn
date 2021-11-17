import sys

from src.geocoding import create_longlat_dict
from src.geocoding import request_geocoding
from src.scraper import scrapping_franchise

if __name__ == "__main__":
    data = scrapping_franchise()
    for key, value in data.items():
        longlat = request_geocoding(key=sys.argv[1], secret_key=sys.argv[2], query=value)
        # longlat_data = create_longlat_dict(store=key, x=longlat["addresses"][0]["x"], y=longlat["addresses"][0]['y'])
