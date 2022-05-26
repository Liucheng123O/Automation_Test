import pytest

from JiaoZiDT_Web_PO.PageObjects.login_page import LoginPage
from JiaoZiDT_Web_PO.TestDatas.login_datas import home_text


@pytest.mark.usefixtures("init_driver")
class TestLogin:
    def test_login_succeed(self,init_driver):

        # LoginPage(init_driver).login()
        # logger.info("*****登录成功******")
        #判断
        assert LoginPage(init_driver).get_msg_from_login_user() == home_text

