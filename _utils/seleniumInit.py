import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 编写人 李昱兴 15027162580
# 本文件主要是用于封装selenium初始化的封装类
# 参数文件具体查看config下的config.json文件

class driverUtils:
    def __init__(self):
        # 从配置文件中加载配置信息
        with open("../config/config.json", 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            self.chrome_driver_path = json_data.get("chrome_driver_path")  # ChromeDriver路径
            self.Privacy = json_data.get("isPrivacy")  # 是否启用无痕模式
            self.timeOut = json_data.get("timeOut")  # 隐式等待时间
            self.mobile = json_data.get("mobile")  # 是否启用移动设备模拟

    # 初始化Chrome浏览器
    def begin(self):
        service = Service(self.chrome_driver_path)  # 设置ChromeDriver服务
        options = webdriver.ChromeOptions()  # 创建Chrome选项
        options.add_argument("--window-size=1080,720")  # 设置浏览器窗口大小
        options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 禁用自动化提示
        options.add_experimental_option("detach", True)  # 防止脚本结束时关闭浏览器

        # 如果启用移动设备模拟，设置模拟的设备名称
        if self.mobile:
            mobile_emulation = {
                "deviceName": "iPhone X"  # 模拟iPhone X设备
            }
            options.add_experimental_option("mobileEmulation", mobile_emulation)

        # 如果启用无痕模式，添加无痕模式参数
        if self.Privacy:
            options.add_argument("--incognito")  # 启用无痕模式

        # 初始化WebDriver实例
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(self.timeOut)  # 设置隐式等待时间
        return driver  # 返回WebDriver实例

if __name__ == '__main__':
    print("已初始化")