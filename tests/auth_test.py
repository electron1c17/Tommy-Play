import logging
from pages.auth_page import AuthPage
from pages.home_page import HomePage
import time

def test_auth(driver_chrome):
    auth_page = AuthPage(driver_chrome)
    home_page = HomePage(driver_chrome)

    auth_page.auth_btn()
    time.sleep(3)
    auth_page.enter_login()
    time.sleep(3)
    auth_page.click_login_btn()
    time.sleep(3)
    auth_page.click_go_password()
    time.sleep(3)
    auth_page.go_enter_password()
    time.sleep(3)
    auth_page.click_finish_auth()
    time.sleep(3)
    home_page.click_go_search()
    time.sleep(3)
    home_page.click_home()
    time.sleep(3)
    home_page.click_avatar()
    time.sleep(3)
    home_page.click_exit()
    time.sleep(3)