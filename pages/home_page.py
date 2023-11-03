from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class HomeLocator(object):
    CONTACTS_LOC = (By.LINK_TEXT, "Контакты")
    TENSOR_IMG = (By.XPATH, "//img[@alt='Разработчик системы СБИС — компания «Тензор»']")
    REGION_LOC = (By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
    PARTNERS_LOC = (By.CLASS_NAME, "sbisru-Contacts-List__col-1")
    CAMCHATKA_REG = (By.XPATH, "//div//li//span[@title='Камчатский край']")
    CITY_PARTNER = (By.XPATH, "//div[@id='city-id-2']")


class HomePage(BasePage):
    def __init__(self, driver):
        self.start_url = 'https://sbis.ru/'
        super().__init__(driver, self.start_url)

    def get_block_contacts(self):
        return self.find_element(HomeLocator.CONTACTS_LOC)

    def get_tensor_image(self):
        return self.find_element(HomeLocator.TENSOR_IMG)

    def get_region(self):
        return self.find_element(HomeLocator.REGION_LOC)

    def get_partners(self):
        try:
            partners = self.find_elements(HomeLocator.PARTNERS_LOC)
            for partner in partners:
                self.scroll_element(partner, 10)
            return partners
        except:
            return []

    def select_region_camchatka(self):
        sel_region = self.find_element(HomeLocator.CAMCHATKA_REG)
        if sel_region:
            self.click_element(sel_region)
            return True
        else:
            return sel_region

    def get_cyti_partner(self):
        return self.find_element(HomeLocator.CITY_PARTNER)
