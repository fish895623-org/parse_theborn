import sys
from collections import OrderedDict
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select


def scrapping_franchise() -> dict:
    options = webdriver.ChromeOptions()

    options.add_argument("no-sandbox")
    options.add_argument("window-size=1920x1080")
    options.add_argument("lang=ko_KR")
    options.add_argument("log-level=3")
    options.add_argument("headless")

    if sys.platform == "win32":
        driver = webdriver.Chrome("chromedriver.exe", options=options)
    else:
        driver = webdriver.Chrome("chromedriver", options=options)

    driver.get("https://www.theborn.co.kr/store/domestic-store/")

    select = Select(driver.find_element_by_xpath('//*[@id="select_brand"]'))
    select.select_by_value("홍콩반점0410")

    store_name = []
    store_address = []

    try:
        while True:
            sleep(1)
            driver.find_element_by_xpath("//i[@class='fa fa-angle-right']").click()
            sleep(1)
            store = driver.find_elements_by_css_selector(
                "#store_list > div > ul > li:nth-child(3)"
            )
            address = driver.find_elements_by_css_selector(
                "#store_list > div > ul > li:nth-child(4)"
            )
            for element in store:
                store_name.append(element.text)

            for element in address:
                store_address.append(element.text)

    except NoSuchElementException:
        print("finished")

    assert len(store_name) == len(store_address)
    # %%
    data = OrderedDict()
    for i in range(len(store_name)):
        data[store_name[i]] = store_address[i]

    driver.close()
    return data
