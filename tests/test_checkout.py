import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestCheckout:
    def test_full_checkout(self, driver):
        page = LoginPage(driver)
        page.enter_username("standard_user")             # 找到用户名输入框，输入 standard_user
        page.enter_password("secret_sauce")              # 找到密码输入框，输入secret_sauce
        page.click_login()                               # 找到登录按钮，点击

        inventory = InventoryPage(driver)
        inventory.add_backpack_to_cart()                 # 将第一个商品加入购物车
        inventory.go_to_cart()                           # 进入购物车

        cart = CartPage(driver)
        cart.click_checkout()                            # 进入结算界面

        checkout = CheckoutPage(driver)
        checkout.fill_info('dulcie','caden','520520')    # 填写信息
        checkout.click_continue()                        # 点击继续
        checkout.click_finish()                          # 点击下单
        assert checkout.get_complete_message() == 'Thank you for your order!' # 验证文字是否一致

