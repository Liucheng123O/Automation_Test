
"""
定义一个登录的前提条件
定义一个关闭浏览器的后置条件
"""
import os
from time import sleep

import pytest
from selenium import webdriver

from JiaoZiDT_Web_PO.PageObjects.login_page import LoginPage
from webauto_PO.TestDatas.Globbal_Datas import host


@pytest.fixture()
def init_driver():
    """
    前置：打开浏览器，访问系统网址
    后置：退出浏览器
    """
    # option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    # # 这里是重点，增加一个参数即可实现在不打开浏览器的情况下完成系列操作
    # driver = webdriver.Chrome(chrome_options=option)

    driver = webdriver.Chrome()
    driver.get(host)
    driver.maximize_window()
    # driver.headless = True
    # 登录--首页
    LoginPage(driver).login()
    yield driver
    driver.quit()
    # sleep(1)
    # os.system('cd D:\pycharm\JiaoZiDT_Web_PO')
    # os.system('allure serve Outputs/allure_reports')


# """
# 登录
# """
# @pytest.fixture()
# def init_login(init_driver):
#     LoginPage(init_driver).login()
#     #返回值
#     yield init_driver
