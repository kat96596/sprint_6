import allure
import pytest
from pages.main_page import MainPage
from data import Urls, FaqData


@allure.feature('FAQ')
class TestFaq:

    @allure.title('Проверка текста ответов на вопросы в разделе "Вопросы о важном"')
    @allure.description('Тест проверяет, что при клике на вопрос открывается соответствующий текст ответа')
    @pytest.mark.parametrize('question_data', FaqData.questions)
    def test_faq_answer_text(self, driver, question_data):
        main_page = MainPage(driver)
        main_page.open(Urls.BASE_URL)  # Предполагается, что метод open есть в BasePage
        main_page.accept_cookies()

        actual_answer = main_page.get_faq_answer_text_by_question(question_data["question"])

        assert question_data["answer"] in actual_answer, \
            (f"Для вопроса '{question_data['question']}' ожидался ответ, содержащий "
             f"'{question_data['answer']}', но получен: '{actual_answer}'")
