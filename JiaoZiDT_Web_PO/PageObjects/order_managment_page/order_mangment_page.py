""" 订单页面对象  """
from time import sleep

# from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from JiaoZiDT_Web_PO.Common import logger
from JiaoZiDT_Web_PO.Common.basepage import BasePage
from JiaoZiDT_Web_PO.PageLocators.order_managment_locs.order_managment_locs import OrerdManagementLocs


class OrderManagementPage(BasePage):
    def user_account(self,account):
        self.input_text(OrerdManagementLocs.useraccount,account,"订单管理页面--使用用户账号搜索")

    def search_button(self):
        self.click_element(OrerdManagementLocs.search,"订单管理页面--点击 搜索 按钮")
        sleep(1)

    def user_data(self):
        return self.get_element_text(OrerdManagementLocs.user_data,'订单管理页面--获取用户数据条数')

    def order(self,number):
        self.input_text(OrerdManagementLocs.order_number,number,"订单管理页面-- 输入订单号码")

    def merchant_name(self,name):
        self.input_text(OrerdManagementLocs.merchant_name,name,'订单管理页面-- 输入商户名称')

    def commodity_name(self,name):
        self.input_text(OrerdManagementLocs.commodity_name,name,'订单管理页面-- 输入商品名称')

    def deal_state(self):
        self.click_element(OrerdManagementLocs.deal_state,'订单管理页面-- 点击交易状态')
        self.click_element(OrerdManagementLocs.paymentsuccess,'订单管理页面-- 点击交易成功')

    def order_create_time(self,s_time,e_time):
        self.click_element(OrerdManagementLocs.order_creation_time,"订单管理页面-- 点击创建订单时间")
        self.input_text(OrerdManagementLocs.start_time,s_time,"订单管理页面-- 开始输入时间")
        # self.driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[1]/span[1]/span[2]/div[1]/input').clear()
        # self.input_text(OrerdManagementLocs.start_time1,"00:00:00","订单管理-- 输入开始时间尾数")

        self.driver.find_element(By.XPATH,'//div[@class="el-date-range-picker__editor el-input el-input--small"]//input[@placeholder="结束日期"]').clear() #清空文本

        # self.driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div/div[1]/span[3]/span[2]/div[1]/input').clear()
        # self.input_text(OrerdManagementLocs.end_time1, "00:00:00", "订单管理-- 输入结束时间尾数")
        self.input_text(OrerdManagementLocs.end_time,e_time,"订单管理页面-- 选择结束时间")
        # self.click_element(OrerdManagementLocs.select_creation_time2,"订单管理页面-- 选择结束时间")
        self.click_element(OrerdManagementLocs.click_creation_time,"订单管理页面-- 点击确定")

    def not_data(self):
        return self.get_element_text(OrerdManagementLocs.notdata,'订单管理页面-- 正在获取数据')

    def detail_button(self):
        self.click_element(OrerdManagementLocs.detail,'订单管理页面-- 点击详细按钮')

    def detail_message(self):
        return self.get_element_text(OrerdManagementLocs.detail_message,"订单管理页面-- 获取订单详细信息")

    def select_page(self):
        self.click_element(OrerdManagementLocs.select_page1,'订单管理页面-- 点击选择页面')

    def get_order(self):
        return self.get_element_text(OrerdManagementLocs.get_order,'订单管理页面--获取编号')

    # def page_right_key(self):
    #     code = self.get_element_attribute(OrerdManagementLocs.get_order, '订单管理页面--获取编号')
    #     while True:
    #         sleep(2)
    #         try:
    #             # code=self.get_element_text(OrerdManagementLocs.get_order,'订单管理页面--获取编号')
    #             if code != "P1501860817337843712124":
    #         except:
    #             self.click_element(OrerdManagementLocs.page_right_key,'订单管理页面--点击翻页按钮')
    #         else:
    #             # driver.find_element(*loc).click()
    #             break













