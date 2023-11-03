from pages.home_page import HomePage
from pages.tensor_page import TensorPage


def test_click_contacts(browser):
    page = HomePage(browser)
    page.get()
    contacts = page.get_block_contacts()
    print(contacts)
    if contacts:
        page.click_element(contacts)
        assert page.get_current_url().find('https://sbis.ru/contacts') != -1, "Раздел контакты не открылся"
    else:
        assert contacts, 'Раздел контакты не найден'


def test_click_image_tensor(browser):
    page = HomePage(browser)
    tensor_img = page.get_tensor_image()
    if tensor_img:
        page.clinck_link_new_window(tensor_img)
        assert page.get_current_url() == 'https://tensor.ru/', 'Страница https://tensor.ru/ не открылась'
    else:
        assert tensor_img, 'Картинка не найдена'


def test_tensor_syte(browser):
    tensor_page = TensorPage(browser)
    assert tensor_page.find_force_people(), 'Блок "Сила в людях" не найден'

    about_tensor = tensor_page.get_about_tensor()
    tensor_page.click_element(about_tensor)
    # time.sleep(10)
    assert tensor_page.get_current_url() == 'https://tensor.ru/about', 'Раздел https://tensor.ru/about не открылся {}'.format(
        tensor_page.get_current_url())


def test_tensor_about(browser):
    about_page = TensorPage(browser)
    title_about = about_page.find_working_title()
    assert title_about, 'Раздел работаем не найден'

    picture_size = about_page.checking_size_images()
    assert len(set(picture_size)) == 1, "Размеры картинок не одинаковые"
