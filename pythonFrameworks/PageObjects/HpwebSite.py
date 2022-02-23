from selenium.webdriver.common.by import By

class HpwebSite:
    Driver = (By.XPATH, "//*[@id='id_3']/ul/li[3]/a")
    Printer = (By.CSS_SELECTOR,"div.product-type-text")
    Printer_Name = (By.ID,"search-input-pfinder")
    Button = (By.CSS_SELECTOR,"div.findButton  button")
    Firmware = (By.CSS_SELECTOR,"a.firmware")
    Link = (By.XPATH,"//*[@id='mp-276693-1']/table/tbody/tr[1]/td[1]/div[2]/p")
    Titile = (By.XPATH,"//*[@id='details-mp-276693-1']/div[1]/div[2]/p[1]")
    DateCode = (By.XPATH,"//*[@id='details-mp-276693-1']/div[1]/div[2]/p[2]")
    Download = (By.XPATH,"//*[@id='mp-276693-1']/table/tbody/tr[1]/td[5]/a")

    def __init__(self,driver):
        self.driver = driver

    def Driver_Page(self):
        return self.driver.find_element(*HpwebSite.Driver)

    def Printer_Page(self):
        return self.driver.find_element(*HpwebSite.Printer)

    def Printer_Name_Page(self):
        return self.driver.find_element(*HpwebSite.Printer_Name)

    def Button_Page(self):
        return self.driver.find_element(*HpwebSite.Button)

    def Firmware_Page(self):
        return self.driver.find_element(*HpwebSite.Firmware)

    def Link_Page(self):
        return self.driver.find_element(*HpwebSite.Link)

    def Titile_Page(self):
        return self.driver.find_element(*HpwebSite.Titile)

    def DateCode_Page(self):
        return self.driver.find_element(*HpwebSite.DateCode)

    def Download_Page(self):
        return self.driver.find_element(*HpwebSite.Download)
