"""
all the methods for women page
"""
from features.pages.base_page import BasePage
from features.resources.women_locators import WomenPageLocators


class WomenPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_tops(self):
        self.click(WomenPageLocators.tops)

    def is_tops_page(self):
        current_url = self.driver.current_url
        expected = 'https://magento.softwaretestingboard.com/women/tops-women.html'
        return current_url == expected, 'url incorrect'

    def get_shopping_categories(self):
        return len(self.get_quantity(WomenPageLocators.shopping_options))

    def get_amount_items(self):
        return self.get_text(WomenPageLocators.tops_50)

    def click_on_price(self):
        self.click(WomenPageLocators.sort_by_box)
        self.click(WomenPageLocators.ascending_price)

    def is_ascending_price(self):
        current_url = self.driver.current_url
        expected = 'https://magento.softwaretestingboard.com/women/tops-women.html?p=1&product_list_order=price'
        return current_url == expected, 'url incorrect'

    def click_on_descending_arrow(self):
        self.click(WomenPageLocators.set_descending)

    def is_descending_price(self):
        current_url = self.driver.current_url
        expected = 'https://magento.softwaretestingboard.com/women/tops-women.html?p=1&product_list_order=price&product_list_dir=desc'
        return current_url == expected, 'url incorrect'

    def click_on_logo(self):
        self.click(WomenPageLocators.logo_LUMA)

    def is_home_page(self):
        current_url = self.driver.current_url
        expected = 'https://magento.softwaretestingboard.com/'
        return current_url == expected, 'is not home page :('
