import time

from selenium import webdriver

driver = webdriver.Edge(executable_path="C:\Program Files\msedgedriver.exe")

driver.maximize_window()

driver.get("https://www.mercurytravels.co.in/flights")

c=driver.find_element_by_xpath("//*[@id='left-search']/div[1]/div/label[2]/input")
print(c.is_selected())
driver.find_element_by_xpath("//*[@id='left-search']/div[1]/div/label[2]/input").click()

driver.find_element_by_xpath("//*[@id='O-R-Trip']/div[1]/div[1]/input").send_keys("HYD")

driver.find_element_by_xpath("//*[@id='O-R-Trip']/div[1]/div[2]/input").send_keys("BLR")
driver.find_element_by_xpath("//*[@id='dpf1']").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[16]/div[1]/table/thead/tr[1]/th[2]").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[16]/div[2]/table/tbody/tr/td/span[11]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='dpf2']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='O-R-Trip']/div[3]/div[4]/select/option[3]").click()
driver.find
#send_keys("Business Class")
#driver.find_element_by_xpath("/html/body/div[17]/div[1]/table/thead/tr[1]/th[2]").click()
#time.sleep(3)
#driver.find_element_by_xpath("/html/body/div[17]/div[2]/table/tbody/tr/td/span[11]").click()
#time.sleep(3)
#driver.find_element_by_xpath("//*[@id='dpf2']").click()
#time.sleep(3)
#driver.find_element_by_xpath("/html/body/div[17]/div[1]/table/tbody/tr[2]/td[5]").click()



#driver.find_element_by_name("departDate").send_keys("10/11/2021")
#driver.find_element_by_id("returnDate").send_keys("21/11/2021")


#driver.find_element_by_xpath("//*[@id='searchFlightsBtn']").click()