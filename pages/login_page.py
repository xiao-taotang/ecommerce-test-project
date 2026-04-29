from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, name):
        self.driver.find_element(By.ID, "user-name").send_keys(name)     # 找到用户名输入框，输入name变量

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)   # 找到密码输入框，输入password变量

    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()     # 找到登录按钮，点击

    def get_error_message(self):
        wrong_message = self.driver.find_element(By.CSS_SELECTOR, ".error-message-container h3").text   # 在div里找到h3中的报错信息
        return wrong_message