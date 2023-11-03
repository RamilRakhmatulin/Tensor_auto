import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='module')
def browser():
    dir = os.path.abspath('chromedriver.exe')
    service = Service(executable_path=dir)
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": dir.replace(os.path.basename('chromedriver.exe'), ''),
             "download.prompt_for_download": False,
             "safebrowsing.enabled": True}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options, service=service)
    yield driver
    driver.quit()
