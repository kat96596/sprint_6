import allure
import pytest
from pages.main_page import MainPage
from data import Urls, FaqData


@allure.feature('FAQ')
class TestFaq:

    @allure.title('Проверка текста ответов на вопросы в разделе "Вопросы о важном"')
    @allure.description('Тест проверяет, что при клике на вопрос открывается соответствующий текст ответа')
    @pytest.mark.parametrize('index, expected_data', enumerate(FaqData.questions))
    def test_faq_answer_text(self, driver, index, expected_data):
        main_page = MainPage(driver)
        main_page.driver.get(Urls.BASE_URL)
        main_page.accept_cookies()

        main_page.click_faq_question(index)
        actual_answer = main_page.get_faq_answer_text(index)

        assert expected_data["answer"] in actual_answer, \
            f"Ожидаемый ответ '{expected_data['answer']}' не найден в '{actual_answer}'"
