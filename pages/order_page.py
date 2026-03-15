from pages.base_page import BasePage
from locators import OrderPageLocators
import allure


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators

    @allure.step("Заполнить форму 'Для кого самокат' данными: {data}")
    def fill_customer_form(self, data):
        self.input_text(self.locators.NAME_INPUT, data["name"])
        self.input_text(self.locators.SURNAME_INPUT, data["surname"])
        self.input_text(self.locators.ADDRESS_INPUT, data["address"])

        self.click_element(self.locators.METRO_STATION_INPUT)
        metro_option = self.find_element(self.locators.METRO_STATION_OPTION)
        metro_option.click()

        self.input_text(self.locators.PHONE_INPUT, data["phone"])

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.click_element(self.locators.NEXT_BUTTON)

    @allure.step("Заполнить форму 'Про аренду' данными: {data}")
    def fill_rental_form(self, data):
        self.input_text(self.locators.DATE_INPUT, data["date"])
        self.click_element(self.locators.RENTAL_PERIOD_DROPDOWN)
        period_options = self.find_elements(self.locators.RENTAL_PERIOD_OPTION)
        for option in period_options:
            if data["rental_period"] in option.text.lower():
                option.click()
                break

        if data["color"] == "black":
            self.click_element(self.locators.COLOR_CHECKBOX_BLACK)
        elif data["color"] == "grey":
            self.click_element(self.locators.COLOR_CHECKBOX_GREY)

        self.input_text(self.locators.COMMENT_INPUT, data["comment"])

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self):
        self.click_element(self.locators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ в модальном окне")
    def confirm_order(self):
        self.click_element(self.locators.CONFIRM_ORDER_BUTTON)

    @allure.step("Проверить, что появилось сообщение об успешном создании заказа")
    def is_success_modal_displayed(self):
        return self.find_element(self.locators.SUCCESS_MODAL).is_displayed()

    @allure.step("Выполнить полный флоу заказа с указанной точкой входа")
    def create_order(self, order_data, entry_point_function):
        entry_point_function()
        self.fill_customer_form(order_data)
        self.click_next_button()
        self.fill_rental_form(order_data)
        self.click_order_button()
        self.confirm_order()
        return self.is_success_modal_displayed()
