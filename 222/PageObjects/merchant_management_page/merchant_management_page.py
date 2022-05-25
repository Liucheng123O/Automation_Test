from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from JiaoZiDT_Web_PO.Common.basepage import BasePage
from JiaoZiDT_Web_PO.PageLocators.merchant_management_locs.merchant_management_locs import MerchantManagementLocs

class MerchantManagementPage(BasePage):

    def merchant_name(self,name):
        self.input_text(MerchantManagementLocs.merchanr_name,name,'商户管理页面--输入商户名称')

    def data(self):
        sleep(1)
        return self.get_element_text(MerchantManagementLocs.data,'商户管理页面-- 获取数目条数')

    def affiliated_unit(self,neme):
        self.input_text(MerchantManagementLocs.affiliated_unit,neme,'商户管理页面-- 输入 所属商务名称')

    def contacts_name(self,name):
        self.input_text(MerchantManagementLocs.contacts_name,name,"商户管理页面-- 输入联系人姓名")

    def contacts_phone(self,phone):
        self.input_text(MerchantManagementLocs.contacts_phone,phone,"商户管理页面-- 请输入联系电话")

    def state(self):
        self.click_element(MerchantManagementLocs.state1,'商户管理页面-- 点击状态框')
        self.click_element(MerchantManagementLocs.state2,"商户管理页面-- 选择”显示“")

    def business_youfang(self):
        self.click_element(MerchantManagementLocs.business,"商户管理页面-- 点击 商圈 框")
        self.click_element(MerchantManagementLocs.business_youfang,"商户管理页面--点击悠方")

    def search(self):
        self.click_element(MerchantManagementLocs.search,'商户管理页面-- 点击搜索')
        sleep(1)

    def id(self,id):
        self.input_text(MerchantManagementLocs.id,id,'商户管理页面-- 输入id')

    def state_open_close(self):
        sleep(0.5)
        self.click_element(MerchantManagementLocs.state_open_close,'商户管理页面-- 点击商户 开启/关闭按钮')
        self.click_element(MerchantManagementLocs.click_open_close,'商户管理页面-- 点击商户 开启/关闭 确定 钮')

    def not_data(self):
        return self.get_element_text(MerchantManagementLocs.not_data,"商户管理页面-- 获取数据文本")

    def state1(self):
        self.click_element(MerchantManagementLocs.state1, '商户管理页面-- 点击状态框')
        self.click_element(MerchantManagementLocs.state3, "商户管理页面-- 选择”隐藏“")

    def change_save(self):
        self.click_element(MerchantManagementLocs.changed,"商户管理页面-- 点击 修改 按钮")
        sleep(1)
        self.click_element(MerchantManagementLocs.save_click,'商户管理页面-- 点击保存')

    def save_hint(self):
        return self.get_element_text(MerchantManagementLocs.save_hint,'商户管理页面--获取提示语')

    def integra_money(self,money):
        sleep(1)
        ront_integral=self.get_element_text(MerchantManagementLocs.get_integral, '商户管理页面--获取充值之前积分数')

        self.click_element(MerchantManagementLocs.recharge_button,'商户管理页面--点击充值')
        self.input_text(MerchantManagementLocs.recharge_integral,money,'商户管理页面-- 输入金额')
        self.click_element(MerchantManagementLocs.recharge_click_buuton,'商户管理页面--点击确定')
        sleep(1)
        integral=self.get_element_text(MerchantManagementLocs.get_integral,'商户管理页面--获取充值之后积分数')
        return int(integral)-int(ront_integral)

    def freeze_money(self,money):
        sleep(1)
        ront_integral=self.get_element_text(MerchantManagementLocs.freeze1,'商户管理页面--冻结前的金额')

        self.click_element(MerchantManagementLocs.freeze, '商户管理页面--点击冻结')
        self.input_text(MerchantManagementLocs.input_freeze_money, money, '商户管理页面-- 输入冻结金额')
        self.click_element(MerchantManagementLocs.recharge_click_buuton, '商户管理页面--点击确定')
        sleep(1)
        integral = self.get_element_text(MerchantManagementLocs.freeze1, '商户管理页面--获取充值之后积分数')
        return int(integral) - int(ront_integral)

    def unfreeze(self,money):
        sleep(1)
        ront_integral = self.get_element_text(MerchantManagementLocs.freeze1, '商户管理页面--解冻结前的金额')

        self.click_element(MerchantManagementLocs.unfreeze, '商户管理页面--点击解冻')
        self.input_text(MerchantManagementLocs.input_unfreeze_money, money, '商户管理页面-- 输入冻结金额')
        self.click_element(MerchantManagementLocs.recharge_click_buuton, '商户管理页面--点击确定')
        sleep(1)
        integral = self.get_element_text(MerchantManagementLocs.freeze1, '商户管理页面--获取充值之后积分数')
        return int(ront_integral) - int(integral)

    def staff_management(self):
        self.click_element(MerchantManagementLocs.staff_management,'商户管理页面-- 点击进入员工管理')

    def add_staff(self,phone,name):
        sleep(1)
        self.click_element(MerchantManagementLocs.add_staff,'商户管理页面-- 点击添加员工')
        self.input_text(MerchantManagementLocs.add_phone,phone,'商户管理页面-- 输入手机号')
        self.input_text(MerchantManagementLocs.add_name,name,'商户管理页面-- 输入名称')
        sleep(1)
        self.click_element(MerchantManagementLocs.add_button,'商户管理页面-- 点击确定')

    def judge_name(self):
        return self.get_element_text(MerchantManagementLocs.judge_name,'商户管理页面-- 判断 获取名称')

    def change_name(self):
        sleep(1)
        return self.get_element_text(MerchantManagementLocs.change_name, '商户管理页面-- 修改后判断 获取名称')

    def delete(self):
        self.click_element(MerchantManagementLocs.delete,'商户管理页面--点击删除按钮')
        sleep(1)
        self.click_element(MerchantManagementLocs.delete_button,'商户管理页面-- 删除确定')

    def change(self,name):
        self.click_element(MerchantManagementLocs.change,'商户管理页面-- 点击修改按钮')
        self.input_text(MerchantManagementLocs.add_name,name,'商户管理页面-- 输入名称')
        self.click_element(MerchantManagementLocs.add_button, '商户管理页面-- 点击确定')















