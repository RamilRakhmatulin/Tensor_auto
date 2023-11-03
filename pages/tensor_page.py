from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TensorLocator(object):
    BLOCK_FORCE_PEOPLE = (By.XPATH, "//*[contains(text(), 'Сила в людях')]")
    ABOUT_TENSOR = (By.XPATH, "//*[contains(text(), 'Сила в людях')]//..//a[@href='/about']")
    WORKING_LOC = (By.XPATH, "//*[contains(text(), 'Работаем')]")
    IMAGE_BLOCK = (By.XPATH, "//*[contains(text(), 'Работаем')]//..//..//img")


class TensorPage(BasePage):
    def find_force_people(self):
        return self.find_element(TensorLocator.BLOCK_FORCE_PEOPLE)

    def get_about_tensor(self):
        # self.signboard_del()
        element = self.find_element(TensorLocator.ABOUT_TENSOR)
        self.scroll_element(element, 0, 300)
        return element

    def find_working_title(self):
        element = self.find_element(TensorLocator.WORKING_LOC)
        self.scroll_element(element, 0, 500)
        return element

    def checking_size_images(self):
        pictures = self.find_elements(TensorLocator.IMAGE_BLOCK)
        if not pictures:
            return []
        picture_size = []
        for picture in pictures:
            picture_size.append((picture.size['width'], picture.size['height']))
        return picture_size
