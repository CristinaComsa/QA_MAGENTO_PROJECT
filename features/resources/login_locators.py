"""
all the selectors used to login page
"""
from selenium.webdriver.common.by import By


class LoginPageLocators:
    sign_in_button = (By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/a')
    customer_message = (By.XPATH, '//*[@id="maincontent"]/div[1]')
    email_field = (By.ID, 'email')
    password_field = (By.ID, 'pass')
    sign_in = (By.XPATH, '//*[@id="send2"]/span')
    welcome_message = (By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[1]/span')
    customer_login_message = (By.XPATH, '//*[@id="maincontent"]/div[1]/h1/span')
    button = (By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button')
    sign_out_button = (By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[3]/a')
