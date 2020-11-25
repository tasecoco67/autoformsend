import setting

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()

driver.get(URL)
time.sleep(2)
driver.find_element_by_xpath(r"//*[@id='i0116']").send_keys(MAIL_ADDRESS)
driver.find_element_by_xpath(r"//*[@id='idSIButton9']").click()
time.sleep(3)
driver.find_element_by_name("Password").send_keys(UTOKYO_PSW)
time.sleep(1)
driver.find_element_by_xpath(r"//*[@id='submitButton']").click()
time.sleep(1)
driver.find_element_by_xpath(r"//*[@id='idBtn_Back']").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@value='ECCSクラウドメール(共通ID@g.ecc.u-tokyo.ac.jp)宛に送信']").click()
import datetime
weekday = datetime.date.today().weekday()
if str(weekday) == "0"or"1"or"2"or"3"or"4":
    driver.find_element_by_xpath("//input[@value='本郷地区／Hongo Area']").click()
driver.find_element_by_class_name('office-form-question-textbox').send_keys(PLACE_NAME)
driver.find_element_by_xpath("//input[@value='37.0度未満／Less than 37.0 degrees Celsius']"
).click()
time.sleep(3)
driver.find_element_by_xpath("//input[@value='いいえ／No']").click()
driver.find_element_by_class_name('office-form-bottom-button').click()
