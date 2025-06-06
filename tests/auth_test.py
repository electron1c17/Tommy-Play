import logging
from pages.auth_page import AuthPage
from pages.home_page import HomePage

def test_auth(driver_chrome):
    auth_page = AuthPage(driver_chrome)
    home_page = HomePage(driver_chrome)
    auth_page.auth_btn()
    auth_page.enter_login()
    auth_page.click_login_btn()
    auth_page.click_go_password()
    auth_page.go_enter_password()
    auth_page.click_finish_auth()
    home_page.click_go_search()
    home_page.click_home()
    home_page.click_avatar()
    home_page.click_exit()
