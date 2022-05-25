from time import sleep

from JiaoZiDT_Web_PO.Common.basepage import BasePage
from JiaoZiDT_Web_PO.PageLocators.commodity_management_locs.commodity_management_locs import CommodityManagementLocs
from JiaoZiDT_Web_PO.PageLocators.home_Page_locs import HomePageLocs


class HomePage(BasePage):
    def management_home(self):
        # self.click_element(HomePageLocs.business_management,"首页--点击进入业务管理",timeout=10)
        sleep(1)
        self.click_element(CommodityManagementLocs.commoditymanagement,"首页-点击进入商品管理")
    def order_home(self):
        # self.click_element(HomePageLocs.business_management, "首页--点击进入业务管理", timeout=10)
        sleep(1)
        self.click_element(CommodityManagementLocs.commoditymanagement, "首页-点击进入商品管理")
        self.click_element(HomePageLocs.orerd_management,"首页--点击进入订单管理",timeout=10)

    def merchant_home(self):
        # self.click_element(HomePageLocs.business_management, "首页--点击进入业务管理", timeout=10)
        sleep(1)
        self.click_element(CommodityManagementLocs.commoditymanagement, "首页-点击进入商品管理")
        self.click_element(HomePageLocs.merchant_management,"首页--点击进入商户管理", timeout=10)

    def city_dining_home(self):
        self.click_element(HomePageLocs.city_dining,'首页-- 点击城市食堂')



