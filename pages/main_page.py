from pages.base_page import BasePage
from locators import MainPageLocators
import allure

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators

    @allure.step("Принять куки")
    def accept_cookies(self):
        self.click_element(self.locators.COOKIE_ACCEPT_BUTTON)

    @allure.step("Получить список всех вопросов в FAQ")
    def get_faq_questions(self):
        items = self.find_elements(self.locators.FAQ_ACCORDION_ITEM)
        questions = []
        for item in items:
            question_element = item.find_element(*self.locators.FAQ_QUESTION_BUTTON)
            questions.append(question_element.text)
        return questions

    @allure.step("Кликнуть на вопрос '{question_text}'")
    def click_faq_question_by_text(self, question_text):
        items = self.find_elements(self.locators.FAQ_ACCORDION_ITEM)
        for item in items:
            question_element = item.find_element(*self.locators.FAQ_QUESTION_BUTTON)
            if question_element.text == question_text:
                question_element.click()
                return
        raise AssertionError(f"Вопрос с текстом '{question_text}' не найден на странице")

    @allure.step("Получить текст ответа на вопрос '{question_text}'")
    def get_faq_answer_text_by_question(self, question_text):
        items = self.find_elements(self.locators.FAQ_ACCORDION_ITEM)
        for item in items:
            question_element = item.find_element(*self.locators.FAQ_QUESTION_BUTTON)
            if question_element.text == question_text:
                # Кликаем, чтобы открыть ответ (если он еще закрыт)
                question_element.click()
                answer_element = item.find_element(*self.locators.FAQ_ANSWER_PANEL)
                return answer_element.text
        raise AssertionError(f"Вопрос с текстом '{question_text}' не найден на странице")

    @allure.step("Нажать на кнопку 'Заказать' в хедере")
    def click_order_button_header(self):
        self.click_element(self.locators.ORDER_BUTTON_HEADER)

    @allure.step("Нажать на кнопку 'Заказать' в середине страницы")
    def click_order_button_middle(self):
        self.click_element(self.locators.ORDER_BUTTON_MIDDLE)

    @allure.step("Нажать на логотип 'Самокат'")
    def click_scooter_logo(self):
        self.click_element(self.locators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип 'Яндекс'")
    def click_yandex_logo(self):
        self.click_element(self.locators.YANDEX_LOGO)
