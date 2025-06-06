from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.go_search = (By.CSS_SELECTOR, "#global-nav-bar > div.gj5VcIUC9oD2p4BsxzGE > div > div > form > div.ODl7TwNawIfBwiZv1Czg > input")
        self.home = (By.CSS_SELECTOR, "#global-nav-bar > div.gj5VcIUC9oD2p4BsxzGE > div > button")
        self.avatar = (By.CSS_SELECTOR, "#global-nav-bar > div.N9r2VuXMBlhRSVF5dCek > div > button.Button-sc-1dqy6lx-0.iFsPEJ.encore-text-body-medium-bold.e-9921-overflow-wrap-anywhere.e-9921-button-tertiary--condensed.KAq2kDjXj2VS4eXrFL4i")
        self.exit = (By.CSS_SELECTOR, "#context-menu > div > ul > li:nth-child(7) > button")

    def click_go_search(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.go_search)).send_keys("Мот")

    def click_home(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.home)).click()

    def click_avatar(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.avatar)).click()

    def click_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.exit)).click()