"""
all the selectors used to home page
"""

from selenium.webdriver.common.by import By


class HomePageLocators:
    title = (By.XPATH, '/html/head/title/text()')
    home_message = (By.XPATH, "/html/body/div[1]/div/p")
    new = (By.XPATH, '//*[@id="ui-id-3"]/span')
    women = (By.XPATH, '//*[@id="ui-id-4"]/span[2]')
    men = (By.XPATH, '//*[@id="ui-id-5"]/span[2]')
    gear = (By.XPATH, '//*[@id="ui-id-6"]/span[2]')
    training = (By.XPATH, '//*[@id="ui-id-7"]/span[2]')
    sale = (By.XPATH, '//*[@id="ui-id-8"]/span')
    search_bar = (By.XPATH,'//*[@id="search"]')
    search_button = (By.XPATH, '//*[@id="search_mini_form"]/div[2]/button')
    pants_gym_message = (By.XPATH, '//*[@id="maincontent"]/div[1]/h1/span')
    diva_gym_tee_product = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[2]/div[2]/ol/li[1]/div/a/span/span/img')
    size_m = (By.XPATH, '//*[@id="option-label-size-143-item-168"]')
    colour_green = (By.XPATH, '//*[@id="option-label-color-93-item-53"]')
    add_to_cart_button = (By.XPATH, '//*[@id="product-addtocart-button"]/span')
    basket_button = (By.XPATH, '/html/body/div[2]/header/div[2]/div[1]/a/span[2]')
    cart_quantity = (By.CLASS_NAME, 'counter-number')
    remove_item = (By.XPATH, '//*[@id="mini-cart"]/li/div/div/div[3]/div[2]/a')
    ok_message = (By.XPATH, '/html/body/div[4]/aside[2]/div[2]/footer/button[2]/span')
    cancel_message = (By.XPATH, '/html/body/div[4]/aside[2]/div[2]/footer/button[1]/span')
    cart_empty_message = (By.XPATH, '//*[@id="minicart-content-wrapper"]/div[2]/strong')

