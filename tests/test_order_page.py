import pytest
import allure
from selenium import webdriver
from data import ValidOrderInfo
from pages.order_page import OrderPage
from urls import PagesUrls


class TestOrderPage:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Заказ самоката')
    @allure.description('Проверка формы заказа с двумя наборами тестовых данных и из двух входных точек')
    @pytest.mark.parametrize(
        "order_button, name, sure_name, address, phone, metro, rent_date, rent_duration, vehicle_color, comment",
        [
            (ValidOrderInfo.order_buttons[0], ValidOrderInfo.user_names[0], ValidOrderInfo.user_sure_names[0],
         ValidOrderInfo.user_address[0], ValidOrderInfo.user_phone_numbers[0], ValidOrderInfo.metro_stations[0],
         ValidOrderInfo.rent_dates[0], ValidOrderInfo.rent_durations[0], ValidOrderInfo.vehicle_colors[0],
         ValidOrderInfo.comments_for_order[0]),

         (ValidOrderInfo.order_buttons[1], ValidOrderInfo.user_names[1], ValidOrderInfo.user_sure_names[1],
         ValidOrderInfo.user_address[1], ValidOrderInfo.user_phone_numbers[1], ValidOrderInfo.metro_stations[1],
         ValidOrderInfo.rent_dates[1], ValidOrderInfo.rent_durations[1], ValidOrderInfo.vehicle_colors[1],
         ValidOrderInfo.comments_for_order[1])
         ]
    )
    def test_order_with_valid_info(self, order_button, name, sure_name, address, phone, metro, rent_date, rent_duration, vehicle_color, comment):
        order_page = OrderPage(self.driver)
        order_page.open_url(PagesUrls.main_page_url)
        order_page.click_order_button(order_button)
        order_page.fill_user_info(name, sure_name, address, phone, metro)
        order_page.fill_rent_info(rent_date, rent_duration, vehicle_color, comment)

        assert order_page.success_order_header_text in order_page.get_element_text(OrderPage.success_order_header)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
