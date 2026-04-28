# 电商平台自动化测试项目

基于 Selenium + pytest 对 [SauceDemo](https://www.saucedemo.com) 电商网站进行自动化测试，覆盖从登录到下单的完整购物流程。

## 技术栈

- Python
- Selenium（UI自动化）
- pytest（测试框架）
- pytest-html（测试报告）

## 项目结构
ecommerce-test-project/
── conftest.py          # 公共fixture，浏览器启动与关闭
── test_login.py        # 登录测试（成功登录、登录失败）
── test_cart.py         # 购物车测试（加入商品、移除商品）
── test_checkout.py     # 完整下单流程测试
── pytest.ini           # pytest配置
── requirements.txt     # 项目依赖
── README.md

## 测试场景

| 文件 | 场景 | 验证点 |
|------|------|--------|
| test_login.py | 正确账号登录 | 跳转到商品页 |
| test_login.py | 被锁定账号登录 | 显示错误提示信息 |
| test_cart.py | 添加商品到购物车 | 购物车角标显示1 |
| test_cart.py | 移除购物车商品 | 购物车角标消失 |
| test_checkout.py | 登录→加购→结算→下单 | 显示下单成功提示 |

## 运行方式

```bash
pip install -r requirements.txt
pytest