import pytest

from JiaoZiDT_Web_PO.PageObjects.home_page import HomePage
""" 商户管理前置后置条件 """

@pytest.fixture()
def init_merchant_management(init_driver):
    HomePage(init_driver).merchant_home()
    yield init_driver
    # quit()


