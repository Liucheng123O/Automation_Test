from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from JiaoZiDT_Web_PO.Common.basepage import BasePage
from JiaoZiDT_Web_PO.PageLocators.login_Page_locs import LoinPageLocs


class LoginPage(BasePage):
    def login(self):
        self.get_element(LoinPageLocs.pass_input,"登录页面--清除密码").clear()
        self.input_text(LoinPageLocs.pass_input,"admin.123","登录页面--输入密码")
        self.input_text(LoinPageLocs.auth_code,"0000","登录页面--输入验证码")
        self.click_element(LoinPageLocs.login_button, "登录页面--点击登录按钮")
        # while True:
        #
        #     # self.input_text(LoinPageLocs.auth_code,"0","登录页面--输入验证码",timeout=10)
        #     sleep(0.5)
        #     self.click_element(LoinPageLocs.login_button,"登录页面--点击登录按钮")
        #     code = self.get_element_text(LoinPageLocs.marked_words,"登录页面--等待错误的提示语",timeout=10)
        #
        #     # 获取正确的提示语
        #     if code == "验证码错误":
        #         # self.click_element(LoinPageLocs.login_button,"登录页面--点击登录",timeout=10)
        #         self.driver.refresh()
        #         sleep(1)
        #     else:
        #         sleep(2)
        #         break
        # # self.click_element(LoinPageLocs.open_list,'首页-- 点击 菜单列表')

        # 获取登录区域的提示信息--判断
    def get_msg_from_login_user(self):
        # 等待
        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(*self.msg_from_login_user))
        self.wait_element_visible(LoinPageLocs.home,'首页--断言是否登录到首页',timeout=15)
        return self.get_element_text(LoinPageLocs.home,'首页--获取文本',timeout=10)



