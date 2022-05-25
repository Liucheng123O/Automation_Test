import pytest

from JiaoZiDT_AppClient_PO.PageObjects.home_page.home_page import HomePage


@pytest.fixture()
def init_merchant_detail(login_app):
    """
    前置：滑动屏幕找到商户、进入商户详情
    后置：关闭应用
    """
    HomePage(login_app).slide_screen_address()
    HomePage(login_app).click_merchants_name()

    yield login_app
    login_app.quit()
