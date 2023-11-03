import os
import re
import time
from pages.sbis_page import SbisPage


def test_footer(browser):
    page = SbisPage(browser)
    page.get()
    footer = page.get_footer_download()
    if footer:
        page.click_element(footer)
        assert page.get_current_url() == 'https://sbis.ru/download?tab=ereport&innerTab=ereport25', "Страница с файлами загрузки не открылась"
    else:
        assert footer, "Раздела Скачать СБИС в Footer'e нет"


def test_sbis_plugin(browser):
    page = SbisPage(browser)
    plagin_page = page.get_plagin_button()
    if plagin_page:
        page.click_element(plagin_page)
        time.sleep(5)
        assert page.get_current_url().find(
            'https://sbis.ru/download?tab=plugin&inner') != -1, 'Страница с плагинами не открылась'
        assert page.get_current_url() == 'https://sbis.ru/download?tab=plugin&innerTab=default' or page.get_current_url() == 'https://sbis.ru/download?tab=plugin&innerTab=windows', 'Не откралвсь страница для Windows'
    else:
        assert plagin_page, 'Раздел "Сбис Плагин не найден"'


def test_download(browser):
    page = SbisPage(browser)
    download_button = page.get_download_button()
    assert download_button, 'Ссылка скачевания файла веб установщика не найдена'
    name_file_download = download_button.text
    size_on_site = ''.join(re.findall(r'[0-9.]', name_file_download))
    SbisPage.size_file_download = float(size_on_site)
    page.click_element(download_button)
    dir = os.path.abspath(__file__).replace(os.path.basename(__file__), '')
    browser.get("chrome://downloads/")
    time.sleep(2)
    while any([filename.endswith(".crdownload") for filename in os.listdir(dir)]):
        time.sleep(2)
        print(".", end="")
    print('\ndone')


def test_after_download(browser):
    page = SbisPage(browser)
    file_downler = 'sbisplugin-setup-web.exe'
    assert os.path.isfile(file_downler), "Файл с плагином не найден в папке скрипта"
    file_size = round(os.path.getsize(os.path.abspath(file_downler)) / (2 ** 20), 2)
    assert file_size == SbisPage.size_file_download, "Размер файла не совпадает с размером указанным на сайте"
    # print("File Size is :", os.path.getsize(os.path.abspath(file_downler))/(2**20) , "MB")
