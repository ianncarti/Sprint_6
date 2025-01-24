from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    header_order_button = [By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']"]
    order_status_button = [By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[text()='Статус заказа']"]
    logo_link_to_dzen = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]
    logo_link_to_main_page = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open_url(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    def wait_for_element_is_visible(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    def click_order_button(self, button_locator):
        self.scroll_to_element(button_locator)
        self.click_element(button_locator)

    def scroll_to_element(self, element_locator):
        element = self.driver.find_element(*element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_for_element_is_visible(element_locator)

    def switch_to_last_browser_tab(self):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])

    def wait_for_url(self, excepted_url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(excepted_url))
