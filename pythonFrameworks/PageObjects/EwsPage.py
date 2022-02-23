from selenium.webdriver.common.by import By


class EwsPage:

    Title = (By.CSS_SELECTOR, "strong.product")
    ConfigPage = (By.ID, "InternalPages_Index_ConfigurationPage")
    Fw_datecodeTitle = (By.ID, "FirmwareDatecodeTitle")
    Fw_datecode = (By.ID, "FirmwareDatecode")
    FirmwareRevisionTitle =(By.ID, "FirmwareRevisionTitle")
    FirmwareRevision = (By.ID, "FirmwareRevision")


    def __init__(self,driver):
        self.driver=driver


    def Title_Page(self):
        return self.driver.find_element(*EwsPage.Title)

    def Config_Page(self):
        return self.driver.find_element(*EwsPage.ConfigPage)

    def Fw_datecode_Title(self):
        return self.driver.find_element(*EwsPage.Fw_datecodeTitle)

    def Fw_date_code(self):
        return self.driver.find_element(*EwsPage.Fw_datecode)

    def Firmware_RevisionTitle(self):
        return self.driver.find_element(*EwsPage.FirmwareRevisionTitle)
    def Firmware_Revision(self):
        return self.driver.find_element(*EwsPage.FirmwareRevision)
