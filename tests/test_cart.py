import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestCart:
    def login(self, driver):
        page = LoginPage(driver)
        page.enter_username("standard_user")             # 找到用户名输入框，输入 standard_user
        page.enter_password("secret_sauce")              # 找到密码输入框，输入secret_sauce
        page.click_login()                               # 找到登录按钮，点击

    def test_add_to_cart(self, driver):
        self.login(driver)
        inventory = InventoryPage(driver)
        inventory.add_backpack_to_cart()                 # 将第一个商品加入购物车
        assert inventory.get_cart_badge_count() == '1'   # 获取购物车角标文本,验证购物车是否显示数字1

    def test_remove_from_cart(self, driver):
        self.login(driver)
        inventory = InventoryPage(driver)
        inventory.add_backpack_to_cart()                 # 将第一个商品加入购物车
        inventory.remove_backpack()                      # 将商品移除购物车
        assert inventory.is_cart_badge_gone()            # 验证购物车角标是否消失

