import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:\Browser\geckodriver.exe.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("/html/body/header/a[2]").click()
time.sleep(3)
print(driver.title)
print(driver.current_url)
driver.back()
time.sleep(3)
driver.find_element_by_id("openwindow").click()
driver.close()

