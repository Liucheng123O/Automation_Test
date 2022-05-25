import pytest

from JiaoZiDT_AppClient_PO.PageObjects.common_page import CommonPage
from JiaoZiDT_AppClient_PO.PageObjects.home_page.home_page import HomePage


@pytest.fixture()
def init_my(login_app):
    """
        前置：点击进入我的
        后置：关闭应用
        """

    CommonPage(login_app).my()

    yield login_app
    login_app.quit()