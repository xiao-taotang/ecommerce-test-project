from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self,driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()   # 将第一个商品加入购物车

    def get_cart_badge_count(self):
        badge = self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_container").text      # 获取购物车角标文本
        return badge

    def is_cart_badge_gone(self):
        try:                                                                # 获取购物车的内容,验证购物车角标是否消失
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge"))
            )
            return True
        except:
            return False


    def remove_backpack(self):
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()        # 将商品移除购物车

    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()  # 进入购物车页面
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )