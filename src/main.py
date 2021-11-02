import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()

options.add_argument("no-sandbox")
options.add_argument("window-size=1920x1080")
options.add_argument("lang=ko_KR")
options.add_argument("log-level=3")

driver = webdriver.Chrome("chromedriver.exe", options=options)
driver.get("https://www.theborn.co.kr/store/domestic-store/")

select = Select(driver.find_element_by_xpath('//*[@id="select_brand"]'))
select.select_by_value("홍콩반점0410")
time.sleep(1)
driver.find_element_by_css_selector("#pagination > li:nth-child(6) > i").click()

driver.quit()
