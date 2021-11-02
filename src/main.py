from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()

options.add_argument("no-sandbox")
options.add_argument("window-size=1920x1080")
options.add_argument("lang=ko_KR")
options.add_argument("log-level=3")
# options.add_argument("headless")

driver = webdriver.Chrome("chromedriver.exe", options=options)
driver.get("https://www.theborn.co.kr/store/domestic-store/")

select = Select(driver.find_element_by_xpath('//*[@id="select_brand"]'))
select.select_by_value("홍콩반점0410")
try:
    while True:
        sleep(1)
        driver.find_element_by_xpath("//i[@class='fa fa-angle-right']").click()
        sleep(1)
        elements = driver.find_elements_by_css_selector(
            "#store_list > div > ul > li:nth-child(3)"
        )
        address = driver.find_elements_by_css_selector(
            "#store_list > div > ul > li:nth-child(4)"
        )
        for element in elements:
            print(element.text)

except NoSuchElementException:
    print("finished")


driver.close()
