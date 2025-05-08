import time
from selenium.webdriver.common.by import By
from _utils.seleniumInit import *
import pytest


# 定义一个 pytest 的 fixture，用于共享 WebDriver 实例
@pytest.fixture(scope="module")
def share_driver():
    # 初始化 WebDriver
    driver = driverUtils().begin()
    print("已经初始化")
    yield driver  # 返回 WebDriver 实例供测试用例使用
    print("准备关闭网页")
    time.sleep(1)
    # driver.quit()  # 关闭浏览器（此处注释掉了）


# 测试全屏的预览功能
def test_fullScreen_preview(share_driver):
    # 打开指定的网页
    share_driver.get("https://notebooklm.google/?location=unsupported")

    # 默认概览模式下全屏的预览，模拟滚动页面
    for i in range(10):
        share_driver.execute_script("window.scrollBy(0, document.body.scrollHeight/10);")  # 滚动页面
        time.sleep(0.5)  # 等待

    # 切换到 plus 模式下全屏的预览
    share_driver.find_element(By.XPATH, "/html/body/app-root/div/app-header/header/nav/ul/li[2]/a").click()
    for i in range(10):
        share_driver.execute_script("window.scrollBy(0, document.body.scrollHeight/10);")  # 滚动页面
        time.sleep(0.5)  # 等待


# 主函数入口，运行 pytest 测试
if __name__ == '__main__':
    pytest.main(['tests'])