
"""
定义一个登录的前提条件
定义一个关闭浏览器的后置条件
"""
import pytest
from selenium import webdriver

# from webauto_PO.PageObjects.login_page import LoginPage
from JiaoZiDT_Web_PO.PageObjects.home_page import HomePage
from JiaoZiDT_Web_PO.PageObjects.login_page import LoginPage
from webauto_PO.TestDatas.Globbal_Datas import host


@pytest.fixture()
def init_commodity_management(init_driver):
    """
    前置：打开浏览器，访问系统网址
    后置：退出浏览器
    """
    # driver = webdriver.Chrome()
    # driver.get(host)
    # driver.maximize_window()
    #登录--首页
    # LoginPage(init_driver).login()
    #进入商品管理
    HomePage(init_driver).management_home()
    yield init_driver
    # driver.quit()


# """
# 登录
# """
# @pytest.fixture()
# def init_login(init_driver):
#     LoginPage(init_driver).login()
#     #返回值
#     yield init_driver
