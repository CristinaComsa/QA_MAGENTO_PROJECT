from selenium import webdriver


class Driver:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    def get_current_url(self):
        return self.driver.current_url

    def quit(self):
        self.driver.quit()

