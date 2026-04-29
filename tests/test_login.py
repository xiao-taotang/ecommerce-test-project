import pytest
from pages.login_page import LoginPage

class TestLogin:
    def test_login_success(self, driver):
        page = LoginPage(driver)
        page.enter_username("standard_user")             # 找到用户名输入框，输入 standard_user
        page.enter_password("secret_sauce")              # 找到密码输入框，输入secret_sauce
        page.click_login()                               # 找到登录按钮，点击
        assert "inventory" in driver.current_url         # 验证登录成功：检查当前网址包含“inventory”

    def test_login_fail(self, driver):
        page = LoginPage(driver)
        page.enter_username("locked_out_user")           # 找到用户名输入框，输入 locked_out_user
        page.enter_password("secret_sauce")              # 找到密码输入框，输入secret_sauce
        page.click_login()                               # 找到登录按钮，点击
        assert 'locked out' in page.get_error_message()  # 在div里找到h3中的报错信息，验证页面出现了错误提示信息

    



