import time

from selenium.webdriver.support.select import Select

from Pageobjects.ShopPage import ShopItems
from Utilities.BaseClass import BaseClass


class main(BaseClass):

    def test_endtoend(self):
        home_Page = ShopItems(self.driver)
        home_Page.Name_Page().send_keys("Jakke Bharath Kumar")
        time.sleep(3)
        home_Page.Email_Page().send_keys("jakkebharath@gmail.com")
        time.sleep(3)
        home_Page.Password_Page().send_keys("Bharath@@2022")
        time.sleep(3)
        home_Page.CheckBox_Page().click()
        time.sleep(3)
        c=Select(home_Page.Gender_Page())
        c.select_by_visible_text("Female")
        time.sleep(3)
        home_Page.RadioButton_Page().click()
        time.sleep(3)
        home_Page.Button_Page().click().click()
        c= home_Page.alert_Page().text
        print(c)
