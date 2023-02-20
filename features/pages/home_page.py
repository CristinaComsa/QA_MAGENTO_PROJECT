"""
all the methods for home page
"""
from features.pages.base_page import BasePage
from features.resources.home_locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.get_title()

    def get_home_message(self):
        return self.get_text(HomePageLocators.home_message)

    def click_on_new_products(self):
        self.click(HomePageLocators.new)

    def is_new_products_page(self):
        current_url = self.driver.current_url
        expected = 'https://magento.softwaretestingboard.com/what-is-new.html'
        return current_url == expected

    def click_on_women_products(self):
        self.click(HomePageLocators.women)

    def is_women_products_page(self):
        current_url = self.driver.current_url
        expected = 'https://magento.softwaretestingboard.com/women.html'
        return current_url == expected

    def click_on_men_products(self):
        self.click(HomePageLocators.men)

    def is_men_products_page(self):
        current_url = self.driver.current_url
        expected = 'https://magento.softwaretestingboard.com/men.html'
        return current_url == expected

    def click_on_gear_products(self):
        self.click(HomePageLocators.gear)

    def is_gear_products_page(self):
        current_url = self.driver.current_url
        expected = 'https://magento.softwaretestingboard.com/gear.html'
        return current_url == expected

    def click_on_training_products(self):
        self.click(HomePageLocators.training)

    def is_training_products_page(self):
        current_url = self.driver.current_url
        expected = 'https://magento.softwaretestingboard.com/training.html'
        return current_url == expected

    def click_on_sale_products(self):
        self.click(HomePageLocators.sale)

    def is_sale_products_page(self):
        current_url = self.driver.current_url
        expected = 'https://magento.softwaretestingboard.com/sale.html'
        return current_url == expected

    def click_on_search_bar(self):
        self.click(HomePageLocators.search_bar)

    def enter_product(self, product):
        self.enter_text(HomePageLocators.search_bar, product)

    def click_on_search_button(self):
        self.click(HomePageLocators.search_button)

    def is_products_page(self):
        return self.get_text(HomePageLocators.pants_gym_message)

    def click_on_product(self):
        self.click(HomePageLocators.diva_gym_tee_product)

    def click_on_size_and_colour(self):
        self.click(HomePageLocators.size_m)
        self.click(HomePageLocators.colour_green)

    def click_on_add_to_cart(self):
        self.click(HomePageLocators.add_to_cart_button)

    def get_cart_counter(self):
        return self.get_text(HomePageLocators.cart_quantity)

    def add_product_to_cart(self,product):
        self.click_on_search_bar()
        self.enter_text(HomePageLocators.search_bar, product)
        self.click_on_search_button()
        self.click_on_product()

    def click_on_basket_button(self):
        self.click(HomePageLocators.basket_button)

    def remove_item(self):
        self.click(HomePageLocators.remove_item)
        self.click(HomePageLocators.ok_message)

    def get_cart_empty_counter(self):
        return self.get_text(HomePageLocators.cart_empty_message)