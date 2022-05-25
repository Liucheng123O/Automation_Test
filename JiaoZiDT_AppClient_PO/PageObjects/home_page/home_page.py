from JiaoZiDT_AppClient_PO.Common.basepage import BasePage
from JiaoZiDT_AppClient_PO.PageLocators.home_locs.home_locs import HomeLocs


class HomePage(BasePage):
    def click_merchants_name(self):
        self.click_element(HomeLocs.merchants_name, "首页 - 获取 商户名称")

    def merchants_name(self):

        return self.get_element_text(HomeLocs.merchants_name, "首页 - 获取 商户名称")

    def merchants_address(self):
        return self.get_element_text(HomeLocs.merchants_address, "首页 - 获取 商户地址 文本")

    def setmeal_name(self):
        return self.get_element_text(HomeLocs.setmeal_name, "首页 - 获取 套餐名称")

    def meal(self):
        return self.get_element_text(HomeLocs.meal, "首页 - 获取 通用饭票 字段")

    def explosive_discount(self):
        return self.get_element_text(HomeLocs.explosive_discount, "首页 - 获取爆品折扣")

    def blue_discount(self):
        return self.get_element_text(HomeLocs.Blue_discount, "首页 - 获取 饭票折扣")

    def location(self):
        return self.get_element_text(HomeLocs.place, "首页 - 获取 定位距离")

    def commodity_title(self):
        return self.get_element_text(HomeLocs.commodity_title, "首页 - 获取 商品副标题")

    def purchase_price(self):
        return self.get_element_text(HomeLocs.purchase_price, "首页 - 获取 商品购买价格")

    def original_price(self):
        return self.get_element_text(HomeLocs.original_price, "首页 - 获取 商品原价")

    def click_original_price(self):
        self.click_element(HomeLocs.original_price, "首页 - 点击 商品原价")

    def slide_screen_address(self):
        return self.slide_the_screen(HomeLocs.merchants_address, "首页 - 滑动屏幕找到 商户地址")

    def slide_screen_title(self):
        return self.slide_the_screen(HomeLocs.commodity_title, "首页 - 滑动屏幕找到 商品副标题")

    def slide_screen_price(self):
        self.slide_the_screen(HomeLocs.purchase_price, "首页 - 滑动屏幕找到商品购买价格")

    def heat(self):
        return self.get_element_text(HomeLocs.heat,'首页 - 获取 热度字段')

    def heat_number(self):
        return self.get_element_text(HomeLocs.heat_number,'首页 - 获取 热度数')

    def navigation(self):
        self.click_element(HomeLocs.place,'首页 - 点击进入导航')

    def navigation_merchants(self):
        return self.get_element(HomeLocs.commercial_name,'首页-导航 获取商户名称')

    def navigation_address(self):
        return self.get_element(HomeLocs.address,'首页-地址 获取商户地址')

    def click_navigation(self):
        self.click_element(HomeLocs.navigation_button,'首页-地址 点击导航按钮')

    def cancel(self):
        return self.get_element_text(HomeLocs.cancel,'首页-地址 获取取消字段')
