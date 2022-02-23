from selenium.webdriver.common.by import By

from PageObjects.EwsPage import EwsPage


class ConfirmationPage:
    Link_item = (By.ID, "details-button")
    ScrollDown = (By.CSS_SELECTOR, "a.small-link")


    def __init__(self,driver):

        self.driver=driver

    def LinkItem_Page(self):
        return self.driver.find_element(*ConfirmationPage.Link_item)

    def ScrollDown_Page(self):
        self.driver.find_element(*ConfirmationPage.ScrollDown).click()
        home_page = EwsPage(self.driver)
        return home_page
