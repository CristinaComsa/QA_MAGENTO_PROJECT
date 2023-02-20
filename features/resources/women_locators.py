"""
all the selectors used to women page
"""
from selenium.webdriver.common.by import By

class WomenPageLocators:
    tops = (By.XPATH, '//*[@id="narrow-by-list2"]/dd/ol/li[1]/a')
    tops_50 = (By.XPATH, '//*[@id="toolbar-amount"]/span[3]')
    shopping_options = (By.XPATH, '//*[@id="narrow-by-list"]/div')
    sort_by_box = (By.ID, 'sorter')
    ascending_price = (By.XPATH, '//*[@id="sorter"]/option[3]')
    set_descending = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[2]/div[4]/a')
    logo_LUMA = (By.XPATH, '/html/body/div[2]/header/div[2]/a/img')

