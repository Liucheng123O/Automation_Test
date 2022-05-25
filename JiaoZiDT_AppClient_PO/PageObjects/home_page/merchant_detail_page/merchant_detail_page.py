from time import sleep

from JiaoZiDT_AppClient_PO.Common.basepage import BasePage
from JiaoZiDT_AppClient_PO.PageLocators.home_locs.home_locs import HomeLocs
from JiaoZiDT_AppClient_PO.PageLocators.home_locs.merchant_detail_locs.merchant_detail_locs import MerchantDetailLocs
from JiaoZiDT_AppClient_PO.PageObjects.home_page.home_page import HomePage


class MerchantDetailPage(BasePage):
    """商户详情 页面对象 """
    def merchant_title(self):
        return self.get_element_text(MerchantDetailLocs.merchant_title,'首页-商户详情页 获取页面标题')

    def merchant_name(self):
        return self.get_element_text(MerchantDetailLocs.merchant_name,'首页-商户详情页 获取商户名称')

    def merchant_area(self):
        return self.get_element_text(MerchantDetailLocs.merchant_area,'首页-商户详情页 获取商户区域信息')

    def business_hours(self):
        return self.get_element_text(MerchantDetailLocs.business_hours,'首页-商户详情页 获取商户营业时间')

    # def merchant_navigation(self):
    #     # self.driver.refresh()
    #     # self.click_element(MerchantDetailLocs.return_button,'首页-商户详情页 点击返回按钮')
    #     while True:
    #         self.click_element(MerchantDetailLocs.merchant_navigation, '首页-商户详情页 点击商户导航地址')
    #         try:
    #             a=self.get_element_text(MerchantDetailLocs.merchant_navigation, '首页-导航 获取导航地址')
    #             print(a)
    #
    #
    #
    #             if a == '中海国际D座1703':
    #                 sleep(2)
    #                 self.click_element(MerchantDetailLocs.return_button, '首页-商户详情页 点击返回按钮')
    #                 self.click_element(HomePage.click_merchants_name,'首页-商户页面')
    #                 self.click_element(MerchantDetailLocs.merchant_navigation,'首页-商户详情页 点击商户导航地址')
    #             else:
    #                 print('进入中海')
    #                 break
    #         except:
    #             print("退出了")



    def common_meal(self):
        return self.get_element_text(MerchantDetailLocs.common_meal,'首页-商户详情页 获取通用饭票标题')

    def discount_title(self):
        return self.get_element_text(MerchantDetailLocs.discount_title,'首页-商户详情页 获取通用饭票折扣标题')

    def purchase_back_title(self):
        return self.get_element_text(MerchantDetailLocs.purchase_back_title,'首页-商户详情页 获取通用饭票随时可退标题')

    def discount_meal07(self):
        return self.get_element_text(MerchantDetailLocs.discount_meal07,'首页-商户详情页 0-7折扣饭票提示')

    def commodity_name07(self):
        return self.get_element_text(MerchantDetailLocs.commodity_name07,'首页-商户详情页 0-7折商品标题')

    def purchase_price07(self):
        return self.get_element_text(MerchantDetailLocs.purchase_price07,'首页-商户详情页 0-7折商品购买价')

    def shop_price07(self):
        return self.get_element_text(MerchantDetailLocs.shop_price07,'首页-商户详情页 0-7折门店价')

    def save_money07(self):
        return self.get_element_text(MerchantDetailLocs.save_money07,'首页-商户详情页 0-7折扣省钱提示')
    def swipe_screen(self):
        self.slide_the_screen(MerchantDetailLocs.save_money785,'首页-商户详情页 7.85省钱')



    def discount_meal785(self):
        return self.get_element_text(MerchantDetailLocs.discount_meal785,'首页-商户详情页 7-8.5折扣饭票提示')

    def commodity_name785(self):
        return self.get_element_text(MerchantDetailLocs.commodity_name785,'首页-商户详情页 7-8.5折商品标题')

    def purchase_price785(self):
        return self.get_element_text(MerchantDetailLocs.purchase_price785,'首页-商户详情页 7-8.5折商品购买价')

    def shop_price785(self):
        return self.get_element_text(MerchantDetailLocs.shop_price785,'首页-商户详情页 7-8.5折门店价')

    def save_money785(self):
        return self.get_element_text(MerchantDetailLocs.save_money785,'首页-商户详情页 7-8.5折扣省钱提示')

    def employ_button(self):
        self.click_element(MerchantDetailLocs.employ_button,'首页-商户详情页 点击去使用')

    def meal_hint(self):
        return self.get_element_text(MerchantDetailLocs.meal_hint,'首页-商户详情页面-饭票页 查看提示 ')

    def combo_hint(self):
        return self.get_element_text(MerchantDetailLocs.combo_hint,'首页-商户详情页面-套餐页 查看提示')

    def order_button(self):
        self.click_element(MerchantDetailLocs.order_buytton07,'首页-商户详情页 点击去下单')



