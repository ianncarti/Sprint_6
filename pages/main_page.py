import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.question = None

    def set_question(self, question):
        self.question = question

    main_page_url = 'https://qa-scooter.praktikum-services.ru/'
    main_page_order_button = [By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button"]
    faq_section = [By.CLASS_NAME, "accordion"]

    @property
    def get_accordion_question_locator(self): #получает локатор вопроса по переданному тексту вопроса
        return [By.XPATH, f".//div[contains(text(), '{self.question}')]"]


    def get_accordion_answer_locator(self): #получает локатор ответа по переданному тексту вопроса
        accordion_answer_locator = (By.XPATH,
                f".//div[contains(@class, 'accordion__heading')]/div[contains(text(), '{self.question}')]/following::p[1]")
        return accordion_answer_locator

    def get_answer_text(self):
        accordion_answer_locator = self.get_accordion_answer_locator()
        return self.get_element_text(accordion_answer_locator)

    @allure.step('Скролл до блока с вопросами и раскрытие соответствующего вопроса')
    def expand_accordion_tab(self):
        self.scroll_to_element(self.faq_section)
        self.click_element(self.get_accordion_question_locator)
