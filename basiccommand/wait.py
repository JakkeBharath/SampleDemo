from idlelib import browser

from selenium import webdriver
driver = webdriver.Edge(executable_path="C:\Program Files\msedgedriver.exe")

driver.get("https://www.guru99.com/")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,500)","")
driver.find_element_by_xpath("//*[@id='java_technologies']/li[1]/a").click()
#driver.execute_script("argument[0].scrollIntoView();",technologies)

#driver.execute_script("window.ScrollBy(0,document.body.scrollHeight)")
#browser.execute_script("window.scrollTo(0,300);")


#driver.implicitly_wait(10)
#driver.find_element_by_xpath("//*[@id='post-2669']/div/div[1]/div[1]/div[2]/div/h4").click()

#driver.find_element_by_xpath("//*[@id='gsc-i-id1']").send_keys("sql")
#driver.implicitly_wait(10)

#driver.find_element_by_xpath("//*[@id='___gcse_0']/div/div/form/table/tbody/tr/td[2]").click()