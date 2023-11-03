from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    _driver = None

    def __init__(self, web_driver, url=''):
        self._driver = web_driver
        self.url = url

    def get(self):
        self._driver.get(self.url)

    def get_current_url(self):
        """ Returns current browser URL. """
        return self._driver.current_url

    def get_title(self):
        """ Returns current browser title. """
        return self._driver.title

    def find_element(self, locator, timeout=10, ):
        try:
            return WebDriverWait(self._driver, timeout).until(EC.presence_of_element_located(locator),
                                                              message=f"Can't find element by locator {locator}")
        except:
            return False

    # def find_
    def find_elements(self, locator, timeout=10):
        try:
            return WebDriverWait(self._driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                              message=f"Can't find elements by locator {locator}")
        except:
            return False

    def scroll_element(self, element, x_offset=0, y_offset=0):
        """ scroll the element. """
        webdriver.ActionChains(self._driver) \
            .scroll_to_element(element) \
            .scroll_by_amount(x_offset, y_offset) \
            .perform()

    def click_element(self, element, hold_seconds=0, x_offset=1, y_offset=1):
        """ click the element. """
        action = webdriver.ActionChains(self._driver)
        action.scroll_to_element(element)
        action.move_to_element_with_offset(element, x_offset, y_offset). \
            pause(hold_seconds).click(on_element=element).perform()

    def clinck_link_new_window(self, element):
        original_window = self._driver.current_window_handle
        self.click_element(element)
        WebDriverWait(self._driver, 10).until(EC.number_of_windows_to_be(2))
        for window_handle in self._driver.window_handles:
            if window_handle != original_window:
                self._driver.switch_to.window(window_handle)
                break

    def signboard_del(self):
        alert = self._driver.switch_to.alert
        alert.accept()
