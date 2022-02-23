import time

from PageObjects.HpwebSite import HpwebSite
from PageObjects.confirmationPage import ConfirmationPage
from Utilities.BaseClass import BaseClass

class TestOne(BaseClass):


    def test_end2end(self):
        list = []
        confirmation_Page= ConfirmationPage(self.driver)
        confirmation_Page.LinkItem_Page().click()
        #self.driver.find_element_by_id("details-button").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,document.body.ScrollHeight)")
        time.sleep(3)
        home_page=confirmation_Page.ScrollDown_Page()
        #self.driver.find_element_by_css_selector("a.small-link").click()
        time.sleep(3)

        #list.append(self.driver.find_element_by_css_selector("strong.product").text)
        list.append(home_page.Title_Page().text)
        print(list)
        print(self.driver.title)
        home_page.Config_Page().click()
        #self.driver.find_element_by_id("InternalPages_Index_ConfigurationPage").click()
        #print(self.driver.find_element_by_id("FirmwareDatecodeTitle").text)
        print(home_page.Fw_datecode_Title().text)
        #c = self.driver.find_element_by_id("FirmwareDatecode").text
        c = home_page.Fw_date_code().text
        print("FirmwareDatecode = ", c)
        print(home_page.Firmware_Revision().text)
        #print(self.driver.find_element_by_id("FirmwareRevisionTitle").text)
        #d = self.driver.find_element_by_id("FirmwareRevision").text
        d=home_page.Firmware_Revision().text
        print("FirmwareDatecode = ", d)
        time.sleep(3)

        self.driver.get("https://www.hp.com/us-en/home.html")
        time.sleep(1)
        Hphome_Page = HpwebSite(self.driver)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        Hphome_Page.Driver_Page().click()
        #self.driver.find_element_by_xpath("//*[@id='id_3']/ul/li[3]/a").click()
        time.sleep(3)
        Hphome_Page.Printer_Page().click()
        #self.driver.find_element_by_css_selector("div.product-type-text").click()
        time.sleep(3)
        print(c)
        b=list[0]
        print(b)
        Hphome_Page.Printer_Name_Page().send_keys(b)
        #self.driver.find_element_by_id("search-input-pfinder").send_keys(list[0])
        time.sleep(3)
        Hphome_Page.Button_Page().click()
        #self.driver.find_element_by_css_selector("div.findButton  button ").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,500)")
        time.sleep(3)
        Hphome_Page.Firmware_Page().click()
        #self.driver.find_element_by_css_selector("a.firmware").click()
        Hphome_Page.Link_Page().click()
        #self.driver.find_element_by_xpath("//*[@id='mp-276693-1']/table/tbody/tr[1]/td[1]/div[2]/p").click()
        k = Hphome_Page.Titile_Page()
        #k = self.driver.find_element_by_xpath("//*[@id='details-mp-276693-1']/div[1]/div[2]/p[1]")
        print(k.text)
        J= Hphome_Page.DateCode_Page().text
        #J = self.driver.find_element_by_xpath("//*[@id='details-mp-276693-1']/div[1]/div[2]/p[2]").text
        print("Version is ", J)
        print(d)
        if J != d:
            Hphome_Page.Download_Page().click()
            #self.driver.find_element_by_xpath("//*[@id='mp-276693-1']/table/tbody/tr[1]/td[5]/a").click()
        print("end")