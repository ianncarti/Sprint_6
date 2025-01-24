import pytest
import allure
from selenium import webdriver
from data import ValidOrderInfo, FaqSectionIds
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import PagesUrls


class TestMainPage:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка перехода на главную страницу через логотип самоката')
    def test_redirect_to_main_page(self):
        main_page = MainPage(self.driver)
        main_page.open_url(PagesUrls.main_page_url)
        main_page.click_order_button(ValidOrderInfo.order_buttons[0])
        main_page.wait_for_element_is_visible(OrderPage.first_name_field)
        main_page.click_element(MainPage.logo_link_to_main_page)

        assert PagesUrls.main_page_url == self.driver.current_url

    @allure.title('Проверка перехода на Дзен через логотип Яндекса')
    def test_redirect_to_dzen(self):
        main_page = MainPage(self.driver)
        main_page.open_url(PagesUrls.main_page_url)
        main_page.click_element(main_page.logo_link_to_dzen)
        main_page.switch_to_last_browser_tab()
        excepted_url = 'https://dzen.ru/?yredirect=true'
        main_page.wait_for_url(excepted_url)

        assert excepted_url in self.driver.current_url

    @allure.title('Раскрытие пунктов аккардеона с вопросами-ответами')
    @allure.description('Раскрываем каждый вопрос в аккордеоне и сверяем ожидаемый текст с актуальным')
    @pytest.mark.parametrize("question, answer", FaqSectionIds.faq_ids)
    def test_expand_faq_accordions(self, question, answer):
        main_page = MainPage(self.driver)
        main_page.set_question(question)
        main_page.open_url(PagesUrls.main_page_url)
        main_page.expand_accordion_tab()
        actual_text = main_page.get_answer_text()

        assert answer == actual_text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
