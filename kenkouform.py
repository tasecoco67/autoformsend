import ibm_db
import ibm_db_dbi
import setting

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()


#driver.get("https://www.u-tokyo.ac.jp/ja/general/healthcheck.html")
driver.get(setting.URL)
driver.implicitly_wait(10)
#driver.find_element_by_xpath(r"//*[@id='content']/div[2]/div[1]/div/div/div[1]/a").click()
driver.find_element_by_xpath(r"//*[@id='i0116']").send_keys(setting.MAIL)
driver.find_element_by_xpath(r"//*[@id='idSIButton9']").click()
driver.find_element_by_xpath(r"//*[@id='passwordInput']").send_keys(setting.PSW)
driver.find_element_by_xpath(r"//*[@id='submitButton']").click()
driver.find_element_by_xpath(r"//*[@id='idBtn_Back']").click()
time.sleep(5)
driver.find_element_by_xpath(setting.ADD).click()
import datetime
weekday = datetime.date.today().weekday()
if str(weekday) == "0"or"1"or"2"or"3"or"4":
    driver.find_element_by_xpath(setting.AREA).click()
driver.find_element_by_class_name('office-form-question-textbox').send_keys(setting.TARGET)
driver.find_element_by_xpath(setting.TEMP).click()
time.sleep(5)
driver.find_element_by_xpath("//input[@value='いいえ／No']").click()
#//*[@id="form-container"]/div/div/div/div/div[3]/div[3]/div[1]/button/div
