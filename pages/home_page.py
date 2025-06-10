from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.course = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-page > div > div:nth-child(2) > div.home-card__bot > div > div.avatar.baseavatar_go.home-card__bot-content-btn.baseavatar > span")
        self.lessons = (By.CSS_SELECTOR, "#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(2)")
        self.video = (By.CSS_SELECTOR, "#app > div > div.container.container_mobile > div > div > div.new-lessons_content > div > div:nth-child(4) > div.flex.gap20 > div:nth-child(3) > div.lesson-card > div > div.lesson-card-left > div.lesson-card-left_actions > button > span")
        self.messenger = (By.CSS_SELECTOR, "#app > div > div.layout > div > div.material-dialog__window > div > ul > li:nth-child(5) > div")
        self.open_chat = (By.CSS_SELECTOR, "#app > div > div.messanger > div.messanger__chats.flex.column.hidden > div.p10.grow.flex.column.hidden.gap10 > div.tab-content.grow.flex.column.hidden > div > div")
        self.enter_message = (By.CSS_SELECTOR, "#app > div > div.messanger > div.messanger__container.active > div > div.message-input.relative.messanger__container-field > div > div > label")
        self.send_message = (By.CSS_SELECTOR, "#app > div > div.messanger > div.messanger__container.active > div > div.message-input.relative.messanger__container-field > button")
        self.homepage = (By.CSS_SELECTOR, "#app > div > div.header > nav > div.header__logo > div > a")
        self.avatar = (By.CSS_SELECTOR, "#app > div > div.header > div > div.header__avatar")
        self.exit = (By.CSS_SELECTOR, "#app > div > div.inforation > div > div > div:nth-child(7) > div")
        self.confirm_exit = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2) > span")


    def click_course(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.course)).click()

    def click_lessons(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.lessons)).click()

    def click_video(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.video)).click()

    def click_messenger(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.messenger)).click()

    def click_open_chat(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.open_chat)).click()

    def enter_message_text(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.enter_message)).send_keys("Это для CI, всем привет")

    def click_send_message(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.send_message)).click()

    def click_homepage(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.homepage)).click()

    def click_avatar(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.avatar)).click()

    def click_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.exit)).click()

    def click_confirm_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.confirm_exit)).click()



