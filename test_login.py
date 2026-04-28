import pytest
from selenium.webdriver.common.by import By

class TestLogin:
    def test_login_success(self, driver):
        driver.find_element(By.ID,"user-name").send_keys("standard_user")      # 找到用户名输入框，输入 standard_user
        driver.find_element(By.ID,"password").send_keys("secret_sauce")        # 找到密码输入框，输入secret_sauce
        driver.find_element(By.ID,"login-button").click()                      # 找到登录按钮，点击
        assert "inventory" in driver.current_url                               # 验证登录成功：检查当前网址包含“inventory”


    def test_login_fail(self, driver):
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")                       # 找到用户名输入框，输入 standard_user
        driver.find_element(By.ID, "password").send_keys("secret_sauce")                           # 找到密码输入框，输入secret_sauce
        driver.find_element(By.ID, "login-button").click()                                         # 找到登录按钮，点击
        wrong_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container h3").text   # 在div里找到h3中的报错信息
        assert 'locked out' in wrong_message                                                       # 验证页面出现了错误提示信息

    



