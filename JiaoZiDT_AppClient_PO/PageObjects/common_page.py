from app_automation.APP_Framework.Common.basepage import BasePage
from app_automation.APP_Framework.PageLocators import common_locs


class CommonPage(BasePage):
    def home(self):
        self.click_element(common_locs.home, "首页--点击“首页”按钮")

    def classify(self):
        self.click_element(common_locs.classify, "分类--点击“分类”按钮")

    def my_meal(self):
        self.click_element(common_locs.my_meal, "我的饭票--点击“我的饭票”按钮")

    def my(self):
        self.click_element(common_locs.my, "我的--点击“我的”按钮")

    def search(self):
        self.click_element(common_locs.search, "通用--“搜索”按钮")

    def close_windows(self):
        try:
            self.click_element(common_locs.close_windows, "首页 -- 点击弹窗关闭按钮")
        except:
            print("首页--弹窗关闭失败！")







