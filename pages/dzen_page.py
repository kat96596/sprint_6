from pages.base_page import BasePage
from locators import DzenPageLocators
import allure


class DzenPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = DzenPageLocators

    @allure.step("Дождаться загрузки главной страницы Дзена")
    def wait_for_page_load(self):
        self.find_element(self.locators.DZEN_MAIN_ELEMENT, time=15)
