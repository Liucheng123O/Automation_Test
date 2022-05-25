import pytest

from JiaoZiDT_Web_PO.PageObjects.home_page import HomePage
from JiaoZiDT_Web_PO.PageObjects.login_page import LoginPage
from selenium import webdriver

from JiaoZiDT_Web_PO.TestDatas.Globbal_Datas import host


@pytest.fixture()
def init_order_management(init_driver):
    # driver = webdriver.Chrome()
    # driver.get(host)
    # driver.maximize_window()
    # # 登录--首页
    # LoginPage(driver).login()
    HomePage(init_driver).order_home()
    yield init_driver

