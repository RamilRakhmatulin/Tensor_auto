from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


class SbisLocator(object):
    FOOTER_LOC = (By.XPATH, "//div[@class='sbisru-Footer sbisru-Header__scheme--default']")
    LINK_DOWN = (By.XPATH, "//li[@class='sbisru-Footer__list-item']//a[text()='Скачать СБИС']")
    PLAGIN_BUT = (By.XPATH, "//div[@class='controls-TabButton__caption' and text()='СБИС Плагин']//..//..")
    DOWNLOAD_BUT = (By.XPATH, "//h3[@class='sbis_ru-DownloadNew-h3' and text()='Веб-установщик ']//..//..//div//div//a")


class SbisPage(BasePage):
    size_file_download = 0

    def __init__(self, driver):
        self.start_url = 'https://sbis.ru/'
        super().__init__(driver, self.start_url)

    def get_footer_download(self):
        download_link = self.find_element(SbisLocator.FOOTER_LOC)
        scroll_orign = ScrollOrigin.from_element(download_link)
        webdriver.ActionChains(self._driver) \
            .scroll_from_origin(scroll_orign, 0, 200) \
            .perform()
        return self.find_element(SbisLocator.LINK_DOWN)

    def get_plagin_button(self):
        return self.find_element(SbisLocator.PLAGIN_BUT)

    def get_download_button(self):
        return self.find_element(SbisLocator.DOWNLOAD_BUT)
