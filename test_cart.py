import pytest
from selenium.webdriver.common.by import By

class TestCart:
    def login(self, driver):
        driver.find_element(By.ID,"user-name").send_keys("standard_user")      # 找到用户名输入框，输入 standard_user
        driver.find_element(By.ID,"password").send_keys("secret_sauce")        # 找到密码输入框，输入secret_sauce
        driver.find_element(By.ID,"login-button").click()                      # 找到登录按钮，点击

    def test_add_to_cart(self, driver):
        self.login(driver)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()  # 将第一个商品加入购物车
        badge = driver.find_element(By.ID, "shopping_cart_container")          # 找到购物车
        assert badge.text == '1'                                                 # 验证购物车是否显示数字1

    def test_remove_from_cart(self, driver):
        self.login(driver)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()      # 将第一个商品加入购物车
        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()           # 将商品移除购物车
        badge_list = driver.find_elements(By.ID, "shopping_cart_badge")            # 获取remove时购物车的内容
        assert len(badge_list) == 0                                                # 验证是否remove后，内容随着购物车角标消失而消失

