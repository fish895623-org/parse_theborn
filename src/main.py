from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()

options.add_argument("no-sandbox")
options.add_argument("window-size=1920x1080")
options.add_argument("lang=ko_KR")
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
)

driver = webdriver.Chrome("chromedriver.exe", options=options)
driver.get("https://www.theborn.co.kr/store/domestic-store/")

driver.implicitly_wait(10)
select = Select(driver.find_element_by_xpath('//*[@id="select_brand"]'))
select.select_by_value("홍콩반점0410")
driver.implicitly_wait(10)

driver.find_element_by_xpath('//i[@class="fa fa-angle-right"').click()

driver.get_screenshot_as_file("capture.png")
driver.quit()
