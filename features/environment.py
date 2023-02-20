from selenium import webdriver

from features.driver import Driver
from features.pages.home_page import HomePage
from features.pages.login_page import LoginPage
from features.pages.women_page import WomenPage


def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver = Driver().driver
    context.home_page = HomePage(context.driver)
    context.login_page = LoginPage(context.driver)
    context.women_page = WomenPage(context.driver)


def after_all(context):
    context.driver.quit()