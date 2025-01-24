import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage
from pages.main_page import MainPage


class OrderPage(BasePage):

    order_page_url = MainPage.main_page_url + '/order'

    #форма заполнения информации о пользователе
    first_name_field = [By.XPATH, ".//input[@placeholder='* Имя']"]
    second_name_field = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    address_field = [By.XPATH, ".//input[contains(@placeholder, 'Адрес')]"]
    phone_number_field = [By.XPATH, ".//input[contains(@placeholder, 'Телефон')]"]
    metro_station_field = [By.XPATH, ".//div[@class='select-search']//input"]
    metro_station_dropdown = [By.XPATH, ".//div[@class='select-search__select']"]
    continue_button = [By.XPATH, ".//button[text()='Далее']"]

    #форма заполнения информации об аренде самоката
    rent_day_field = [By.XPATH, ".//div[@class='react-datepicker__input-container']/input"]
    rent_day_last_date_in_datepicker = [By.XPATH, ".//div[@class='react-datepicker__week'][last()]/div[contains(class, reakt)][last()]"]
    rent_day_second_last_date_in_datepicker = [By.XPATH, ".//div[@class='react-datepicker__week'][last()]/div[contains(class, reakt)][last()-1]"]
    rent_duration_field = [By.XPATH, ".//div[@class='Dropdown-root']"]
    rent_duration_1_day = [By.XPATH, ".//div[@class='Dropdown-option'][position()=1]"]
    rent_duration_5_days = [By.XPATH, ".//div[@class='Dropdown-option'][position()=5]"]
    color_black = [By.XPATH, ".//label[contains(@for, 'black')]"]
    color_grey = [By.XPATH, ".//label[contains(@for, 'grey')]"]
    comment_field = [By.XPATH, ".//input[contains(@placeholder, 'Комментарий')]"]
    finish_order_button = [By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']"]

    confirm_order_button = [By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Да']"]

    success_order_header = [By.XPATH, ".//div[text()='Заказ оформлен']"]

    success_order_header_text = "Заказ оформлен"


    def first_name_input_valid_name(self, name):
        self.send_keys(self.first_name_field, name)

    def sure_name_input_valid_second_name(self, sure_name):
        self.send_keys(self.second_name_field, sure_name)

    def address_input_valid_user_address(self, address):
        self.send_keys(self.address_field, address)

    def phone_number_input_valid_user_phone(self, phone):
        self.send_keys(self.phone_number_field, phone)

    def metro_station_field_select_metro_station(self, metro):
        self.send_keys(self.metro_station_field, metro) #вводит название станции
        self.click_element(self.metro_station_dropdown) #кликает на предлагаемый вариант в дропдауне

    def click_continue_button(self):
        self.click_element(self.continue_button)

    @allure.step('Заполнение данных о пользователе')
    def fill_user_info (self, name, sure_name, address, phone, metro):
        self.first_name_input_valid_name(name)
        self.sure_name_input_valid_second_name(sure_name)
        self.address_input_valid_user_address(address)
        self.phone_number_input_valid_user_phone(phone)
        self.metro_station_field_select_metro_station(metro)
        self.click_continue_button()

    def pick_rent_date(self, date):
        self.click_element(self.rent_day_field)
        self.click_element(date)

    def fill_comment_field(self, comment):
        self.send_keys(self.comment_field, comment)

    def pick_rent_duration(self, days_amount):
        self.click_element(self.rent_duration_field) #жмём на поле с дропдауном
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(days_amount)) #ждём пока выпадет
        self.click_element(days_amount) #жмём на соответсвующий вариант

    def pick_vehicle_color(self, color):
        self.click_element(color)

    def click_finish_order_button(self):
        self.click_element(self.finish_order_button)

    def click_confirm_order_button(self):
        self.click_element(self.confirm_order_button)

    @allure.step('Заполнение данных об аренде самоката')
    def fill_rent_info(self, date, days_amount, color, comment):
        self.pick_rent_date(date)
        self.pick_rent_duration(days_amount)
        self.pick_vehicle_color(color)
        self.fill_comment_field(comment)
        self.click_finish_order_button()
        self.click_confirm_order_button()
