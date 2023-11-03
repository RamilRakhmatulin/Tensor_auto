import time
from pages.home_page import HomePage


def test_click_contacts(browser):
    page = HomePage(browser)
    page.get()
    contacts = page.get_block_contacts()
    if contacts:
        page.click_element(contacts)
        assert page.get_current_url().find('https://sbis.ru/contacts') != -1, "Раздел контакты не открылся"
    else:
        assert contacts, 'Раздел контакты не найден'


def test_region(browser):
    page = HomePage(browser)
    region = page.get_region()
    assert region, 'Регион не найден'
    assert region.text == 'Республика Татарстан', 'Регион не совпадает с республикой Татарстан'


def test_partners(browser):
    page = HomePage(browser)
    assert len(page.get_partners()) > 0, 'Список партнеров не найден'


def test_select_region(browser):
    page = HomePage(browser)
    region = page.get_region()
    if region:
        page.click_element(region)
        browser.implicitly_wait(2)
        assert page.select_region_camchatka(), 'Регион камчатка не найден'
    else:
        assert region, 'Регион не найден'


def test_url_region_partners_camchatka(browser):
    page = HomePage(browser)
    time.sleep(2)
    assert page.get_current_url().find('41-kamchatskij-kraj') != -1, 'Ссылка на страницу не изменилась {}'.format(
        page.get_current_url())
    assert page.get_title() == 'СБИС Контакты — Камчатский край', 'Заголовок не совпадает с "СБИС Контакты — Камчатский край" '
    region = page.get_region()
    assert region.text == 'Камчатский край', 'Регион не совпадает с Камчатским Краем'
    assert len(page.get_partners()) > 0, 'Список партнеров региона Камчатский край не найден'
    city_partner = page.get_cyti_partner()
    if city_partner:
        assert city_partner.text == 'Петропавловск-Камчатский', 'Город партнера не совпадает с Петропавловским-Камчатским'
    else:
        assert city_partner, 'Город партнера не найден'
