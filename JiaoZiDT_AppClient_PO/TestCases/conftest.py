from time import sleep

import pytest
import yaml
from appium.webdriver.common.mobileby import MobileBy
# from selenium.webdriver.remote import webdriver

from selenium.webdriver.support import expected_conditions as EC, expected_conditions

from app_automation.APP_Framework.Common.basepage import BasePage
from app_automation.APP_Framework.PageLocators import common_locs
from app_automation.APP_Framework.PageObjects import common_page
from app_automation.APP_Framework.PageObjects.common_page import CommonPage
from app_automation.APP_Framework.config.config import init_driver
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
@pytest.fixture()
def login_app():
    #打开app
    dr = init_driver()
    driver = webdriver.Remote(
        # appium 端口号
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities=dr
    )
    #"关闭首页弹窗！
    CommonPage(driver).close_windows()

    yield driver
    # driver.quit()

