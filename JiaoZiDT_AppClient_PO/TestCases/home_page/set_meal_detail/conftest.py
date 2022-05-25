import pytest

from JiaoZiDT_AppClient_PO.PageObjects.home_page.home_page import HomePage


@pytest.fixture()
def init_set_meal_detail(login_app):
    """
    前置：滑动屏幕找到商品原价、点击进入套餐详情
    后置：关闭应用
    """
    HomePage(login_app).slide_screen_price()
    HomePage(login_app).click_original_price()

    yield login_app
    login_app.quit()
