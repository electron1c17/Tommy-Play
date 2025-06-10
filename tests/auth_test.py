import pytest
import logging
import time
from pages.auth_page import AuthPage
from pages.home_page import HomePage

def test_auth(driver_chrome):
    auth_page = AuthPage(driver_chrome)
    home_page = HomePage(driver_chrome)
    auth_page.enter_login()
    time.sleep(2)
    auth_page.click_auth_btn()
    time.sleep(2)
    auth_page.enter_password()
    time.sleep(2)
    auth_page.click_finish_auth()
    try:
        auth_page.click_dropdown()
        auth_page.click_close_session()
    except Exception as e:
        logging.error("Ошибка при клике на кнопку сессий", exc_info=True)

    time.sleep(2)
    home_page.click_course()
    time.sleep(2)
    home_page.click_lessons()
    time.sleep(2)
    home_page.click_video()
    time.sleep(2)
    home_page.click_messenger()
    time.sleep(2)
    home_page.click_open_chat()
    time.sleep(2)
    home_page.enter_message_text()
    time.sleep(2)
    home_page.click_send_message()
    time.sleep(2)
    home_page.click_homepage()
    time.sleep(2)
    home_page.click_avatar()
    time.sleep(2)
    home_page.click_exit()
    time.sleep(2)
    home_page.click_confirm_exit()
    time.sleep(2)


