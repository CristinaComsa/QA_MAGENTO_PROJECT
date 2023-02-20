"""

"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    URL = 'https://magento.softwaretestingboard.com/'

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def get_quantity(self,by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))

    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    def get_title(self, title) -> str:
        """Returns the title of the page"""
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
