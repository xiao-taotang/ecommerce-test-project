from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self,driver):
        self.driver = driver

    def fill_info(self,first_name,last_name,postal_code):
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.ID,"first-name"))
        )
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)        # 填写信息
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(By.ID, "continue").click()                      # 点击继续

    def click_finish(self):
        self.driver.find_element(By.ID, "finish").click()                        # 点击下单

    def get_complete_message(self):
        finish_text = self.driver.find_element(By.CSS_SELECTOR,".complete-header").text    # 获取结束页的文字
        return finish_text