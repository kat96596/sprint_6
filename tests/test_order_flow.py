import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.dzen_page import DzenPage
from data import Urls, OrderData


@allure.feature('Заказ самоката')
class TestOrderFlow:

    @allure.title('Позитивный сценарий заказа самоката')
    @allure.description('Тест проверяет полный флоу заказа самоката с разными наборами данных и точками входа')
    @pytest.mark.parametrize('order_data, entry_point', [
        (OrderData.first_order_data, 'header'),
        (OrderData.second_order_data, 'middle')
    ])
    def test_create_order_positive(self, driver, order_data, entry_point):
        main_page = MainPage(driver)
        main_page.driver.get(Urls.BASE_URL)
        main_page.accept_cookies()

        order_page = OrderPage(driver)

        if entry_point == 'header':
            result = order_page.create_order(order_data, main_page.click_order_button_header)
        else:
            result = order_page.create_order(order_data, main_page.click_order_button_middle)

        assert result, "Заказ не был успешно создан"

    @allure.title('Проверка перехода на главную страницу по клику на логотип "Самокат"')
    @allure.description('Тест проверяет, что клик на логотип "Самокат" возвращает на главную страницу')
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.driver.get(Urls.BASE_URL)

        main_page.click_order_button_header()

        order_page = OrderPage(driver)
        order_page.wait_for_element_visible(order_page.NAME_INPUT)

        main_page.click_scooter_logo()

        assert main_page.get_current_url() == Urls.BASE_URL, "Не произошел переход на главную страницу Самоката"

    @allure.title('Проверка перехода на Дзен по клику на логотип "Яндекс"')
    @allure.description('Тест проверяет, что клик на логотип "Яндекс" открывает страницу Дзена в новом окне')
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.driver.get(Urls.BASE_URL)

        main_page.click_yandex_logo()

        main_page.switch_to_new_window()

        dzen_page = DzenPage(driver)
        dzen_page.wait_for_page_load()

        current_url = main_page.get_current_url()
        assert Urls.DZEN_URL in current_url, f"Ожидался переход на Дзен, получен URL: {current_url}"
