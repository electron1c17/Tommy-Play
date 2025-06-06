from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.auth = (By.CSS_SELECTOR, "#global-nav-bar > div.N9r2VuXMBlhRSVF5dCek > div > div.LKFFk88SIRC9QKKUWR5u > button.encore-text-body-medium-bold.e-9921-button-primary.e-9921-button")
        self.login = (By.CSS_SELECTOR, "#login-username")
        self.login_btn = (By.CSS_SELECTOR, "#login-button")
        self.go_password = (By.CSS_SELECTOR, "#encore-web-main-content > div:nth-child(2) > div > div > div > form > div.EmailVerificationChallenge__InputBlock-sc-55dvy9-5.jipEUB > section > button")
        self.enter_password = (By.CSS_SELECTOR, "#login-password")
        self.finish_auth = (By.CSS_SELECTOR, "#login-button")

    def auth_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.auth)).click()

    def enter_login(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.login)).send_keys("tommyplay178@gmail.com")

    def click_login_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.login_btn)).click()

    def click_go_password(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.go_password)).click()

    def go_enter_password(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.enter_password)).send_keys("Murdagij9639?")

    def click_finish_auth(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.finish_auth)).click()