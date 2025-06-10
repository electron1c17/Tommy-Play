from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.login = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-center > div > label > input")
        self.auth_btn = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-bot > button")
        self.password = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-center.log-in__newContent-right-block-center-checkpass > div.log-in__newContent-right-block-center-inp > label > input")
        self.dropdown = (By.CSS_SELECTOR, "#dialog > div > div > div > div.material-dialog__window-body.material-dialog__window-body_modify > div > div:nth-child(2) > div > div")
        self.close_session = (By.CSS_SELECTOR, "#dialog > div > div > div > div.material-dialog__window-body.material-dialog__window-body_modify > div > div:nth-child(2) > div.drop-down-component__content > div.sessions__item-content > button > span")
        self.finish_btn = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-bot > button")


    def enter_login(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.login)).send_keys("phone")

    def click_auth_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.auth_btn)).click()

    def enter_password(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.password)).send_keys("password")

    def click_dropdown(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.dropdown)).click()

    def click_close_session(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.close_session)).click()

    def click_finish_auth(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.finish_btn)).click()
