import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    main_page_order_button = [By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button"]
    faq_section = [By.CLASS_NAME, "accordion"]

    def __init__(self, driver):
        super().__init__(driver)
        self.question = None

    @allure.step('Создаём переменную, в которую будем передавать текст вопроса')
    def set_question(self, question):
        self.question = question

    @property
    def get_accordion_question_locator(self): #получает локатор вопроса по переданному тексту вопроса
        return [By.XPATH, f".//div[contains(text(), '{self.question}')]"]


    def get_accordion_answer_locator(self): #получает локатор ответа по переданному тексту вопроса
        accordion_answer_locator = (By.XPATH,
                f".//div[contains(@class, 'accordion__heading')]/div[contains(text(), '{self.question}')]/following::p[1]")
        return accordion_answer_locator

    @allure.step('Получаем текст элемента с ответом на основе текста вопроса')
    def get_answer_text(self):
        accordion_answer_locator = self.get_accordion_answer_locator()
        return self.get_element_text(accordion_answer_locator)

    @allure.step('Скролл до блока с вопросами и раскрытие соответствующего вопроса')
    def expand_accordion_tab(self):
        self.scroll_to_element(self.faq_section)
        self.click_element(self.get_accordion_question_locator)
